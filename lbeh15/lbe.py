from ._lbeh15 import ZERO_C_IN_K, CELSIUS_SYMBOL
from ._lbeh15 import KELVIN_SYMBOL, LBE_MELTING_TEMPERATURE
from ._lbeh15 import LBE_MELTING_LATENT_HEAT, LBE_BOILING_TEMPERATURE
from ._lbeh15 import LBE_VAPORISATION_HEAT, LBE_KEYWORD
from ._lbeh15 import LEFT_KEYWORD, RIGHT_KEYWORD
from ._lbeh15 import PropertiesInterface
from ._lbeh15 import PropertiesFromXInterface
from ._utils import p_s, delta_h, sigma, rho, alpha, u_s
from ._utils import beta_s, cp, mi, r, conductivity
from ._utils import p_s_initializer


class LBE(PropertiesInterface):
    """
    Class to model lead-bismuth eutectic properties at a given temperature

    Parameters
    ----------
    T : float
        Temperature
    temperature_units : str
        Units used to specify temperature. Can be 'K' or 'degC' for
        Kelvin and Celsius respectively
    """
    def __init__(self, T, temperature_units=KELVIN_SYMBOL):
        super().__init__(T, temperature_units)

    def _set_constants(self):
        self._T_m0 = LBE_MELTING_TEMPERATURE
        self._Q_m0 = LBE_MELTING_LATENT_HEAT
        self._T_b0 = LBE_BOILING_TEMPERATURE
        self._Q_b0 = LBE_VAPORISATION_HEAT

    def _fill_properties(self):
        self._p_s = p_s(self.T, LBE_KEYWORD)
        self._sigma = sigma(self.T, LBE_KEYWORD)
        self._rho = rho(self.T, LBE_KEYWORD)
        self._alpha = alpha(self.T, LBE_KEYWORD)
        self._u_s = u_s(self.T, LBE_KEYWORD)
        self._beta_s = beta_s(self.T, LBE_KEYWORD)
        self._cp = cp(self.T, LBE_KEYWORD)
        self._delta_h = delta_h(self.T, LBE_KEYWORD)
        self._mi = mi(self.T, LBE_KEYWORD)
        self._r = r(self.T, LBE_KEYWORD)
        self._conductivity = conductivity(self.T, LBE_KEYWORD)


class _LBEFromX(PropertiesFromXInterface):
    """
    Class to model lead-bismuth eutectic properties from one of its properties.

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
    index : int
        index used to select the temperature corresponding
        to target (if more then one are retrieved)
    """
    def __init__(self, function_of_T, target,
                 guess=LBE_MELTING_TEMPERATURE*2.0, index=0):
        super().__init__(function_of_T, target, LBE_KEYWORD, guess, index)

    def _get_fluid_instance(self, T):
        """
        Returns an instance of :class:`lbe.LBE`

        Parameters
        ----------
        T : float
            temperature in [K]
        """
        return LBE(T, KELVIN_SYMBOL)


class LBEP_s(_LBEFromX):
    """
    Class to model lead-bismuth eutectic properties
    from saturation vapour pressure

    Parameters
    ----------
    saturation_pressure : float
        value of the saturation vapour pressure in [Pa]
    guess : float
        initial guess of the temperature in [K]
        that returns property target value
    """
    def __init__(self, saturation_pressure,
                 guess=LBE_MELTING_TEMPERATURE*2.0):
        if guess == LBE_MELTING_TEMPERATURE*2.0:
            guess = p_s_initializer(saturation_pressure)
        super().__init__(p_s, saturation_pressure, guess)


class LBESigma(_LBEFromX):
    """
    Class to model lead-bismuth eutectic properties from surface tension

    Parameters
    ----------
    surface_tension : float
        value of surface tension [N/m]
    guess : float
        initial guess of the temperature in [K]
        that returns property target value
    """
    def __init__(self, surface_tension,
                 guess=LBE_MELTING_TEMPERATURE*2.0):
        super().__init__(sigma, surface_tension, guess)


class LBERho(_LBEFromX):
    """
    Class to model lead-bismuth eutectic properties from density

    Parameters
    ----------
    density : float
        value of density [kg/m^3]
    guess : float
        initial guess of the temperature in [K]
        that returns property target value
    """
    def __init__(self, density,
                 guess=LBE_MELTING_TEMPERATURE*2.0):
        super().__init__(rho, density, guess)


class LBEAlpha(_LBEFromX):
    """
    Class to model lead-bismuth eutectic properties
    from thermal expansion coefficient

    Parameters
    ----------
    expansion_coefficient : float
        value of temperature expansion coefficient [1/K]
    guess : float
        initial guess of the temperature in [K]
        that returns property target value
    """
    def __init__(self, expansion_coefficient,
                 guess=LBE_MELTING_TEMPERATURE*2.0):
        super().__init__(alpha, expansion_coefficient, guess)


class LBEU_s(_LBEFromX):
    """
    Class to model lead-bismuth eutectic properties from sound velocity

    Parameters
    ----------
    sound_velocity : float
        value of sound velocity [m/s]
    guess : float
        initial guess of the temperature in [K]
        that returns property target value
    """
    def __init__(self, sound_velocity,
                 guess=LBE_MELTING_TEMPERATURE*2.0):
        super().__init__(u_s, sound_velocity, guess)


class LBEBeta_s(_LBEFromX):
    """
    Class to model lead-bismuth eutectic properties
    from isentropic compressibility

    Parameters
    ----------
    isentropic_compressibility : float
        value of isentropic compressibility [1/Pa]
    guess : float
        initial guess of the temperature in [K]
        that returns property target value
    """
    def __init__(self, isentropic_compressibility,
                 guess=LBE_MELTING_TEMPERATURE*2.0):
        super().__init__(beta_s, isentropic_compressibility, guess)


class LBECp(_LBEFromX):
    """
    Class to model lead-bismuth eutectic properties from specific heat capacity

    Parameters
    ----------
    specific_heat : float
        value of specific heat capacity [J/(kg*K)]
    guess : float
        initial guess of the temperature in [K]
        that returns property target value
    side : str
        If more than one solution is available for
        a given specific_heat, this parameter is used
        to select the one at the left or at the right
        of specif heat function minimum. It must be
        'left' or 'right'
    """
    def __init__(self, specific_heat,
                 guess=LBE_MELTING_TEMPERATURE*2.0, side=LEFT_KEYWORD):
        index = 0
        if side == RIGHT_KEYWORD:
            index = 1
        if side != RIGHT_KEYWORD and side != LEFT_KEYWORD:
            raise ValueError("Side can be {:s} or {:s}, {:s} was provided"
                             .format(LEFT_KEYWORD, RIGHT_KEYWORD, side))
        super().__init__(cp, specific_heat, guess, index=index)
        self.__T_at_cp_min = 1566.510

    @property
    def T_at_cp_min(self):
        """
        float : temperature in [K] corresponding to specific heat minimum
        """
        return self.__T_at_cp_min

    @property
    def T_at_cp_min_in_celsius(self):
        """
        float : temperature in [degC] corresponding to specific heat minimum
        """
        return self.__T_at_cp_min - ZERO_C_IN_K


class LBEDelta_h(_LBEFromX):
    """
    Class to model lead-bismuth eutectic properties from specifc enthalpy
    (in respect to lead-bismuth eutectic melting point)

    Parameters
    ----------
    enthalpy : float
        value of specifc enthalpy [J/kg]
    guess : float
        initial guess of the temperature in [K]
        that returns property target value
    """
    def __init__(self, enthalpy,
                 guess=LBE_MELTING_TEMPERATURE*2.0):
        super().__init__(delta_h, enthalpy, guess)


class LBEMi(_LBEFromX):
    """
    Class to model lead-bismuth eutectic properties from dynamic viscosity

    Parameters
    ----------
    dynamic_viscosity : float
        value of dynamic viscosity [Pa*s]
    guess : float
        initial guess of the temperature in [K]
        that returns property target value
    """
    def __init__(self, dynamic_viscosity,
                 guess=LBE_MELTING_TEMPERATURE*2.0):
        super().__init__(mi, dynamic_viscosity, guess)


class LBER(_LBEFromX):
    """
    Class to model lead-bismuth eutectic properties from electrical resistivity

    Parameters
    ----------
    electrical_resistivity : float
        value of electrical resistivity [Ohm*m]
    guess : float
        initial guess of the temperature in [K]
        that returns property target value
    """
    def __init__(self, electrical_resistivity,
                 guess=LBE_MELTING_TEMPERATURE*2.0):
        super().__init__(r, electrical_resistivity, guess)


class LBEConductivity(_LBEFromX):
    """
    Class to model lead-bismuth eutectic properties from thermal conductivity

    Parameters
    ----------
    thermal_conductivity : float
        value of thermal conductivity [W/(m*K)]
    guess : float
        initial guess of the temperature in [K]
        that returns property target value
    """
    def __init__(self, thermal_conductivity,
                 guess=LBE_MELTING_TEMPERATURE*2.0):
        super().__init__(conductivity, thermal_conductivity, guess)
