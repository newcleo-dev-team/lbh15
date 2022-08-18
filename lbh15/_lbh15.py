import warnings
from scipy.optimize import fsolve
from scipy.constants import atmosphere
from abc import ABC, abstractmethod, abstractclassmethod

# KEYWORDS
LEAD_KEYWORD = "lead"
BISMUTH_KEYWORD = "bismuth"
LBE_KEYWORD = "lbe"
GURVICH_KEYWORD = 'gurvich1991'
SOBOLEV_KEYWORD = 'sobolev2011'
PROPERTIES_FOR_INITIALIZATION = (['T', 'p_s', 'sigma',
                                  'rho', 'alpha', 'u_s',
                                  'beta_s', 'cp', 'h',
                                  'mu', 'r', 'k'])

# LEAD CONSTANTS
LEAD_MELTING_TEMPERATURE = 600.6  # [K]
LEAD_MELTING_LATENT_HEAT = 23.07e3  # [J/kg]
LEAD_BOILING_TEMPERATURE = 2021  # [K]
LEAD_VAPORISATION_HEAT = 858.6e3  # [J/kg]
LEAD_T_AT_CP_MIN_GURVICH = 1682.522  # [K]
LEAD_T_AT_CP_MIN_SOBOLEV = 1568.665  # [K]
LEAD_CP_MIN_GURVICH = 137.287133  # [J/(kg*K)]
LEAD_CP_MIN_SOBOLEV = 136.348649  # [J/(kg*K)]

# BISMUTH CONSTANTS
BISMUTH_MELTING_TEMPERATURE = 544.6  # [K]
BISMUTH_MELTING_LATENT_HEAT = 53.3e3  # [J/kg]
BISMUTH_BOILING_TEMPERATURE = 1831  # [K]
BISMUTH_VAPORISATION_HEAT = 856.2e3  # [J/kg]
BISMUTH_T_AT_CP_MIN = 1342.753  # [K]
BISMUTH_CP_MIN = 130.151844  # [J/(kg*K)]

# LEAD-BISMUTH-EUTECTIC CONSTANTS
LBE_MELTING_TEMPERATURE = 398.0  # [K]
LBE_MELTING_LATENT_HEAT = 38.6e3  # [J/kg]
LBE_BOILING_TEMPERATURE = 1927  # [K]
LBE_VAPORISATION_HEAT = 856.6e3  # [J/kg]
LBE_T_AT_CP_MIN = 1566.510  # [K]
LBE_CP_MIN = 133.568103  # [J/(kg*K)]


def p_s_initializer(p_s):
    """
    Returns a temperature guess according to the value
    of the saturation vapour pressure

    Parameters
    ----------
    p_s : float
        saturation vapour pressure in [Pa]

    Returns
    -------
    rvalue : float
        Temperature guess in [K]
    """
    if p_s < 1e-2:
        rvalue = 800
    elif p_s >= 1e-2 and p_s < 1e2:
        rvalue = 1200
    else:
        rvalue = 2000

    return rvalue


class LiquidMetalInterface(ABC):
    """
    Abstract class that defines liquid metal properties object

    Parameters
    ----------
    cp_high_range : bool
        True to initialize the object with temperature larger than
        the one corresponding to cp minumum (if present), False otherwise.
        It is used if **kwargs contains 'cp', i.e., if initialization from
        specific heat is required
    **kwargs : dict
        Dictionary that spefifies the quantity from which the parameter shall
        be initialized. The available ones are:

        - 'T' : temperature [K]
        - 'p_s' : saturation vapour pressure [Pa]
        - 'sigma' : surface tension [N/m]
        - 'rho' : density [Kg/m^3]
        - 'alpha' : thermal expansion coefficient [1/K]
        - 'u_s': speed of sound [m/s]
        - 'beta_s' : isentropic compressibility [1/Pa]
        - 'cp' : specific heat capacity [J/(kg*K)]
        - 'h' : specific hentalpy (in respect to melting point) [J/kg]
        - 'mu' : dynamic viscosity [Pa*s]
        - 'r' : electrical resistivity [Ohm*m]
        - 'k' : thermal conductivity [W/(m*K)]
    """
    _T_m0 = 0
    _Q_m0 = 0
    _T_b0 = 0
    _Q_b0 = 0
    __p = 0
    __T = 0
    _guess = 0
    __T_assigned = False
    __cp_high_range = False
    __properties = {}
    __same_name_counter = 0
    _liquid_metal_name = ''
    _correlations_to_use = {}

    def __init__(self, cp_high_range=False, **kwargs):
        self.__cp_high_range = cp_high_range
        self.__fill_class_attributes(kwargs)

    def __new__(cls, cp_high_range=False, **kwargs):
        propertyObjectList = cls._load_properties()
        for propertyObject in propertyObjectList:
            # property must be added if its specific correlation is not specified
            addProperty = (not cls._correlations_to_use or 
                           propertyObject.name not in cls._correlations_to_use.keys())
            # if property was specified then check that correlation names match
            if not addProperty:
                addProperty = (propertyObject.correlation_name ==
                               cls._correlations_to_use[propertyObject.name])
            if addProperty:
                cls.__addProperty(propertyObject)
        
        keys_to_remove = []
        for key in cls._correlations_to_use.keys():
            if not hasattr(cls, key):
                warnings.warn("Could not find property '{:s}' "
                              "implementing '{:s}' correlation. "
                              "Property was not added.\nGoing to remove it from "
                              "correlations_to_use dictionary."
                              .format(key, cls._correlations_to_use[key]),
                              stacklevel=4)
                keys_to_remove.append(key)
        for key_to_remove in keys_to_remove:
            cls._correlations_to_use.pop(key_to_remove)

        obj = object.__new__(cls)
        return obj

    @staticmethod
    def properties_for_initialization():
        """
        List of available properties that can be used for
        initialization

        Returns
        -------
        list
        """
        return PROPERTIES_FOR_INITIALIZATION.copy()

    @classmethod
    def set_correlation_to_use(cls, property_name, correlation_name):
        cls._correlations_to_use[property_name] = correlation_name

    @classmethod
    def correlations_to_use(cls):
        return cls._correlations_to_use

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
    def T_assigned(self):
        """
        bool : true if temperature correctly assigned, false otherwise
        """
        return self.__T_assigned

    @property
    def Pr(self):
        """
        float : Prandtl number [-]
        """
        return self.cp * self.mu / self.k

    @abstractclassmethod
    def _load_properties(cls):
        """
        Loads properties
        """
        raise NotImplementedError("{:s}._load_properties NOT IMPLEMENTED"
                                  .format(type(cls).__name__))

    @abstractmethod
    def _set_constants(self):
        """
        Sets the class constants
        """
        raise NotImplementedError("{:s}._set_constants NOT IMPLEMENTED"
                                  .format(type(self).__name__))

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
            initialization_helper = None
            propertyObjectList = self.__properties
            for key in self.__properties:
                if self.__generate_key(input_property) == key:
                    function_of_T = self.__properties[key]['correlation']
                    initialization_helper = self.__properties[key]['initialization_helper']
                    break

            if function_of_T is not None:
                if initialization_helper(input_value) is not None:
                    self._guess = initialization_helper(input_value)
                def function_to_solve(T, target):
                    return function_of_T(T) - target

                if input_property != 'cp':
                    res = fsolve(function_to_solve, x0=[self._guess],
                                 args=(input_value), xtol=1e-10)
                    rvalue = res[0]
                else:
                    res = fsolve(function_to_solve,
                                 x0=[self._guess, 4*self._guess],
                                 args=(input_value), xtol=1e-10)
                    if len(res) > 0 and self.__cp_high_range:
                        rvalue = res[1]
                    else:
                        rvalue = res[0]

        return rvalue

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
            valid_prop = LiquidMetalInterface.properties_for_initialization()
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
                self.__p = atmosphere
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
            self._T_assigned = True
            self.__T = T
        else:
            if T >= self.T_b0:
                raise ValueError("Temperature must be smaller than "
                                 "boiling temperature ({:.2f} [K]), {:.2f} "
                                 "[K] was provided".format(self.T_b0, T))
            elif T > 0 and T <= self.T_m0:
                raise ValueError("Temperature must be larger than "
                                 "melting temerature ({:.2f} [K]), {:.2f} "
                                 "[K] was provided".format(self.T_m0, T))
            else:
                raise ValueError("Temperature must be "
                                 "strictly positive, "
                                 "{:.2f} [K] was provided".format(T))

    def __check_validity_range(self, validity_range, property_name):
        """
        Checks if temperature is inside validity range of property. If not
        warns the user.

        Parameters
        ----------
        validity_range : list
            List of two elements with lower and upper bound temperature
            of property validity range
        property_name : str
            name of the property
        """
        inside = False
        if self.T >= validity_range[0] and self.T <= validity_range[1]:
            inside = True
        if not inside:
            warnings.warn("The {:s} is requested at "
                          "temperature value of {:.2f} K "
                          "that is not in validity range "
                          "[{:.2f}, {:.2f}] K"
                          .format(property_name, self.T,
                                  validity_range[0], validity_range[1]),
                          stacklevel=3)

    @classmethod
    def __addProperty(cls, propertyObject):
        """
        Adds the property to class attributes. In particular, it adds
        the value as class property with name '<prpertyObject.name>' and
        '<prpertyObject.name>_print_info' as class method to get additional
        information on property

        Parameters
        ----------
        propertyObject : :class:`_properties.PropertyInterface`
            Object which inherits from :class:`_properties.PropertyInterface`
        """
        propDictionary = {}
        propDictionary['correlation'] = propertyObject.correlation
        propDictionary['validity_range'] = propertyObject.range
        propDictionary['units'] = propertyObject.units
        propDictionary['long_name'] = propertyObject.long_name
        propDictionary['description'] = propertyObject.description
        propDictionary['initialization_helper'] = propertyObject.initialization_helper
        key = cls.__generate_key(propertyObject.name)
        cls.__properties[key] = propDictionary

        @property
        def new_property(cls):
            name = propertyObject.name
            validity_range = cls.__properties[key]['validity_range']
            long_name = cls.__properties[key]['long_name']
            cls.__check_validity_range(validity_range, long_name)
            return cls.__properties[key]['correlation'](cls.__T)

        def new_property_print_info(cls, info=''):
            name = propertyObject.name
            value = ("Value: {:.4f} {:s}"
                    .format(cls.__properties[key]['correlation'](cls.__T),
                            cls.__properties[key]['units']))
            validity = ("Validity range: [{:.2f}, {:.2f}] K"
                        .format(cls.__properties[key]['validity_range'][0],
                                cls.__properties[key]['validity_range'][1]))
            long_name = ("Long name: {:s}"
                        .format(cls.__properties[key]['long_name']))
            units = "Units: {:s}".format(cls.__properties[key]['units'])
            description = ("Description:\n{:s}{:s}"
                        .format(2*"\t",
                                cls.__properties[key]['description']))

            if info == '' or info == 'all':
                print("{:s}:".format(name))
                print("\t{:s}".format(value))
                print("\t{:s}".format(validity))
                print("\t{:s}".format(long_name))
                print("\t{:s}".format(units))
                print("\t{:s}".format(description))
            elif info == 'value':
                print("{:s}:".format(name))
                print("\t{:s}".format(value))
            elif info == 'validity_range':
                print("{:s}:".format(name))
                print("\t{:s}".format(validity))
            elif info == 'long_name':
                print("{:s}:".format(name))
                print("\t{:s}".format(long_name))
            elif info == 'units':
                print("{:s}:".format(name))
                print("\t{:s}".format(units))
            elif info == 'description':
                print("{:s}:".format(name))
                print("\t{:s}".format(description))
            else:
                print("Type of info not known. "
                    "Plese select one of the following:\n"
                    "\t'all' or '' to print all info\n"
                    "\t'value' to print the value\n"
                    "\t'validity_range' to print the "
                    "correlation validity range\n"
                    "\t'long_name' to print the full name\n"
                    "\t'description to print the description")

        setattr(cls, propertyObject.name, new_property)
        setattr(cls, propertyObject.name+"_print_info",
                new_property_print_info)

    @classmethod
    def __generate_key(cls, property_name):
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
        return property_name + '_' + cls._liquid_metal_name
