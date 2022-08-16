import numpy as np
from ._properties import PropertiesInterface
from .._lbh15 import LEAD_MELTING_TEMPERATURE as T_m0
from .._lbh15 import LEAD_BOILING_TEMPERATURE as T_b0
from .._lbh15 import SOBOLEV_KEYWORD, GURVICH_KEYWORD


class p_s(PropertiesInterface):
    """
    Liquid lead saturation vapour pressure
    property class
    """
    def __init__(self):
        super().__init__()
        self._range = [T_m0, T_b0]
        self._units = "[Pa]"
        self._long_name = "saturation vapour pressure"
        self._description = "Liquid lead " + self._long_name

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
        return 5.76e9 * np.exp(-22131/T)


class sigma(PropertiesInterface):
    """
    Liquid lead surface tension
    property class
    """
    def __init__(self):
        super().__init__()
        self._range = [T_m0, 1300.0]
        self._units = "[N/m]"
        self._long_name = "surface tension"
        self._description = "Liquid lead " + self._long_name

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
        return (525.9 - 0.113*T)*1e-3


class rho(PropertiesInterface):
    """
    Liquid lead density
    property class
    """
    def __init__(self):
        super().__init__()
        self._range = [T_m0, T_b0]
        self._units = "[kg/m^3]"
        self._long_name = "density"
        self._description = "Liquid lead " + self._long_name

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
        return 11441 - 1.2795*T


class alpha(PropertiesInterface):
    """
    Liquid lead thermal expansion coefficient
    property class
    """
    def __init__(self):
        super().__init__()
        self._range = [T_m0, T_b0]
        self._units = "[1/K]"
        self._long_name = "thermal expansion coefficient"
        self._description = "Liquid lead " + self._long_name

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
        return 1/(8942 - T)


class u_s(PropertiesInterface):
    """
    Liquid lead sound velocity
    property class
    """
    def __init__(self):
        super().__init__()
        self._range = [T_m0, 2000.0]
        self._units = "[m/s]"
        self._long_name = "sound velocity"
        self._description = "Sound velocity in liquid lead"

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
        return 1953 - 0.246*T


class beta_s(PropertiesInterface):
    """
    Liquid lead isentropic compressibility
    property class
    """
    def __init__(self):
        super().__init__()
        self._range = [T_m0, 2000.0]
        self._units = "[1/Pa]"
        self._long_name = "isentropic compressibility"
        self._description = "Liquid lead " + self._long_name

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
    Liquid lead specific heat capacity
    property class

    Parameters
    ----------
    cp_correlation_to_use : str
        Name of cp correlation, can be 'sobolev2011' or 'gurvich1991'
    """
    def __init__(self, cp_correlation_to_use=SOBOLEV_KEYWORD):
        super().__init__()
        self._range = [T_m0, 2000.0]
        self._units = "[J/kg*K]"
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
        if self._cp_correlation_to_use == SOBOLEV_KEYWORD:
            rvalue = (176.2 - 4.923e-2*T + 1.544e-5*T**2
                      - 1.524e6*T**-2)
        else:
            rvalue = (175.1 - 4.961e-2*T + 1.985e-5*T**2
                      - 2.099e-9*T**3 - 1.524e6*T**-2)
        return rvalue


class h(PropertiesInterface):
    """
    Liquid lead specific enthalpy
    property class
    """
    def __init__(self):
        super().__init__()
        self._range = [T_m0, 2000.0]
        self._units = "[J/kg]"
        self._long_name = "specific enthalpy"
        self._description = "Liquid lead " + self._long_name \
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
        return (176.2*(T - T_m0)
                - 2.4615e-2*(T**2 - T_m0**2)
                + 5.147e-6*(T**3 - T_m0**3)
                + 1.524e6*(T**-1 - T_m0**-1))


class mu(PropertiesInterface):
    """
    Liquid lead dynamic viscosity
    property class
    """
    def __init__(self):
        super().__init__()
        self._range = [T_m0, 1473.0]
        self._units = "[Pa*s]"
        self._long_name = "dynamic viscosity"
        self._description = "Liquid lead " + self._long_name

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
        return 4.55e-4 * np.exp(1069/T)


class r(PropertiesInterface):
    """
    Liquid lead electrical resistivity
    property class
    """
    def __init__(self):
        super().__init__()
        self._range = [T_m0, 1273.0]
        self._units = "[Ohm*m]"
        self._long_name = "electrical resistivity"
        self._description = "Liquid lead " + self._long_name

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
        return (67.0 + 0.0471*T)*1e-8


class k(PropertiesInterface):
    """
    Liquid lead thermal conductivity
    property class
    """
    def __init__(self):
        super().__init__()
        self._range = [T_m0, 1300.0]
        self._units = "[W/(m*K)]"
        self._long_name = "thermal conductivity"
        self._description = "Liquid lead " + self._long_name

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
        return 9.2 + 0.011*T
