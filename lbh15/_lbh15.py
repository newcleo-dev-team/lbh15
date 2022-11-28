import warnings
import sys
import inspect
import importlib
import platform
import copy
from abc import ABC, abstractmethod, abstractclassmethod
from .properties.interface import PropertyInterface

# KEYWORDS
LEAD_KEYWORD = "lead"
BISMUTH_KEYWORD = "bismuth"
LBE_KEYWORD = "lbe"
GURVICH_KEYWORD = 'gurvich1991'
SOBOLEV_KEYWORD = 'sobolev2011'

# LEAD CONSTANTS
LEAD_MELTING_TEMPERATURE = 600.6  # [K]
LEAD_MELTING_LATENT_HEAT = 23.07e3  # [J/kg]
LEAD_BOILING_TEMPERATURE = 2021  # [K]
LEAD_VAPORISATION_HEAT = 858.6e3  # [J/kg]

# BISMUTH CONSTANTS
BISMUTH_MELTING_TEMPERATURE = 544.6  # [K]
BISMUTH_MELTING_LATENT_HEAT = 53.3e3  # [J/kg]
BISMUTH_BOILING_TEMPERATURE = 1831  # [K]
BISMUTH_VAPORISATION_HEAT = 856.2e3  # [J/kg]

# LEAD-BISMUTH-EUTECTIC CONSTANTS
LBE_MELTING_TEMPERATURE = 398.0  # [K]
LBE_MELTING_LATENT_HEAT = 38.6e3  # [J/kg]
LBE_BOILING_TEMPERATURE = 1927  # [K]
LBE_VAPORISATION_HEAT = 856.6e3  # [J/kg]


class LiquidMetalInterface(ABC):
    """
    Abstract class that defines liquid metal properties object

    Parameters
    ----------
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
    __p = 0
    __T = 0
    __custom_properties_path = {}

    def __init__(self, **kwargs):
        from scipy.constants import atmosphere
        self.__p = atmosphere
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

    @property
    def T(self):
        """
        float : temperature used to compute properties [K]
        """
        return self.__T

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
        if (key in self.__properties.keys() and
                self.__properties[key].correlation_name != correlation_name):
            self._correlations_to_use[property_name] = correlation_name
            self.__fill_instance_properties()

    @classmethod
    def properties_for_initialization(cls):
        """
        List of available properties that can be used for
        initialization

        Returns
        -------
        list
        """
        objList = cls._load_properties()
        objList += cls.__load_custom_properties()
        rvalue = ['T'] + [objList[i].name for i in range(len(objList))]
        return list(dict.fromkeys(rvalue))

    @classmethod
    def correlations_available(cls):
        """
        Dictionary of correlations available for each property

        Returns
        -------
        dict
        """
        objList = cls._load_properties()
        objList += cls.__load_custom_properties()
        rvalue = {}
        for obj in objList:
            corr_name = obj.correlation_name
            if obj.name in rvalue.keys():
                if type(rvalue[obj.name]) == list:
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
        if lm_name not in cls.__custom_properties_path.keys():
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
            propertyObjectList = self.__properties
            is_injective = False
            key = self.__generate_key(input_property)
            if key in self.__properties.keys():
                function_of_T = self.__properties[key].correlation
                helper = self.__properties[key].initialization_helper
                is_injective = self.__properties[key].is_injective

            if function_of_T is not None:
                from scipy.optimize import fsolve

                if helper(input_value) is not None:
                    self._guess = helper(input_value)

                def function_to_solve(T, target):
                    return function_of_T(T) - target

                if is_injective:
                    res = fsolve(function_to_solve, x0=[self._guess],
                                 args=(input_value), xtol=1e-10)
                    rvalue = res[0]
                else:
                    if input_property in self._roots_to_use.keys():
                        index = self._roots_to_use[input_property]
                        res = fsolve(function_to_solve,
                                     x0=[self._guess, 3*self._guess],
                                     args=(input_value), xtol=1e-10)

                        if len(res) > index - 1:
                            rvalue = res[index]
                        else:
                            rvalue = res[0]

        return rvalue

    def __fill_instance_properties(self, **kwargs):
        """
        Fills instance properties.
        """
        propertyObjectList = self._load_properties()
        propertyObjectList += self.__load_custom_properties()
        for propertyObject in propertyObjectList:
            # always add property if specific correlation is not specified
            name = propertyObject.name
            addProperty = (not self.__corr2use or
                           name not in self.__corr2use.keys())
            # if correlation was specified, check that correlation names match
            if not addProperty:
                addProperty = (propertyObject.correlation_name ==
                               self.__corr2use[name])
            if addProperty:
                self.__add_property(propertyObject)

        keys_to_remove = self.__check_properties()
        for key_to_remove in keys_to_remove:
            self.__corr2use.pop(key_to_remove)
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
                             "{:d} were provided".format(len(kwargs)))
        else:
            valid_prop = self.properties_for_initialization()
            input_property = list(kwargs.keys())[0]
            input_value = kwargs[input_property]
            if input_property not in valid_prop:
                list_to_print = "\n\n"
                for sym in valid_prop:
                    list_to_print += sym+"\n"
                list_to_print += "\n"
                raise ValueError("Initialization can be done only with one of "
                                 "the following properties:{:s}"
                                 "{:s} was provided"
                                 .format(list_to_print, input_property))
            else:
                self._set_constants()
                temperature = self.__compute_T(input_value, input_property)
                self.__assign_T(temperature)

    def __assign_T(self, T):
        """
        Function used to set class temperature, checking if
        temperature value in K is strictly positive

        Parameters
        ----------
        T : float
            Temperature in [K]
        """
        if T > self.T_m0 and T < self.T_b0:
            self.__T = T
        else:
            if T >= self.T_b0:
                raise ValueError("Temperature must be smaller than "
                                 "boiling temperature ({:.2f} [K]), {:.2f} "
                                 "[K] was provided".format(self.T_b0, T))
            elif T > 0 and T <= self.T_m0:
                raise ValueError("Temperature must be larger than "
                                 "melting temperature ({:.2f} [K]), {:.2f} "
                                 "[K] was provided".format(self.T_m0, T))
            else:
                raise ValueError("Temperature must be "
                                 "strictly positive, "
                                 "{:.2f} [K] was provided".format(T))

    def __add_property(self, propertyObject):
        """
        Adds the property to class attributes. In particular, it adds
        '<prpertyObject.name>_info' as class method to get additional
        information on property. Moreover it adds propertyObject
        to instance dictionary which will be used in dunder __getattr__
        to return attribute '<prpertyObject.name>'.

        Parameters
        ----------
        propertyObject : :class:`_properties.PropertyInterface`
            Object which inherits from :class:`_properties.PropertyInterface`
        """
        key = self.__generate_key(propertyObject.name)
        self.__properties[key] = propertyObject

        def new_property_info(print_info=True, n_tab=0):
            name = propertyObject.name
            propertyVal = self.__properties[key].correlation(self.__T)
            if propertyVal < 1e-2:
                value = ("Value: {:.2e} {:s}"
                         .format(propertyVal,
                                 self.__properties[key].units))
            else:
                value = ("Value: {:.2f} {:s}"
                         .format(propertyVal,
                                 self.__properties[key].units))
            validity = ("Validity range: [{:.2f}, {:.2f}] K"
                        .format(self.__properties[key].range[0],
                                self.__properties[key].range[1]))
            corr_name = ("Correlation name: '{:s}'"
                         .format(self.__properties[key].correlation_name))
            long_name = ("Long name: {:s}"
                         .format(self.__properties[key].long_name))
            units = "Units: {:s}".format(self.__properties[key].units)
            description = ("Description:\n{:s}{:s}"
                           .format((n_tab+2)*"\t",
                                   self.__properties[key].description))

            all_info = "{:s}{:s}:\n".format(n_tab*"\t", name)
            all_info += "{:s}{:s}\n".format((n_tab+1)*"\t", value)
            all_info += "{:s}{:s}\n".format((n_tab+1)*"\t", validity)
            all_info += "{:s}{:s}\n".format((n_tab+1)*"\t", corr_name)
            all_info += "{:s}{:s}\n".format((n_tab+1)*"\t", long_name)
            all_info += "{:s}{:s}\n".format((n_tab+1)*"\t", units)
            all_info += "{:s}{:s}".format((n_tab+1)*"\t", description)

            if print_info:
                print(all_info)
            else:
                return all_info

        setattr(self, propertyObject.name+"_info",
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
            is_in_default = key in self._default_corr_to_use.keys()
            remove_property = False

            if prop_key not in self.__properties.keys():
                if not is_in_default:
                    warnings.warn("Could not find property '{:s}'."
                                  "Property was not added."
                                  "\nGoing to remove it from correlations "
                                  "to use."
                                  .format(key), stacklevel=5)
                    remove_property = True
                else:
                    def_corr_name = self._default_corr_to_use[key]
                    warnings.warn("Could not find property '{:s}' "
                                  "implementing '{:s}' correlation. "
                                  "\nGoing to restore default correlation "
                                  "'{:s}'."
                                  .format(key, corr_name, def_corr_name),
                                  stacklevel=5)
                    self.__corr2use[key] = def_corr_name
                    update_properties = True
            else:
                if corr_name != self.__properties[prop_key].correlation_name:
                    warnings.warn("Could not find property '{:s}' "
                                  "implementing '{:s}' correlation. "
                                  "\nGoing to remove it from correlations "
                                  "to use."
                                  .format(key, corr_name),
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
    def __load_custom_properties(cls):
        """
        Load custom property objects

        Returns
        -------
        list
            list of property objects, i.e. of classes which inherit from
            :class:`_properties.PropertyInterface`
        """
        customPropertyObjectList = []
        if cls.__name__ in cls.__custom_properties_path.keys():
            lm_path = cls.__custom_properties_path[cls.__name__]
            for path in lm_path.keys():
                if path not in sys.path:
                    sys.path.append(path)
                module_name = lm_path[path]
                module = importlib.import_module(module_name)
                for name, obj in inspect.getmembers(module):
                    if inspect.isclass(obj) and obj is not PropertyInterface:
                        if issubclass(obj, PropertyInterface):
                            customPropertyObjectList.append(obj())
        return customPropertyObjectList

    @abstractmethod
    def _set_constants(self):
        """
        Sets the class constants
        """
        raise NotImplementedError("{:s}._set_constants NOT IMPLEMENTED"
                                  .format(type(self).__name__))

    @abstractclassmethod
    def _load_properties(cls):
        """
        Loads properties
        """
        raise NotImplementedError("{:s}._load_properties NOT IMPLEMENTED"
                                  .format(cls.__name__))

    def __getattr__(self, name):
        key = self.__generate_key(name)
        if key in self.__properties.keys():
            return self.__properties[key].correlation(self.__T, True)
        else:
            raise AttributeError("'{:s}' object has no attribute '{:s}'"
                                 .format(type(self).__name__, name))

    def __str__(self):
        rvalue = ("{:s} liquid metal @T={:.2f} K\n"
                  .format(type(self).__name__, self.T))
        rvalue += "\nConstants:\n"
        rvalue += "\tPressure: {:.2f} [Pa]\n".format(self.p)
        rvalue += "\tMelting Temperature: {:.2f} [K]\n".format(self.T_m0)
        rvalue += "\tBoiling Temperature: {:.2f} [K]\n".format(self.T_b0)
        rvalue += "\tMelting latent heat: {:.2f} [J/kg]\n".format(self.Q_m0)
        rvalue += "\tVaporisation heat: {:.2f} [J/kg]\n".format(self.Q_b0)
        rvalue += "\nThermophysical properties:\n"
        for key in self.__properties.keys():
            prop_name = key.replace("_"+self._liquid_metal_name, "")
            info = getattr(self, prop_name+"_info")(print_info=False, n_tab=1)
            rvalue += info + "\n"
        return rvalue

    def __repr__(self):
        rvalue = "{:s}(T={:.2f}, ".format(type(self).__name__, self.T)
        for key in self.__properties.keys():
            property_name = key.replace("_"+self._liquid_metal_name, "")
            attrValue = getattr(self, property_name)
            if attrValue < 1e-2:
                rvalue += "{:s}={:.2e}, ".format(property_name, attrValue)
            else:
                rvalue += "{:s}={:.2f}, ".format(property_name, attrValue)
        rvalue = rvalue[:-2]
        rvalue += ")"
        return rvalue
