from scipy.optimize import fsolve
import math
from ._pyll import ZERO_C_IN_K, CELSIUS_SYMBOL
from ._pyll import KELVIN_SYMBOL, MELTING_TEMPERATURE
from ._pyll import MELTING_LATENT_HEAT, BOILING_TEMPERATURE
from ._pyll import VAPORISATION_HEAT
from ._utils import p_s, delta_h, sigma, rho, alpha, u_s
from ._utils import beta_s, cp, mi


def _get_temperature_in_kelvin(temperature, units):
    """
    Converts input temperature in Kelvin, raising value error
    if units provided are neither 'K' or '°C'

    Parameters
    ----------
    T : float
        Temperature
    temperature_units : str
        Units used to specify temperature. Can be 'K' or '°C' for
        Kelvin and Celsius respectively

    Returns
    -------
    rvalue : float
        Temperature in K
    """
    rvalue = 0
    if units == CELSIUS_SYMBOL:
        rvalue = temperature + ZERO_C_IN_K
    elif units == KELVIN_SYMBOL:
        rvalue = temperature
    else:
        raise ValueError("Temperature units must be one of {:s}, {:s}".
                         format(CELSIUS_SYMBOL, KELVIN_SYMBOL))

    return rvalue


class LeadProperties(object):
    """
    Class to model lead properties at a given temperature

    Parameters
    ----------
    T : float
        Temperature
    temperature_units : str
        Units used to specify temperature. Can be 'K' or '°C' for
        Kelvin and Celsius respectively
    """
    __T = 0
    __T_assigned = False
    __T_m0 = 0
    __Q_m0 = 0
    __T_b0 = 0
    __Q_b0 = 0
    __p_s = 0
    __sigma = 0
    __rho = 0
    __alpha = 0
    __u_s = 0
    __beta_s = 0
    __delta_h = 0
    __mi = 0

    def __init__(self, T, temperature_units=KELVIN_SYMBOL):
        self.__fill_class_attributes(T, temperature_units)

    @property
    def T(self):
        """
        float : temperature used to compute properties [K]
        """
        return self.__T

    @property
    def T_in_celsius(self):
        """
        float : temperature used to compute properties [°C]
        """
        return self.T - ZERO_C_IN_K

    @property
    def T_assigned(self):
        """
        bool : true if temperature correctly assigned, false otherwise
        """
        return self.__T_assigned

    @property
    def T_m0(self):
        """
        float : lead melting temperature [K]
        """
        return self.__T_m0

    @property
    def Q_m0(self):
        """
        float : lead melting latent heat [J/kg]
        """
        return self.__Q_m0

    @property
    def T_b0(self):
        """
        float : lead boiling temperature [K]
        """
        return self.__T_b0

    @property
    def Q_b0(self):
        """
        float : lead vaporisation heat [J/kg]
        """
        return self.__Q_b0

    @property
    def p_s(self):
        """
        float : lead saturation vapour pressure [Pa]
        """
        return self.__p_s

    @property
    def sigma(self):
        """
        float : lead surface tension [N/m]
        """
        return self.__sigma

    @property
    def rho(self):
        """
        float : lead density [kg/m^3]
        """
        return self.__rho

    @property
    def alpha(self):
        """
        float : lead thermal expansion coefficient [1/K]
        """
        return self.__alpha

    @property
    def u_s(self):
        """
        float : sound velocity in lead [m/s]
        """
        return self.__u_s

    @property
    def beta_s(self):
        """
        float : lead isentropic compressibility [1/Pa]
        """
        return self.__beta_s

    @property
    def cp(self):
        """
        float : lead specific heat capacity [J/(kg*K)]
        """
        return self.__cp

    @property
    def delta_h(self):
        """
        float : lead specific enthalpy difference from melting point [J/kg]
        """
        return self.__delta_h

    @property
    def mi(self):
        """
        float : lead dynamic viscosity [Ps*s]
        """
        return self.__mi

    def __fill_class_attributes(self, T, temperature_units):
        """
        Fills all the class attributes.

        Parameters
        ----------
        T : float
            Temperature
        temperature_units : str
            Units used to specify temperature. Can be 'K' or '°C' for
            Kelvin and Celsius respectively
        """
        self.__assign_T(T, temperature_units)

        # continue if temperature was correctly assigned
        if self.T_assigned:
            self.__T_m0 = MELTING_TEMPERATURE
            self.__Q_m0 = MELTING_LATENT_HEAT
            self.__T_b0 = BOILING_TEMPERATURE
            self.__Q_b0 = VAPORISATION_HEAT
            self.__p_s = p_s(self.T)
            self.__sigma = sigma(self.T)
            self.__rho = rho(self.T)
            self.__alpha = alpha(self.T)
            self.__u_s = u_s(self.T)
            self.__beta_s = beta_s(self.T)
            self.__cp = cp(self.T)
            self.__delta_h = delta_h(self.T)
            self.__mi = mi(self.T)

    def __assign_T(self, T, temperature_units):
        """
        Function used to set class temperature, checking if
        temperature value in K is strictly positive

        Parameters
        ----------
        T : float
            Temperature
        temperature_units : str
            Units used to specify temperature. Can be 'K' or '°C' for
            Kelvin and Celsius respectively
        """
        temp = _get_temperature_in_kelvin(T, temperature_units)

        if temp > 0:
            self.__T_assigned = True
            self.__T = temp
        else:
            raise ValueError("Temperature in Kelvin must be strictly positive,\
                             {:7.2f} [K] was provided".format(temp))


class _LeadPropertiesFromX(LeadProperties):
    """
    Class to model lead properties from one of its properties.

    Parameters
    ----------
    function_of_T : function
        function that implements the dependency of the property on temperature
        in [K]
    target : float
        value of the property
    guess : float
        initial guess of the temperature in [K]
        that returns property target value
    """
    def __init__(self, function_of_T, target, guess=MELTING_TEMPERATURE*1.5):

        def function_to_solve(T, target):
            return function_of_T(T) - target

        temp = fsolve(function_to_solve, x0=[guess], args=[target])[0]
        super().__init__(temp, KELVIN_SYMBOL)


class LeadPropertiesP_s(_LeadPropertiesFromX):
    """
    Class to model lead properties from saturation vapour pressure

    Parameters
    ----------
    saturation_pressure : float
        value of the saturation vapour pressure in [Pa]
    guess : float
        initial guess of the temperature in [K]
        that returns property target value
    """
    def __init__(self, saturation_pressure, guess=MELTING_TEMPERATURE*1.5):
        super().__init__(p_s, saturation_pressure, guess)


class LeadPropertiesSigma(_LeadPropertiesFromX):
    """
    Class to model lead properties from surface tension

    Parameters
    ----------
    surface_tension : float
        value of surface tension [N/m]
    guess : float
        initial guess of the temperature in [K]
        that returns property target value
    """
    def __init__(self, surface_tension, guess=MELTING_TEMPERATURE*1.5):
        super().__init__(sigma, surface_tension, guess)


class LeadPropertiesRho(_LeadPropertiesFromX):
    """
    Class to model lead properties from density

    Parameters
    ----------
    density : float
        value of density [kg/m^3]
    guess : float
        initial guess of the temperature in [K]
        that returns property target value
    """
    def __init__(self, density, guess=MELTING_TEMPERATURE*1.5):
        super().__init__(rho, density, guess)


class LeadPropertiesAlpha(_LeadPropertiesFromX):
    """
    Class to model lead properties from thermal expansion coefficient

    Parameters
    ----------
    expansion_coefficient : float
        value of temperature expansion coefficient [1/K]
    guess : float
        initial guess of the temperature in [K]
        that returns property target value
    """
    def __init__(self, expansion_coefficient, guess=MELTING_TEMPERATURE*1.5):
        super().__init__(alpha, expansion_coefficient, guess)


class LeadPropertiesU_s(_LeadPropertiesFromX):
    """
    Class to model lead properties from sound velocity

    Parameters
    ----------
    sound_velocity : float
        value of sound velocity [m/s]
    guess : float
        initial guess of the temperature in [K]
        that returns property target value
    """
    def __init__(self, sound_velocity, guess=MELTING_TEMPERATURE*1.5):
        super().__init__(u_s, sound_velocity, guess)


class LeadPropertiesBeta_s(_LeadPropertiesFromX):
    """
    Class to model lead properties from isentropic compressibility

    Parameters
    ----------
    isentropic_compressibility : float
        value of isentropic compressibility [1/Pa]
    guess : float
        initial guess of the temperature in [K]
        that returns property target value
    """
    def __init__(self, isentropic_compressibility,
                 guess=MELTING_TEMPERATURE*1.5):
        super().__init__(beta_s, isentropic_compressibility, guess)


class LeadPropertiesCp(_LeadPropertiesFromX):
    """
    Class to model lead properties from specific heat capacity

    Parameters
    ----------
    specific_heat : float
        value of specific heat capacity [J/(kg*K)]
    guess : float
        initial guess of the temperature in [K]
        that returns property target value
    """
    def __init__(self, specific_heat, guess=MELTING_TEMPERATURE*1.5):
        super().__init__(cp, specific_heat, guess)


class LeadPropertiesDelta_h(_LeadPropertiesFromX):
    """
    Class to model lead properties from specifc enthalpy
    (in respect to lead melting point)

    Parameters
    ----------
    enthalpy : float
        value of specifc enthalpy [J/kg]
    guess : float
        initial guess of the temperature in [K]
        that returns property target value
    """
    def __init__(self, enthalpy, guess=MELTING_TEMPERATURE*1.5):
        super().__init__(delta_h, enthalpy, guess)


class LeadPropertiesMi(_LeadPropertiesFromX):
    """
    Class to model lead properties from dynamic viscosity

    Parameters
    ----------
    dynamic_viscosity : float
        value of dynamic viscosity [Pa*s]
    guess : float
        initial guess of the temperature in [K]
        that returns property target value
    """
    def __init__(self, dynamic_viscosity, guess=MELTING_TEMPERATURE*1.5):
        super().__init__(mi, dynamic_viscosity, guess)
