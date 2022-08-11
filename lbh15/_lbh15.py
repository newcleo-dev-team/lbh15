import warnings
from scipy.optimize import fsolve
from scipy.constants import atmosphere
from abc import ABC, abstractmethod

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
    _p = 0
    _T = 0
    _T_assigned = False
    _guess = 0
    __cp_high_range = False
    _propertyNames = []

    def __init__(self, cp_high_range=False, **kwargs):
        self.__properties = {}
        self.__cp_high_range = cp_high_range
        self.__fill_class_attributes(kwargs)

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
        return self._p

    @property
    def T(self):
        """
        float : temperature used to compute properties [K]
        """
        return self._T

    @property
    def T_assigned(self):
        """
        bool : true if temperature correctly assigned, false otherwise
        """
        return self._T_assigned

    @property
    def Pr(self):
        """
        float : Prandtl number [-]
        """
        return self.cp * self.mu / self.k

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

    def __fill_properties(self):
        """
        Fills the class properties
        """
        propertyObjectList = self._load_properties()
        for propertyObject in propertyObjectList:
            self._propertyNames.append(propertyObject.name)
            propDictionary = {}
            propDictionary['value'] = propertyObject.correlation(self.T)
            propDictionary['validity_range'] = propertyObject.range
            propDictionary['units'] = propertyObject.units
            propDictionary['long_name'] = propertyObject.long_name
            propDictionary['description'] = propertyObject.description
            self.__properties[self._propertyNames[-1]] = propDictionary

            @property
            def new_property(self):
                self.__check_validity_range(self.__properties[self._propertyNames[-1]]['validity_range'],
                                            self.__properties[self._propertyNames[-1]]['long_name'])
                return self.__properties[self._propertyNames[-1]]['value']
            
            def new_property_print_info(self, info=''):
                key = self._propertyNames[-1]
                name = "Name: " + key
                value = "Value: " + self.__properties[key]['value'] + " " + self.__properties[key]['units']
                long_name = "Long name: " + self.__properties[key]['description']
                descr = self.__properties[key]['description']
                validity = "Validity range: [" + self.__properties[key]['validity_range'] + "] K"
                units = "Units: " + self.__properties[key]['units']
                if info == '' or info == 'all':
                    print(name)
                    print("\t"+value)
                    print("\t"+long_name)
                    print("\t"+descr)
                    print("\t"+validity)
                    print("\t"+units)
                elif info == 'name':
                    print(name)
                elif info == 'value':
                    print(value)
                elif info == 'long_name':
                    print(long_name)
                elif info == 'description':
                    print(descr)
                elif info == 'validity_range':
                    print(validity_range)
                elif info == 'units':
                    print(units)

            setattr(LiquidMetalInterface, propertyObject.name, new_property)
            setattr(LiquidMetalInterface, propertyObject.name+"_print_info", new_property)

    @abstractmethod
    def _load_properties(self):
        raise NotImplementedError("{:s}._load_properties NOT IMPLEMENTED"
                                  .format(type(self).__name__))

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
            propertyObjectList = self._load_properties()
            for propertyObject in propertyObjectList:
                if input_property == propertyObject.name:
                    function_of_T = propertyObject.correlation
                    break

            if function_of_T is not None:
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
                self._p = atmosphere
                self._set_constants()
                temperature = self.__compute_T(input_value, input_property)
                self.__assign_T(temperature)
                if self.T_assigned:
                    self.__fill_properties()

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
            self._T = T
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
