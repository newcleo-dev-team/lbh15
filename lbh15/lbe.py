"""
Module with liquid lead-bismuth-eutectic (lbe) properties.
:class:`.lbe.LBE` object can be initialized with the temperature
or with one of the available properties (see :class:`.lbe.LBE` for \
the full list).

Each object has the following themophysical properties:

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
        \\exp{\\Big(-22852/T\\Big)}`
    - :math:`\\sigma` lbe surface tension \
      :math:`\\Big[\\frac{N}{m}\\Big]`:

        :math:`\\sigma(T) = \\displaystyle\\Big(448.5 \
        - 0.0799{\\cdot}T\\Big)\\cdot10^{-3}`
    - :math:`\\rho` lbe density \
      :math:`\\Big[\\frac{kg}{m^3}\\Big]`:

        :math:`\\rho(T) = \\displaystyle11065 - 1.293{\\cdot}T`
    - :math:`\\alpha` lbe thermal expansion coefficient \
      :math:`\\Big[\\frac{1}{K}\\Big]`:

        :math:`\\alpha(T) = \\displaystyle\\Big(8558 - T\\Big)^{-1}`
    - :math:`u_s` speed of sound in lbe \
      :math:`\\Big[\\frac{m}{s}\\Big]`:

        :math:`u_s(T) = \\displaystyle1855 - 0.212{\\cdot}T`
    - :math:`\\beta_s` lbe isentropic compressibility \
      :math:`\\Big[\\frac{1}{Pa}\\Big]`:

        :math:`\\beta_s(T) = \\displaystyle\\frac{1}{\\rho(T){\\cdot}u_s(T)^2}`
    - :math:`c_p` lbe specific heat capacity \
      :math:`\\Big[\\frac{J}{kg{\\cdot}K}\\Big]`:

        :math:`c_p(T) = \\displaystyle164.8 - 3.94\\cdot10^{-2}{\\cdot}T \
        + 1.25\\cdot10^{-5}{\\cdot}T^2 - 4.56\\cdot10^{5}{\\cdot}T^{-2}`
    - :math:`h` lbe specific enthalpy (as difference with \
      respect to the melting point enthalpy) \
      :math:`\\Big[\\frac{J}{kg{\\cdot}K}\\Big]`:

        :math:`h(T) = \\displaystyle\
        164.8\\cdot\\Big(T - T_{m0}\\Big) \
        - 1.97\\cdot10^{-2}\\Big(T^2 - T_{m0}^2\\Big) \
        + 4.167\\cdot10^{-6}\\Big(T^3 - T_{m0}^3\\Big)`

        :math:`\\qquad\\qquad- 4.56\\cdot10^5\\Big(T^{-1} - T_{m0}^{-1}\\Big)`
    - :math:`\\mu` lbe dynamic visocity :math:`[Pa{\\cdot}s]`:

        :math:`\\mu(T) = \\displaystyle4.94\\cdot10^{-4}\\cdot\
        \\exp{\\Big(754.1/T\\Bigg)}`
    - :math:`r` lbe electrical resistivity :math:`[\\Omega{\\cdot}m]`:

        :math:`r(T) = \\displaystyle\\Big(90.9 + 0.048{\\cdot}T\\Big)\
        \\cdot10^{-8}`
    - :math:`k` lbe thermal conductivity \
      :math:`\\Big[\\frac{W}{m{\\cdot}K}\\Big]`:

        :math:`k(T) = \\displaystyle3.284 + 1.617\\cdot10^{-2}{\\cdot}T \
        - 2.305\\cdot10^{-6}{\\cdot}T^2`
    - :math:`Pr` Prandtl number :math:`[-]`:

        :math:`Pr(T) = \\displaystyle\\frac{c_p(T)\\cdot\\mu(T)}{k(T)}`

where :math:`T` is the lbe temperature in :math:`[K]`
"""
import numpy as np
from ._lbh15 import LBE_MELTING_TEMPERATURE
from ._lbh15 import LBE_MELTING_LATENT_HEAT, LBE_BOILING_TEMPERATURE
from ._lbh15 import LBE_VAPORISATION_HEAT, LBE_KEYWORD
from ._lbh15 import LBE_T_AT_CP_MIN, LBE_CP_MIN
from ._lbh15 import PropertiesInterface, p_s_initializer


class LBE(PropertiesInterface):
    """
    Class to model lead-bismuth eutectic properties at a given temperature

    Parameters
    ----------
    cp_high_range : bool
        True to initialize the object with temperature larger than
        the one corresponding to cp minumum (if present), False otherwise.
        It is used if \\**kwargs contains 'cp', i.e., if initialization from
        specific heat is required
    \\**kwargs : dict
        Dictionary that specifies the quantity from which the object shall
        be initialized. The available ones are:

        - **T** (float) : temperature [K]
        - **p_s** (float) : saturation vapour pressure [Pa]
        - **sigma** (float) : surface tension [N/m]
        - **rho** (float) : density [Kg/m^3]
        - **alpha** (float) : thermal expansion coefficient [1/K]
        - **u_s** (float) : speed of sound [m/s]
        - **beta_s** (float) : isentropic compressibility [1/Pa]
        - **cp** (float) : specific heat capacity [J/(kg*K)]
        - **h** (float) : specific hentalpy \
        (in respect to melting point) [J/kg]
        - **mu** (float) : dynamic viscosity [Pa*s]
        - **r** (float) : electrical resistivity [Ohm*m]
        - **k** (float) : thermal conductivity [W/(m*K)]

    Examples
    --------
    >>> liquid_lbe = LBE(T=600.0)
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
        Temperature in [K] corresponding to specific heat minimum

        Returns
        -------
        float
        """
        return LBE_T_AT_CP_MIN

    @staticmethod
    def cp_min():
        """
        Minimum value of cp correlation in [J/(kg*K)]

        Returns
        -------
        float
        """
        return LBE_CP_MIN

    def _set_validity_ranges(self):
        """
        Sets validity range for each property
        """
        self._p_s_validity = [self.T_m0, self.T_b0]
        self._sigma_validity = [self.T_m0, 1400.0]
        self._rho_validity = [self.T_m0, self.T_b0]
        self._alpha_validity = [self.T_m0, self.T_b0]
        self._u_s_validity = [400.0, 1100.0]
        self._beta_s_validity = [400.0, 1100.0]
        self._cp_validity = [400.0, 1100.0]
        self._h_validity = [400.0, 1100.0]
        self._mu_validity = [self.T_m0, 1300.0]
        self._r_validity = [self.T_m0, 1100.0]
        self._k_validity = [self.T_m0, 1100.0]

    def _set_constants(self):
        """
        Sets the class constants
        """
        self._T_m0 = LBE_MELTING_TEMPERATURE
        self._Q_m0 = LBE_MELTING_LATENT_HEAT
        self._T_b0 = LBE_BOILING_TEMPERATURE
        self._Q_b0 = LBE_VAPORISATION_HEAT

    def _p_s_correlation(self, T):
        """
        Correlation used to compute saturation vapour pressure

        Parameters
        ----------
        T : float
            Temperature in [K]

        Returns
        -------
        saturation vapour pressure in [Pa] : float
        """
        return 1.22e10 * np.exp(-22552/T)

    def _sigma_correlation(self, T):
        """
        Correlation used to compute surface tension

        Parameters
        ----------
        T : float
            Temperature in [K]

        Returns
        -------
        surface tension in [N/m] : float
        """
        return (448.5 - 0.0799*T)*1e-3

    def _rho_correlation(self, T):
        """
        Correlation used to compute density

        Parameters
        ----------
        T : float
            Temperature in [K]

        Returns
        -------
        density in [kg/m^3] : float
        """
        return 11065 - 1.293*T

    def _alpha_correlation(self, T):
        """
        Correlation used to compute thermal expansion coefficient

        Parameters
        ----------
        T : float
            Temperature in [K]

        Returns
        -------
        thermal expansion coefficient in [1/K] : float
        """
        return 1/(8558 - T)

    def _u_s_correlation(self, T):
        """
        Correlation used to compute sound velocity

        Parameters
        ----------
        T : float
            Temperature in [K]

        Returns
        -------
        sound velocity in [m/s] : float
        """
        return 1855 - 0.212*T

    def _beta_s_correlation(self, T):
        """
        Correlation used to compute isentropic compressibility

        Parameters
        ----------
        T : float
            Temperature in [K]

        Returns
        -------
        isentropic compressibility in [1/Pa] : float
        """
        return 1/(self._rho_correlation(T) * self._u_s_correlation(T)**2)

    def _cp_correlation(self, T):
        """
        Correlation used to compute specific heat capacity

        Parameters
        ----------
        T : float
            Temperature in [K]

        Returns
        -------
        specific heat capacity in [J/(kg*K)] : float
        """
        return (164.8 - 3.94e-2*T + 1.25e-5*T**2
                - 4.56e5*T**-2)

    def _h_correlation(self, T):
        """
        Correlation used to compute specific enthalpy

        Parameters
        ----------
        T : float
            Temperature in [K]

        Returns
        -------
        specific enthalpy in [J/kg] : float
        """
        return (164.8*(T - LBE_MELTING_TEMPERATURE)
                - 1.97e-2*(T**2 - LBE_MELTING_TEMPERATURE**2)
                + 4.167e-6*(T**3 - LBE_MELTING_TEMPERATURE**3)
                + 4.56e5*(T**-1 - LBE_MELTING_TEMPERATURE**-1))

    def _mu_correlation(self, T):
        """
        Correlation used to compute dynamic viscosity

        Parameters
        ----------
        T : float
            Temperature in [K]

        Returns
        -------
        dynamic viscosity in [Pa*s] : float
        """
        return 4.94e-4*np.exp(754.1/T)

    def _r_correlation(self, T):
        """
        Correlation used to compute electrical resistivity

        Parameters
        ----------
        T : float
            Temperature in [K]

        Returns
        -------
        electrical resistivity in [Ohm*m] : float
        """
        return (90.9 + 0.048*T)*1e-8

    def _k_correlation(self, T):
        """
        Correlation used to compute thermal conductivity

        Parameters
        ----------
        T : float
            Temperature in [K]

        Returns
        -------
        thermal conductivity in [W/(m*K)] : float
        """
        return 3.284 + 1.617e-2*T - 2.305e-6*T**2