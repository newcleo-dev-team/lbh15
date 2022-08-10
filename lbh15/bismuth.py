"""
Module with liquid bismuth properties.
Bismuth object can be initialized with the temperature
or with one of the available properties (see :class:`.Bismuth` for \
the full list).

Each object has the following themophysical properties:

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
        \\exp{\\Big(-22858/T\\Big)}`
    - :math:`\\sigma` bismuth surface tension \
      :math:`\\Big[\\frac{N}{m}\\Big]`:

        :math:`\\sigma(T) = \\displaystyle\\Big(420.8 \
        - 0.081{\\cdot}T\\Big)\\cdot10^{-3}`
    - :math:`\\rho` bismuth density \
      :math:`\\Big[\\frac{kg}{m^3}\\Big]`:

        :math:`\\rho(T) = \\displaystyle10725 - 1.22{\\cdot}T`
    - :math:`\\alpha` bismuth thermal expansion coefficient \
      :math:`\\Big[\\frac{1}{K}\\Big]`:

        :math:`\\alpha(T) = \\displaystyle\\Big(8791 - T\\Big)^{-1}`
    - :math:`u_s` speed of sound in bismuth \
      :math:`\\Big[\\frac{m}{s}\\Big]`:

        :math:`u_s(T) = \\displaystyle1616 + 0.187{\\cdot}T \
        - 2.2\\cdot10^{-4}{\\cdot}T`
    - :math:`\\beta_s` bismuth isentropic compressibility \
      :math:`\\Big[\\frac{1}{Pa}\\Big]`:

        :math:`\\beta_s(T) = \\displaystyle\\frac{1}{\\rho(T){\\cdot}u_s(T)^2}`
    - :math:`c_p` bismuth specific heat capacity \
      :math:`\\Big[\\frac{J}{kg{\\cdot}K}\\Big]`:

        :math:`c_p(T) = \\displaystyle118.2 - 5.934\\cdot10^{-3}{\\cdot}T \
        + 7.183\\cdot10^{6}{\\cdot}T^{-2}`
    - :math:`h` bismuth specific enthalpy (as difference with \
      respect to the melting point enthalpy) \
      :math:`\\Big[\\frac{J}{kg{\\cdot}K}\\Big]`:

        :math:`h(T) = \\displaystyle\
        118.2\\cdot\\Big(T - T_{m0}\\Big) \
        + 2.967\\cdot10^{-3}\\Big(T^2 - T_{m0}^2\\Big) \
        - 7.183\\cdot10^6\\Big(T^{-1} - T_{m0}^{-1}\\Big)`
    - :math:`\\mu` bismuth dynamic visocity :math:`[Pa{\\cdot}s]`:

        :math:`\\mu(T) = \\displaystyle4.456\\cdot10^{-4}\\cdot\
        \\exp{\\Big(780/T\\Big)}`
    - :math:`r` bismuth electrical resistivity :math:`[\\Omega{\\cdot}m]`:

        :math:`r(T) = \\displaystyle\\Big(98.96 + 0.0554{\\cdot}T\\Big)\
        \\cdot10^{-8}`
    - :math:`k` bismuth thermal conductivity \
      :math:`\\Big[\\frac{W}{m{\\cdot}K}\\Big]`:

        :math:`k(T) = \\displaystyle7.34 + 9.5\\cdot10^{-3}{\\cdot}T`
    - :math:`Pr` Prandtl number :math:`[-]`:

        :math:`Pr = \\displaystyle\\frac{c_p\\cdot\\mu}{k}`

where :math:`T` is the bismuth temperature in :math:`[K]`
"""
import numpy as np
from ._lbh15 import BISMUTH_MELTING_TEMPERATURE
from ._lbh15 import BISMUTH_MELTING_LATENT_HEAT, BISMUTH_BOILING_TEMPERATURE
from ._lbh15 import BISMUTH_VAPORISATION_HEAT, BISMUTH_KEYWORD
from ._lbh15 import BISMUTH_T_AT_CP_MIN, BISMUTH_CP_MIN
from ._lbh15 import PropertiesInterface, p_s_initializer


class Bismuth(PropertiesInterface):
    """
    Class to model bismuth properties at a given temperature

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
    >>> liquid_bismuth = Bismuth(T=670.0)
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
        Temperature in [K] corresponding to specific heat minimum

        Returns
        -------
        float
        """
        return BISMUTH_T_AT_CP_MIN

    @staticmethod
    def cp_min():
        """
        Minimum value of cp correlation in [J/(kg*K)]

        Returns
        -------
        float
        """
        return BISMUTH_CP_MIN

    def _set_validity_ranges(self):
        """
        Sets validity range for each property
        """
        self._p_s_validity = [self.T_m0, self.T_b0]
        self._sigma_validity = [self.T_m0, 1400.0]
        self._rho_validity = [self.T_m0, self.T_b0]
        self._alpha_validity = [self.T_m0, self.T_b0]
        self._u_s_validity = [self.T_m0, 1800.0]
        self._beta_s_validity = [self.T_m0, 1800.0]
        self._cp_validity = [self.T_m0, self.T_b0]
        self._h_validity = [self.T_m0, self.T_b0]
        self._mu_validity = [self.T_m0, 1300.0]
        self._r_validity = [545.0, 1423.0]
        self._k_validity = [self.T_m0, 1000.0]

    def _set_constants(self):
        """
        Sets the class constants
        :meta private:
        """
        self._T_m0 = BISMUTH_MELTING_TEMPERATURE
        self._Q_m0 = BISMUTH_MELTING_LATENT_HEAT
        self._T_b0 = BISMUTH_BOILING_TEMPERATURE
        self._Q_b0 = BISMUTH_VAPORISATION_HEAT

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
        return 2.67e10 * np.exp(-22858/T)

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
        return (420.8 - 0.081*T)*1e-3

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
        return 10725 - 1.22*T

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
        return 1/(8791 - T)

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
        return 1616 + 0.187*T - 2.2e-4*T**2

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
        return 118.2 + 5.934e-3*T + 7.183e6*T**-2

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
        return (118.2*(T - BISMUTH_MELTING_TEMPERATURE)
                + 2.967e-3*(T**2 - BISMUTH_MELTING_TEMPERATURE**2)
                - 7.183e6*(T**-1 - BISMUTH_MELTING_TEMPERATURE**-1))

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
        return 4.456e-4*np.exp(780/T)

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
        return (98.96 + 0.0554*T)*1e-8

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
        return 7.34 + 9.5e-3*T
