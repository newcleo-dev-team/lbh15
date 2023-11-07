"""Module with the definition of thermophysical property objects for bismuth"""
from typing import List
from typing import Union
import numpy as np
from scipy.constants import atm
from .interface import PropertyInterface
from .interface import range_warning
from .._decorators import typecheck_for_method
from .._commons import BISMUTH_MELTING_TEMPERATURE as T_m0
from .._commons import BISMUTH_BOILING_TEMPERATURE as T_b0


class p_s(PropertyInterface):
    """
    Liquid bismuth saturation vapour pressure
    property class
    """
    @range_warning
    @typecheck_for_method
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Correlation used to compute saturation vapour pressure

        Parameters
        ----------
        T : float
            Temperature in [K]
        p : float, optional
            Pressure in [Pa], by default atmospheric pressure, i.e.,
            101325.0 Pa
        verbose : bool, optional
            True to tell decorator to print warning about
            range check failing, False otherwise. By default False

        Returns
        -------
        saturation vapour pressure in [Pa] : float
        """
        return 2.67e10 * np.exp(-22858/T)

    @typecheck_for_method
    def initialization_helper(self,
                              property_value: float) -> Union[None, float]:
        """
        Returns a temperature guess according to the value
        of the saturation vapour pressure

        Parameters
        ----------
        property_value : float
            saturation vapour pressure in [Pa]
        verbose : bool, optional
            True to tell decorator to print warning about
            range check failing, False otherwise. By default False

        Returns
        -------
        rvalue : float
            Temperature guess in [K]
        """
        if property_value < 1e-2:
            return 800
        if 1e-2 <= property_value < 1e2:
            return 1200
        return 2000

    @property
    def correlation_name(self) -> str:
        """
        str : name of the correlation
        """
        return 'sobolev2011'

    @property
    def range(self) -> List[float]:
        """
        list : temperature validity range for property correlation
        """
        return [T_m0, T_b0]

    @property
    def units(self) -> str:
        """
        str : property units
        """
        return "[Pa]"

    @property
    def long_name(self) -> str:
        """
        str : property long name
        """
        return "saturation vapour pressure"

    @property
    def description(self) -> str:
        """
        str : property description
        """
        return f"Liquid bismuth {self.long_name}"


class sigma(PropertyInterface):
    """
    Liquid bismuth surface tension
    property class
    """
    @range_warning
    @typecheck_for_method
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Correlation used to compute surface tension

        Parameters
        ----------
        T : float
            Temperature in [K]
        p : float, optional
            Pressure in [Pa], by default atmospheric pressure, i.e.,
            101325.0 Pa
        verbose : bool, optional
            True to tell decorator to print warning about
            range check failing, False otherwise. By default False

        Returns
        -------
        surface tension in [N/m] : float
        """
        return (420.8 - 0.081*T)*1e-3

    @property
    def correlation_name(self) -> str:
        """
        str : name of the correlation
        """
        return 'sobolev2011'

    @property
    def range(self) -> List[float]:
        """
        list : temperature validity range for property correlation
        """
        return [T_m0, 1400.0]

    @property
    def units(self) -> str:
        """
        str : property units
        """
        return "[N/m]"

    @property
    def long_name(self) -> str:
        """
        str : property long name
        """
        return "surface tension"

    @property
    def description(self) -> str:
        """
        str : property description
        """
        return f"Liquid bismuth {self.long_name}"


class rho(PropertyInterface):
    """
    Liquid bismuth density
    property class
    """
    @range_warning
    @typecheck_for_method
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Correlation used to compute density

        Parameters
        ----------
        T : float
            Temperature in [K]
        p : float, optional
            Pressure in [Pa], by default atmospheric pressure, i.e.,
            101325.0 Pa
        verbose : bool, optional
            True to tell decorator to print warning about
            range check failing, False otherwise. By default False

        Returns
        -------
        density in [kg/m^3] : float
        """
        rho_0 = 10725 - 1.22 * T
        u_s_val = u_s().correlation(T, p)
        alpha_val = alpha().correlation(T, p)
        return rho_0 +\
            (1 / u_s_val / u_s_val
             + T * alpha_val * alpha_val / cp().correlation(T, p)) * (p - atm)

    @property
    def correlation_name(self) -> str:
        """
        str : name of the correlation
        """
        return "imbeni1998"

    @property
    def range(self) -> List[float]:
        """
        list : temperature validity range for property correlation
        """
        return [T_m0, T_b0]

    @property
    def units(self) -> str:
        """
        str : property units
        """
        return "[kg/m^3]"

    @property
    def long_name(self) -> str:
        """
        str : property long name
        """
        return "density"

    @property
    def description(self) -> str:
        """
        str : property description
        """
        return f"Liquid bismuth {self.long_name}"


class alpha(PropertyInterface):
    """
    Liquid bismuth thermal expansion coefficient
    property class
    """
    @range_warning
    @typecheck_for_method
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Correlation used to compute thermal expansion coefficient

        Parameters
        ----------
        T : float
            Temperature in [K]
        p : float, optional
            Pressure in [Pa], by default atmospheric pressure, i.e.,
            101325.0 Pa
        verbose : bool, optional
            True to tell decorator to print warning about
            range check failing, False otherwise. By default False

        Returns
        -------
        thermal expansion coefficient in [1/K] : float
        """
        return 1/(8791 - T)

    @property
    def range(self) -> List[float]:
        """
        list : temperature validity range for property correlation
        """
        return [T_m0, T_b0]

    @property
    def units(self) -> str:
        """
        str : property units
        """
        return "[1/K]"

    @property
    def long_name(self) -> str:
        """
        str : property long name
        """
        return "thermal expansion coefficient"

    @property
    def description(self) -> str:
        """
        str : property description
        """
        return f"Liquid bismuth {self.long_name}"


class u_s(PropertyInterface):
    """
    Liquid bismuth sound velocity
    property class
    """
    @range_warning
    @typecheck_for_method
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Correlation used to compute sound velocity

        Parameters
        ----------
        T : float
            Temperature in [K]
        p : float, optional
            Pressure in [Pa], by default atmospheric pressure, i.e.,
            101325.0 Pa
        verbose : bool, optional
            True to tell decorator to print warning about
            range check failing, False otherwise. By default False

        Returns
        -------
        sound velocity in [m/s] : float
        """
        return 1616 + T * (0.187 - 2.2e-4 * T)

    @property
    def correlation_name(self) -> str:
        """
        str : name of the correlation
        """
        return 'sobolev2011'

    @property
    def range(self) -> List[float]:
        """
        list : temperature validity range for property correlation
        """
        return [T_m0, 1800.0]

    @property
    def units(self) -> str:
        """
        str : property units
        """
        return "[m/s]"

    @property
    def long_name(self) -> str:
        """
        str : property long name
        """
        return "sound velocity"

    @property
    def description(self) -> str:
        """
        str : property description
        """
        return "Sound velocity in liquid bismuth"


class beta_s(PropertyInterface):
    """
    Liquid bismuth isentropic compressibility
    property class
    """
    @range_warning
    @typecheck_for_method
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Correlation used to compute isentropic compressibility

        Parameters
        ----------
        T : float
            Temperature in [K]
        p : float, optional
            Pressure in [Pa], by default atmospheric pressure, i.e.,
            101325.0 Pa
        verbose : bool, optional
            True to tell decorator to print warning about
            range check failing, False otherwise. By default False

        Returns
        -------
        isentropic compressibility in [1/Pa] : float
        """
        u_s_val = u_s().correlation(T, p)
        return 1 / (rho().correlation(T, p) * u_s_val * u_s_val)

    @property
    def range(self) -> List[float]:
        """
        list : temperature validity range for property correlation
        """
        return [T_m0, 1800.0]

    @property
    def units(self) -> str:
        """
        str : property units
        """
        return "[1/Pa]"

    @property
    def long_name(self) -> str:
        """
        str : property long name
        """
        return "isentropic compressibility"

    @property
    def description(self) -> str:
        """
        str : property description
        """
        return f"Liquid bismuth {self.long_name}"


class cp(PropertyInterface):
    """
    Liquid bismuth specific heat capacity
    property class
    """
    @range_warning
    @typecheck_for_method
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Correlation used to compute specific heat capacity

        Parameters
        ----------
        T : float
            Temperature in [K]
        p : float, optional
            Pressure in [Pa], by default atmospheric pressure, i.e.,
            101325.0 Pa
        verbose : bool, optional
            True to tell decorator to print warning about
            range check failing, False otherwise. By default False

        Returns
        -------
        specific heat capacity in [J/(kg*K)] : float
        """
        return 118.2 + 5.934e-3*T + 7.183e6/T/T

    @property
    def correlation_name(self) -> str:
        """
        str : name of the correlation
        """
        return "imbeni1998"

    @property
    def is_injective(self) -> bool:
        """
        bool : True if correlation is injective,
        False otherwise
        """
        return False

    @property
    def range(self) -> List[float]:
        """
        list : temperature validity range for property correlation
        """
        return [T_m0, T_b0]

    @property
    def units(self) -> str:
        """
        str : property units
        """
        return "[J/(kg*K)]"

    @property
    def long_name(self) -> str:
        """
        str : property long name
        """
        return "specific heat capacity"

    @property
    def description(self) -> str:
        """
        str : property description
        """
        return f"Liquid bismuth {self.long_name}"


class h(PropertyInterface):
    """
    Liquid bismuth specific enthalpy
    property class
    """
    @range_warning
    @typecheck_for_method
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Correlation used to compute specific enthalpy

        Parameters
        ----------
        T : float
            Temperature in [K]
        p : float, optional
            Pressure in [Pa], by default atmospheric pressure, i.e.,
            101325.0 Pa
        verbose : bool, optional
            True to tell decorator to print warning about
            range check failing, False otherwise. By default False

        Returns
        -------
        specific enthalpy in [J/kg] : float
        """
        return T * (118.2 + 2.967e-3 * T) - T_m0 * (118.2 + 2.967e-3 * T_m0)\
            - 7.183e6 * (1 / T - 1 / T_m0)

    @property
    def correlation_name(self) -> str:
        """
        str : name of the correlation
        """
        return 'sobolev2011'

    @property
    def range(self) -> List[float]:
        """
        list : temperature validity range for property correlation
        """
        return [T_m0, T_b0]

    @property
    def units(self) -> str:
        """
        str : property units
        """
        return "[J/kg]"

    @property
    def long_name(self) -> str:
        """
        str : property long name
        """
        return "specific enthalpy"

    @property
    def description(self) -> str:
        """
        str : property description
        """
        return (f"Liquid bismuth {self.long_name} "
                "(as difference with respect to "
                "the melting point enthalpy)")


class mu(PropertyInterface):
    """
    Liquid bismuth dynamic viscosity
    property class
    """
    @range_warning
    @typecheck_for_method
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Correlation used to compute dynamic viscosity

        Parameters
        ----------
        T : float
            Temperature in [K]
        p : float, optional
            Pressure in [Pa], by default atmospheric pressure, i.e.,
            101325.0 Pa
        verbose : bool, optional
            True to tell decorator to print warning about
            range check failing, False otherwise. By default False

        Returns
        -------
        dynamic viscosity in [Pa*s] : float
        """
        return 4.456e-4*np.exp(780/T)

    @property
    def correlation_name(self) -> str:
        """
        str : name of the correlation
        """
        return "lucas1984b"

    @property
    def range(self) -> List[float]:
        """
        list : temperature validity range for property correlation
        """
        return [T_m0, 1300.0]

    @property
    def units(self) -> str:
        """
        str : property units
        """
        return "[Pa*s]"

    @property
    def long_name(self) -> str:
        """
        str : property long name
        """
        return "dynamic viscosity"

    @property
    def description(self) -> str:
        """
        str : property description
        """
        return f"Liquid bismuth {self.long_name}"


class r(PropertyInterface):
    """
    Liquid bismuth electrical resistivity
    property class
    """
    @range_warning
    @typecheck_for_method
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Correlation used to compute electrical resistivity

        Parameters
        ----------
        T : float
            Temperature in [K]
        p : float, optional
            Pressure in [Pa], by default atmospheric pressure, i.e.,
            101325.0 Pa
        verbose : bool, optional
            True to tell decorator to print warning about
            range check failing, False otherwise. By default False

        Returns
        -------
        electrical resistivity in [Ohm*m] : float
        """
        return (98.96 + 0.0554*T)*1e-8

    @property
    def range(self) -> List[float]:
        """
        list : temperature validity range for property correlation
        """
        return [545.0, 1423.0]

    @property
    def units(self) -> str:
        """
        str : property units
        """
        return "[Ohm*m]"

    @property
    def long_name(self) -> str:
        """
        str : property long name
        """
        return "electrical resistivity"

    @property
    def description(self) -> str:
        """
        str : property description
        """
        return f"Liquid bismuth {self.long_name}"


class k(PropertyInterface):
    """
    Liquid bismuth thermal conductivity
    property class
    """
    @range_warning
    @typecheck_for_method
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Correlation used to compute thermal conductivity

        Parameters
        ----------
        T : float
            Temperature in [K]
        p : float, optional
            Pressure in [Pa], by default atmospheric pressure, i.e.,
            101325.0 Pa
        verbose : bool, optional
            True to tell decorator to print warning about
            range check failing, False otherwise. By default False

        Returns
        -------
        thermal conductivity in [W/(m*K)] : float
        """
        return 7.34 + 9.5e-3*T

    @property
    def correlation_name(self) -> str:
        """
        str : name of the correlation
        """
        return "touloukian1970b"

    @property
    def range(self) -> List[float]:
        """
        list : temperature validity range for property correlation
        """
        return [T_m0, 1000.0]

    @property
    def units(self) -> str:
        """
        str : property units
        """
        return "[W/(m*K)]"

    @property
    def long_name(self) -> str:
        """
        str : property long name
        """
        return "thermal conductivity"

    @property
    def description(self) -> str:
        """
        str : property description
        """
        return f"Liquid bismuth {self.long_name}"
