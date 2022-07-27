import warnings
from scipy.optimize import fsolve
from scipy.constants import atmosphere

# KEYWORDS
LEAD_KEYWORD = "lead"
BISMUTH_KEYWORD = "bismuth"
LBE_KEYWORD = "lbe"

# LEAD CONSTANTS
LEAD_MELTING_TEMPERATURE = 600.6  # [K]
LEAD_MELTING_LATENT_HEAT = 23.07e3  # [J/kg]
LEAD_BOILING_TEMPERATURE = 2021  # [K]
LEAD_VAPORISATION_HEAT = 858.6e3  # [J/kg]
LEAD_T_AT_CP_MIN = 1682.522  # [K]
LEAD_T_AT_CP_COMPACT_MIN = 1568.665  # [K]

# BISMUTH CONSTANTS
BISMUTH_MELTING_TEMPERATURE = 544.6  # [K]
BISMUTH_MELTING_LATENT_HEAT = 53.3e3  # [J/kg]
BISMUTH_BOILING_TEMPERATURE = 1831  # [K]
BISMUTH_VAPORISATION_HEAT = 856.2e3  # [J/kg]
BISMUTH_T_AT_CP_MIN = 1342.753  # [K]

# LEAD-BISMUTH-EUTECTIC CONSTANTS
LBE_MELTING_TEMPERATURE = 398.0  # [K]
LBE_MELTING_LATENT_HEAT = 38.6e3  # [J/kg]
LBE_BOILING_TEMPERATURE = 1927  # [K]
LBE_VAPORISATION_HEAT = 856.6e3  # [J/kg]
LBE_T_AT_CP_MIN = 1566.510  # [K]


class PropertiesInterface:
    """
    Base class that defines liquid metal properties object
    at a given temperature

    Parameters
    ----------
    T : float
        Temperature in [K]
    """
    _T_m0 = 0
    _Q_m0 = 0
    _T_b0 = 0
    _Q_b0 = 0
    _p = 0
    _T = 0
    _T_assigned = False
    _p_s = 0
    _p_s_validity = [0, 0]
    _sigma = 0
    _sigma_validity = [0, 0]
    _rho = 0
    _rho_validity = [0, 0]
    _alpha = 0
    _alpha_validity = [0, 0]
    _u_s = 0
    _u_s_validity = [0, 0]
    _beta_s = 0
    _beta_s_validity = [0, 0]
    _cp = 0
    _cp_validity = [0, 0]
    _delta_h = 0
    _delta_h_validity = [0, 0]
    _mu = 0
    _mu_validity = [0, 0]
    _r = 0
    _r_validity = [0, 0]
    _k = 0
    _k_validity = [0, 0]

    def __init__(self, T):
        self._p = atmosphere
        self._set_constants()
        self.__fill_class_attributes(T)

    @property
    def T_m0(self):
        """
        float : melting temperature [K]
        """
        return self._T_m0

    @property
    def Q_m0(self):
        """
        float : melting latent heat [J/kg]
        """
        return self._Q_m0

    @property
    def T_b0(self):
        """
        float : boiling temperature [K]
        """
        return self._T_b0

    @property
    def Q_b0(self):
        """
        float : vaporisation heat [J/kg]
        """
        return self._Q_b0

    @property
    def p(self):
        """
        float : pressure adopted for property calculation, i.e.,
        atmospheric pressure
        """
        return self._p

    @property
    def T(self):
        """
        float : temperature used to compute properties [K]
        """
        return self._T

    @property
    def T_assigned(self):
        """
        bool : true if temperature correctly assigned, false otherwise
        """
        return self._T_assigned

    @property
    def p_s(self):
        """
        float : saturation vapour pressure [Pa]
        """
        self._check_validity_range(self._p_s_validity, 'p_s')
        return self._p_s

    @property
    def sigma(self):
        """
        float : surface tension [N/m]
        """
        self._check_validity_range(self._sigma_validity, 'sigma')
        return self._sigma

    @property
    def rho(self):
        """
        float : density [kg/m^3]
        """
        self._check_validity_range(self._rho_validity, 'rho')
        return self._rho

    @property
    def alpha(self):
        """
        float : thermal expansion coefficient [1/K]
        """
        self._check_validity_range(self._alpha_validity, 'alpha')
        return self._alpha

    @property
    def u_s(self):
        """
        float : sound velocity in [m/s]
        """
        self._check_validity_range(self._u_s_validity, 'u_s')
        return self._u_s

    @property
    def beta_s(self):
        """
        float : isentropic compressibility [1/Pa]
        """
        self._check_validity_range(self._beta_s_validity, 'beta_s')
        return self._beta_s

    @property
    def cp(self):
        """
        float : specific heat capacity [J/(kg*K)]
        """
        self._check_validity_range(self._cp_validity, 'cp')
        return self._cp

    @property
    def delta_h(self):
        """
        float : specific enthalpy difference from melting point [J/kg]
        """
        self._check_validity_range(self._delta_h_validity, 'delta_h')
        return self._delta_h

    @property
    def mu(self):
        """
        float : dynamic viscosity [Ps*s]
        """
        self._check_validity_range(self._mu_validity, 'mu')
        return self._mu

    @property
    def r(self):
        """
        float : electrical resistivity [Ohm*m]
        """
        self._check_validity_range(self._r_validity, 'r')
        return self._r

    @property
    def k(self):
        """
        float : thermal conductivity [W/(m*K)]
        """
        self._check_validity_range(self._k_validity, 'k')
        return self._k

    def _check_validity_range(self, validity_range, property_name):
        """
        Checks if temperature is inside validity range of property. If not
        warns the user.

        Parameters
        ----------
        validity_range : list
            List of two elements with lower and upper bound temperature
            of property validity range
        property_name : str
            name of the property
        """
        inside = False
        if self.T >= validity_range[0] and self.T <= validity_range[1]:
            inside = True
        if not inside:
            warnings.warn("Temperature {:7.2f} is outside {:s} range"
                          "[{:7.2f}, {:7.2f}] K"
                          .format(self.T, property_name,
                                  validity_range[0], validity_range[1]),
                          stacklevel=3)

    def _fill_properties(self):
        """
        Fills the class properties
        """
        raise NotImplementedError("{:s}._fill_properties NOT IMPLEMENTED"
                                  .format(type(self).__name__))

    def _set_constants(self):
        """
        Sets the class constants
        """
        raise NotImplementedError("{:s}._set_constants NOT IMPLEMENTED"
                                  .format(type(self).__name__))

    def __fill_class_attributes(self, T):
        """
        Fills all the class attributes.

        Parameters
        ----------
        T : float
            Temperature in [K]
        """
        self.__assign_T(T)

        # continue if temperature was correctly assigned
        if self.T_assigned:
            self._fill_properties()

    def __assign_T(self, T):
        """
        Function used to set class temperature, checking if
        temperature value in K is strictly positive

        Parameters
        ----------
        T : float
            Temperature in [K]
        """
        if T > self.T_m0 and T < self.T_b0:
            self._T_assigned = True
            self._T = T
        else:
            if T >= self.T_b0:
                raise ValueError("Temperature must be smaller than "
                                 "boiling temperature ({:7.2f} [K]), {:7.2f} "
                                 "[K] was provided".format(self.T_b0, T))
            elif T > 0 and T <= self.T_m0:
                raise ValueError("Temperature must be larger than "
                                 "melting temerature ({:7.2f} [K]), {:7.2f} "
                                 "[K] was provided".format(self.T_m0, T))
            else:
                raise ValueError("Temperature must be "
                                 "strictly positive, "
                                 "{:7.2f} [K] was provided".format(T))


class PropertiesFromXInterface:
    """
    Base class that defines liquid metal properties object
    initialized with one of its properties.

    Parameters
    ----------
    function_of_T : function
        function that implements the dependency of the property on temperature
        in [K]
    target : float
        physical property value
    fluid : str
        fluid for which calculation shall be performed,
        can be one among lead, bismuth or lbe
    guess : float
        initial guess of temperature in [K]
    high_range : bool
        True to initialize the object with temperature larger than
        the one corresponding to function_of_T minumum (if present),
        False otherwise
    """
    def __init__(self, function_of_T, target, fluid, guess, high_range=False):

        self._function_of_T = function_of_T

        if not high_range:
            res = fsolve(self._function_to_solve, x0=[guess],
                         args=(fluid, target), xtol=1e-10)
            temp = res[0]
        else:
            res = fsolve(self._function_to_solve, x0=[guess, 4*guess],
                         args=(fluid, target), xtol=1e-10)
            if len(res) > 0:
                temp = res[1]
            else:
                temp = res[0]
        instance = self._get_fluid_instance(temp)

        warnings.filterwarnings('ignore')
        if instance is not None:
            for attr in dir(instance):
                if not attr.startswith('_') and not hasattr(self, attr):
                    setattr(self, attr, getattr(instance, attr))

    def _get_fluid_instance(self, T):
        """
        Returns a fluid properties object

        Parameters
        ----------
        T : float
            temperature in [K]
        """
        raise NotImplementedError("{:s}._get_fluid_instance NOT IMPLEMENTED"
                                  .format(type(self).__name__))

    def _function_to_solve(self, T, fluid, target):
        """
        Defines the function for which the root must be found

        Parameters
        ----------
        T : float
            Temperature in [K]
        target : float
            physical property value
        fluid : str
            fluid for which calculation shall be performed,
            can be one among lead, bismuth or lbe

        Returns
        -------
        float
            evaluation of the correlation at T minus the target
        """
        return self._function_of_T(T, fluid) - target
