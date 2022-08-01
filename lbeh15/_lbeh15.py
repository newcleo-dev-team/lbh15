import warnings
from scipy.optimize import fsolve
from scipy.constants import atmosphere
from abc import ABC, abstractmethod

# KEYWORDS
LEAD_KEYWORD = "lead"
BISMUTH_KEYWORD = "bismuth"
LBE_KEYWORD = "lbe"
GURVICH_KEYWORD = 'gurvich1991'
SOBOLEV_KEYWORD = 'sobolev2011'
PROPERTIES_FOR_INITIALIZATION = (['T', 'p_s', 'sigma',
                                  'rho', 'alpha', 'u_s',
                                  'beta_s', 'cp', 'h',
                                  'mu', 'r', 'k'])

# LEAD CONSTANTS
LEAD_MELTING_TEMPERATURE = 600.6  # [K]
LEAD_MELTING_LATENT_HEAT = 23.07e3  # [J/kg]
LEAD_BOILING_TEMPERATURE = 2021  # [K]
LEAD_VAPORISATION_HEAT = 858.6e3  # [J/kg]
LEAD_T_AT_CP_MIN_GURVICH = 1682.522  # [K]
LEAD_T_AT_CP_MIN_SOBOLEV = 1568.665  # [K]
LEAD_CP_MIN_GURVICH = 137.287133  # [J/(kg*K)]
LEAD_CP_MIN_SOBOLEV = 136.348649  # [J/(kg*K)]

# BISMUTH CONSTANTS
BISMUTH_MELTING_TEMPERATURE = 544.6  # [K]
BISMUTH_MELTING_LATENT_HEAT = 53.3e3  # [J/kg]
BISMUTH_BOILING_TEMPERATURE = 1831  # [K]
BISMUTH_VAPORISATION_HEAT = 856.2e3  # [J/kg]
BISMUTH_T_AT_CP_MIN = 1342.753  # [K]
BISMUTH_CP_MIN = 130.151844  # [J/(kg*K)]

# LEAD-BISMUTH-EUTECTIC CONSTANTS
LBE_MELTING_TEMPERATURE = 398.0  # [K]
LBE_MELTING_LATENT_HEAT = 38.6e3  # [J/kg]
LBE_BOILING_TEMPERATURE = 1927  # [K]
LBE_VAPORISATION_HEAT = 856.6e3  # [J/kg]
LBE_T_AT_CP_MIN = 1566.510  # [K]
LBE_CP_MIN = 133.568103  # [J/(kg*K)]


def p_s_initializer(p_s):
    """
    Returns a temperature guess according to the value
    of the saturation vapour pressure

    Parameters
    ----------
    p_s : float
        saturation vapour pressure in [Pa]

    Returns
    -------
    rvalue : float
        Temperature guess in [K]
    """
    if p_s < 1e-2:
        rvalue = 800
    elif p_s >= 1e-2 and p_s < 1e2:
        rvalue = 1200
    else:
        rvalue = 2000

    return rvalue


class PropertiesInterface(ABC):
    """
    Abstract class that defines liquid metal properties object
    at a given temperature

    Parameters
    ----------
    cp_high_range : bool
        True to initialize the object with temperature larger than
        the one corresponding to cp minumum (if present), False otherwise.
        It is used if **kwargs contains 'cp', i.e., if initialization from
        specific heat is required
    **kwargs : dict
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
    _h = 0
    _h_validity = [0, 0]
    _mu = 0
    _mu_validity = [0, 0]
    _r = 0
    _r_validity = [0, 0]
    _k = 0
    _k_validity = [0, 0]
    _guess = 0
    __cp_high_range = False

    def __init__(self, cp_high_range=False, **kwargs):
        self.__cp_high_range = cp_high_range
        self.__fill_class_attributes(kwargs)

    @staticmethod
    def properties_for_initialization():
        """
        List of available properties that can be used for
        initialization

        Returns
        -------
        list
        """
        return PROPERTIES_FOR_INITIALIZATION.copy()

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
    def p_s_validity(self):
        """
        list : temperature validity range for p_s correlation
        """
        return self._p_s_validity.copy()

    @property
    def sigma(self):
        """
        float : surface tension [N/m]
        """
        self._check_validity_range(self._sigma_validity, 'sigma')
        return self._sigma

    @property
    def sigma_validity(self):
        """
        list : temperature validity range for sigma correlation
        """
        return self._sigma_validity.copy()

    @property
    def rho(self):
        """
        float : density [kg/m^3]
        """
        self._check_validity_range(self._rho_validity, 'rho')
        return self._rho

    @property
    def rho_validity(self):
        """
        list : temperature validity range for rho correlation
        """
        return self._rho_validity.copy()

    @property
    def alpha(self):
        """
        float : thermal expansion coefficient [1/K]
        """
        self._check_validity_range(self._alpha_validity, 'alpha')
        return self._alpha

    @property
    def alpha_validity(self):
        """
        list : temperature validity range for alpha correlation
        """
        return self._alpha_validity.copy()

    @property
    def u_s(self):
        """
        float : sound velocity in [m/s]
        """
        self._check_validity_range(self._u_s_validity, 'u_s')
        return self._u_s

    @property
    def u_s_validity(self):
        """
        list : temperature validity range for u_s correlation
        """
        return self._u_s_validity.copy()

    @property
    def beta_s(self):
        """
        float : isentropic compressibility [1/Pa]
        """
        self._check_validity_range(self._beta_s_validity, 'beta_s')
        return self._beta_s

    @property
    def beta_s_validity(self):
        """
        list : temperature validity range for beta_s correlation
        """
        return self._beta_s_validity.copy()

    @property
    def cp(self):
        """
        float : specific heat capacity [J/(kg*K)]
        """
        self._check_validity_range(self._cp_validity, 'cp')
        return self._cp

    @property
    def cp_validity(self):
        """
        list : temperature validity range for cp correlation
        """
        return self._cp_validity.copy()

    @property
    def h(self):
        """
        float : specific enthalpy difference from melting point [J/kg]
        """
        self._check_validity_range(self._h_validity, 'h')
        return self._h

    @property
    def h_validity(self):
        """
        list : temperature validity range for h correlation
        """
        return self._h_validity.copy()

    @property
    def mu(self):
        """
        float : dynamic viscosity [Ps*s]
        """
        self._check_validity_range(self._mu_validity, 'mu')
        return self._mu

    @property
    def mu_validity(self):
        """
        list : temperature validity range for mu correlation
        """
        return self._mu_validity.copy()

    @property
    def r(self):
        """
        float : electrical resistivity [Ohm*m]
        """
        self._check_validity_range(self._r_validity, 'r')
        return self._r

    @property
    def r_validity(self):
        """
        list : temperature validity range for r correlation
        """
        return self._r_validity.copy()

    @property
    def k(self):
        """
        float : thermal conductivity [W/(m*K)]
        """
        self._check_validity_range(self._k_validity, 'k')
        return self._k

    @property
    def k_validity(self):
        """
        list : temperature validity range for k correlation
        """
        return self._k_validity.copy()

    @property
    def Pr(self):
        """
        float : Prandtl number [-]
        """
        return self.cp * self.mu / self.k

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
            warnings.warn("Temperature {:.2f} is outside {:s} range "
                          "[{:.2f}, {:.2f}] K"
                          .format(self.T, property_name,
                                  validity_range[0], validity_range[1]),
                          stacklevel=3)

    @abstractmethod
    def _fill_properties(self):
        """
        Fills the class properties
        """
        raise NotImplementedError("{:s}._fill_properties NOT IMPLEMENTED"
                                  .format(type(self).__name__))

    @abstractmethod
    def _set_constants(self):
        """
        Sets the class constants
        """
        raise NotImplementedError("{:s}._set_constants NOT IMPLEMENTED"
                                  .format(type(self).__name__))

    @abstractmethod
    def _p_s_correlation(self, T):
        """
        Correlation used to compute saturation vapour pressure

        Parameters
        ----------
        T : float
            Temperature in [K]
        """
        raise NotImplementedError("{:s}._p_s_correlation NOT IMPLEMENTED"
                                  .format(type(self).__name__))

    @abstractmethod
    def _sigma_correlation(self, T):
        """
        Correlation used to compute surface tension

        Parameters
        ----------
        T : float
            Temperature in [K]
        """
        raise NotImplementedError("{:s}._sigma_correlation NOT IMPLEMENTED"
                                  .format(type(self).__name__))

    @abstractmethod
    def _rho_correlation(self, T):
        """
        Correlation used to compute density

        Parameters
        ----------
        T : float
            Temperature in [K]
        """
        raise NotImplementedError("{:s}._rho_correlation NOT IMPLEMENTED"
                                  .format(type(self).__name__))

    @abstractmethod
    def _alpha_correlation(self, T):
        """
        Correlation used to compute thermal expansion coefficient

        Parameters
        ----------
        T : float
            Temperature in [K]
        """
        raise NotImplementedError("{:s}._alpha_correlation NOT IMPLEMENTED"
                                  .format(type(self).__name__))

    @abstractmethod
    def _u_s_correlation(self, T):
        """
        Correlation used to compute sound velocity

        Parameters
        ----------
        T : float
            Temperature in [K]
        """
        raise NotImplementedError("{:s}._u_s_correlation NOT IMPLEMENTED"
                                  .format(type(self).__name__))

    @abstractmethod
    def _beta_s_correlation(self, T):
        """
        Correlation used to compute isentropic compressibility

        Parameters
        ----------
        T : float
            Temperature in [K]
        """
        raise NotImplementedError("{:s}._beta_s_correlation NOT IMPLEMENTED"
                                  .format(type(self).__name__))

    @abstractmethod
    def _cp_correlation(self, T):
        """
        Correlation used to compute specific heat capacity

        Parameters
        ----------
        T : float
            Temperature in [K]
        """
        raise NotImplementedError("{:s}._cp_correlation NOT IMPLEMENTED"
                                  .format(type(self).__name__))

    @abstractmethod
    def _h_correlation(self, T):
        """
        Correlation used to compute specific enthalpy

        Parameters
        ----------
        T : float
            Temperature in [K]
        """
        raise NotImplementedError("{:s}._h_correlation NOT IMPLEMENTED"
                                  .format(type(self).__name__))

    @abstractmethod
    def _mu_correlation(self, T):
        """
        Correlation used to compute dynamic viscosity

        Parameters
        ----------
        T : float
            Temperature in [K]
        """
        raise NotImplementedError("{:s}._mu_correlation NOT IMPLEMENTED"
                                  .format(type(self).__name__))

    @abstractmethod
    def _r_correlation(self, T):
        """
        Correlation used to compute electrical resistivity

        Parameters
        ----------
        T : float
            Temperature in [K]
        """
        raise NotImplementedError("{:s}._r_correlation NOT IMPLEMENTED"
                                  .format(type(self).__name__))

    @abstractmethod
    def _k_correlation(self, T):
        """
        Correlation used to compute thermal conductivity

        Parameters
        ----------
        T : float
            Temperature in [K]
        """
        raise NotImplementedError("{:s}._k_correlation NOT IMPLEMENTED"
                                  .format(type(self).__name__))

    def __compute_T(self, input_value, input_property):
        """
        Computes the temperature in [K] that is then set as value
        of the object property

        Parameters
        ----------
        input_value : float
            value of the property used to compute the temperature
        input_property : str
            name of the property used to perform the calculation
        """
        if input_property == 'T':
            rvalue = input_value
        else:
            function_of_T = None
            if input_property == 'p_s':
                function_of_T = self._p_s_correlation
            elif input_property == 'sigma':
                function_of_T = self._sigma_correlation
            elif input_property == 'rho':
                function_of_T = self._rho_correlation
            elif input_property == 'alpha':
                function_of_T = self._alpha_correlation
            elif input_property == 'u_s':
                function_of_T = self._u_s_correlation
            elif input_property == 'beta_s':
                function_of_T = self._beta_s_correlation
            elif input_property == 'cp':
                function_of_T = self._cp_correlation
            elif input_property == 'h':
                function_of_T = self._h_correlation
            elif input_property == 'mu':
                function_of_T = self._mu_correlation
            elif input_property == 'r':
                function_of_T = self._r_correlation
            elif input_property == 'k':
                function_of_T = self._k_correlation

            if function_of_T is not None:
                def function_to_solve(T, target):
                    return function_of_T(T) - target

                if input_property != 'cp':
                    res = fsolve(function_to_solve, x0=[self._guess],
                                 args=(input_value), xtol=1e-10)
                    rvalue = res[0]
                else:
                    res = fsolve(function_to_solve,
                                 x0=[self._guess, 4*self._guess],
                                 args=(input_value), xtol=1e-10)
                    if len(res) > 0 and self.__cp_high_range:
                        rvalue = res[1]
                    else:
                        rvalue = res[0]

        return rvalue

    def __fill_class_attributes(self, kwargs):
        """
        Fills all the class attributes.

        Parameters
        ----------
        T : float
            Temperature in [K]
        """
        if len(kwargs) != 1:
            raise ValueError("One and only one parameter at "
                             "time can be used for initialization. "
                             "{:d} were provided".format(len(kwargs)))
        else:
            valid_prop = PropertiesInterface.properties_for_initialization()
            input_property = list(kwargs.keys())[0]
            input_value = kwargs[input_property]
            if input_property not in valid_prop:
                list_to_print = "\n\n"
                for sym in valid_prop:
                    list_to_print += sym+"\n"
                list_to_print += "\n"
                raise ValueError("Initialization can be done only with one of "
                                 "the following properties:{:s}"
                                 "{:s} was provided"
                                 .format(list_to_print, input_property))
            else:
                self._p = atmosphere
                self._set_constants()
                temperature = self.__compute_T(input_value, input_property)
                self.__assign_T(temperature)
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
                                 "boiling temperature ({:.2f} [K]), {:.2f} "
                                 "[K] was provided".format(self.T_b0, T))
            elif T > 0 and T <= self.T_m0:
                raise ValueError("Temperature must be larger than "
                                 "melting temerature ({:.2f} [K]), {:.2f} "
                                 "[K] was provided".format(self.T_m0, T))
            else:
                raise ValueError("Temperature must be "
                                 "strictly positive, "
                                 "{:.2f} [K] was provided".format(T))
