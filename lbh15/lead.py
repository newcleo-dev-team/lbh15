"""
Module with liquid lead properties.
:class:`.lead.Lead` object can be initialized with the temperature
or with one of the available properties (see :class:`.lead.Lead` for \
the full list).

Each object has the following themophysical properties:

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
        \\exp{\\Big(-22131/T\\Big)}`
    - :math:`\\sigma` lead surface tension \
      :math:`\\Big[\\frac{N}{m}\\Big]`:

        :math:`\\sigma(T) = \\displaystyle\\Big(525.9 \
        - 0.113{\\cdot}T\\Big)\\cdot10^{-3}`
    - :math:`\\rho` lead density \
      :math:`\\Big[\\frac{kg}{m^3}\\Big]`:

        :math:`\\rho(T) = \\displaystyle11441 - 1.2795{\\cdot}T`
    - :math:`\\alpha` lead thermal expansion coefficient \
      :math:`\\Big[\\frac{1}{K}\\Big]`:

        :math:`\\alpha(T) = \\displaystyle\\Big(8942 - T\\Big)^{-1}`
    - :math:`u_s` speed of sound in lead \
      :math:`\\Big[\\frac{m}{s}\\Big]`:

        :math:`u_s(T) = \\displaystyle1953 - 0.246{\\cdot}T`
    - :math:`\\beta_s` lead isentropic compressibility \
      :math:`\\Big[\\frac{1}{Pa}\\Big]`:

        :math:`\\beta_s(T) = \\displaystyle\\frac{1}{\\rho(T){\\cdot}u_s(T)^2}`
    - :math:`c_p` lead specific heat capacity :math:`\\Big[\
      \\frac{J}{kg{\\cdot}K}\\Big]`, two correlations are available,\
      sobolev2011 and gurvich1991. The first one is the\
      default one used by :class:`.lead.Lead` and its inherited classes:

        :math:`c_p(T) = \\displaystyle176.2 - 4.923\\cdot10^{-2}{\\cdot}T \
        + 1.544\\cdot10^{-5}{\\cdot}T^2 - 1.524\\cdot10^{6}{\\cdot}T^{-2}`

        :math:`c_p(T) = \\displaystyle175.1 - 4.961\\cdot10^{-2}{\\cdot}T \
        + 1.985\\cdot10^{-5}{\\cdot}T^2 - 2.099\\cdot10^{-9}{\\cdot}T^3 \
        - 1.524\\cdot10^{6}{\\cdot}T^{-2}`
    - :math:`h` lead specific enthalpy (as difference with \
      respect to the melting point enthalpy) \
      :math:`\\Big[\\frac{J}{kg{\\cdot}K}\\Big]`:

        :math:`h(T) = \\displaystyle\
        176.2\\cdot\\Big(T - T_{m0}\\Big) \
        - 2.4615\\cdot10^{-2}\\Big(T^2 - T_{m0}^2\\Big) \
        + 5.147\\cdot10^{-6}\\Big(T^3 - T_{m0}^3\\Big)`

        :math:`\\qquad\\qquad+ 1.524\\cdot10^6\\Big(T^{-1} - T_{m0}^{-1}\\Big)`
    - :math:`\\mu` lead dynamic visocity :math:`[Pa{\\cdot}s]`:

        :math:`\\mu(T) = \\displaystyle4.55\\cdot10^{-4}\\cdot\
        \\exp{\\Big(1069/T\\Big)}`
    - :math:`r` lead electrical resistivity :math:`[\\Omega{\\cdot}m]`:

        :math:`r(T) = \\displaystyle\\Big(67.0 + 0.0471{\\cdot}T\\Big)\
        \\cdot10^{-8}`
    - :math:`k` lead thermal conductivity \
      :math:`\\Big[\\frac{W}{m{\\cdot}K}\\Big]`:

        :math:`k(T) = \\displaystyle9.2 + 0.011{\\cdot}T`
    - :math:`Pr` Prandtl number :math:`[-]`:

        :math:`Pr(T) = \\displaystyle\\frac{c_p(T)\\cdot\\mu(T)}{k(T)}`

where :math:`T` is the lead temperature in :math:`[K]`
"""
import numpy as np
from ._lbh15 import LEAD_MELTING_TEMPERATURE
from ._lbh15 import LEAD_MELTING_LATENT_HEAT, LEAD_BOILING_TEMPERATURE
from ._lbh15 import SOBOLEV_KEYWORD, GURVICH_KEYWORD
from ._lbh15 import LEAD_VAPORISATION_HEAT, LEAD_KEYWORD
from ._lbh15 import LEAD_T_AT_CP_MIN_SOBOLEV, LEAD_T_AT_CP_MIN_GURVICH
from ._lbh15 import LEAD_CP_MIN_SOBOLEV, LEAD_CP_MIN_GURVICH
from ._lbh15 import PropertiesInterface, p_s_initializer


class Lead(PropertiesInterface):
    """
    Class to model lead properties at a given temperature

    Parameters
    ----------
    cp_correlation_to_use : str
        Name of cp correlation, can be 'sobolev2011' or 'gurvich1991'
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
    Compare :class:`.lead.Lead` specific heat values at T=800 K
    with with cp_correlation_to_use equal to sobolev2011 and gurvich1991:

    >>> liquid_lead_1 = Lead(T=800)  # cp_correlation_to_use=sobolev2011
    >>> liquid_lead_2 = Lead(T=800, cp_correlation_to_use=gurvich1991)
    >>> liquid_lead_1.cp, liquid_lead_2.cp
    (144.31634999999997, 144.66006199999998)
    """
    def __init__(self, cp_correlation_to_use=SOBOLEV_KEYWORD,
                 cp_high_range=False, **kwargs):
        self._cp_correlation_to_use = cp_correlation_to_use
        if 'p_s' in kwargs.keys():
            self._guess = p_s_initializer(kwargs['p_s'])
        else:
            self._guess = LEAD_MELTING_TEMPERATURE*1.7
        super().__init__(cp_high_range=cp_high_range, **kwargs)

    @staticmethod
    def T_at_cp_min(cp_correlation_to_use=SOBOLEV_KEYWORD):
        """
        Temperature in [K] corresponding to specific heat minimum

        Parameters
        ----------
        cp_correlation_to_use : str
            Name of cp correlation, can be 'sobolev2011' or 'gurvich1991'

        Returns
        -------
        float
        """
        if cp_correlation_to_use == SOBOLEV_KEYWORD:
            rvalue = LEAD_T_AT_CP_MIN_SOBOLEV
        elif cp_correlation_to_use == GURVICH_KEYWORD:
            rvalue = LEAD_T_AT_CP_MIN_GURVICH
        else:
            raise ValueError("cp correlation can be one among: {:s}, "
                             "{:s}. {:s} was provided"
                             .format(SOBOLEV_KEYWORD, GURVICH_KEYWORD,
                                     cp_correlation_to_use))

        return rvalue

    @staticmethod
    def cp_min(cp_correlation_to_use=SOBOLEV_KEYWORD):
        """
        Minimum value of cp correlation in [J/(kg*K)]

        Parameters
        ----------
        cp_correlation_to_use : str
            Name of cp correlation, can be 'sobolev2011' or 'gurvich1991'

        Returns
        -------
        float
        """
        if cp_correlation_to_use == SOBOLEV_KEYWORD:
            rvalue = LEAD_CP_MIN_SOBOLEV
        elif cp_correlation_to_use == GURVICH_KEYWORD:
            rvalue = LEAD_CP_MIN_GURVICH
        else:
            raise ValueError("cp correlation can be one among: {:s}, "
                             "{:s}. {:s} was provided"
                             .format(SOBOLEV_KEYWORD, GURVICH_KEYWORD,
                                     cp_correlation_to_use))

        return rvalue

    def _set_validity_ranges(self):
        """
        Sets validity range for each property
        """
        self._p_s_validity = [self.T_m0, self.T_b0]
        self._sigma_validity = [self.T_m0, 1300.0]
        self._rho_validity = [self.T_m0, self.T_b0]
        self._alpha_validity = [self.T_m0, self.T_b0]
        self._u_s_validity = [self.T_m0, 2000.0]
        self._beta_s_validity = [self.T_m0, 2000.0]
        self._cp_validity = [self.T_m0, 2000.0]
        self._h_validity = [self.T_m0, 2000.0]
        self._mu_validity = [self.T_m0, 1473.0]
        self._r_validity = [601.0, 1273.0]
        self._k_validity = [self.T_m0, 1300.0]

    def _set_constants(self):
        """
        Sets the class constants
        """
        self._T_m0 = LEAD_MELTING_TEMPERATURE
        self._Q_m0 = LEAD_MELTING_LATENT_HEAT
        self._T_b0 = LEAD_BOILING_TEMPERATURE
        self._Q_b0 = LEAD_VAPORISATION_HEAT

    @property
    def cp_correlation_used(self):
        """
        str : name of cp correlation used
        """
        return self._cp_correlation_to_use

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
        return 5.76e9 * np.exp(-22131/T)

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
        return (525.9 - 0.113*T)*1e-3

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
        return 11441 - 1.2795*T

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
        return 1/(8942 - T)

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
        return 1953 - 0.246*T

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
        if self.cp_correlation_used == SOBOLEV_KEYWORD:
            rvalue = (176.2 - 4.923e-2*T + 1.544e-5*T**2
                      - 1.524e6*T**-2)
        elif self.cp_correlation_used == GURVICH_KEYWORD:
            rvalue = (175.1 - 4.961e-2*T + 1.985e-5*T**2
                      - 2.099e-9*T**3 - 1.524e6*T**-2)
        else:
            raise ValueError("cp correlation can be one among: {:s}, "
                             "{:s}. {:s} was provided"
                             .format(SOBOLEV_KEYWORD, GURVICH_KEYWORD,
                                     self.cp_correlation_used))
        return rvalue

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
        return (176.2*(T - LEAD_MELTING_TEMPERATURE)
                - 2.4615e-2*(T**2 - LEAD_MELTING_TEMPERATURE**2)
                + 5.147e-6*(T**3 - LEAD_MELTING_TEMPERATURE**3)
                + 1.524e6*(T**-1 - LEAD_MELTING_TEMPERATURE**-1))

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
        return 4.55e-4*np.exp(1069/T)

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
        return (67.0 + 0.0471*T)*1e-8

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
        return 9.2 + 0.011*T