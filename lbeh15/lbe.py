"""
Module that contains liquid lead-bismuth-eutectic (lbe) properties objects.
Those objects can be initialized with the temperature
(:class:`.lbe.LBE`) or with one of the available properties
(:class:`.lbe.LBEMu`, :class:`.lbe.LBERho`, etc)

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
    - :math:`h` lbe specific enthalpy (in respect to melting \
      point) :math:`\\Big[\\frac{J}{kg{\\cdot}K}\\Big]`:

        :math:`h(T) = \\displaystyle\
        164.8\\cdot\\Big(T - T_{m0}\\Big) \
        - 1.97\\cdot10^{-2}\\Big(T^2 - T_{m0}^2\\Big) \
        + 4.167\\cdot10^{-2}\\Big(T^3 - T_{m0}^3\\Big)`

        :math:`\\qquad\\qquad- 7.183\\cdot10^6\\Big(T^{-1} - T_{m0}^{-1}\\Big)`
    - :math:`\\mu` lbe dynamic visocity :math:`[Pa{\\cdot}s]`:

        :math:`\\mu(T) = \\displaystyle4.94\\cdot10^{-4}\\cdot\
        \\exp\\Bigg({\\frac{754.1}{T}}\\Bigg)`
    - :math:`r` lbe electrical resistivity :math:`[\\Omega{\\cdot}m]`:

        :math:`r(T) = \\displaystyle\\Big(90.9 + 0.048{\\cdot}T\\Big)\
        \\cdot10^{-8}`
    - :math:`k` lbe thermal conductivity \
      :math:`\\Big[\\frac{W}{m{\\cdot}K}\\Big]`:

        :math:`k(T) = \\displaystyle3.284 + 1.617\\cdot10^{-2}{\\cdot}T \
        - 2.305\\cdot10^{-6}{\\cdot}T^2`

where :math:`T` is the lbe temperature in :math:`[K]`
"""
from ._lbeh15 import LBE_MELTING_TEMPERATURE
from ._lbeh15 import LBE_MELTING_LATENT_HEAT, LBE_BOILING_TEMPERATURE
from ._lbeh15 import LBE_VAPORISATION_HEAT, LBE_KEYWORD
from ._lbeh15 import LBE_T_AT_CP_MIN
from ._lbeh15 import PropertiesInterface
from ._utils import p_s, h, sigma, rho, alpha, u_s
from ._utils import beta_s, cp, mu, r, k
from ._utils import p_s_initializer


class LBE(PropertiesInterface):
    """
    Class to model lead-bismuth eutectic properties at a given temperature

    Parameters
    ----------
    T : float
        Temperature in [K]

    Examples
    --------
    >>> liquid_lbe = LBE(600)
    >>> liquid_lbe.mu  # [Pa*s]
    0.001736052003181349
    """
    def __init__(self, cp_high_range=False, **kwargs):
        if 'p_s' in kwargs.keys():
            self._guess = p_s_initializer(kwargs['p_s'])
        else:
            self._guess = LBE_MELTING_TEMPERATURE*2.0
        super().__init__(cp_high_range, **kwargs)

    @staticmethod
    def T_at_cp_min():
        """
        float : temperature in [K] corresponding to specific heat minimum
        """
        return LBE_T_AT_CP_MIN

    @staticmethod
    def cp_min():
        """
        float : specific heat minimum
        """
        return cp(LBE.T_at_cp_min(), LBE_KEYWORD)

    def _set_constants(self):
        self._T_m0 = LBE_MELTING_TEMPERATURE
        self._Q_m0 = LBE_MELTING_LATENT_HEAT
        self._T_b0 = LBE_BOILING_TEMPERATURE
        self._Q_b0 = LBE_VAPORISATION_HEAT

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
        self._u_s_validity = [self.T_m0, self.T_b0]
        self._beta_s = self._beta_s_correlation(self.T)
        self._u_s_validity = [self.T_m0, self.T_b0]
        self._cp = self._cp_correlation(self.T)
        self._cp_validity = [400.0, self.T_b0]
        self._h = self._h_correlation(self.T)
        self._h_validity = [400.0, self.T_b0]
        self._mu = self._mu_correlation(self.T)
        self._mu_validity = [self.T_m0, self.T_b0]
        self._r = self._r_correlation(self.T)
        self._r_validity = [self.T_m0, 1100.0]
        self._k = self._k_correlation(self.T)
        self._k_validity = [self.T_m0, 1100.0]

    def _p_s_correlation(self, T):
        return p_s(T, LBE_KEYWORD)
    
    def _sigma_correlation(self, T):
        return sigma(T, LBE_KEYWORD)

    def _rho_correlation(self, T):
        return rho(T, LBE_KEYWORD)

    def _alpha_correlation(self, T):
        return alpha(T, LBE_KEYWORD)

    def _u_s_correlation(self, T):
        return u_s(T, LBE_KEYWORD)

    def _beta_s_correlation(self, T):
        return beta_s(T, LBE_KEYWORD)
    
    def _cp_correlation(self, T):
        return cp(T, LBE_KEYWORD)

    def _h_correlation(self, T):
        return h(T, LBE_KEYWORD)

    def _mu_correlation(self, T):
        return mu(T, LBE_KEYWORD)

    def _r_correlation(self, T):
        return r(T, LBE_KEYWORD)
    
    def _k_correlation(self, T):
        return k(T, LBE_KEYWORD)