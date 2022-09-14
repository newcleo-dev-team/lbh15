from .interface import PropertyInterface
from .._lbh15 import LBE_MELTING_TEMPERATURE as T_m0
from .._lbh15 import LBE_BOILING_TEMPERATURE as T_b0
from .._lbh15 import SOBOLEV_KEYWORD, GURVICH_KEYWORD


class p_s(PropertyInterface):
    """
    Liquid lead-bismuth eutectic saturation vapour pressure
    property class
    """
    def __init__(self):
        super().__init__()
        self._range = [T_m0, T_b0]
        self._units = "[Pa]"
        self._long_name = "saturation vapour pressure"
        self._description = "Liquid lbe {:s}".format(self._long_name)

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
        import numpy as np
        return 1.22e10 * np.exp(-22552/T)

    def initialization_helper(self, property_value):
        """
        Returns a temperature guess according to the value
        of the saturation vapour pressure

        Parameters
        ----------
        property_value : float
            saturation vapour pressure in [Pa]

        Returns
        -------
        rvalue : float
            Temperature guess in [K]
        """
        if property_value < 1e-2:
            rvalue = 800
        elif property_value >= 1e-2 and property_value < 1e2:
            rvalue = 1200
        else:
            rvalue = 2000

        return rvalue


class sigma(PropertyInterface):
    """
    Liquid lead-bismuth eutectic surface tension
    property class
    """
    def __init__(self):
        super().__init__()
        self._range = [T_m0, 1400.0]
        self._units = "[N/m]"
        self._long_name = "surface tension"
        self._description = "Liquid lbe {:s}".format(self._long_name)

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


class rho(PropertyInterface):
    """
    Liquid lead-bismuth eutectic density
    property class
    """
    def __init__(self):
        super().__init__()
        self._range = [T_m0, T_b0]
        self._units = "[kg/m^3]"
        self._long_name = "density"
        self._description = "Liquid lbe {:s}".format(self._long_name)

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


class alpha(PropertyInterface):
    """
    Liquid lead-bismuth eutectic thermal expansion coefficient
    property class
    """
    def __init__(self):
        super().__init__()
        self._range = [T_m0, T_b0]
        self._units = "[1/K]"
        self._long_name = "thermal expansion coefficient"
        self._description = "Liquid lbe {:s}".format(self._long_name)

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


class u_s(PropertyInterface):
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


class beta_s(PropertyInterface):
    """
    Liquid lead-bismuth eutectic isentropic compressibility
    property class
    """
    def __init__(self):
        super().__init__()
        self._range = [400.0, 1100.0]
        self._units = "[1/Pa]"
        self._long_name = "isentropic compressibility"
        self._description = "Liquid lbe {:s}".format(self._long_name)

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


class cp(PropertyInterface):
    """
    Liquid lead-bismuth eutectic specific heat capacity
    property class
    """
    def __init__(self):
        super().__init__()
        self._range = [400.0, 1100.0]
        self._units = "[J/kg*K]"
        self._long_name = "specific heat capacity"
        self._description = "Liquid lbe {:s}".format(self._long_name)
        self._is_injective = False

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


class h(PropertyInterface):
    """
    Liquid lead-bismuth eutectic specific enthalpy
    property class
    """
    def __init__(self):
        super().__init__()
        self._range = [400.0, 1100.0]
        self._units = "[J/kg]"
        self._long_name = "specific enthalpy"
        self._description = ("Liquid lbe {:s} "
                             "(as difference with respect to"
                             "the melting point enthalpy)"
                             .format(self._long_name))

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


class mu(PropertyInterface):
    """
    Liquid lead-bismuth eutectic dynamic viscosity
    property class
    """
    def __init__(self):
        super().__init__()
        self._range = [T_m0, 1300.0]
        self._units = "[Pa*s]"
        self._long_name = "dynamic viscosity"
        self._description = "Liquid lbe {:s}".format(self._long_name)

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
        import numpy as np
        return 4.94e-4*np.exp(754.1/T)


class r(PropertyInterface):
    """
    Liquid lead-bismuth eutectic electrical resistivity
    property class
    """
    def __init__(self):
        super().__init__()
        self._range = [T_m0, 1100.0]
        self._units = "[Ohm*m]"
        self._long_name = "electrical resistivity"
        self._description = "Liquid lbe {:s}".format(self._long_name)

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


class k(PropertyInterface):
    """
    Liquid lead-bismuth eutectic thermal conductivity
    property class
    """
    def __init__(self):
        super().__init__()
        self._range = [T_m0, 1100.0]
        self._units = "[W/(m*K)]"
        self._long_name = "thermal conductivity"
        self._description = "Liquid lbe {:s}".format(self._long_name)

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
