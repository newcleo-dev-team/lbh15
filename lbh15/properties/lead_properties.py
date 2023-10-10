"""Module with the definition of thermophysical property objects for lead"""
from typing import List
from typing import Union
import numpy as np
from scipy.constants import atm
from .interface import PropertyInterface
from .interface import range_warning
from .._decorators import typecheck_for_method
from .._commons import LEAD_MELTING_TEMPERATURE as T_m0
from .._commons import LEAD_BOILING_TEMPERATURE as T_b0
from .._commons import SOBOLEV_KEYWORD, GURVICH_KEYWORD


class p_s(PropertyInterface):
    """
    Liquid lead saturation vapour pressure
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
        return 5.76e9 * np.exp(-22131/T)

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
            rvalue = 800
        elif 1e-2 <= property_value < 1e2:
            rvalue = 1200
        else:
            rvalue = 2000

        return rvalue

    @property
    def correlation_name(self) -> str:
        """
        str : name of the correlation
        """
        return SOBOLEV_KEYWORD

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
        return f"Liquid lead {self.long_name}"


class sigma(PropertyInterface):
    """
    Liquid lead surface tension
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
        return (525.9 - 0.113*T)*1e-3

    @property
    def correlation_name(self) -> str:
        """
        str : name of the correlation
        """
        return "jauch1986"

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
        return f"Liquid lead {self.long_name}"


class rho(PropertyInterface):
    """
    Liquid lead density
    property class
    """
    @range_warning
    @typecheck_for_method
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Correlation used to compute density. sobolev2011 correlation
        is used as specific heat capacity in pressure dependent
        term of the correlation.

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
        rho_0 = 11441 - 1.2795*T
        u_s_val = u_s().correlation(T, p)
        cp_val = cp_sobolev2011().correlation(T, p)
        alpha_val = alpha().correlation(T, p)
        return rho_0 + ((1.0/u_s_val/u_s_val + T*alpha_val*alpha_val/cp_val)
                        * (p - atm))

    @property
    def correlation_name(self) -> str:
        """
        str : name of the correlation
        """
        return "sobolev2008a"

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
        return f"Liquid lead {self.long_name}"


class alpha(PropertyInterface):
    """
    Liquid lead thermal expansion coefficient
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
        return 1/(8942 - T)

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
        return f"Liquid lead {self.long_name}"


class u_s(PropertyInterface):
    """
    Liquid lead sound velocity
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
        return 1953 - 0.246*T

    @property
    def correlation_name(self) -> str:
        """
        str : name of the correlation
        """
        return SOBOLEV_KEYWORD

    @property
    def range(self) -> List[float]:
        """
        list : temperature validity range for property correlation
        """
        return [T_m0, 2000.0]

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
        return "Sound velocity in liquid lead"


class beta_s(PropertyInterface):
    """
    Liquid lead isentropic compressibility
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
        rho_val = rho().correlation(T, p)
        u_s_val = u_s().correlation(T, p)
        return 1/(rho_val * u_s_val*u_s_val)

    @property
    def range(self) -> List[float]:
        """
        list : temperature validity range for property correlation
        """
        return [T_m0, 2000.0]

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
        return f"Liquid lead {self.long_name}"


class cp_sobolev2011(PropertyInterface):
    """
    Liquid lead specific heat capacity
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
        return (176.2 - 4.923e-2*T + 1.544e-5*T*T
                - 1.524e6/T/T)

    @property
    def name(self) -> str:
        """
        str : name of the property
        """
        return "cp"

    @property
    def correlation_name(self) -> str:
        """
        str : name of the correlation
        """
        return SOBOLEV_KEYWORD

    @property
    def is_invertible(self) -> bool:
        """
        bool : True if correlation is invertible,
        False otherwise
        """
        return False

    @property
    def range(self) -> List[float]:
        """
        list : temperature validity range for property correlation
        """
        return [T_m0, 2000.0]

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
        return f"Liquid lead {self.long_name}"


class cp_gurvich1991(PropertyInterface):
    """
    Liquid lead specific heat capacity
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
        return (175.1 - 4.961e-2*T + 1.985e-5*T*T
                - 2.099e-9*T*T*T - 1.524e6/T/T)

    @property
    def name(self) -> str:
        """
        str : name of the property
        """
        return "cp"

    @property
    def correlation_name(self) -> str:
        """
        str : name of the correlation
        """
        return GURVICH_KEYWORD

    @property
    def is_invertible(self) -> bool:
        """
        bool : True if correlation is invertible,
        False otherwise
        """
        return False

    @property
    def range(self) -> List[float]:
        """
        list : temperature validity range for property correlation
        """
        return [T_m0, 2000.0]

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
        return f"Liquid lead {self.long_name}"


class h(PropertyInterface):
    """
    Liquid lead specific enthalpy
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
        return (176.2*(T - T_m0)
                - 2.4615e-2*(T*T - T_m0*T_m0)
                + 5.147e-6*(T*T*T - T_m0*T_m0*T_m0)
                + 1.524e6*(1/T - 1/T_m0))

    @property
    def correlation_name(self) -> str:
        """
        str : name of the correlation
        """
        return SOBOLEV_KEYWORD

    @property
    def range(self) -> List[float]:
        """
        list : temperature validity range for property correlation
        """
        return [T_m0, 2000.0]

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
        return (f"Liquid lead {self.long_name} "
                "(as difference with respect to "
                "the melting point enthalpy)")


class mu(PropertyInterface):
    """
    Liquid lead dynamic viscosity
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
        return 4.55e-4 * np.exp(1069/T)

    @property
    def range(self) -> List[float]:
        """
        list : temperature validity range for property correlation
        """
        return [T_m0, 1473.0]

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
        return f"Liquid lead {self.long_name}"


class r(PropertyInterface):
    """
    Liquid lead electrical resistivity
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
        return (67.0 + 0.0471*T)*1e-8

    @property
    def range(self) -> List[float]:
        """
        list : temperature validity range for property correlation
        """
        return [T_m0, 1273.0]

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
        return f"Liquid lead {self.long_name}"


class k(PropertyInterface):
    """
    Liquid lead thermal conductivity
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
        return 9.2 + 0.011*T

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
        return f"Liquid lead {self.long_name}"
