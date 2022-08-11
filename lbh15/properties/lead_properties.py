from ._properties import PropertiesInterface
from .._lbh15 import LEAD_MELTING_TEMPERATURE as T_m0
from .._lbh15 import LEAD_BOILING_TEMPERATURE as T_b0
from .._lbh15 import SOBOLEV_KEYWORD, GURVICH_KEYWORD
import numpy as np

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

"""
class p_s(PropertiesInterface):
    def __init__(self):
        super().__init__()
        self._range = [T_m0, T_b0]
        self._units = "[Pa]"
        self._long_name = "saturation vapour pressure"
        self._description = "Liquid lead " + self._long_name

    def correlation(self, T):
        return 5.76e9 * np.exp(-22131/T)


class sigma(PropertiesInterface):
    def __init__(self):
        super().__init__()
        self._range = [T_m0, 1300.0]
        self._units = "[N/m]"
        self._long_name = "surface tension"
        self._description = "Liquid lead " + self._long_name

    def correlation(self, T):
        return (525.9 - 0.113*T)*1e-3


class rho(PropertiesInterface):
    def __init__(self):
        super().__init__()
        self._range = [T_m0, T_b0]
        self._units = "[1/K]"
        self._long_name = "density"
        self._description = "Liquid lead " + self._long_name 

    def correlation(self, T):
        return 11441 - 1.2795*T


class alpha(PropertiesInterface):
    def __init__(self):
        super().__init__()
        self._range = [T_m0, T_b0]
        self._units = "[kg/m^3]"
        self._long_name = "thermal expansion coefficient"
        self._description = "Liquid lead " + self._long_name

    def correlation(self, T):
        return 1/(8942 - T)


class u_s(PropertiesInterface):
    def __init__(self):
        super().__init__()
        self._range = [T_m0, 2000.0]
        self._units = "[m/s]"
        self._long_name = "sound velocity"
        self._description = "Sound velocity in liquid lead"

    def correlation(self, T):
        return 1953 - 0.246*T


class beta_s(PropertiesInterface):
    def __init__(self):
        super().__init__()
        self._range = [T_m0, 2000.0]
        self._units = "[1/Pa]"
        self._long_name = "isentropic compressibility"
        self._description = "Liquid lead " + self._long_name

    def correlation(self, T):
        rho_obj = rho()
        u_s_obj = u_s()
        return 1/(rho_obj.correlation(T) * u_s_obj.correlation(T)**2)


class cp(PropertiesInterface):
    def __init__(self, cp_correlation_to_use):
        super().__init__()
        self._range = [T_m0, 2000.0]
        self._units = "[j/kg*K]"
        self._long_name = "specific heat capacity"
        self._description = "Liquid lead " + self._long_name
        if cp_correlation_to_use == SOBOLEV_KEYWORD:
            self._cp_correlation_to_use = SOBOLEV_KEYWORD
        elif cp_correlation_to_use == GURVICH_KEYWORD:
            self._cp_correlation_to_use = GURVICH_KEYWORD
        else:
            raise ValueError("cp correlation can be one among: {:s}, "
                             "{:s}. {:s} was provided"
                             .format(SOBOLEV_KEYWORD, GURVICH_KEYWORD,
                                     cp_correlation_to_use))

    def correlation(self, T):
        if self._cp_correlation_to_use == SOBOLEV_KEYWORD:
            rvalue = (176.2 - 4.923e-2*T + 1.544e-5*T**2
                      - 1.524e6*T**-2)
        else:
            rvalue = (175.1 - 4.961e-2*T + 1.985e-5*T**2
                      - 2.099e-9*T**3 - 1.524e6*T**-2)
        return rvalue


class h(PropertiesInterface):
    def __init__(self):
        super().__init__()
        self._range = [T_m0, 2000.0]
        self._units = "[1/Pa]"
        self._long_name = "specific enthalpy"
        self._description = "Liquid lead " + self._long_name

    def correlation(self, T):
        return (176.2*(T - T_m0)
                - 2.4615e-2*(T**2 - T_m0**2)
                + 5.147e-6*(T**3 - T_m0**3)
                + 1.524e6*(T**-1 - T_m0**-1))


class mu(PropertiesInterface):
    def __init__(self):
        super().__init__()
        self._range = [T_m0, 1473.0]
        self._units = "[Pa*s]"
        self._long_name = "dynamic viscosity"
        self._description = "Liquid lead " + self._long_name

    def correlation(self, T):
        return 4.55e-4 * np.exp(1069/T)


class r(PropertiesInterface):
    def __init__(self):
        super().__init__()
        self._range = [T_m0, 1273.0]
        self._units = "[Ohm*m]"
        self._long_name = "electrical resistivity"
        self._description = "Liquid lead " + self._long_name

    def correlation(self, T):
        return (67.0 + 0.0471*T)*1e-8


class k(PropertiesInterface):
    def __init__(self):
        super().__init__()
        self._range = [T_m0, 1300.0]
        self._units = "[W/(m*K)]"
        self._long_name = "thermal conductivity"
        self._description = "Liquid lead " + self._long_name

    def correlation(self, T):
        return 9.2 + 0.011*T