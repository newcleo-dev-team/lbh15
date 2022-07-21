from scipy.optimize import fsolve

# CONSTANTS
P_ATM = 101325  # [Pa]
ZERO_C_IN_K = 273.15
CELSIUS_SYMBOL = "degC"
KELVIN_SYMBOL = "K"
LEAD_KEYWORD = "lead"
BISMUTH_KEYWORD = "bismuth"
LBE_KEYWORD = "lbe"

# LEAD CONSTANTS
LEAD_MELTING_TEMPERATURE = 600.6  # [K]
LEAD_MELTING_LATENT_HEAT = 23.07e3  # [J/kg]
LEAD_BOILING_TEMPERATURE = 2021  # [K]
LEAD_VAPORISATION_HEAT = 858.6e3  # [J/kg]
LEAD_T_AT_CP_MIN = 1682.522  # [K]

# BISMUTH CONSTANTS
BISMUTH_MELTING_TEMPERATURE = 544.6  # [K]
BISMUTH_MELTING_LATENT_HEAT = 53.3e3  # [J/kg]
BISMUTH_BOILING_TEMPERATURE = 1831  # [K]
BISMUTH_VAPORISATION_HEAT = 856.2e3  # [J/kg]
BISMUTH_T_AT_CP_MIN = 1342.753  # [K]

# LEAD-BISMUTH-EUTECTIC CONSTANTS
LBE_MELTING_TEMPERATURE = 398.0  # [K]
LBE_MELTING_LATENT_HEAT = 38.6e3  # [J/kg]
LBE_BOILING_TEMPERATURE = 1927  # [K]
LBE_VAPORISATION_HEAT = 856.6e3  # [J/kg]
LBE_T_AT_CP_MIN = 1566.510  # [K]


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
    Base class that defines liquid metal properties object
    at a given temperature

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
    _p = 0

    def __init__(self, T, temperature_units=KELVIN_SYMBOL):
        self._p = P_ATM
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
    def p_s(self):
        """
        float : saturation vapour pressure [Pa]
        """
        return self._p_s

    @property
    def sigma(self):
        """
        float : surface tension [N/m]
        """
        return self._sigma

    @property
    def rho(self):
        """
        float : density [kg/m^3]
        """
        return self._rho

    @property
    def alpha(self):
        """
        float : thermal expansion coefficient [1/K]
        """
        return self._alpha

    @property
    def u_s(self):
        """
        float : sound velocity in [m/s]
        """
        return self._u_s

    @property
    def beta_s(self):
        """
        float : isentropic compressibility [1/Pa]
        """
        return self._beta_s

    @property
    def cp(self):
        """
        float : specific heat capacity [J/(kg*K)]
        """
        return self._cp

    @property
    def delta_h(self):
        """
        float : specific enthalpy difference from melting point [J/kg]
        """
        return self._delta_h

    @property
    def mi(self):
        """
        float : dynamic viscosity [Ps*s]
        """
        return self._mi

    @property
    def r(self):
        """
        float : electrical resistivity [Ohm*m]
        """
        return self._r

    @property
    def conductivity(self):
        """
        float : thermal conductivity [W/(m*K)]
        """
        return self._conductivity

    @property
    def p(self):
        """
        float : pressure adopted for property calculation, i.e.,
        atmospheric pressure
        """
        return self._p

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
    """
    Base class that defines liquid metal properties object
    initialized with one of its properties.

    Parameters
    ----------
    function_of_T : function
        function that implements the dependency of the property on temperature
        in [K]
    target : float
        physical property value
    fluid : str
        fluid for which calculation shall be performed,
        can be one among lead, bismuth or lbe
    guess : float
        initial guess of temperature in [K]
    index : int
        index used to select the temperature corresponding
        to target (if more then one are retrieved)
    """
    def __init__(self, function_of_T, target, fluid, guess, second_root=False):

        def function_to_solve(T, fluid, target):
            return function_of_T(T, fluid) - target

        if not second_root:
            res = fsolve(function_to_solve, x0=[guess],
                         args=(fluid, target), xtol=1e-10)
            temp = res[0]
        else:
            res = fsolve(function_to_solve, x0=[guess, 4*guess],
                         args=(fluid, target), xtol=1e-10)
            temp = res[1]
        instance = self._get_fluid_instance(temp)

        if instance is not None:
            for attr in dir(instance):
                if not attr.startswith('_'):
                    setattr(self, attr, getattr(instance, attr))

    def _get_fluid_instance(self, T):
        """
        Returns a fluid properties object

        Parameters
        ----------
        T : float
            temperature in [K]
        """
        raise NotImplementedError("{:s}._get_fluid_instance NOT IMPLEMENTED"
                                  .format(type(self).__name__))
