import math
from scipy.optimize import fsolve
import numpy as np

from ._pyll import ZERO_C_IN_K, CELSIUS_SYMBOL, KELVIN_SYMBOL, MELTING_TEMPERATURE
from ._pyll import MELTING_LATENT_HEAT, BOILING_TEMPERATURE, VAPORISATION_HEAT
from ._utils import delta_h

def _get_temperature_in_kelvin(temperature, units):
    rvalue = 0
    if units == CELSIUS_SYMBOL: 
        rvalue = temperature + ZERO_C_IN_K
    elif units == KELVIN_SYMBOL: 
        rvalue = temperature
    else: 
        raise ValueError("Temperature units must be one of {:s}, {:s}".format(CELSIUS_SYMBOL, KELVIN_SYMBOL)) 
    
    return rvalue


# critical point not added
class LeadProperties(object): 

    __T = 0
    __T_assigned = False
    __T_m0 = 0 #[K]
    __Q_m0 = 0 #[J/kg]
    __T_b0 = 0 #[K]
    __Q_b0 = 0 #[J/kg]
    __p_s  = 0 #[Pa]
    __sigma = 0 #[N/m] surface tension
    __rho = 0 #[kg/m^3]
    __alpha = 0 #[1/K]
    __u_s = 0 #[m/s] sound velocity
    __beta_s = 0 # adiabatic compressibility
    __delta_h = 0 # delta of enthalpy in respect to melting point
    __mi = 0 #[Pa*s]
    def __init__(self, T, temperatureUnits=KELVIN_SYMBOL):
        self.__fill_class_attributes(T, temperatureUnits)


    def __fill_class_attributes(self, T, temperatureUnits):

        self.__assign_T(T, temperatureUnits)

        if self.T_assigned:
            self.__T_m0 = MELTING_TEMPERATURE
            self.__Q_m0 = MELTING_LATENT_HEAT
            self.__T_b0 = BOILING_TEMPERATURE
            self.__Q_b0 = VAPORISATION_HEAT
            self.__p_s = 1.88e13 * self.T * math.exp(-23325/self.T)
            self.__sigma = (525.9 - 0.113*self.T)/1000
            self.__rho = 11441 - 1.2795*self.T
            self.__alpha = 1/(8942 - self.T)
            self.__u_s = 1953 - 0.246*self.T
            self.__beta_s = 1/(self.rho * self.u_s**2)
            self.__cp = 175.1 - 4.961e-2*self.T +1.985e-5*self.T**2 - 2.099e-9*self.T**3 - 1.524e6*self.T**-2
            self.__delta_h = delta_h(self.T)
            self.__mi = 4.55e-4*math.exp(1069/self.T)

    def __assign_T(self, T, temperatureUnits): 
        temp = _get_temperature_in_kelvin(T, temperatureUnits)

        if temp > 0:
            self.__T_assigned = True
            self.__T = temp
        else: 
            raise ValueError("Temperature in Kelvin must be strictly positive, {:7.2f} [K] was provided".format(temp))

    @property
    def T(self): 
        return self.__T

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
    def delta_h(self): 
        return self.__delta_h

    @property
    def mi(self):
        return self.__mi

class LeadPropertiesSigma(LeadProperties): 
    def __init__(self, sigma):
        temp = 1/0.113*(525.9 - 1000*sigma)
        super().__init__(temp, KELVIN_SYMBOL)

class LeadPropertiesRho(LeadProperties): 
    def __init__(self, rho): 
        temp = (11441 - rho)/1.2795
        super().__init__(temp, KELVIN_SYMBOL)

class LeadPropertiesAlpha(LeadProperties): 
    def __init__(self, alpha): 
        temp = 8942 - 1/alpha
        super().__init__(temp, KELVIN_SYMBOL)

class LeadPropertiesU_s(LeadProperties): 
    def __init__(self, u_s): 
        temp = (1953 - u_s)/0.246
        super().__init__(temp, KELVIN_SYMBOL)
