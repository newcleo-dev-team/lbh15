import numpy as np
from ._properties import PropertiesInterface
from .._lbh15 import LBE_MELTING_TEMPERATURE as T_m0
from .._lbh15 import LBE_BOILING_TEMPERATURE as T_b0
from .._lbh15 import SOBOLEV_KEYWORD, GURVICH_KEYWORD


class p_s(PropertiesInterface):
    def __init__(self):
        super().__init__()
        self._range = [T_m0, T_b0]
        self._units = "[Pa]"
        self._long_name = "saturation vapour pressure"
        self._description = "Liquid lbe " + self._long_name

    def correlation(self, T):
        return 1.22e10 * np.exp(-22552/T)


class sigma(PropertiesInterface):
    def __init__(self):
        super().__init__()
        self._range = [T_m0, 1400.0]
        self._units = "[N/m]"
        self._long_name = "surface tension"
        self._description = "Liquid lbe " + self._long_name

    def correlation(self, T):
        return (448.5 - 0.0799*T)*1e-3


class rho(PropertiesInterface):
    def __init__(self):
        super().__init__()
        self._range = [T_m0, T_b0]
        self._units = "[kg/m^3]"
        self._long_name = "density"
        self._description = "Liquid lbe " + self._long_name

    def correlation(self, T):
        return 10725 - 1.22*T


class alpha(PropertiesInterface):
    def __init__(self):
        super().__init__()
        self._range = [T_m0, T_b0]
        self._units = "[1/K]"
        self._long_name = "thermal expansion coefficient"
        self._description = "Liquid lbe " + self._long_name

    def correlation(self, T):
        return 1/(8558 - T)


class u_s(PropertiesInterface):
    def __init__(self):
        super().__init__()
        self._range = [400.0, 1100.0]
        self._units = "[m/s]"
        self._long_name = "sound velocity"
        self._description = "Sound velocity in liquid lbe"

    def correlation(self, T):
        return 1855 - 0.212*T


class beta_s(PropertiesInterface):
    def __init__(self):
        super().__init__()
        self._range = [400.0, 1100.0]
        self._units = "[1/Pa]"
        self._long_name = "isentropic compressibility"
        self._description = "Liquid lbe " + self._long_name

    def correlation(self, T):
        rho_obj = rho()
        u_s_obj = u_s()
        return 1/(rho_obj.correlation(T) * u_s_obj.correlation(T)**2)


class cp(PropertiesInterface):
    def __init__(self):
        super().__init__()
        self._range = [400.0, 1100.0]
        self._units = "[j/kg*K]"
        self._long_name = "specific heat capacity"
        self._description = "Liquid lbe " + self._long_name

    def correlation(self, T):
        return (164.8 - 3.94e-2*T + 1.25e-5*T**2
                - 4.56e5*T**-2)


class h(PropertiesInterface):
    def __init__(self):
        super().__init__()
        self._range = [400.0, 1100.0]
        self._units = "[1/Pa]"
        self._long_name = "specific enthalpy"
        self._description = "Liquid lbe " + self._long_name

    def correlation(self, T):
        return (164.8*(T - T_m0)
                - 1.97e-2*(T**2 - T_m0**2)
                + 4.167e-6*(T**3 - T_m0**3)
                + 4.56e5*(T**-1 - T_m0**-1))


class mu(PropertiesInterface):
    def __init__(self):
        super().__init__()
        self._range = [T_m0, 1300.0]
        self._units = "[Pa*s]"
        self._long_name = "dynamic viscosity"
        self._description = "Liquid lbe " + self._long_name

    def correlation(self, T):
        return 4.94e-4*np.exp(754.1/T)


class r(PropertiesInterface):
    def __init__(self):
        super().__init__()
        self._range = [T_m0, 1100.0]
        self._units = "[Ohm*m]"
        self._long_name = "electrical resistivity"
        self._description = "Liquid lbe " + self._long_name

    def correlation(self, T):
        return (90.9 + 0.048*T)*1e-8


class k(PropertiesInterface):
    def __init__(self):
        super().__init__()
        self._range = [T_m0, 1100.0]
        self._units = "[W/(m*K)]"
        self._long_name = "thermal conductivity"
        self._description = "Liquid lbe " + self._long_name

    def correlation(self, T):
        return 3.284 + 1.617e-2*T - 2.305e-6*T**2
