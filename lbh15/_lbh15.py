"""Module with the definition of liquid metal object base class,
i.e., LiquidMetalInterface"""
import warnings
import sys
import inspect
import importlib
import os.path
import platform
import copy
from abc import ABC
from abc import abstractmethod
from collections import defaultdict
from typing import Dict
from typing import List
from typing import Tuple
from typing import Union
from scipy.constants import atm
from scipy.optimize import fsolve
from .properties.interface import PropertyInterface

warnings.simplefilter("always")


class LiquidMetalInterface(ABC):
    """
    Abstract class that defines liquid metal properties object

    Parameters
    ----------
    p : float, optional
        Pressure in [Pa], by default the atmospheric pressure value, i.e.,
        101325.0 Pa
    **kwargs : dict
        One-item dictionary that specifies the quantity which the object shall
        be initialized from. The default available ones are:

        - 'T' : temperature [K]
        - 'p_s' : saturation vapour pressure [Pa]
        - 'sigma' : surface tension [N/m]
        - 'rho' : density [Kg/m^3]
        - 'alpha' : thermal expansion coefficient [1/K]
        - 'u_s': speed of sound [m/s]
        - 'beta_s' : isentropic compressibility [1/Pa]
        - 'cp' : specific heat capacity [J/(kg \\cdot K)]
        - 'h' : specific enthalpy (in respect to melting point) [J/kg]
        - 'mu' : dynamic viscosity [Pa*s]
        - 'r' : electrical resistivity [Ohm*m]
        - 'k' : thermal conductivity [W/(m*K)]
    """
    _T_m0: float = 0
    _Q_m0: float = 0
    _T_b0: float = 0
    _Q_b0: float = 0
    _M: float = 0
    _guess: float = 0
    _correlations_to_use: Dict[str, str] = {}
    _roots_to_use: Dict[str, int] = {}
    _default_corr_to_use: Dict[str, str] = {}
    _properties_modules_list: List[str] = []
    _custom_properties_path: Dict[str, List[str]] = {}
    _available_properties_dict: Dict[str, PropertyInterface] = {}
    _available_correlations_dict: Dict[str, List[str]] = {}
    __p: float = 0
    __T: float = 0

    def __init__(self, p: float = atm, **kwargs):
        if len(kwargs) != 1:
            raise ValueError("One and only one property at "
                             "time can be used for initialization. "
                             f"{len(kwargs)} were provided")
        self.__assign_p(p)
        self.__properties: Dict[str, PropertyInterface] = {}
        self.__corr2use: Dict[str, str] = \
            copy.deepcopy(self.__class__._correlations_to_use)
        self.__fill_instance_properties()
        self._set_constants()
        name, value = kwargs.popitem()
        self.__fill_instance_attributes(name, value)

    @property
    def T_m0(self) -> float:
        """
        float : melting temperature :math:`[K]`
        """
        return self._T_m0

    @property
    def Q_m0(self) -> float:
        """
        float : melting latent heat :math:`[J/kg]`
        """
        return self._Q_m0

    @property
    def T_b0(self) -> float:
        """
        float : boiling temperature :math:`[K]`
        """
        return self._T_b0

    @property
    def Q_b0(self) -> float:
        """
        float : vaporisation heat :math:`[J/kg]`
        """
        return self._Q_b0

    @property
    def M(self) -> float:
        """
        float : metal molar mass :math:`[g/mol]`
        """
        return self._M

    @property
    def p(self) -> float:
        """
        float : pressure adopted for property calculation :math:`[Pa]`, \
            i.e., atmospheric pressure
        """
        return self.__p

    @p.setter
    def p(self, p: float) -> None:
        """
        p(p: float) -> None

        Set liquid metal pressure

        Parameters
        ----------
        p : float
            Pressure in [Pa]
        """
        self.__assign_p(p)

    @property
    def T(self) -> float:
        """
        float : temperature used to compute properties :math:`[K]`
        """
        return self.__T

    @T.setter
    def T(self, T: float) -> None:
        """
        Set liquid metal temperature

        Parameters
        ----------
        T : float
            Temperature in [K]
        """
        self.__assign_T(T)

    @property
    def Pr(self) -> float:
        """
        float : Prandtl number :math:`[-]`
        """
        return self.cp * self.mu / self.k

    @property
    def used_correlations(self) -> Dict[str, str]:
        """
        Returns the dictionary defining the correlation used for the \
        corresponding property. Only properties are considered for \
        which a specific correlation has been chosen a priori.

        Returns
        -------
        Dict[str, str]
        """
        return copy.deepcopy(self.__corr2use)

    def change_correlation_to_use(self, property_name: str,
                                  correlation_name: str) -> None:
        """
        Changes property correlation if property is defined as instance
        attribute, otherwise a warning message is returned without
        applying any change.

        Parameters
        ----------
        property_name : str
            Name of the property
        correlation_name : str
            Name of the correlation
        """
        # Manage the case the property is not among the currently used ones
        if property_name not in self.__properties:
            warnings.warn(f"'{property_name}' property not in use."
                          "\nNothing to change.", stacklevel=5)
            return
        # Manage the case the input correlation is already used
        if (self.__properties[property_name].correlation_name
                == correlation_name):
            warnings.warn(f"'{property_name}' property "
                          f"implementing '{correlation_name}' correlation "
                          "already in use. \nNothing to change.",
                          stacklevel=5)
            return
        # Manage the case the input correlation not among the available ones
        key = property_name + "__" + correlation_name
        if key not in self._available_properties_dict:
            warnings.warn(f"'{property_name}' property implementing "
                          f"'{correlation_name}' correlation not among"
                          "the available ones. \nNothing to change.",
                          stacklevel=5)
            return
        # If here, the input correlation is to apply
        self.__add_property(self._available_properties_dict[key])
        if property_name in self._default_corr_to_use:
            self.__corr2use[property_name] = correlation_name

    def check_temperature(self, T: float) -> Tuple[bool, str]:
        """
        Checks whether the provided temperature value belongs to the valid \
            temperature range, i.e., the liquid temperature range.

        Parameters
        ----------
        T : float
            Temperature in :math:`[K]`

        Returns
        -------
        Tuple[bool, str]:
            bool:
                `True` if check is ok, `False` otherwise
            str:
                error message (if any) associated
                to the temperature check
        """
        # Manage acceptable value
        if self.T_m0 < T < self.T_b0:
            return True, ""
        # Manage value outside the acceptable range
        if T >= self.T_b0:
            error_message = ("Temperature must be smaller than "
                             f"boiling temperature ({self.T_b0:.2f} [K]), "
                             f"{T:.2f} [K] was provided")
        elif 0 < T <= self.T_m0:
            error_message = ("Temperature must be larger than "
                             f"melting temperature ({self.T_m0:.2f} [K]), "
                             f"{T:.2f} [K] was provided")
        else:
            error_message = ("Temperature must be strictly positive, "
                             f"{T:.2f} [K] was provided")
        return False, error_message

    @classmethod
    def properties_for_initialization(cls) -> List[str]:
        """
        Returns the list of the available properties an instance can be
        initialized from.

        Returns
        -------
        List[str]
        """
        obj_list = cls.__load_properties()
        obj_list += cls.__load_custom_properties()
        rvalue = ['T'] + [obj_list[i].name for i in range(len(obj_list))]
        return list(dict.fromkeys(rvalue))

    @classmethod
    def available_correlations(cls) -> Dict[str, List[str]]:
        """
        Returns the dictionary containing the available correlations \
        for each property.

        Returns
        -------
        Dict[str, List[str]]
        """
        obj_list = cls.__load_properties()
        obj_list += cls.__load_custom_properties()
        return cls.__extract_available_correlations(obj_list)

    @classmethod
    def set_correlation_to_use(cls, property_name: str,
                               correlation_name: str) -> None:
        """
        Sets the correlation to use for the specified property.

        Parameters
        ----------
        property_name : str
            Name of the property
        correlation_name : str
            Name of the correlation
        """
        cls._correlations_to_use[property_name] = correlation_name

    @classmethod
    def set_root_to_use(cls, property_name: str, root_index: int) -> None:
        """
        Sets the index of the root to use for computing the temperature \
        from the correlation function of the property the instantiation \
        is based on. Temperature roots are sorted in ascending order, i.e, \
        :math:`T_i <= T_j`, with :math:`i < j`. Used only if property \
        correlation is not injective.

        Parameters
        ----------
        property_name : str
            Name of the property
        root_index : int
            Index of the temperature root to use
        """
        cls._roots_to_use[property_name] = root_index

    @classmethod
    def set_custom_properties_path(cls, file_path: str) -> None:
        """
        Sets the absolute path of the file where looking for \
        custom properties.

        Parameters
        ----------
        file_path : str
            absolute path of the file where custom properties are implemented
        """
        # Exit if the file passed as argument does not exist
        if (not os.path.isfile(file_path)):
            warnings.warn(f"'{file_path}' provided file not found!"
                          "\nPlease check the file path and try again!"
                          "\nNo custom property added.", stacklevel=5)
            return
        char = '\\' if 'Windows' in platform.system() else '/'
        res = file_path.split(char)
        file_name = res[-1][:-3]
        path = file_path[:-len(res[-1])]
        if path not in cls._custom_properties_path:
            cls._custom_properties_path[path] = [file_name]
        else:
            cls._custom_properties_path[path].append(file_name)

    @classmethod
    def correlations_to_use(cls) -> Dict[str, str]:
        """
        Returns the dictionary defining the correlation used for the \
        corresponding property. Only properties are considered for \
        which a specific correlation has been chosen a priori.

        Returns
        -------
        Dict[str, str]
        """
        return copy.deepcopy(cls._correlations_to_use)

    @classmethod
    def roots_to_use(cls) -> Dict[str, int]:
        """
        Returns the dictionary containing, for each specified property, \
        the index of the root to use for identifying the temperature \
        of the liquid metal. Useful when the initialization is \
        performed from a property whose correlation is not injective.

        Returns
        -------
        Dict[str, int]
        """
        return copy.deepcopy(cls._roots_to_use)

    def __compute_T(self, input_value: float, input_property: str) -> float:
        """
        Computes the temperature in [K] that is then set as value
        of the object property

        Parameters
        ----------
        input_value : float
            value of the property used to compute the temperature
        input_property : str
            name of the property used to perform the calculation
        """
        # Manage the simplest case
        if input_property == 'T':
            return input_value

        # Retrieve the correlation to solve
        function_of_T = self.__properties[input_property].correlation
        if function_of_T is None:
            raise UnboundLocalError("No correlation found for property "
                                    f"{input_property}! The temperature "
                                    "value can not be computed!")

        def function_to_solve(T: float, target: float) -> float:
            return function_of_T(T, self.__p) - target

        # Retrieve the initial guess, if any
        helper = self.__properties[input_property].initialization_helper
        if helper is not None and helper(input_value) is not None:
            self._guess = helper(input_value) or 0.0

        # Solve the correlation-derived function depending on the
        # injectivity of the property correlation
        if self.__properties[input_property].is_injective:
            index = 0
            res, _, ier, msg = fsolve(function_to_solve, x0=[self._guess],
                                      args=(input_value), xtol=1e-10,
                                      full_output=True)
        else:
            index = (self._roots_to_use[input_property]
                     if input_property in self._roots_to_use else 0)
            res, _, ier, msg = fsolve(function_to_solve,
                                      x0=[self._guess, 3*self._guess],
                                      args=(input_value), xtol=1e-10,
                                      full_output=True)
        # Raise an exception in case the solver did not converge
        if ier == 0:
            raise RuntimeError(f"Error: {msg}\n"
                               "The temperature value can not be computed!")
        # Select the desired root
        if len(res) > index - 1:
            return res[index]
        return res[0]

    def __fill_instance_properties(self) -> None:
        """
        Fills instance properties.
        """
        # Build the dict attribute storing all the property objects
        # loaded from loaded modules and the dict attribute storing
        # all the corresponding available correlations. Both these actions
        # are performed only once, when an instance is built, that is,
        # when the property dict attribute is empty.
        if len(self._available_properties_dict) == 0:
            available_properties_list = self.__load_properties()
            available_properties_list += self.__load_custom_properties()
            self._available_properties_dict = {e.name + '__' +
                                               e.correlation_name: e for e in
                                               available_properties_list}
            self._available_correlations_dict = \
                self.__extract_available_correlations(
                    available_properties_list)

        for key, property_object in self._available_properties_dict.items():
            name = key.split("__")[0]
            # Add the property in case the specific correlation is not
            # specified or it is specified and the correlation names
            # does not match with what already stored
            if not self.__corr2use or name not in self.__corr2use.keys()\
                    or key.split("__")[1] == self.__corr2use[name]:
                self.__add_property(property_object)

        self.__align_corrs_to_properties()

    def __fill_instance_attributes(self, property_name: str,
                                   property_value: float) -> None:
        """
        Fills all the class attributes.

        Parameters
        ----------
        property_name : str
            name of the property the liquid metal instance
            is initialized upon
        property_value: float
            value of the property the liquid metal instance
            is initialized upon
        """
        valid_prop = set(['T'] + [p.split("__")[0] for p in
                                  self._available_properties_dict])
        if property_name not in valid_prop:
            list_to_print = "\n\n"
            list_to_print += '\n'.join(valid_prop)
            list_to_print += "\n\n"
            raise ValueError("Initialization can be done only with one of "
                             f"the following properties:{list_to_print}"
                             f"{property_name} was provided")

        temperature = self.__compute_T(property_value, property_name)
        self.__assign_T(temperature)

    def __assign_T(self, T: float) -> None:
        """
        Function used to set temperature, checking if temperature value
        is valid, i.e., strictly positive and (if yes) inside
        the range of melting and boiling temperature.

        Parameters
        ----------
        T : float
            Temperature in [K]
        """
        temp_ok, error_message = self.check_temperature(T)
        if not temp_ok:
            raise ValueError(error_message)
        self.__T = T

    def __assign_p(self, p: float) -> None:
        """
        Function used to set pressure, checking if
        pressure value is valid, i.e., strictly positive.

        Parameters
        ----------
            p : float
            Pressure in [Pa]
        """
        if p <= 0:
            raise ValueError("Pressure must be strictly positive, "
                             f"{p:.2f} [Pa] was provided")
        self.__p = p

    def __add_property(self, property_object: PropertyInterface) -> None:
        """
        Adds the property to class attributes. In particular, it adds
        '<prpertyObject.name>_info' as class method to get additional
        information on property. Moreover it adds property_object
        to instance dictionary which will be used in dunder __getattr__
        to return attribute '<prpertyObject.name>'.

        Parameters
        ----------
        property_object : :class:`_properties.PropertyInterface`
            Object which inherits from :class:`_properties.PropertyInterface`
        """
        key = property_object.name
        self.__properties[key] = property_object
        setattr(self, property_object.name+"_info",
                lambda: self.__properties[key].info(self.__T, self.__p,
                                                    True, 0))

    def __align_corrs_to_properties(self) -> None:
        """
        This method updates the instance correlation dictionary by
        aligning it to the instance property objects dict. In particular,
        it cleans the dict containing the correlations to use and,
        accordingly, it adapts the property objects dict
        """
        # Copy the corrs dict for freezing the dict to loop over
        __corr2use_ref = copy.deepcopy(self.__corr2use)
        for key in __corr2use_ref.keys():
            corr_name = __corr2use_ref[key]
            is_in_default = key in self._default_corr_to_use

            if key not in self.__properties:
                if not is_in_default:
                    warnings.warn(f"Could not find '{key}' property "
                                  f"implementing '{corr_name}' correlation. "
                                  f"\nGoing to restore {key} property from "
                                  f"the {type(self)}-related modules, "
                                  "if any.",
                                  stacklevel=5)
                    self.__remove_property(key)
                    if key in self._available_correlations_dict:
                        self.__add_property(
                            self._available_properties_dict[
                                key + "__" +
                                self._available_correlations_dict[key][-1]])
                else:
                    def_corr_name = self._default_corr_to_use[key]
                    warnings.warn(f"Could not find property '{key}' "
                                  f"implementing '{corr_name}' correlation. "
                                  "\nGoing to restore default correlation "
                                  f"'{def_corr_name}'.",
                                  stacklevel=5)
                    self.__corr2use[key] = def_corr_name
                    self.__add_property(
                        self._available_properties_dict[
                            key + "__" + def_corr_name])
            else:
                if corr_name != self.__properties[key].correlation_name:
                    warnings.warn(f"Could not find property '{key}' "
                                  f"implementing '{corr_name}' correlation. "
                                  "\nGoing to remove it from correlations "
                                  "to use.",
                                  stacklevel=5)
                    if is_in_default:
                        self.__corr2use[key] = \
                            self.__properties[key].correlation_name
                    else:
                        self.__remove_property(key)

    @classmethod
    def __load_custom_properties(cls) -> List[PropertyInterface]:
        """
        Load custom property objects

        Returns
        -------
        list
            list of property objects, i.e. of classes which inherit from
            :class:`_properties.PropertyInterface`
        """
        customproperty_obj_list = []
        modules = []
        for path, modules_list in cls._custom_properties_path.items():
            if path not in sys.path:
                sys.path.append(path)
            for module in modules_list:
                importlib.import_module(module)
                modules.append(module)
            customproperty_obj_list += cls.__load_properties(modules)
        return customproperty_obj_list

    @classmethod
    def __load_properties(cls,
                          modules: Union[List[str], None] = None
                          ) -> List[PropertyInterface]:
        """
        Loads property objects corresponding to liquid metal. The list of
        module names can be passed as argument, otherwise the class-related
        list is adopted.

        Parameters
        ----------
        modules : :obj:`typing.List`, optional
            list of module names to read the property objects from; if
            `None`, the class-related list is adopted. By default, `None`
            is passed.

        Returns
        -------
        list
            list of property objects, i.e. of classes which inherit from
            :class:`_properties.PropertyInterface`
        """
        # Consider default modules if none is provided
        if modules is None:
            modules = cls._properties_modules_list

        def is_valid(obj):
            '''
            Predicate for filtering the modules to load
            '''
            return inspect.isclass(obj) and obj is not PropertyInterface \
                and not inspect.isabstract(obj) \
                and issubclass(obj, PropertyInterface)

        # Filter any empty module
        eff_modules = [module for module in modules if module]
        # Collect all valid properties neglecting duplicates
        mod = []
        for module in eff_modules:
            mod += inspect.getmembers(sys.modules[module], is_valid)
        mod_set = set(list(map(list, zip(*mod)))[1])
        # Build property instances and add them to the list to return
        prop_list = []
        for prop in mod_set:
            prop_obj = prop()
            # Not allowed properties whose name begins with "__"
            if not prop_obj.name[:2] == '__':
                prop_list.append(prop_obj)
        return prop_list

    @staticmethod
    def __extract_available_correlations(
            prop_obj_list: List[PropertyInterface]) -> Dict[str, List[str]]:
        """
        Private static method for extracting the available correlations
        from the list collecting all the available property classes.

        Parameters
        ----------
        prop_obj_list : :obj:`typing.List`
            list of :class:`_properties.PropertyInterface` instances
            which to extract the available correlations from

        Returns
        -------
        dict
            dictionary collecting all the property class names as keys
            together with the list collecting the corresponding
            available correlation names as values
        """
        avail_corrs = defaultdict(list)
        for prop in prop_obj_list:
            avail_corrs[prop.name].append(prop.correlation_name)
        return avail_corrs

    def __remove_property(self, property_name: str) -> None:
        """
        Private method for removing the property name passed
        as argument from both the instance and the class dicts
        storing the properties currently used together with
        their corresponding correlation.

        Parameters
        ----------
        property_name : str
            name of the property to remove from both the instance and
            the class dicts storing the properties currently used together with
            their corresponding correlation.

        Returns
        -------
        None
        """
        self.__corr2use.pop(property_name)
        self._correlations_to_use.pop(property_name, None)

    @abstractmethod
    def _set_constants(self) -> None:
        """
        Sets the class constants
        """
        raise NotImplementedError(f"{type(self).__name__}._set_constants "
                                  "NOT IMPLEMENTED")

    def __getattr__(self, name: str):
        if name[:2] == '__' or name not in self.__properties:
            raise AttributeError(f"'{type(self).__name__}' object "
                                 f"has no attribute '{name}'")

        return self.__properties[name].correlation(self.__T, self.__p, True)

    def __str__(self) -> str:
        rvalue = (f"{type(self).__name__} liquid metal "
                  f"@(T={self.T:.2f} [K], p={self.p:.2f} [Pa])\n")
        rvalue += "\nConstants:\n"
        rvalue += f"\tMelting Temperature: {self.T_m0:.2f} [K]\n"
        rvalue += f"\tBoiling Temperature: {self.T_b0:.2f} [K]\n"
        rvalue += f"\tMelting latent heat: {self.Q_m0:.2f} [J/kg]\n"
        rvalue += f"\tVaporisation heat: {self.Q_b0:.2f} [J/kg]\n"
        rvalue += f"\tMolar mass: {self.M:.2f} [g/mol]\n"
        rvalue += "\nThermophysical properties:\n"
        for key in self.__properties:
            prop_name = key.replace("_"+type(self).__name__, "")
            info = getattr(self, prop_name+"_info")(print_info=False, n_tab=1)
            rvalue += info + "\n"
        return rvalue

    def __repr__(self) -> str:
        rvalue = f"{type(self).__name__}(T={self.T:.2f}, p={self.p:.2f}, "
        for key in self.__properties:
            attr_value = getattr(self, key)
            if attr_value < 1e-2:
                rvalue += f"{key}={attr_value:.2e}, "
            else:
                rvalue += f"{key}={attr_value:.2f}, "
        rvalue = rvalue[:-2]
        rvalue += ")"
        return rvalue
