import numpy as np
from ._properties import PropertiesInterface
from .._lbh15 import BISMUTH_MELTING_TEMPERATURE as T_m0
from .._lbh15 import BISMUTH_BOILING_TEMPERATURE as T_b0
from .._lbh15 import SOBOLEV_KEYWORD, GURVICH_KEYWORD


class p_s(PropertiesInterface):
    def __init__(self):
        super().__init__()
        self._range = [T_m0, T_b0]
        self._units = "[Pa]"
        self._long_name = "saturation vapour pressure"
        self._description = "Liquid bismuth " + self._long_name

    def correlation(self, T):
        return 2.67e10 * np.exp(-22858/T)


class sigma(PropertiesInterface):
    def __init__(self):
        super().__init__()
        self._range = [T_m0, 1400.0]
        self._units = "[N/m]"
        self._long_name = "surface tension"
        self._description = "Liquid bismuth " + self._long_name

    def correlation(self, T):
        return (420.8 - 0.081*T)*1e-3


class rho(PropertiesInterface):
    def __init__(self):
        super().__init__()
        self._range = [T_m0, T_b0]
        self._units = "[kg/m^3]"
        self._long_name = "density"
        self._description = "Liquid bismuth " + self._long_name

    def correlation(self, T):
        return 10725 - 1.22*T


class alpha(PropertiesInterface):
    def __init__(self):
        super().__init__()
        self._range = [T_m0, T_b0]
        self._units = "[1/K]"
        self._long_name = "thermal expansion coefficient"
        self._description = "Liquid bismuth " + self._long_name

    def correlation(self, T):
        return 1/(8791 - T)


class u_s(PropertiesInterface):
    def __init__(self):
        super().__init__()
        self._range = [T_m0, 1800.0]
        self._units = "[m/s]"
        self._long_name = "sound velocity"
        self._description = "Sound velocity in liquid bismuth"

    def correlation(self, T):
        return 1616 + 0.187*T - 2.2e-4*T**2


class beta_s(PropertiesInterface):
    def __init__(self):
        super().__init__()
        self._range = [T_m0, 1800.0]
        self._units = "[1/Pa]"
        self._long_name = "isentropic compressibility"
        self._description = "Liquid bismuth " + self._long_name

    def correlation(self, T):
        rho_obj = rho()
        u_s_obj = u_s()
        return 1/(rho_obj.correlation(T) * u_s_obj.correlation(T)**2)


class cp(PropertiesInterface):
    def __init__(self):
        super().__init__()
        self._range = [T_m0, T_b0]
        self._units = "[j/kg*K]"
        self._long_name = "specific heat capacity"
        self._description = "Liquid bismuth " + self._long_name

    def correlation(self, T):
        return 118.2 + 5.934e-3*T + 7.183e6*T**-2


class h(PropertiesInterface):
    def __init__(self):
        super().__init__()
        self._range = [T_m0, T_b0]
        self._units = "[1/Pa]"
        self._long_name = "specific enthalpy"
        self._description = "Liquid bismuth " + self._long_name

    def correlation(self, T):
        return (118.2*(T - T_m0)
                + 2.967e-3*(T**2 - T_m0**2)
                - 7.183e6*(T**-1 - T_m0**-1))


class mu(PropertiesInterface):
    def __init__(self):
        super().__init__()
        self._range = [T_m0, 1300.0]
        self._units = "[Pa*s]"
        self._long_name = "dynamic viscosity"
        self._description = "Liquid bismuth " + self._long_name

    def correlation(self, T):
        return 4.456e-4*np.exp(780/T)


class r(PropertiesInterface):
    def __init__(self):
        super().__init__()
        self._range = [545.0, 1423.0]
        self._units = "[Ohm*m]"
        self._long_name = "electrical resistivity"
        self._description = "Liquid bismuth " + self._long_name

    def correlation(self, T):
        return (98.96 + 0.0554*T)*1e-8


class k(PropertiesInterface):
    def __init__(self):
        super().__init__()
        self._range = [T_m0, 1000.0]
        self._units = "[W/(m*K)]"
        self._long_name = "thermal conductivity"
        self._description = "Liquid bismuth " + self._long_name

    def correlation(self, T):
        return 7.34 + 9.5e-3*T
