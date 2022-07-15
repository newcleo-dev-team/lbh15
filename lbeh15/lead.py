from scipy.optimize import fsolve
from ._lbeh15 import ZERO_C_IN_K, CELSIUS_SYMBOL
from ._lbeh15 import KELVIN_SYMBOL, LEAD_MELTING_TEMPERATURE
from ._lbeh15 import LEAD_MELTING_LATENT_HEAT, LEAD_BOILING_TEMPERATURE
from ._lbeh15 import LEAD_VAPORISATION_HEAT
from ._lbeh15 import PropertiesInterface
from ._utils import p_s, delta_h, sigma, rho, alpha, u_s
from ._utils import beta_s, cp, mi


class Lead(PropertiesInterface):
    """
    Class to model lead properties at a given temperature

    Parameters
    ----------
    T : float
        Temperature
    temperature_units : str
        Units used to specify temperature. Can be 'K' or '°C' for
        Kelvin and Celsius respectively
    """
    def __init__(self, T, temperature_units=KELVIN_SYMBOL):
        super().__init__(T, temperature_units)

    def _set_constants(self):        
        self._T_m0 = LEAD_MELTING_TEMPERATURE
        self._Q_m0 = LEAD_MELTING_LATENT_HEAT
        self._T_b0 = LEAD_BOILING_TEMPERATURE
        self._Q_b0 = LEAD_VAPORISATION_HEAT

    def _fill_properties(self):
        self._p_s = p_s(self.T)
        self._sigma = sigma(self.T)
        self._rho = rho(self.T)
        self._alpha = alpha(self.T)
        self._u_s = u_s(self.T)
        self._beta_s = beta_s(self.T)
        self._cp = cp(self.T)
        self._delta_h = delta_h(self.T)
        self._mi = mi(self.T)

class _LeadPropertiesFromX(Lead):
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
    """
    def __init__(self, function_of_T, target, guess=LEAD_MELTING_TEMPERATURE*1.5):

        def function_to_solve(T, target):
            return function_of_T(T) - target

        temp = fsolve(function_to_solve, x0=[guess], args=[target])[0]
        super().__init__(temp, KELVIN_SYMBOL)


class LeadPropertiesP_s(_LeadPropertiesFromX):
    """
    Class to model lead properties from saturation vapour pressure

    Parameters
    ----------
    saturation_pressure : float
        value of the saturation vapour pressure in [Pa]
    guess : float
        initial guess of the temperature in [K]
        that returns property target value
    """
    def __init__(self, saturation_pressure, guess=LEAD_MELTING_TEMPERATURE*1.5):
        super().__init__(p_s, saturation_pressure, guess)


class LeadPropertiesSigma(_LeadPropertiesFromX):
    """
    Class to model lead properties from surface tension

    Parameters
    ----------
    surface_tension : float
        value of surface tension [N/m]
    guess : float
        initial guess of the temperature in [K]
        that returns property target value
    """
    def __init__(self, surface_tension, guess=LEAD_MELTING_TEMPERATURE*1.5):
        super().__init__(sigma, surface_tension, guess)


class LeadPropertiesRho(_LeadPropertiesFromX):
    """
    Class to model lead properties from density

    Parameters
    ----------
    density : float
        value of density [kg/m^3]
    guess : float
        initial guess of the temperature in [K]
        that returns property target value
    """
    def __init__(self, density, guess=LEAD_MELTING_TEMPERATURE*1.5):
        super().__init__(rho, density, guess)


class LeadPropertiesAlpha(_LeadPropertiesFromX):
    """
    Class to model lead properties from thermal expansion coefficient

    Parameters
    ----------
    expansion_coefficient : float
        value of temperature expansion coefficient [1/K]
    guess : float
        initial guess of the temperature in [K]
        that returns property target value
    """
    def __init__(self, expansion_coefficient, guess=LEAD_MELTING_TEMPERATURE*1.5):
        super().__init__(alpha, expansion_coefficient, guess)


class LeadPropertiesU_s(_LeadPropertiesFromX):
    """
    Class to model lead properties from sound velocity

    Parameters
    ----------
    sound_velocity : float
        value of sound velocity [m/s]
    guess : float
        initial guess of the temperature in [K]
        that returns property target value
    """
    def __init__(self, sound_velocity, guess=LEAD_MELTING_TEMPERATURE*1.5):
        super().__init__(u_s, sound_velocity, guess)


class LeadPropertiesBeta_s(_LeadPropertiesFromX):
    """
    Class to model lead properties from isentropic compressibility

    Parameters
    ----------
    isentropic_compressibility : float
        value of isentropic compressibility [1/Pa]
    guess : float
        initial guess of the temperature in [K]
        that returns property target value
    """
    def __init__(self, isentropic_compressibility,
                 guess=LEAD_MELTING_TEMPERATURE*1.5):
        super().__init__(beta_s, isentropic_compressibility, guess)


class LeadPropertiesCp(_LeadPropertiesFromX):
    """
    Class to model lead properties from specific heat capacity

    Parameters
    ----------
    specific_heat : float
        value of specific heat capacity [J/(kg*K)]
    guess : float
        initial guess of the temperature in [K]
        that returns property target value
    """
    def __init__(self, specific_heat, guess=LEAD_MELTING_TEMPERATURE*1.5):
        super().__init__(cp, specific_heat, guess)


class LeadPropertiesDelta_h(_LeadPropertiesFromX):
    """
    Class to model lead properties from specifc enthalpy
    (in respect to lead melting point)

    Parameters
    ----------
    enthalpy : float
        value of specifc enthalpy [J/kg]
    guess : float
        initial guess of the temperature in [K]
        that returns property target value
    """
    def __init__(self, enthalpy, guess=LEAD_MELTING_TEMPERATURE*1.5):
        super().__init__(delta_h, enthalpy, guess)


class LeadPropertiesMi(_LeadPropertiesFromX):
    """
    Class to model lead properties from dynamic viscosity

    Parameters
    ----------
    dynamic_viscosity : float
        value of dynamic viscosity [Pa*s]
    guess : float
        initial guess of the temperature in [K]
        that returns property target value
    """
    def __init__(self, dynamic_viscosity, guess=LEAD_MELTING_TEMPERATURE*1.5):
        super().__init__(mi, dynamic_viscosity, guess)
