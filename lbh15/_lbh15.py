"""Module with the definition of liquid metal object base class,
i.e., LiquidMetalInterface"""
import warnings
import sys
import inspect
import importlib
import platform
import copy
from abc import ABC, abstractmethod
from .properties.interface import PropertyInterface
from ._constants import P_ATM


class LiquidMetalInterface(ABC):
    """
    Abstract class that defines liquid metal properties object

    Parameters
    ----------
    p : float, optional
        Pressure in [Pa], by default atmospheric pressure, i.e.,
        101325.0 Pa
    **kwargs : dict
        Dictionary that specifies the quantity from which the parameter shall
        be initialized. The default available ones are:

        - 'T' : temperature [K]
        - 'p_s' : saturation vapour pressure [Pa]
        - 'sigma' : surface tension [N/m]
        - 'rho' : density [Kg/m^3]
        - 'alpha' : thermal expansion coefficient [1/K]
        - 'u_s': speed of sound [m/s]
        - 'beta_s' : isentropic compressibility [1/Pa]
        - 'cp' : specific heat capacity [J/(kg*K)]
        - 'h' : specific enthalpy (in respect to melting point) [J/kg]
        - 'mu' : dynamic viscosity [Pa*s]
        - 'r' : electrical resistivity [Ohm*m]
        - 'k' : thermal conductivity [W/(m*K)]
    """
    _T_m0 = 0
    _Q_m0 = 0
    _T_b0 = 0
    _Q_b0 = 0
    _guess = 0
    _correlations_to_use = {}
    _roots_to_use = {}
    _default_corr_to_use = {}
    _properties_module = ""
    __p = 0
    __T = 0
    __custom_properties_path = {}

    def __init__(self, p=P_ATM, **kwargs):
        self.__assign_p(p)
        self.__properties = {}
        self.__corr2use = copy.deepcopy(self.__class__._correlations_to_use)
        self.__fill_instance_properties()
        self.__fill_class_attributes(kwargs)

    @property
    def T_m0(self):
        """
        float : melting temperature [K]
        """
        return self._T_m0

    @property
    def Q_m0(self):
        """
        float : melting latent heat [J/kg]
        """
        return self._Q_m0

    @property
    def T_b0(self):
        """
        float : boiling temperature [K]
        """
        return self._T_b0

    @property
    def Q_b0(self):
        """
        float : vaporisation heat [J/kg]
        """
        return self._Q_b0

    @property
    def p(self):
        """
        float : pressure adopted for property calculation, i.e.,
        atmospheric pressure
        """
        return self.__p

    @p.setter
    def p(self, p):
        """
        Set liquid metal pressure

        Parameters
        ----------
        p : float
            Pressure in [Pa]
        """
        self.__assign_p(p)

    @property
    def T(self):
        """
        float : temperature used to compute properties [K]
        """
        return self.__T

    @T.setter
    def T(self, T):
        """
        Set liquid metal temperature

        Parameters
        ----------
        T : float
            Temperature in [K]
        """
        self.__assign_T(T)

    @property
    def Pr(self):
        """
        float : Prandtl number [-]
        """
        return self.cp * self.mu / self.k

    @property
    def correlations_used(self):
        """
        Returns the dictionary with the specific
        correlation used for each specified property

        Returns
        -------
        dict
        """
        return copy.deepcopy(self.__corr2use)

    def change_correlation_to_use(self, property_name, correlation_name):
        """
        Changes property correlation, if property is defined as instance
        attribute.

        Parameters
        ----------
        property_name : str
            Name of the thermophysical property
        correlation_name : str
            Name of the correlation
        """
        key = self.__generate_key(property_name)
        if (key in self.__properties and
                self.__properties[key].correlation_name != correlation_name):
            self.__corr2use[property_name] = correlation_name
            self.__fill_instance_properties()

    def check_temperature(self, T):
        """
        Checks that the provided temperature
        belongs to the correct temperature range, i.e.,
        liquid temperature range.

        Parameters
        ----------
        T : float
            Temperature in [K]

        Returns
        -------
        rvalue : bool
            True if check is ok, False otherwise
        error_message : str
            Contains the error message (if any) associated
            to the temperature check
        """
        if self.T_m0 < T < self.T_b0:
            rvalue = True
            error_message = ""
        else:
            rvalue = False
            if T >= self.T_b0:
                error_message = ("Temperature must be smaller than "
                                 f"boiling temperature ({self.T_b0:.2f} [K]), "
                                 f"{T:.2f} [K] was provided")
            elif 0 < T <= self.T_m0:
                error_message = ("Temperature must be larger than "
                                 f"melting temperature ({self.T_m0:.2f} [K]), "
                                 f"{T:.2f} [K] was provided")
            else:
                error_message = ("Temperature must be "
                                 "strictly positive, "
                                 f"{T:.2f} [K] was provided")

        return rvalue, error_message

    @classmethod
    def properties_for_initialization(cls):
        """
        List of available properties that can be used for
        initialization

        Returns
        -------
        list
        """
        obj_list = cls.__load_properties()
        obj_list += cls.__load_custom_properties()
        rvalue = ['T'] + [obj_list[i].name for i in range(len(obj_list))]
        return list(dict.fromkeys(rvalue))

    @classmethod
    def correlations_available(cls):
        """
        Dictionary of correlations available for each property

        Returns
        -------
        dict
        """
        obj_list = cls.__load_properties()
        obj_list += cls.__load_custom_properties()
        rvalue = {}
        for obj in obj_list:
            corr_name = obj.correlation_name
            if obj.name in rvalue:
                if isinstance(rvalue[obj.name], list):
                    rvalue[obj.name].append(corr_name)
                else:
                    rvalue[obj.name] = [rvalue[obj.name]] + [corr_name]
            else:
                rvalue[obj.name] = corr_name
        return rvalue

    @classmethod
    def set_correlation_to_use(cls, property_name, correlation_name):
        """
        Set specific correlation to use for property

        Parameters
        ----------
        property_name : str
            Name of the property
        correlation_name : str
            Name of the correlation
        """
        cls._correlations_to_use[property_name] = correlation_name

    @classmethod
    def set_root_to_use(cls, property_name, root_index):
        """
        Set which temperature root shall be used for initialization
        from property. Temperature roots are sorted in ascending order, i.e,
        T_i <= T_j with i < j. Used only if property correlation
        is not injective

        Parameters
        ----------
        property_name : str
            Name of the property
        root_index : int
            Index used to choose the temperature root
        """
        cls._roots_to_use[property_name] = root_index

    @classmethod
    def set_custom_properties_path(cls, file_path):
        """
        Set absolute path of file where looking for custom properties

        Parameters
        ----------
        file_path : str
            absolute path of file where custom properties are implemented
        """
        char = '/' if 'Linux' in platform.system() else '\\'
        res = file_path.split(char)
        file_name = res[-1][:-3]
        path = file_path[:-len(res[-1])]
        lm_name = cls.__name__
        if lm_name not in cls.__custom_properties_path:
            cls.__custom_properties_path[lm_name] = {}
        cls.__custom_properties_path[lm_name][path] = file_name

    @classmethod
    def correlations_to_use(cls):
        """
        Returns the dictionary with the specific
        correlation to use for each specified property

        Returns
        -------
        dict
        """
        return copy.deepcopy(cls._correlations_to_use)

    @classmethod
    def roots_to_use(cls):
        """
        Returns the dictionary with temperature
        roots to use for each specified property

        Returns
        -------
        dict
        """
        return copy.deepcopy(cls._roots_to_use)

    def __compute_T(self, input_value, input_property):
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
        if input_property == 'T':
            rvalue = input_value
        else:
            function_of_T = None
            helper = None
            is_injective = False
            key = self.__generate_key(input_property)
            if key in self.__properties:
                function_of_T = self.__properties[key].correlation
                helper = self.__properties[key].initialization_helper
                is_injective = self.__properties[key].is_injective

            if function_of_T is not None:
                from scipy.optimize import fsolve

                if helper(input_value) is not None:
                    self._guess = helper(input_value)

                def function_to_solve(T, target):
                    return function_of_T(T, self.__p) - target

                if is_injective:
                    res = fsolve(function_to_solve, x0=[self._guess],
                                 args=(input_value), xtol=1e-10)
                    rvalue = res[0]
                else:
                    index = (self._roots_to_use[input_property]
                             if input_property in self._roots_to_use
                             else 0)
                    res = fsolve(function_to_solve,
                                 x0=[self._guess, 3*self._guess],
                                 args=(input_value), xtol=1e-10)
                    if len(res) > index - 1:
                        rvalue = res[index]
                    else:
                        rvalue = res[0]

        return rvalue

    def __fill_instance_properties(self):
        """
        Fills instance properties.
        """
        property_obj_list = self.__load_properties()
        property_obj_list += self.__load_custom_properties()
        for property_object in property_obj_list:
            # always add property if specific correlation is not specified
            name = property_object.name
            add_property = (not self.__corr2use or
                            name not in self.__corr2use.keys())
            # if correlation was specified, check that correlation names match
            if not add_property:
                add_property = (property_object.correlation_name ==
                                self.__corr2use[name])
            if add_property:
                self.__add_property(property_object)

        keys_to_remove = self.__check_properties()
        for key_to_remove in keys_to_remove:
            self.__corr2use.pop(key_to_remove)
            if key_to_remove in self._correlations_to_use:
                self._correlations_to_use.pop(key_to_remove)

    def __fill_class_attributes(self, kwargs):
        """
        Fills all the class attributes.

        Parameters
        ----------
        T : float
            Temperature in [K]
        """
        if len(kwargs) != 1:
            raise ValueError("One and only one property at "
                             "time can be used for initialization. "
                             f"{len(kwargs)} were provided")

        valid_prop = self.properties_for_initialization()
        input_property = list(kwargs.keys())[0]
        input_value = kwargs[input_property]
        if input_property not in valid_prop:
            list_to_print = "\n\n"
            for sym in valid_prop:
                list_to_print += sym+"\n"
            list_to_print += "\n"
            raise ValueError("Initialization can be done only with one of "
                             f"the following properties:{list_to_print}"
                             f"{input_property} was provided")

        self._set_constants()
        temperature = self.__compute_T(input_value, input_property)
        self.__assign_T(temperature)

    def __assign_T(self, T):
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
        if temp_ok:
            self.__T = T
        else:
            raise ValueError(error_message)

    def __assign_p(self, p):
        """
        Function used to set pressure, checking if
        pressure value is valid, i.e., strictly positive.

        Parameters
        ----------
            p : float
            Pressure in [Pa]
        """
        if p > 0:
            self.__p = p
        else:
            raise ValueError("Pressure must be "
                             "strictly positive, "
                             f"{p:.2f} [Pa] was provided")

    def __add_property(self, property_object):
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
        key = self.__generate_key(property_object.name)
        self.__properties[key] = property_object

        def new_property_info(print_info=True, n_tab=0):
            return self.__properties[key].info(self.__T, self.__p,
                                               print_info, n_tab)

        setattr(self, property_object.name+"_info",
                new_property_info)

    def __generate_key(self, property_name):
        """
        Generates the key that will be used to store the property
        in class dictionary

        Parameters
        ----------
        property_name : str
            Name of the property

        Returns
        -------
        str
            Generated key
        """
        return property_name + '_' + type(self).__name__

    def __check_properties(self):
        keys_to_remove = []
        update_properties = False
        for key in self.__corr2use.keys():
            prop_key = self.__generate_key(key)
            corr_name = self.__corr2use[key]
            is_in_default = key in self._default_corr_to_use
            remove_property = False

            if prop_key not in self.__properties:
                if not is_in_default:
                    warnings.warn(f"Could not find property '{key}' "
                                  f"implementing '{corr_name}' correlation. "
                                  "\nGoing to restore package default one, "
                                  "if any.",
                                  stacklevel=5)
                    remove_property = True
                    corr_avail = self.correlations_available()
                    if key in corr_avail:
                        isstr = isinstance(corr_avail[key], str)
                        self.__corr2use[key] = (corr_avail[key] if isstr
                                                else corr_avail[key][-1])
                        update_properties = True
                else:
                    def_corr_name = self._default_corr_to_use[key]
                    warnings.warn(f"Could not find property '{key}' "
                                  f"implementing '{corr_name}' correlation. "
                                  "\nGoing to restore default correlation "
                                  f"'{def_corr_name}'.",
                                  stacklevel=5)
                    self.__corr2use[key] = def_corr_name
                    remove_property = True
                    update_properties = True
            else:
                if corr_name != self.__properties[prop_key].correlation_name:
                    warnings.warn(f"Could not find property '{key}' "
                                  f"implementing '{corr_name}' correlation. "
                                  "\nGoing to remove it from correlations "
                                  "to use.",
                                  stacklevel=5)
                    remove_property = not is_in_default
                    if not remove_property:
                        self.__corr2use[key] = self._default_corr_to_use[key]

            if remove_property:
                keys_to_remove.append(key)

        if update_properties:
            self.__fill_instance_properties()

        return keys_to_remove

    @classmethod
    def __load_properties(cls):
        """
        Loads property objects corresponding to liquid metal

        Returns
        -------
        list
            list of property objects, i.e. of classes which inherit from
            :class:`_properties.PropertyInterface`
        """
        property_obj_list = []
        module = cls._properties_module
        if module:
            for _, obj in inspect.getmembers(sys.modules[module]):
                if inspect.isclass(obj) and obj is not PropertyInterface:
                    if issubclass(obj, PropertyInterface):
                        property_obj_list.append(obj())
        return property_obj_list

    @classmethod
    def __load_custom_properties(cls):
        """
        Load custom property objects

        Returns
        -------
        list
            list of property objects, i.e. of classes which inherit from
            :class:`_properties.PropertyInterface`
        """
        customproperty_obj_list = []
        if cls.__name__ in cls.__custom_properties_path:
            lm_path = cls.__custom_properties_path[cls.__name__]
            for path in lm_path.keys():
                if path not in sys.path:
                    sys.path.append(path)
                module_name = lm_path[path]
                module = importlib.import_module(module_name)
                for _, obj in inspect.getmembers(module):
                    if inspect.isclass(obj) and obj is not PropertyInterface:
                        if issubclass(obj, PropertyInterface):
                            customproperty_obj_list.append(obj())
        return customproperty_obj_list

    @abstractmethod
    def _set_constants(self):
        """
        Sets the class constants
        """
        raise NotImplementedError(f"{type(self).__name__}._set_constants "
                                  "NOT IMPLEMENTED")

    def __getattr__(self, name):
        key = self.__generate_key(name)
        if key not in self.__properties:
            raise AttributeError(f"'{type(self).__name__}' object "
                                 f"has no attribute '{name}'")

        return self.__properties[key].correlation(self.__T, self.__p, True)

    def __str__(self):
        rvalue = (f"{type(self).__name__} liquid metal "
                  f"@(T={self.T:.2f} [K], p={self.p:.2f} [Pa])\n")
        rvalue += "\nConstants:\n"
        rvalue += f"\tMelting Temperature: {self.T_m0:.2f} [K]\n"
        rvalue += f"\tBoiling Temperature: {self.T_b0:.2f} [K]\n"
        rvalue += f"\tMelting latent heat: {self.Q_m0:.2f} [J/kg]\n"
        rvalue += f"\tVaporisation heat: {self.Q_b0:.2f} [J/kg]\n"
        rvalue += "\nThermophysical properties:\n"
        for key in self.__properties:
            prop_name = key.replace("_"+type(self).__name__, "")
            info = getattr(self, prop_name+"_info")(print_info=False, n_tab=1)
            rvalue += info + "\n"
        return rvalue

    def __repr__(self):
        rvalue = f"{type(self).__name__}(T={self.T:.2f}, "
        for key in self.__properties:
            property_name = key.replace("_"+type(self).__name__, "")
            attr_value = getattr(self, property_name)
            if attr_value < 1e-2:
                rvalue += f"{property_name}={attr_value:.2e}, "
            else:
                rvalue += f"{property_name}={attr_value:.2f}, "
        rvalue = rvalue[:-2]
        rvalue += ")"
        return rvalue
