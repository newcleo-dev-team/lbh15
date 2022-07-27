"""
Module that contains liquid lead properties objects.
Those objects can be initialized with the temperature
(:class:`.lead.Lead`) or with one of the available properties
(:class:`.lead.LeadMi`, :class:`.lead.LeadRho`, etc)

Each object has the following properties:

    - :math:`T_{m0}` lead melting temperature:

        :math:`600.6 [K]`
    - :math:`Q_{m0}` lead melting latent heat:

        :math:`23.07\\cdot10^3 \\Big[\\frac{J}{kg}\\Big]`
    - :math:`T_{b0}` lead boiling temperature:

        :math:`2021 [K]`
    - :math:`Q_{b0}` lead vaporisation heat:

        :math:`858.6\\cdot10^3 \\Big[\\frac{J}{kg}\\Big]`
    - :math:`p_s` lead saturation vapour pressure :math:`[Pa]`:

        :math:`p_s(T) = \\displaystyle5.79\\cdot10^9\\cdot\
        \\exp{\\Bigg(\\frac{-22131}{T}\\Bigg)}`
    - :math:`\\sigma` lead surface tension \
      :math:`\\Big[\\frac{N}{m}\\Big]`:

        :math:`\\sigma(T) = \\displaystyle\\Big(525.9 \
        - 0.113{\\cdot}T\\Big)\\cdot10^{-3}`
    - :math:`\\rho` lead density \
      :math:`\\Big[\\frac{kg}{m^3}\\Big]`:

        :math:`\\rho(T) = \\displaystyle11441 - 1.2795{\\cdot}T`
    - :math:`\\alpha` lead thermal expansion coefficient \
      :math:`\\Big[\\frac{1}{K}\\Big]`:

        :math:`\\alpha(T) = \\displaystyle\\frac{1}{8942 - T}`
    - :math:`u_s` speed of sound in lead \
      :math:`\\Big[\\frac{m}{s}\\Big]`:

        :math:`u_s(T) = \\displaystyle1953 - 0.246{\\cdot}T`
    - :math:`\\beta_s` lead isentropic compressibility \
      :math:`\\Big[\\frac{1}{Pa}\\Big]`:

        :math:`\\beta_s(T) = \\displaystyle\\frac{1}{\\rho(T){\\cdot}u_s(T)^2}`
    - :math:`c_p` lead specific heat \
      :math:`\\Big[\\frac{J}{kg{\\cdot}K}\\Big]`:

        :math:`c_p(T) = \\displaystyle175.1 - 4.961\\cdot10^{-2}{\\cdot}T \
        + 1.985\\cdot10^{-5}{\\cdot}T^2 - 2.099\\cdot10^{-9}{\\cdot}T^3 \
        - 1.524\\cdot10^{6}{\\cdot}T^{-2}`
    - :math:`{\\Delta}h` lead specific enthalpy (in respect to melting point) \
      :math:`\\Big[\\frac{J}{kg{\\cdot}K}\\Big]`:

        :math:`{\\Delta}h(T) = \\displaystyle\
        176.2\\cdot\\Big(T - T_{m0}\\Big) \
        - 2.4615\\cdot10^{-2}\\Big(T^2 - T_{m0}^2\\Big) \
        + 5.147\\cdot10^{-6}\\Big(T^3 - T_{m0}^3\\Big) \
        + 1.524\\cdot10^6\\Big(T^{-1} - T_{m0}^{-1}\\Big)`
    - :math:`\\mu` lead dynamic visocity :math:`[Pa{\\cdot}s]`:

        :math:`\\mu(T) = \\displaystyle4.55\\cdot10^{-4}\\cdot\
        \\exp\\Bigg({\\frac{1069}{T}}\\Bigg)`
    - :math:`r` lead electrical resistivity :math:`[\\Omega{\\cdot}m]`:

        :math:`r(T) = \\displaystyle\\Big(67.0 + 0.0471{\\cdot}T\\Big)\\cdot10^{-8}`
    - :math:`k` lead thermal conductivity \
      :math:`\\Big[\\frac{W}{m{\\cdot}K}\\Big]`:

        :math:`k(T) = \\displaystyle9.2 + 0.011{\\cdot}T`

Where :math:`T` is the lead temperature in :math:`[K]`
"""
from ._lbeh15 import LEAD_MELTING_TEMPERATURE
from ._lbeh15 import LEAD_MELTING_LATENT_HEAT, LEAD_BOILING_TEMPERATURE
from ._lbeh15 import LEAD_VAPORISATION_HEAT, LEAD_KEYWORD
from ._lbeh15 import LEAD_T_AT_CP_MIN
from ._lbeh15 import PropertiesInterface
from ._lbeh15 import PropertiesFromXInterface
from ._utils import p_s, delta_h, sigma, rho, alpha, u_s
from ._utils import beta_s, cp, mu, r, k
from ._utils import p_s_initializer


class Lead(PropertiesInterface):
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
    def __init__(self, T):
        super().__init__(T)

    def _set_constants(self):
        self._T_m0 = LEAD_MELTING_TEMPERATURE
        self._Q_m0 = LEAD_MELTING_LATENT_HEAT
        self._T_b0 = LEAD_BOILING_TEMPERATURE
        self._Q_b0 = LEAD_VAPORISATION_HEAT

    def _fill_properties(self):
        self._p_s = p_s(self.T, LEAD_KEYWORD)
        self._sigma = sigma(self.T, LEAD_KEYWORD)
        self._rho = rho(self.T, LEAD_KEYWORD)
        self._alpha = alpha(self.T, LEAD_KEYWORD)
        self._u_s = u_s(self.T, LEAD_KEYWORD)
        self._beta_s = beta_s(self.T, LEAD_KEYWORD)
        self._cp = cp(self.T, LEAD_KEYWORD)
        self._delta_h = delta_h(self.T, LEAD_KEYWORD)
        self._mu = mu(self.T, LEAD_KEYWORD)
        self._r = r(self.T, LEAD_KEYWORD)
        self._k = k(self.T, LEAD_KEYWORD)


class _LeadFromX(PropertiesFromXInterface):
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
    second_root : bool
        true to initialize the object with the second root
        of function_of_T, false for the first one.
        Needed if target value is similar to the minimum
        and the solution at the right of the minimum (second root)
        is the desired one
    """
    def __init__(self, function_of_T, target,
                 guess=LEAD_MELTING_TEMPERATURE*1.7, second_root=False):
        super().__init__(function_of_T, target, LEAD_KEYWORD,
                         guess, second_root)

    def _get_fluid_instance(self, T):
        """
        Returns an instance of :class:`.lead.Lead`

        Parameters
        ----------
        T : float
            temperature in [K]
        """
        return Lead(T)


class LeadP_s(_LeadFromX):
    """
    Class to model lead properties from saturation vapour pressure

    Parameters
    ----------
    saturation_pressure : float
        value of the saturation vapour pressure in [Pa]
    """
    def __init__(self, saturation_pressure):
        guess = p_s_initializer(saturation_pressure)
        super().__init__(p_s, saturation_pressure, guess)


class LeadSigma(_LeadFromX):
    """
    Class to model lead properties from surface tension

    Parameters
    ----------
    surface_tension : float
        value of surface tension [N/m]
    """
    def __init__(self, surface_tension):
        super().__init__(sigma, surface_tension)


class LeadRho(_LeadFromX):
    """
    Class to model lead properties from density

    Parameters
    ----------
    density : float
        value of density [kg/m^3]
    """
    def __init__(self, density):
        super().__init__(rho, density)


class LeadAlpha(_LeadFromX):
    """
    Class to model lead properties from thermal expansion coefficient

    Parameters
    ----------
    expansion_coefficient : float
        value of temperature expansion coefficient [1/K]
    """
    def __init__(self, expansion_coefficient):
        super().__init__(alpha, expansion_coefficient)


class LeadU_s(_LeadFromX):
    """
    Class to model lead properties from sound velocity

    Parameters
    ----------
    sound_velocity : float
        value of sound velocity [m/s]
    """
    def __init__(self, sound_velocity):
        super().__init__(u_s, sound_velocity)


class LeadBeta_s(_LeadFromX):
    """
    Class to model lead properties from isentropic compressibility

    Parameters
    ----------
    isentropic_compressibility : float
        value of isentropic compressibility [1/Pa]
    """
    def __init__(self, isentropic_compressibility):
        super().__init__(beta_s, isentropic_compressibility)


class LeadCp(_LeadFromX):
    """
    Class to model lead properties from specific heat capacity

    Parameters
    ----------
    specific_heat : float
        value of specific heat capacity [J/(kg*K)]
    guess : float
        initial guess of the temperature in [K]
        that returns property target value
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
        return LEAD_T_AT_CP_MIN


class LeadDelta_h(_LeadFromX):
    """
    Class to model lead properties from specifc enthalpy
    (in respect to lead melting point)

    Parameters
    ----------
    enthalpy : float
        value of specifc enthalpy [J/kg]
    """
    def __init__(self, enthalpy):
        super().__init__(delta_h, enthalpy)


class LeadMu(_LeadFromX):
    """
    Class to model lead properties from dynamic viscosity

    Parameters
    ----------
    dynamic_viscosity : float
        value of dynamic viscosity [Pa*s]
    """
    def __init__(self, dynamic_viscosity):
        super().__init__(mu, dynamic_viscosity)


class LeadR(_LeadFromX):
    """
    Class to model lead properties from electrical resistivity

    Parameters
    ----------
    electrical_resistivity : float
        value of electrical resistivity [Ohm*m]
    """
    def __init__(self, electrical_resistivity):
        super().__init__(r, electrical_resistivity)


class LeadK(_LeadFromX):
    """
    Class to model lead properties from thermal conductivity

    Parameters
    ----------
    thermal_conductivity : float
        value of thermal conductivity [W/(m*K)]
    """
    def __init__(self, thermal_conductivity):
        super().__init__(k, thermal_conductivity)
