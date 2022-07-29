"""
Module that contains liquid bismuth properties objects.
Those objects can be initialized with the temperature
(:class:`.bismuth.Bismuth`) or with one of the available properties
(:class:`.bismuth.BismuthMu`, :class:`.bismuth.BismuthRho`, etc)

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

        :math:`\\beta_s(T) = \\displaystyle\\frac{1}{\\rho(T){\\cdot}u_s(T)^2}`
    - :math:`c_p` bismuth specific heat \
      :math:`\\Big[\\frac{J}{kg{\\cdot}K}\\Big]`:

        :math:`c_p(T) = \\displaystyle118.2 - 5.934\\cdot10^{-3}{\\cdot}T \
        + 7.183\\cdot10^{6}{\\cdot}T^{-2}`
    - :math:`h` bismuth specific enthalpy (in respect to melting \
      point) :math:`\\Big[\\frac{J}{kg{\\cdot}K}\\Big]`:

        :math:`h(T) = \\displaystyle\
        118.2\\cdot\\Big(T - T_{m0}\\Big) \
        + 2.967\\cdot10^{-2}\\Big(T^2 - T_{m0}^2\\Big) \
        - 7.183\\cdot10^6\\Big(T^{-1} - T_{m0}^{-1}\\Big)`
    - :math:`\\mu` bismuth dynamic visocity :math:`[Pa{\\cdot}s]`:

        :math:`\\mu(T) = \\displaystyle4.456\\cdot10^{-4}\\cdot\
        \\exp\\Bigg({\\frac{780}{T}}\\Bigg)`
    - :math:`r` bismuth electrical resistivity :math:`[\\Omega{\\cdot}m]`:

        :math:`r(T) = \\displaystyle\\Big(98.96 + 0.0554{\\cdot}T\\Big)\
        \\cdot10^{-8}`
    - :math:`k` bismuth thermal conductivity \
      :math:`\\Big[\\frac{W}{m{\\cdot}K}\\Big]`:

        :math:`k(T) = \\displaystyle7.34 + 9.5\\cdot10^{-3}{\\cdot}T`

where :math:`T` is the bismuth temperature in :math:`[K]`
"""
from ._lbeh15 import BISMUTH_MELTING_TEMPERATURE
from ._lbeh15 import BISMUTH_MELTING_LATENT_HEAT, BISMUTH_BOILING_TEMPERATURE
from ._lbeh15 import BISMUTH_VAPORISATION_HEAT, BISMUTH_KEYWORD
from ._lbeh15 import BISMUTH_T_AT_CP_MIN
from ._lbeh15 import PropertiesInterface
from ._utils import p_s, h, sigma, rho, alpha, u_s
from ._utils import beta_s, cp, mu, r, k
from ._utils import p_s_initializer


class Bismuth(PropertiesInterface):
    """
    Class to model bismuth properties at a given temperature

    Parameters
    ----------
    T : float
        Temperature

    Examples
    --------
    >>> liquid_bismuth = Bismuth(670)
    >>> liquid_bismuth.k  # [W/(m*K)]
    13.705
    """
    def __init__(self, cp_high_range=False, **kwargs):
        if 'p_s' in kwargs.keys():
            self._guess = p_s_initializer(kwargs['p_s'])
        else:
            self._guess = BISMUTH_MELTING_TEMPERATURE*1.5
        super().__init__(cp_high_range, **kwargs)

    @staticmethod
    def T_at_cp_min():
        """
        float : temperature in [K] corresponding to specific heat minimum
        """
        return BISMUTH_T_AT_CP_MIN

    @staticmethod
    def cp_min():
        """
        float : specific heat minimum
        """
        return cp(BISMUTH.T_at_cp_min(), BISMUTH_KEYWORD)

    def _set_constants(self):
        self._T_m0 = BISMUTH_MELTING_TEMPERATURE
        self._Q_m0 = BISMUTH_MELTING_LATENT_HEAT
        self._T_b0 = BISMUTH_BOILING_TEMPERATURE
        self._Q_b0 = BISMUTH_VAPORISATION_HEAT

    def _fill_properties(self):
        self._p_s = self._p_s_correlation(self.T)
        self._p_s_validity = [self.T_m0, self.T_b0]
        self._sigma = self._sigma_correlation(self.T)
        self._sigma_validity = [self.T_m0, 1400.0]
        self._rho = self._rho_correlation(self.T)
        self._rho_validity = [self.T_m0, self.T_b0]
        self._alpha = self._alpha_correlation(self.T)
        self._alpha_validity = [self.T_m0, self.T_b0]
        self._u_s = self._u_s_correlation(self.T)
        self._u_s_validity = [self.T_m0, 1800.0]
        self._beta_s = self._beta_s_correlation(self.T)
        self._beta_s_validity = [self.T_m0, 1800.0]
        self._cp = self._cp_correlation(self.T)
        self._cp_validity = [self.T_m0, self.T_b0]
        self._h = self._h_correlation(self.T)
        self._h_validity = [self.T_m0, self.T_b0]
        self._mu = self._mu_correlation(self.T)
        self._mu_validity = [self.T_m0, 1300.0]
        self._r = self._r_correlation(self.T)
        self._r_validity = [545.0, 1423.0]
        self._k = self._k_correlation(self.T)
        self._k_validity = [self.T_m0, 1000.0]

    def _p_s_correlation(self, T):
        return p_s(T, BISMUTH_KEYWORD)
    
    def _sigma_correlation(self, T):
        return sigma(T, BISMUTH_KEYWORD)

    def _rho_correlation(self, T):
        return rho(T, BISMUTH_KEYWORD)

    def _alpha_correlation(self, T):
        return alpha(T, BISMUTH_KEYWORD)

    def _u_s_correlation(self, T):
        return u_s(T, BISMUTH_KEYWORD)

    def _beta_s_correlation(self, T):
        return beta_s(T, BISMUTH_KEYWORD)
    
    def _cp_correlation(self, T):
        return cp(T, BISMUTH_KEYWORD)

    def _h_correlation(self, T):
        return h(T, BISMUTH_KEYWORD)

    def _mu_correlation(self, T):
        return mu(T, BISMUTH_KEYWORD)

    def _r_correlation(self, T):
        return r(T, BISMUTH_KEYWORD)
    
    def _k_correlation(self, T):
        return k(T, BISMUTH_KEYWORD)
