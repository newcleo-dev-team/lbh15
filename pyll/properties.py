from scipy.optimize import fsolve
import math
from ._pyll import ZERO_C_IN_K, CELSIUS_SYMBOL
from ._pyll import KELVIN_SYMBOL, MELTING_TEMPERATURE
from ._pyll import MELTING_LATENT_HEAT, BOILING_TEMPERATURE
from ._pyll import VAPORISATION_HEAT
from ._utils import p_s, delta_h, sigma, rho, alpha, u_s
from ._utils import beta_s, cp, mi


def _get_temperature_in_kelvin(temperature, units):
    rvalue = 0
    if units == CELSIUS_SYMBOL:
        rvalue = temperature + ZERO_C_IN_K
    elif units == KELVIN_SYMBOL:
        rvalue = temperature
    else:
        raise ValueError("Temperature units must be one of {:s}, {:s}".
                         format(CELSIUS_SYMBOL, KELVIN_SYMBOL))

    return rvalue


# critical point not added
class LeadProperties(object):

    __T = 0
    __T_assigned = False
    __T_m0 = 0  # [K]
    __Q_m0 = 0  # [J/kg]
    __T_b0 = 0  # [K]
    __Q_b0 = 0  # [J/kg]
    __p_s = 0  # [Pa]
    __sigma = 0  # [N/m] surface tension
    __rho = 0  # [kg/m^3]
    __alpha = 0  # [1/K]
    __u_s = 0  # [m/s] sound velocity
    __beta_s = 0  # adiabatic compressibility
    __delta_h = 0  # delta of enthalpy in respect to melting point
    __mi = 0  # [Pa*s]

    def __init__(self, T, temperatureUnits=KELVIN_SYMBOL):
        self.__fill_class_attributes(T, temperatureUnits)

    def __fill_class_attributes(self, T, temperatureUnits):

        self.__assign_T(T, temperatureUnits)

        if self.T_assigned:
            self.__T_m0 = MELTING_TEMPERATURE
            self.__Q_m0 = MELTING_LATENT_HEAT
            self.__T_b0 = BOILING_TEMPERATURE
            self.__Q_b0 = VAPORISATION_HEAT
            self.__p_s = p_s(self.T)
            self.__sigma = sigma(self.T)
            self.__rho = rho(self.T)
            self.__alpha = alpha(self.T)
            self.__u_s = u_s(self.T)
            self.__beta_s = beta_s(self.T)
            self.__cp = cp(self.T)
            self.__delta_h = delta_h(self.T)
            self.__mi = mi(self.T)

    def __assign_T(self, T, temperatureUnits):
        temp = _get_temperature_in_kelvin(T, temperatureUnits)

        if temp > 0:
            self.__T_assigned = True
            self.__T = temp
        else:
            raise ValueError("Temperature in Kelvin must be strictly positive,\
                             {:7.2f} [K] was provided".format(temp))

    @property
    def T(self):
        return self.__T

    @property
    def T_in_celsius(self):
        return self.T - ZERO_C_IN_K

    @property
    def T_assigned(self):
        return self.__T_assigned

    @property
    def T_m0(self):
        return self.__T_m0

    @property
    def Q_m0(self):
        return self.__Q_m0

    @property
    def T_b0(self):
        return self.__T_b0

    @property
    def Q_b0(self):
        return self.__Q_b0

    @property
    def p_s(self):
        return self.__p_s

    @property
    def sigma(self):
        return self.__sigma

    @property
    def rho(self):
        return self.__rho

    @property
    def alpha(self):
        return self.__alpha

    @property
    def u_s(self):
        return self.__u_s

    @property
    def beta_s(self):
        return self.__beta_s

    @property
    def cp(self):
        return self.__cp

    @property
    def delta_h(self):
        return self.__delta_h

    @property
    def mi(self):
        return self.__mi


class _LeadPropertiesFromX(LeadProperties):
    def __init__(self, function_of_T, target, guess=MELTING_TEMPERATURE*1.5):

        def function_to_solve(T, target):
            return function_of_T(T) - target

        temp = fsolve(function_to_solve, x0=[guess], args=[target])[0]
        super().__init__(temp, KELVIN_SYMBOL)


class LeadPropertiesP_s(_LeadPropertiesFromX):
    def __init__(self, saturation_pressure, guess=MELTING_TEMPERATURE*1.5):
        super().__init__(p_s, saturation_pressure, guess)


class LeadPropertiesSigma(_LeadPropertiesFromX):
    def __init__(self, surface_tension, guess=MELTING_TEMPERATURE*1.5):
        super().__init__(sigma, surface_tension, guess)


class LeadPropertiesRho(_LeadPropertiesFromX):
    def __init__(self, density, guess=MELTING_TEMPERATURE*1.5):
        super().__init__(rho, density, guess)


class LeadPropertiesAlpha(_LeadPropertiesFromX):
    def __init__(self, expansion_coefficient, guess=MELTING_TEMPERATURE*1.5):
        super().__init__(alpha, expansion_coefficient, guess)


class LeadPropertiesU_s(_LeadPropertiesFromX):
    def __init__(self, sound_velocity, guess=MELTING_TEMPERATURE*1.5):
        super().__init__(u_s, sound_velocity, guess)


class LeadPropertiesBeta_s(_LeadPropertiesFromX):
    def __init__(self, adiabatic_compressibility,
                 guess=MELTING_TEMPERATURE*1.5):
        super().__init__(beta_s, adiabatic_compressibility, guess)


class LeadPropertiesCp(_LeadPropertiesFromX):
    def __init__(self, specific_heat, guess=MELTING_TEMPERATURE*1.5):
        super().__init__(cp, specific_heat, guess)


class LeadPropertiesDelta_h(_LeadPropertiesFromX):
    def __init__(self, enthalpy, guess=MELTING_TEMPERATURE*1.5):
        super().__init__(delta_h, enthalpy, guess)


class LeadPropertiesMi(_LeadPropertiesFromX):
    def __init__(self, dynamic_viscosity, guess=MELTING_TEMPERATURE*1.5):
        super().__init__(mi, dynamic_viscosity, guess)
