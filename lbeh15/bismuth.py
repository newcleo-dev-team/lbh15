from ._lbeh15 import ZERO_C_IN_K, CELSIUS_SYMBOL
from ._lbeh15 import KELVIN_SYMBOL, BISMUTH_MELTING_TEMPERATURE
from ._lbeh15 import BISMUTH_MELTING_LATENT_HEAT, BISMUTH_BOILING_TEMPERATURE
from ._lbeh15 import BISMUTH_VAPORISATION_HEAT, BISMUTH_KEYWORD
from ._lbeh15 import LEFT_KEYWORD, RIGHT_KEYWORD
from ._lbeh15 import PropertiesInterface
from ._lbeh15 import PropertiesFromXInterface
from ._utils import p_s, delta_h, sigma, rho, alpha, u_s
from ._utils import beta_s, cp, mi, r, conductivity
from ._utils import p_s_initializer


class Bismuth(PropertiesInterface):
    """
    Class to model bismuth properties at a given temperature

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
        self._T_m0 = BISMUTH_MELTING_TEMPERATURE
        self._Q_m0 = BISMUTH_MELTING_LATENT_HEAT
        self._T_b0 = BISMUTH_BOILING_TEMPERATURE
        self._Q_b0 = BISMUTH_VAPORISATION_HEAT

    def _fill_properties(self):
        self._p_s = p_s(self.T, BISMUTH_KEYWORD)
        self._sigma = sigma(self.T, BISMUTH_KEYWORD)
        self._rho = rho(self.T, BISMUTH_KEYWORD)
        self._alpha = alpha(self.T, BISMUTH_KEYWORD)
        self._u_s = u_s(self.T, BISMUTH_KEYWORD)
        self._beta_s = beta_s(self.T, BISMUTH_KEYWORD)
        self._cp = cp(self.T, BISMUTH_KEYWORD)
        self._delta_h = delta_h(self.T, BISMUTH_KEYWORD)
        self._mi = mi(self.T, BISMUTH_KEYWORD)
        self._r = r(self.T, BISMUTH_KEYWORD)
        self._conductivity = conductivity(self.T, BISMUTH_KEYWORD)


class _BismuthFromX(PropertiesFromXInterface):
    """
    Class to model bismuth properties from one of its properties.

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
                 guess=BISMUTH_MELTING_TEMPERATURE*1.5, index=0):
        super().__init__(function_of_T, target, BISMUTH_KEYWORD, guess, index)

    def _get_fluid_instance(self, T):
        """
        Returns an instance of :class:`bismuth.Bismuth`

        Parameters
        ----------
        T : float
            temperature in [K]
        """
        return Bismuth(T, KELVIN_SYMBOL)


class BismuthP_s(_BismuthFromX):
    """
    Class to model bismuth properties from saturation vapour pressure

    Parameters
    ----------
    saturation_pressure : float
        value of the saturation vapour pressure in [Pa]
    guess : float
        initial guess of the temperature in [K]
        that returns property target value
    """
    def __init__(self, saturation_pressure,
                 guess=BISMUTH_MELTING_TEMPERATURE*1.5):
        if guess == BISMUTH_MELTING_TEMPERATURE*1.5:
            guess = p_s_initializer(saturation_pressure)
        super().__init__(p_s, saturation_pressure, guess)


class BismuthSigma(_BismuthFromX):
    """
    Class to model bismuth properties from surface tension

    Parameters
    ----------
    surface_tension : float
        value of surface tension [N/m]
    guess : float
        initial guess of the temperature in [K]
        that returns property target value
    """
    def __init__(self, surface_tension,
                 guess=BISMUTH_MELTING_TEMPERATURE*1.5):
        super().__init__(sigma, surface_tension, guess)


class BismuthRho(_BismuthFromX):
    """
    Class to model bismuth properties from density

    Parameters
    ----------
    density : float
        value of density [kg/m^3]
    guess : float
        initial guess of the temperature in [K]
        that returns property target value
    """
    def __init__(self, density,
                 guess=BISMUTH_MELTING_TEMPERATURE*1.5):
        super().__init__(rho, density, guess)


class BismuthAlpha(_BismuthFromX):
    """
    Class to model bismuth properties from thermal expansion coefficient

    Parameters
    ----------
    expansion_coefficient : float
        value of temperature expansion coefficient [1/K]
    guess : float
        initial guess of the temperature in [K]
        that returns property target value
    """
    def __init__(self, expansion_coefficient,
                 guess=BISMUTH_MELTING_TEMPERATURE*1.5):
        super().__init__(alpha, expansion_coefficient, guess)


class BismuthU_s(_BismuthFromX):
    """
    Class to model bismuth properties from sound velocity

    Parameters
    ----------
    sound_velocity : float
        value of sound velocity [m/s]
    guess : float
        initial guess of the temperature in [K]
        that returns property target value
    """
    def __init__(self, sound_velocity,
                 guess=BISMUTH_MELTING_TEMPERATURE*1.5):
        super().__init__(u_s, sound_velocity, guess)


class BismuthBeta_s(_BismuthFromX):
    """
    Class to model bismuth properties from isentropic compressibility

    Parameters
    ----------
    isentropic_compressibility : float
        value of isentropic compressibility [1/Pa]
    guess : float
        initial guess of the temperature in [K]
        that returns property target value
    """
    def __init__(self, isentropic_compressibility,
                 guess=BISMUTH_MELTING_TEMPERATURE*1.5):
        super().__init__(beta_s, isentropic_compressibility, guess)


class BismuthCp(_BismuthFromX):
    """
    Class to model bismuth properties from specific heat capacity

    Parameters
    ----------
    specific_heat : float
        value of specific heat capacity [J/(kg*K)]
    guess : float
        initial guess of the temperature in [K]
        that returns property target value
    """
    def __init__(self, specific_heat,
                 guess=BISMUTH_MELTING_TEMPERATURE*1.5, side=LEFT_KEYWORD):
        index = 0
        if side == RIGHT_KEYWORD:
            index = 1
        if side != RIGHT_KEYWORD and side != LEFT_KEYWORD:
            raise ValueError("Side can be {:s} or {:s}, {:s} was provided"
                             .format(LEFT_KEYWORD, RIGHT_KEYWORD, side))
        super().__init__(cp, specific_heat, guess, index=index)
        self.__T_at_cp_min = 1342.753

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


class BismuthDelta_h(_BismuthFromX):
    """
    Class to model bismuth properties from specifc enthalpy
    (in respect to bismuth melting point)

    Parameters
    ----------
    enthalpy : float
        value of specifc enthalpy [J/kg]
    guess : float
        initial guess of the temperature in [K]
        that returns property target value
    """
    def __init__(self, enthalpy,
                 guess=BISMUTH_MELTING_TEMPERATURE*1.5):
        super().__init__(delta_h, enthalpy, guess)


class BismuthMi(_BismuthFromX):
    """
    Class to model bismuth properties from dynamic viscosity

    Parameters
    ----------
    dynamic_viscosity : float
        value of dynamic viscosity [Pa*s]
    guess : float
        initial guess of the temperature in [K]
        that returns property target value
    """
    def __init__(self, dynamic_viscosity,
                 guess=BISMUTH_MELTING_TEMPERATURE*1.5):
        super().__init__(mi, dynamic_viscosity, guess)


class BismuthR(_BismuthFromX):
    """
    Class to model bismuth properties from electrical resistivity

    Parameters
    ----------
    electrical_resistivity : float
        value of electrical resistivity [Ohm*m]
    guess : float
        initial guess of the temperature in [K]
        that returns property target value
    """
    def __init__(self, electrical_resistivity,
                 guess=BISMUTH_MELTING_TEMPERATURE*1.5):
        super().__init__(r, electrical_resistivity, guess)


class BismuthConductivity(_BismuthFromX):
    """
    Class to model bismuth properties from thermal conductivity

    Parameters
    ----------
    thermal_conductivity : float
        value of thermal conductivity [W/(m*K)]
    guess : float
        initial guess of the temperature in [K]
        that returns property target value
    """
    def __init__(self, thermal_conductivity,
                 guess=BISMUTH_MELTING_TEMPERATURE*1.5):
        super().__init__(conductivity, thermal_conductivity, guess)
