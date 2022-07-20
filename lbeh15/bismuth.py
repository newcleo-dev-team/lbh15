"""
Module that contains liquid bismuth properties objects.
Those objects can be initialized with the temperature
(:class:`.bismuth.Bismuth`) or with one of the available properties
(:class:`.bismuth.BismuthMi`, :class:`.bismuth.BismuthRho`, ecc)

Each object has the following properties:
    - :math:`T_{m0}` bismuth melting temperature:
        :math:`544.6 [K]`
    - :math:`Q_{m0}` bismuth melting latent heat:
        :math:`53.3\\cdot10^3 \\Big[\\frac{J}{kg}\\Big]`
    - :math:`T_{b0}` bismuth boiling temperature:
        :math:`1831 [K]`
    - :math:`Q_{b0}` bismuth vaporisation heat:
        :math:`856.2\\cdot10^3 \\Big[\\frac{J}{kg}\\Big]`
    - :math:`p_s` bismuth saturation vapour pressure :math:`[Pa]`:
        :math:`p_s(T) = \\displaystyle2.67\\cdot10^{10}\\cdot\
        \\exp{\\Bigg(\\frac{-22858}{T}\\Bigg)}`
    - :math:`\\sigma` bismuth surface tension \
      :math:`\\Big[\\frac{N}{m}\\Big]`:
        :math:`\\sigma(T) = \\displaystyle\\Big(420.8 \
        - 0.81{\\cdot}T\\Big)\\cdot10^{-3}`
    - :math:`\\rho` bismuth density \
      :math:`\\Big[\\frac{kg}{m^3}\\Big]`:
        :math:`\\rho(T) = \\displaystyle10725 - 1.22{\\cdot}T`
    - :math:`\\alpha` bismuth thermal expansion coefficient \
      :math:`\\Big[\\frac{1}{K}\\Big]`:
        :math:`\\alpha(T) = \\displaystyle\\frac{1}{8791 - T}`
    - :math:`u_s` speed of sound in bismuth \
      :math:`\\Big[\\frac{m}{s}\\Big]`:
        :math:`u_s(T) = \\displaystyle1616 + 0.246{\\cdot}T \
        - 2.2\\cdot10^{-4}{\\cdot}T`
    - :math:`\\beta_s` bismuth isentropic compressibility \
      :math:`\\Big[\\frac{1}{Pa}\\Big]`:
        :math:`\\beta_s(T) = \\displaystyle\\frac{1}{\\rho(T) \
        - u_s(T)}`
    - :math:`c_p` bismuth specific heat \
      :math:`\\Big[\\frac{J}{kg{\\cdot}K}\\Big]`:
        :math:`c_p(T) = \\displaystyle118.2 - 5.934\\cdot10^{-3}{\\cdot}T \
        + 7.183\\cdot10^{6}{\\cdot}T^{-2}`
    - :math:`{\\Delta}h` bismuth specific enthalpy (in respect to melting \
      point) :math:`\\Big[\\frac{J}{kg{\\cdot}K}\\Big]`:
        :math:`{\\Delta}h(T) = \\displaystyle\
        118.2\\cdot\\Big(T - T_{m0}\\Big) \
        + 2.967\\cdot10^{-2}\\Big(T^2 - T_{m0}^2\\Big) \
        - 7.183\\cdot10^6\\Big(T^{-1} - T_{m0}^{-1}\\Big)`
    - :math:`\\mu` bismuth dynamic visocity :math:`[Pa{\\cdot}s]`:
        :math:`\\mu(T) = 4.456\\cdot10^{-4}\\exp{\\frac{780}{T}}`
    - :math:`r` bismuth electrical resistivity :math:`[\\Omega{\\cdot}m]`:
        :math:`r(T) = \\Big(98.96 + 0.0554{\\cdot}T\\Big)\\cdot10^{-8}`
    - :math:`\\lambda` bismuth thermal conductivity \
      :math:`\\Big[\\frac{W}{m{\\cdot}K}\\Big]`:
        :math:`{\\lambda}(T) = 7.34 + 9.5\\cdot10^{-3}{\\cdot}T`

Where :math:`T` is the bismuth temperature in :math:`[K]`
"""
from ._lbeh15 import ZERO_C_IN_K, CELSIUS_SYMBOL
from ._lbeh15 import KELVIN_SYMBOL, BISMUTH_MELTING_TEMPERATURE
from ._lbeh15 import BISMUTH_MELTING_LATENT_HEAT, BISMUTH_BOILING_TEMPERATURE
from ._lbeh15 import BISMUTH_VAPORISATION_HEAT, BISMUTH_KEYWORD
from ._lbeh15 import BISMUTH_T_AT_CP_MIN
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
    second_root : bool
        true to initialize the object with the second root
        of function_of_T, false for the first one. 
        Needed if target value is similar to the minimum
        and the solution at the right of the minimum (second root)
        is the desired one
    """
    def __init__(self, function_of_T, target,
                 guess=BISMUTH_MELTING_TEMPERATURE*1.5, second_root=False):
        super().__init__(function_of_T, target, BISMUTH_KEYWORD, guess, second_root)

    def _get_fluid_instance(self, T):
        """
        Returns an instance of :class:`.bismuth.Bismuth`

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
    """
    def __init__(self, saturation_pressure):
        guess = p_s_initializer(saturation_pressure)
        super().__init__(p_s, saturation_pressure, guess)


class BismuthSigma(_BismuthFromX):
    """
    Class to model bismuth properties from surface tension

    Parameters
    ----------
    surface_tension : float
        value of surface tension [N/m]
    """
    def __init__(self, surface_tension):
        super().__init__(sigma, surface_tension)


class BismuthRho(_BismuthFromX):
    """
    Class to model bismuth properties from density

    Parameters
    ----------
    density : float
        value of density [kg/m^3]
    """
    def __init__(self, density):
        super().__init__(rho, density)


class BismuthAlpha(_BismuthFromX):
    """
    Class to model bismuth properties from thermal expansion coefficient

    Parameters
    ----------
    expansion_coefficient : float
        value of temperature expansion coefficient [1/K]
    """
    def __init__(self, expansion_coefficient):
        super().__init__(alpha, expansion_coefficient)


class BismuthU_s(_BismuthFromX):
    """
    Class to model bismuth properties from sound velocity

    Parameters
    ----------
    sound_velocity : float
        value of sound velocity [m/s]
    """
    def __init__(self, sound_velocity):
        super().__init__(u_s, sound_velocity)


class BismuthBeta_s(_BismuthFromX):
    """
    Class to model bismuth properties from isentropic compressibility

    Parameters
    ----------
    isentropic_compressibility : float
        value of isentropic compressibility [1/Pa]
    """
    def __init__(self, isentropic_compressibility):
        super().__init__(beta_s, isentropic_compressibility)


class BismuthCp(_BismuthFromX):
    """
    Class to model bismuth properties from specific heat capacity

    Parameters
    ----------
    specific_heat : float
        value of specific heat capacity [J/(kg*K)]
    second_root : bool
        true to initialize the object with the second root
        of specific_heat function, false for the first one. 
        Needed if specific_heat value is similar to the minimum
        and the solution at the right of the minimum (second root)
        is the desired one
    """
    def __init__(self, specific_heat, second_root=False):
        super().__init__(cp, specific_heat, second_root=second_root)

    @staticmethod
    def T_at_cp_min():
        """
        float : temperature in [K] corresponding to specific heat minimum
        """
        return BISMUTH_T_AT_CP_MIN

    @staticmethod
    def T_at_cp_min_in_celsius():
        """
        float : temperature in [degC] corresponding to specific heat minimum
        """
        return BismuthCp.T_at_cp_min() - ZERO_C_IN_K


class BismuthDelta_h(_BismuthFromX):
    """
    Class to model bismuth properties from specifc enthalpy
    (in respect to bismuth melting point)

    Parameters
    ----------
    enthalpy : float
        value of specifc enthalpy [J/kg]
    """
    def __init__(self, enthalpy):
        super().__init__(delta_h, enthalpy)


class BismuthMi(_BismuthFromX):
    """
    Class to model bismuth properties from dynamic viscosity

    Parameters
    ----------
    dynamic_viscosity : float
        value of dynamic viscosity [Pa*s]
    """
    def __init__(self, dynamic_viscosity):
        super().__init__(mi, dynamic_viscosity)


class BismuthR(_BismuthFromX):
    """
    Class to model bismuth properties from electrical resistivity

    Parameters
    ----------
    electrical_resistivity : float
        value of electrical resistivity [Ohm*m]
    """
    def __init__(self, electrical_resistivity):
        super().__init__(r, electrical_resistivity)


class BismuthConductivity(_BismuthFromX):
    """
    Class to model bismuth properties from thermal conductivity

    Parameters
    ----------
    thermal_conductivity : float
        value of thermal conductivity [W/(m*K)]
    """
    def __init__(self, thermal_conductivity):
        super().__init__(conductivity, thermal_conductivity)
