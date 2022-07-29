"""
Module that contains liquid lead properties objects.
Those objects can be initialized with the temperature
(:class:`.lead.Lead`) or with one of the available properties
(:class:`.lead.LeadMu`, :class:`.lead.LeadRho`, etc)

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
    - :math:`c_p` lead specific heat :math:`\\Big[\
      \\frac{J}{kg{\\cdot}K}\\Big]`, two correlations are available,\
      sobolev2011 and gurvich1991. The first one is the\
      default one used by :class:`.lead.Lead` and its inherited classes:

        :math:`c_p(T) = \\displaystyle176.2 - 4.923\\cdot10^{-2}{\\cdot}T \
        + 1.544\\cdot10^{-5}{\\cdot}T^2 - 1.524\\cdot10^{6}{\\cdot}T^{-2}`

        :math:`c_p(T) = \\displaystyle175.1 - 4.961\\cdot10^{-2}{\\cdot}T \
        + 1.985\\cdot10^{-5}{\\cdot}T^2 - 2.099\\cdot10^{-9}{\\cdot}T^3 \
        - 1.524\\cdot10^{6}{\\cdot}T^{-2}`
    - :math:`h` lead specific enthalpy (in respect to melting point) \
      :math:`\\Big[\\frac{J}{kg{\\cdot}K}\\Big]`:

        :math:`h(T) = \\displaystyle\
        176.2\\cdot\\Big(T - T_{m0}\\Big) \
        - 2.4615\\cdot10^{-2}\\Big(T^2 - T_{m0}^2\\Big) \
        + 5.147\\cdot10^{-6}\\Big(T^3 - T_{m0}^3\\Big)`

        :math:`\\qquad\\qquad+ 1.524\\cdot10^6\\Big(T^{-1} - T_{m0}^{-1}\\Big)`
    - :math:`\\mu` lead dynamic visocity :math:`[Pa{\\cdot}s]`:

        :math:`\\mu(T) = \\displaystyle4.55\\cdot10^{-4}\\cdot\
        \\exp\\Bigg({\\frac{1069}{T}}\\Bigg)`
    - :math:`r` lead electrical resistivity :math:`[\\Omega{\\cdot}m]`:

        :math:`r(T) = \\displaystyle\\Big(67.0 + 0.0471{\\cdot}T\\Big)\
        \\cdot10^{-8}`
    - :math:`k` lead thermal conductivity \
      :math:`\\Big[\\frac{W}{m{\\cdot}K}\\Big]`:

        :math:`k(T) = \\displaystyle9.2 + 0.011{\\cdot}T`

where :math:`T` is the lead temperature in :math:`[K]`
"""
from ._lbeh15 import LEAD_MELTING_TEMPERATURE
from ._lbeh15 import LEAD_MELTING_LATENT_HEAT, LEAD_BOILING_TEMPERATURE
from ._lbeh15 import SOBOLEV_KEYWORD, GURVICH_KEYWORD
from ._lbeh15 import LEAD_VAPORISATION_HEAT, LEAD_KEYWORD
from ._lbeh15 import LEAD_T_AT_CP_MIN, LEAD_T_AT_CP_COMPACT_MIN
from ._lbeh15 import PropertiesInterface
from ._utils import p_s, h, sigma, rho, alpha, u_s
from ._utils import beta_s, cp, mu, r, k
from ._utils import p_s_initializer


class Lead(PropertiesInterface):
    """
    Class to model lead properties at a given temperature

    Parameters
    ----------
    cp_correlation : str
        Name of cp correlation, can be 'sobolev2011' or 'gurvich1991'
    cp_high_range : bool
        True to initialize the object with temperature larger than
        the one corresponding to cp minumum (if present), False otherwise.
        It is used if \**kwargs contains 'cp', i.e., if initialization from
        specific heat is required
    \**kwargs : dict
        Dictionary that spefifies the quantity from which the parameter shall
        be initialized. The available ones are:

        - 'T' : temperature [K]
        - 'p_s' : saturation vapour pressure [Pa]
        - 'sigma' : surface tension [N/m] 
        - 'rho' : density [Kg/m^3]
        - 'alpha' : thermal expansion coefficient [1/K]
        - 'u_s': speed of sound [m/s]
        - 'beta_s' : isentropic compressibility [1/Pa]
        - 'cp' : specific heat capacity [J/(kg*K)]
        - 'h' : specific hentalpy (in respect to melting point) [J/kg]
        - 'mu' : dynamic viscosity [Pa*s]
        - 'r' : electrical resistivity [Ohm*m]
        - 'k' : thermal conductivity [W/(m*K)]

    Examples
    --------
    Compare :class:`.lead.Lead` specific heat values at T=800 K
    with with cp_correlation equal to sobolev2011 and gurvich1991:

    >>> liquid_lead_1 = Lead(800)  # correlation=sobolev2011
    >>> liquid_lead_2 = Lead(800, correlation=gurvich1991)
    >>> liquid_lead_1.cp, liquid_lead_2.cp
    (144.31634999999997, 144.66006199999998)
    """
    def __init__(self, cp_correlation_to_use=SOBOLEV_KEYWORD, cp_high_range=False, **kwargs):
        self._cp_correlation_to_use = cp_correlation_to_use
        if 'p_s' in kwargs.keys():
            self._guess = p_s_initializer(kwargs['p_s'])
        else:
            self._guess = LEAD_MELTING_TEMPERATURE*1.7
        super().__init__(cp_high_range=cp_high_range, **kwargs)

    @staticmethod
    def T_at_cp_min(cp_correlation=SOBOLEV_KEYWORD):
        """
        Temperature in [K] corresponding to specific heat minimum

        Parameters
        ----------
        cp_correlation : str
            Name of cp correlation, can be 'sobolev2011' or 'gurvich1991'
        """
        if cp_correlation:
            rvalue = LEAD_T_AT_CP_COMPACT_MIN
        else:
            rvalue = LEAD_T_AT_CP_MIN

        return rvalue

    @staticmethod
    def cp_min(cp_correlation=SOBOLEV_KEYWORD):
        """
        Minimum value of cp correlation in [J/(kg*K)]

        Parameters
        ----------
        cp_correlation : str
            Name of cp correlation, can be 'sobolev2011' or 'gurvich1991'
        """
        return cp(Lead.T_at_cp_min(cp_correlation),
                  LEAD_KEYWORD, cp_correlation)

    def _fill_properties(self):
        """
        Fills the class properties
        """
        self._p_s = self._p_s_correlation(self.T)
        self._p_s_validity = [self.T_m0, self.T_b0]
        self._sigma = self._sigma_correlation(self.T)
        self._sigma_validity = [self.T_m0, 1300.0]
        self._rho = self._rho_correlation(self.T)
        self._rho_validity = [self.T_m0, self.T_b0]
        self._alpha = self._alpha_correlation(self.T)
        self._alpha_validity = [self.T_m0, self.T_b0]
        self._u_s = self._u_s_correlation(self.T)
        self._u_s_validity = [self.T_m0, 2000.0]
        self._beta_s = self._beta_s_correlation(self.T)
        self._beta_s_validity = [self.T_m0, 2000.0]
        self._cp = self._cp_correlation(self.T)
        self._cp_validity = [self.T_m0, 2000.0]
        self._h = self._h_correlation(self.T)
        self._h_validity = [self.T_m0, 2000.0]
        self._mu = self._mu_correlation(self.T)
        self._mu_validity = [self.T_m0, 1473.0]
        self._r = self._r_correlation(self.T)
        self._r_validity = [601.0, 1273.0]
        self._k = self._k_correlation(self.T)
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
        return p_s(T, LEAD_KEYWORD)
    
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
        return sigma(T, LEAD_KEYWORD)

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
        return rho(T, LEAD_KEYWORD)

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
        return alpha(T, LEAD_KEYWORD)

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
        return u_s(T, LEAD_KEYWORD)

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
        return beta_s(T, LEAD_KEYWORD)
    
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
        return cp(T, LEAD_KEYWORD, self.cp_correlation_used)

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
        return h(T, LEAD_KEYWORD)

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
        return mu(T, LEAD_KEYWORD)

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
        return r(T, LEAD_KEYWORD)
    
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
        return k(T, LEAD_KEYWORD)
