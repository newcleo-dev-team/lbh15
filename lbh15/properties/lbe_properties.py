import numpy as np
from ._properties import PropertiesInterface
from .._lbh15 import LBE_MELTING_TEMPERATURE as T_m0
from .._lbh15 import LBE_BOILING_TEMPERATURE as T_b0
from .._lbh15 import SOBOLEV_KEYWORD, GURVICH_KEYWORD


class p_s(PropertiesInterface):
    """
    Liquid lead-bismuth eutectic saturation vapour pressure
    property class
    """
    def __init__(self):
        super().__init__()
        self._range = [T_m0, T_b0]
        self._units = "[Pa]"
        self._long_name = "saturation vapour pressure"
        self._description = "Liquid lbe " + self._long_name

    def correlation(self, T):
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
        return 1.22e10 * np.exp(-22552/T)


class sigma(PropertiesInterface):
    """
    Liquid lead-bismuth eutectic surface tension
    property class
    """
    def __init__(self):
        super().__init__()
        self._range = [T_m0, 1400.0]
        self._units = "[N/m]"
        self._long_name = "surface tension"
        self._description = "Liquid lbe " + self._long_name

    def correlation(self, T):
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
        return (448.5 - 0.0799*T)*1e-3


class rho(PropertiesInterface):
    """
    Liquid lead-bismuth eutectic density
    property class
    """
    def __init__(self):
        super().__init__()
        self._range = [T_m0, T_b0]
        self._units = "[kg/m^3]"
        self._long_name = "density"
        self._description = "Liquid lbe " + self._long_name

    def correlation(self, T):
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
        return 11065 - 1.293*T


class alpha(PropertiesInterface):
    """
    Liquid lead-bismuth eutectic thermal expansion coefficient
    property class
    """
    def __init__(self):
        super().__init__()
        self._range = [T_m0, T_b0]
        self._units = "[1/K]"
        self._long_name = "thermal expansion coefficient"
        self._description = "Liquid lbe " + self._long_name

    def correlation(self, T):
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
        return 1/(8558 - T)


class u_s(PropertiesInterface):
    """
    Liquid lead-bismuth eutectic sound velocity
    property class
    """
    def __init__(self):
        super().__init__()
        self._range = [400.0, 1100.0]
        self._units = "[m/s]"
        self._long_name = "sound velocity"
        self._description = "Sound velocity in liquid lbe"

    def correlation(self, T):
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
        return 1855 - 0.212*T


class beta_s(PropertiesInterface):
    """
    Liquid lead-bismuth eutectic isentropic compressibility
    property class
    """
    def __init__(self):
        super().__init__()
        self._range = [400.0, 1100.0]
        self._units = "[1/Pa]"
        self._long_name = "isentropic compressibility"
        self._description = "Liquid lbe " + self._long_name

    def correlation(self, T):
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
        rho_obj = rho()
        u_s_obj = u_s()
        return 1/(rho_obj.correlation(T) * u_s_obj.correlation(T)**2)


class cp(PropertiesInterface):
    """
    Liquid lead-bismuth eutectic specific heat capacity
    property class
    """
    def __init__(self):
        super().__init__()
        self._range = [400.0, 1100.0]
        self._units = "[J/kg*K]"
        self._long_name = "specific heat capacity"
        self._description = "Liquid lbe " + self._long_name

    def correlation(self, T):
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
        return (164.8 - 3.94e-2*T + 1.25e-5*T**2
                - 4.56e5*T**-2)


class h(PropertiesInterface):
    """
    Liquid lead-bismuth eutectic specific enthalpy
    property class
    """
    def __init__(self):
        super().__init__()
        self._range = [400.0, 1100.0]
        self._units = "[J/kg]"
        self._long_name = "specific enthalpy"
        self._description = "Liquid lbe " + self._long_name \
                            + " (as difference with respect to the melting point enthalpy)"

    def correlation(self, T):
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
        return (164.8*(T - T_m0)
                - 1.97e-2*(T**2 - T_m0**2)
                + 4.167e-6*(T**3 - T_m0**3)
                + 4.56e5*(T**-1 - T_m0**-1))


class mu(PropertiesInterface):
    """
    Liquid lead-bismuth eutectic dynamic viscosity
    property class
    """
    def __init__(self):
        super().__init__()
        self._range = [T_m0, 1300.0]
        self._units = "[Pa*s]"
        self._long_name = "dynamic viscosity"
        self._description = "Liquid lbe " + self._long_name

    def correlation(self, T):
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
        return 4.94e-4*np.exp(754.1/T)


class r(PropertiesInterface):
    """
    Liquid lead-bismuth eutectic electrical resistivity
    property class
    """
    def __init__(self):
        super().__init__()
        self._range = [T_m0, 1100.0]
        self._units = "[Ohm*m]"
        self._long_name = "electrical resistivity"
        self._description = "Liquid lbe " + self._long_name

    def correlation(self, T):
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
        return (90.9 + 0.048*T)*1e-8


class k(PropertiesInterface):
    """
    Liquid lead-bismuth eutectic thermal conductivity
    property class
    """
    def __init__(self):
        super().__init__()
        self._range = [T_m0, 1100.0]
        self._units = "[W/(m*K)]"
        self._long_name = "thermal conductivity"
        self._description = "Liquid lbe " + self._long_name

    def correlation(self, T):
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
        return 3.284 + 1.617e-2*T - 2.305e-6*T**2
