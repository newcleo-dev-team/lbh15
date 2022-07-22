"""
Module that contains liquid lead-bismuth-eutectic (lbe) properties objects.
Those objects can be initialized with the temperature
(:class:`.lbe.LBE`) or with one of the available properties
(:class:`.lbe.LBEMi`, :class:`.lbe.LBERho`, ecc)

Each object has the following properties:

    - :math:`T_{m0}` lbe melting temperature:

        :math:`398.0 [K]`
    - :math:`Q_{m0}` lbe melting latent heat:

        :math:`38.6\\cdot10^3 \\Big[\\frac{J}{kg}\\Big]`
    - :math:`T_{b0}` lbe boiling temperature:

        :math:`1927 [K]`
    - :math:`Q_{b0}` lbe vaporisation heat:

        :math:`856.6\\cdot10^3 \\Big[\\frac{J}{kg}\\Big]`
    - :math:`p_s` lbe saturation vapour pressure :math:`[Pa]`:

        :math:`p_s(T) = \\displaystyle1.22\\cdot10^{10}\\cdot\
        \\exp{\\Bigg(\\frac{-22852}{T}\\Bigg)}`
    - :math:`\\sigma` lbe surface tension \
      :math:`\\Big[\\frac{N}{m}\\Big]`:

        :math:`\\sigma(T) = \\displaystyle\\Big(448.5 \
        - 0.0799{\\cdot}T\\Big)\\cdot10^{-3}`
    - :math:`\\rho` lbe density \
      :math:`\\Big[\\frac{kg}{m^3}\\Big]`:

        :math:`\\rho(T) = \\displaystyle11065 - 1.293{\\cdot}T`
    - :math:`\\alpha` lbe thermal expansion coefficient \
      :math:`\\Big[\\frac{1}{K}\\Big]`:

        :math:`\\alpha(T) = \\displaystyle\\frac{1}{8558 - T}`
    - :math:`u_s` speed of sound in lbe \
      :math:`\\Big[\\frac{m}{s}\\Big]`:

        :math:`u_s(T) = \\displaystyle1855 - 0.212{\\cdot}T`
    - :math:`\\beta_s` lbe isentropic compressibility \
      :math:`\\Big[\\frac{1}{Pa}\\Big]`:

        :math:`\\beta_s(T) = \\displaystyle\\frac{1}{\\rho(T){\\cdot}u_s(T)^2}`
    - :math:`c_p` lbe specific heat \
      :math:`\\Big[\\frac{J}{kg{\\cdot}K}\\Big]`:

        :math:`c_p(T) = \\displaystyle164.8 - 3.94\\cdot10^{-3}{\\cdot}T \
        + 1.25\\cdot10^{-5}{\\cdot}T^2 - 4.56\\cdot10^{5}{\\cdot}T^{-2}`
    - :math:`{\\Delta}h` lbe specific enthalpy (in respect to melting \
      point) :math:`\\Big[\\frac{J}{kg{\\cdot}K}\\Big]`:

        :math:`{\\Delta}h(T) = \\displaystyle\
        164.8\\cdot\\Big(T - T_{m0}\\Big) \
        - 1.97\\cdot10^{-2}\\Big(T^2 - T_{m0}^2\\Big) \
        + 4.167\\cdot10^{-2}\\Big(T^3 - T_{m0}^3\\Big) \
        - 7.183\\cdot10^6\\Big(T^{-1} - T_{m0}^{-1}\\Big)`
    - :math:`\\mu` lbe dynamic visocity :math:`[Pa{\\cdot}s]`:

        :math:`\\mu(T) = 4.94\\cdot10^{-4}\\exp{\\frac{754.1}{T}}`
    - :math:`r` lbe electrical resistivity :math:`[\\Omega{\\cdot}m]`:

        :math:`r(T) = \\Big(90.9 + 0.048{\\cdot}T\\Big)\\cdot10^{-8}`
    - :math:`\\lambda` lbe thermal conductivity \
      :math:`\\Big[\\frac{W}{m{\\cdot}K}\\Big]`:

        :math:`{\\lambda}(T) = 3.284 + 1.617\\cdot10^{-2}{\\cdot}T \
        - 2.305\\cdot10^{-6}{\\cdot}T^2`

Where :math:`T` is the lbe temperature in :math:`[K]`
"""
from ._lbeh15 import ZERO_C_IN_K, CELSIUS_SYMBOL
from ._lbeh15 import KELVIN_SYMBOL, LBE_MELTING_TEMPERATURE
from ._lbeh15 import LBE_MELTING_LATENT_HEAT, LBE_BOILING_TEMPERATURE
from ._lbeh15 import LBE_VAPORISATION_HEAT, LBE_KEYWORD
from ._lbeh15 import LBE_T_AT_CP_MIN
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
    second_root : bool
        true to initialize the object with the second root
        of function_of_T, false for the first one.
        Needed if target value is similar to the minimum
        and the solution at the right of the minimum (second root)
        is the desired one
    """
    def __init__(self, function_of_T, target,
                 guess=LBE_MELTING_TEMPERATURE*2.0, second_root=False):
        super().__init__(function_of_T, target, LBE_KEYWORD,
                         guess, second_root)

    def _get_fluid_instance(self, T):
        """
        Returns an instance of :class:`.lbe.LBE`

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
    """
    def __init__(self, saturation_pressure):
        guess = p_s_initializer(saturation_pressure)
        super().__init__(p_s, saturation_pressure, guess)


class LBESigma(_LBEFromX):
    """
    Class to model lead-bismuth eutectic properties from surface tension

    Parameters
    ----------
    surface_tension : float
        value of surface tension [N/m]
    """
    def __init__(self, surface_tension):
        super().__init__(sigma, surface_tension)


class LBERho(_LBEFromX):
    """
    Class to model lead-bismuth eutectic properties from density

    Parameters
    ----------
    density : float
        value of density [kg/m^3]
    """
    def __init__(self, density):
        super().__init__(rho, density)


class LBEAlpha(_LBEFromX):
    """
    Class to model lead-bismuth eutectic properties
    from thermal expansion coefficient

    Parameters
    ----------
    expansion_coefficient : float
        value of temperature expansion coefficient [1/K]
    """
    def __init__(self, expansion_coefficient):
        super().__init__(alpha, expansion_coefficient)


class LBEU_s(_LBEFromX):
    """
    Class to model lead-bismuth eutectic properties from sound velocity

    Parameters
    ----------
    sound_velocity : float
        value of sound velocity [m/s]
    """
    def __init__(self, sound_velocity):
        super().__init__(u_s, sound_velocity)


class LBEBeta_s(_LBEFromX):
    """
    Class to model lead-bismuth eutectic properties
    from isentropic compressibility

    Parameters
    ----------
    isentropic_compressibility : float
        value of isentropic compressibility [1/Pa]
    """
    def __init__(self, isentropic_compressibility):
        super().__init__(beta_s, isentropic_compressibility)


class LBECp(_LBEFromX):
    """
    Class to model lead-bismuth eutectic properties from specific heat capacity

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
        return LBE_T_AT_CP_MIN

    @property
    def T_at_cp_min_in_celsius():
        """
        float : temperature in [degC] corresponding to specific heat minimum
        """
        return LBECp.T_at_cp_min() - ZERO_C_IN_K


class LBEDelta_h(_LBEFromX):
    """
    Class to model lead-bismuth eutectic properties from specifc enthalpy
    (in respect to lead-bismuth eutectic melting point)

    Parameters
    ----------
    enthalpy : float
        value of specifc enthalpy [J/kg]
    """
    def __init__(self, enthalpy):
        super().__init__(delta_h, enthalpy)


class LBEMi(_LBEFromX):
    """
    Class to model lead-bismuth eutectic properties from dynamic viscosity

    Parameters
    ----------
    dynamic_viscosity : float
        value of dynamic viscosity [Pa*s]
    """
    def __init__(self, dynamic_viscosity):
        super().__init__(mi, dynamic_viscosity)


class LBER(_LBEFromX):
    """
    Class to model lead-bismuth eutectic properties from electrical resistivity

    Parameters
    ----------
    electrical_resistivity : float
        value of electrical resistivity [Ohm*m]
    """
    def __init__(self, electrical_resistivity):
        super().__init__(r, electrical_resistivity)


class LBEConductivity(_LBEFromX):
    """
    Class to model lead-bismuth eutectic properties from thermal conductivity

    Parameters
    ----------
    thermal_conductivity : float
        value of thermal conductivity [W/(m*K)]
    """
    def __init__(self, thermal_conductivity):
        super().__init__(conductivity, thermal_conductivity)
