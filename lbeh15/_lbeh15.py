from scipy.optimize import fsolve

# CONSTANTS
ZERO_C_IN_K = 273.15
CELSIUS_SYMBOL = "degC"
KELVIN_SYMBOL = "K"
LEAD_KEYWORD = "lead"
BISMUTH_KEYWORD = "bismuth"
LBE_KEYWORD = "lbe"

# LEAD CONSTANTS
LEAD_MELTING_TEMPERATURE = 600.6
LEAD_MELTING_LATENT_HEAT = 23.07e3
LEAD_BOILING_TEMPERATURE = 2021
LEAD_VAPORISATION_HEAT = 858.6e3

# BISMUTH CONSTANTS
BISMUTH_MELTING_TEMPERATURE = 544.6
BISMUTH_MELTING_LATENT_HEAT = 53.3e3
BISMUTH_BOILING_TEMPERATURE = 1831
BISMUTH_VAPORISATION_HEAT = 856.2e3

# LEAD-BISMUTH-EUTECTIC CONSTANTS
LBE_MELTING_TEMPERATURE = 398.0
LBE_MELTING_LATENT_HEAT = 38.6e3
LBE_BOILING_TEMPERATURE = 1927
LBE_VAPORISATION_HEAT = 856.6e3


# LOOK FOR PACKAGE TO REPLACE IT
def _get_temperature_in_kelvin(temperature, units):
    """
    Converts input temperature in Kelvin, raising value error
    if units provided are neither 'K' or 'degC'

    Parameters
    ----------
    T : float
        Temperature
    temperature_units : str
        Units used to specify temperature. Can be 'K' or 'degC' for
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


class PropertiesInterface:
    """
    Class to model lead properties at a given temperature

    Parameters
    ----------
    T : float
        Temperature
    temperature_units : str
        Units used to specify temperature. Can be 'K' or 'degC' for
        Kelvin and Celsius respectively
    """
    _T_m0 = 0
    _Q_m0 = 0
    _T_b0 = 0
    _Q_b0 = 0
    _T = 0
    _T_assigned = False
    _p_s = 0
    _sigma = 0
    _rho = 0
    _alpha = 0
    _u_s = 0
    _beta_s = 0
    _delta_h = 0
    _mi = 0
    _r = 0
    _conductivity = 0

    def __init__(self, T, temperature_units=KELVIN_SYMBOL):
        self._set_constants()
        self.__fill_class_attributes(T, temperature_units)

    @property
    def T(self):
        """
        float : temperature used to compute properties [K]
        """
        return self._T

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
        return self._T_assigned

    @property
    def T_m0(self):
        """
        float : lead melting temperature [K]
        """
        return self._T_m0

    @property
    def Q_m0(self):
        """
        float : lead melting latent heat [J/kg]
        """
        return self._Q_m0

    @property
    def T_b0(self):
        """
        float : lead boiling temperature [K]
        """
        return self._T_b0

    @property
    def Q_b0(self):
        """
        float : lead vaporisation heat [J/kg]
        """
        return self._Q_b0

    @property
    def p_s(self):
        """
        float : lead saturation vapour pressure [Pa]
        """
        return self._p_s

    @property
    def sigma(self):
        """
        float : lead surface tension [N/m]
        """
        return self._sigma

    @property
    def rho(self):
        """
        float : lead density [kg/m^3]
        """
        return self._rho

    @property
    def alpha(self):
        """
        float : lead thermal expansion coefficient [1/K]
        """
        return self._alpha

    @property
    def u_s(self):
        """
        float : sound velocity in lead [m/s]
        """
        return self._u_s

    @property
    def beta_s(self):
        """
        float : lead isentropic compressibility [1/Pa]
        """
        return self._beta_s

    @property
    def cp(self):
        """
        float : lead specific heat capacity [J/(kg*K)]
        """
        return self._cp

    @property
    def delta_h(self):
        """
        float : lead specific enthalpy difference from melting point [J/kg]
        """
        return self._delta_h

    @property
    def mi(self):
        """
        float : lead dynamic viscosity [Ps*s]
        """
        return self._mi

    @property
    def r(self):
        """
        float : lead electrical resistivity [Ohm*m]
        """
        return self._r

    @property
    def conductivity(self):
        """
        float : lead thermal conductivity [W/(m*K)]
        """
        return self._conductivity

    def _fill_properties(self):
        raise NotImplementedError("{:s}._fill_properties NOT IMPLEMENTED"
                                  .format(type(self).__name__))

    def _set_constants(self):
        raise NotImplementedError("{:s}._set_constants NOT IMPLEMENTED"
                                  .format(type(self).__name__))

    def __fill_class_attributes(self, T, temperature_units):
        """
        Fills all the class attributes.

        Parameters
        ----------
        T : float
            Temperature
        temperature_units : str
            Units used to specify temperature. Can be 'K' or 'degC' for
            Kelvin and Celsius respectively
        """
        self.__assign_T(T, temperature_units)

        # continue if temperature was correctly assigned
        if self.T_assigned:
            self._fill_properties()

    def __assign_T(self, T, temperature_units):
        """
        Function used to set class temperature, checking if
        temperature value in K is strictly positive

        Parameters
        ----------
        T : float
            Temperature
        temperature_units : str
            Units used to specify temperature. Can be 'K' or 'degC' for
            Kelvin and Celsius respectively
        """
        temp = _get_temperature_in_kelvin(T, temperature_units)

        if temp > self.T_m0 and temp < self.T_b0:
            self._T_assigned = True
            self._T = temp
        else:
            if temp >= self.T_b0:
                raise ValueError("Temperature in Kelvin must be smaller than "
                                 "boiling temperature ({:7.2f} [K]), {:7.2f} "
                                 "[K] was provided".format(self.T_b0, temp))
            elif temp > 0 and temp <= self.T_m0:
                raise ValueError("Temperature in Kelvin must be larger than "
                                 "melting temerature ({:7.2f} [K]), {:7.2f} "
                                 "[K] was provided".format(self.T_m0, temp))
            else:
                raise ValueError("Temperature in Kelvin must be "
                                 "strictly positive, "
                                 "{:7.2f} [K] was provided".format(temp))


class PropertiesFromXInterface:
    def __init__(self, function_of_T, target, guess):

        def function_to_solve(T, target):
            return function_of_T(T) - target

        temp = fsolve(function_to_solve, x0=[guess], args=[target])[0]
        instance = self._get_fluid_instance(temp)

        if instance is not None:
            for attr in dir(instance):
                if not attr.startswith('_'):
                    setattr(self, attr, getattr(instance, attr))

    def _get_fluid_instance(self, T):
        raise NotImplementedError("{:s}._get_fluid_instance NOT IMPLEMENTED"
                                  .format(type(self).__name__))
