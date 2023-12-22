"""Module with the definition of the thermo-physical property objects
for *lead*."""
from typing import List
from typing import Union
import numpy as np
from scipy.constants import atm
from .interface import PropertyInterface
from .._decorators import range_warning
from .._commons import LEAD_MELTING_TEMPERATURE as T_m0
from .._commons import LEAD_BOILING_TEMPERATURE as T_b0


class p_s(PropertyInterface):
    """
    Liquid lead *saturation vapour pressure* property class.
    """
    @range_warning
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Returns the value of the *saturation vapour pressure* by
        applying the property correlation.

        Parameters
        ----------
        T : float
            Temperature in :math:`[K]`
        p : float, optional
            Pressure in :math:`[Pa]`, by default the atmospheric pressure
            value, i.e., :math:`101325.0 Pa`
        verbose : bool, optional
            `True` to tell the decorator to print a warning message in case of
            range check failing, `False` otherwise. By default, `False`

        Returns
        -------
        float:
            saturation vapour pressure in :math:`[Pa]`
        """
        return 5.76e9 * np.exp(-22131/T)

    def initialization_helper(self,
                              property_value: float) -> Union[None, float]:
        """
        Returns the temperature guess value according to the value
        of the saturation vapour pressure passed as argument.
        It is used by the root finder algorithm.

        Parameters
        ----------
        property_value : float
            saturation vapour pressure in :math:`[Pa]`

        Returns
        -------
        float
            Temperature guess value in :math:`[K]`
        """
        if property_value < 1e-2:
            return 800
        if 1e-2 <= property_value < 1e2:
            return 1200
        return 2000

    @property
    def correlation_name(self) -> str:
        """
        str : Name of the correlation
        """
        return 'sobolev2011'

    @property
    def range(self) -> List[float]:
        """
        List[float] : Temperature validity range of the saturation vapour
        pressure correlation function
        """
        return [T_m0, T_b0]

    @property
    def units(self) -> str:
        """
        str : Saturation vapour pressure unit
        """
        return "[Pa]"

    @property
    def long_name(self) -> str:
        """
        str : Saturation vapour pressure long name
        """
        return "saturation vapour pressure"

    @property
    def description(self) -> str:
        """
        str : Saturation vapour pressure description
        """
        return f"Liquid lead {self.long_name}"


class sigma(PropertyInterface):
    """
    Liquid lead *surface tension* property class.
    """
    @range_warning
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Returns the value of the *surface tension* by
        applying the property correlation.

        Parameters
        ----------
        T : float
            Temperature in :math:`[K]`
        p : float, optional
            Pressure in :math:`[Pa]`, by default the atmospheric pressure
            value, i.e., :math:`101325.0 Pa`
        verbose : bool, optional
            `True` to tell the decorator to print a warning message in case of
            range check failing, `False` otherwise. By default, `False`

        Returns
        -------
        float:
            surface tension in :math:`[N/m]`
        """
        return (525.9 - 0.113*T)*1e-3

    @property
    def correlation_name(self) -> str:
        """
        str : Name of the correlation
        """
        return "jauch1986"

    @property
    def range(self) -> List[float]:
        """
        List[float] : Temperature validity range of the surface
        tension correlation function
        """
        return [T_m0, 1300.0]

    @property
    def units(self) -> str:
        """
        str : Surface tension unit
        """
        return "[N/m]"

    @property
    def long_name(self) -> str:
        """
        str : Surface tension long name
        """
        return "surface tension"

    @property
    def description(self) -> str:
        """
        str : Surface tension description
        """
        return f"Liquid lead {self.long_name}"


class rho(PropertyInterface):
    """
    Liquid lead *density* property class.
    """
    @range_warning
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Returns the value of the *density* by applying the property
        correlation. *sobolev2011* correlation is used for the specific
        heat capacity in the pressure-dependent term.

        Parameters
        ----------
        T : float
            Temperature in :math:`[K]`
        p : float, optional
            Pressure in :math:`[Pa]`, by default the atmospheric pressure
            value, i.e., :math:`101325.0 Pa`
        verbose : bool, optional
            `True` to tell the decorator to print a warning message in case of
            range check failing, `False` otherwise. By default, `False`

        Returns
        -------
        float:
            density in :math:`[kg/m^3]`
        """
        rho_0 = 11441 - 1.2795*T
        u_s_val = u_s().correlation(T, p)
        alpha_val = alpha().correlation(T, p)
        return rho_0 +\
            (1.0 / u_s_val / u_s_val +
             T * alpha_val * alpha_val /
             cp_sobolev2011().correlation(T, p)) * (p - atm)

    @property
    def correlation_name(self) -> str:
        """
        str : Name of the correlation
        """
        return "sobolev2008a"

    @property
    def range(self) -> List[float]:
        """
        List[float] : Temperature validity range of the density
        correlation function
        """
        return [T_m0, T_b0]

    @property
    def units(self) -> str:
        """
        str : Density unit
        """
        return "[kg/m^3]"

    @property
    def long_name(self) -> str:
        """
        str : Density long name
        """
        return "density"

    @property
    def description(self) -> str:
        """
        str : Density description
        """
        return f"Liquid lead {self.long_name}"


class alpha(PropertyInterface):
    """
    Liquid lead *thermal expansion coefficient* property class.
    """
    @range_warning
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Returns the value of the *thermal expansion coefficient* by
        applying the property correlation.

        Parameters
        ----------
        T : float
            Temperature in :math:`[K]`
        p : float, optional
            Pressure in :math:`[Pa]`, by default the atmospheric pressure
            value, i.e., :math:`101325.0 Pa`
        verbose : bool, optional
            `True` to tell the decorator to print a warning message in case of
            range check failing, `False` otherwise. By default, `False`

        Returns
        -------
        float:
            thermal expansion coefficient in :math:`[1/K]`
        """
        return 1/(8942 - T)

    @property
    def range(self) -> List[float]:
        """
        List[float] : Temperature validity range of the thermal expansion
        coefficient correlation function
        """
        return [T_m0, T_b0]

    @property
    def units(self) -> str:
        """
        str : Thermal expansion coefficient unit
        """
        return "[1/K]"

    @property
    def long_name(self) -> str:
        """
        str : Thermal expansion coefficient long name
        """
        return "thermal expansion coefficient"

    @property
    def description(self) -> str:
        """
        str : Thermal expansion coefficient description
        """
        return f"Liquid lead {self.long_name}"


class u_s(PropertyInterface):
    """
    Liquid lead *sound velocity* property class.
    """
    @range_warning
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Returns the value of the *sound velocity* by
        applying the property correlation.

        Parameters
        ----------
        T : float
            Temperature in :math:`[K]`
        p : float, optional
            Pressure in :math:`[Pa]`, by default the atmospheric pressure
            value, i.e., :math:`101325.0 Pa`
        verbose : bool, optional
            `True` to tell the decorator to print a warning message in case of
            range check failing, `False` otherwise. By default, `False`

        Returns
        -------
        float:
            sound velocity in :math:`[m/s]`
        """
        return 1953 - 0.246*T

    @property
    def correlation_name(self) -> str:
        """
        str : Name of the correlation
        """
        return 'sobolev2011'

    @property
    def range(self) -> List[float]:
        """
        List[float] : Temperature validity range of the sound velocity
        correlation function
        """
        return [T_m0, 2000.0]

    @property
    def units(self) -> str:
        """
        str : Sound velocity unit
        """
        return "[m/s]"

    @property
    def long_name(self) -> str:
        """
        str : Sound velocity long name
        """
        return "sound velocity"

    @property
    def description(self) -> str:
        """
        str : Sound velocity description
        """
        return "Sound velocity in liquid lead"


class beta_s(PropertyInterface):
    """
    Liquid lead *isentropic compressibility* property class.
    """
    @range_warning
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Returns the value of the *isentropic compressibility* by
        applying the property correlation.

        Parameters
        ----------
        T : float
            Temperature in :math:`[K]`
        p : float, optional
            Pressure in :math:`[Pa]`, by default the atmospheric pressure
            value, i.e., :math:`101325.0 Pa`
        verbose : bool, optional
            `True` to tell the decorator to print a warning message in case of
            range check failing, `False` otherwise. By default, `False`

        Returns
        -------
        float:
            isentropic compressibility in :math:`[1/Pa]`
        """
        u_s_val = u_s().correlation(T, p)
        return 1 / (rho().correlation(T, p) * u_s_val * u_s_val)

    @property
    def range(self) -> List[float]:
        """
        List[float] : Temperature validity range of the isentropic
        compressibility correlation function
        """
        return [T_m0, 2000.0]

    @property
    def units(self) -> str:
        """
        str : Isentropic compressibility unit
        """
        return "[1/Pa]"

    @property
    def long_name(self) -> str:
        """
        str : Isentropic compressibility long name
        """
        return "isentropic compressibility"

    @property
    def description(self) -> str:
        """
        str : Isentropic compressibility description
        """
        return f"Liquid lead {self.long_name}"


class cp_sobolev2011(PropertyInterface):
    """
    Liquid lead *specific heat capacity* property class exploiting
    the **sobolev2011** correlation.
    """
    @range_warning
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Returns the value of the *specific heat capacity* by
        applying the **sobolev2011** correlation.

        Parameters
        ----------
        T : float
            Temperature in :math:`[K]`
        p : float, optional
            Pressure in :math:`[Pa]`, by default the atmospheric pressure
            value, i.e., :math:`101325.0 Pa`
        verbose : bool, optional
            `True` to tell the decorator to print a warning message in case of
            range check failing, `False` otherwise. By default, `False`

        Returns
        -------
        float:
            specific heat capacity in :math:`[J/(kg \\cdot K)]`
        """
        return 176.2 - T * (4.923e-2 - 1.544e-5 * T) - 1.524e6 / T / T

    @property
    def name(self) -> str:
        """
        str : Name of the property
        """
        return "cp"

    @property
    def correlation_name(self) -> str:
        """
        str : Name of the correlation
        """
        return 'sobolev2011'

    @property
    def is_injective(self) -> bool:
        """
        bool : `True` if the correlation is injective,
        `False` otherwise.
        """
        return False

    @property
    def range(self) -> List[float]:
        """
        List[float] : Temperature validity range of the specific heat
        capacity correlation function
        """
        return [T_m0, 2000.0]

    @property
    def units(self) -> str:
        """
        str : Specific heat capacity unit
        """
        return "[J/(kg*K)]"

    @property
    def long_name(self) -> str:
        """
        str : Specific heat capacity long name
        """
        return "specific heat capacity"

    @property
    def description(self) -> str:
        """
        str : Specific heat capacity description
        """
        return f"Liquid lead {self.long_name}"


class cp_gurvich1991(PropertyInterface):
    """
    Liquid lead *specific heat capacity* property class exploiting
    the **gurvich1991** correlation.
    """
    @range_warning
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Returns the value of the *specific heat capacity* by
        applying the **gurvich1991** correlation.

        Parameters
        ----------
        T : float
            Temperature in :math:`[K]`
        p : float, optional
            Pressure in :math:`[Pa]`, by default the atmospheric pressure
            value, i.e., :math:`101325.0 Pa`
        verbose : bool, optional
            `True` to tell the decorator to print a warning message in case of
            range check failing, `False` otherwise. By default, `False`

        Returns
        -------
        float:
            specific heat capacity in :math:`[J/(kg \\cdot K)]`
        """
        return 175.1 - T * (4.961e-2 - T * (1.985e-5 - 2.099e-9 * T))\
            - 1.524e6 / T / T

    @property
    def name(self) -> str:
        """
        str : Name of the property
        """
        return "cp"

    @property
    def correlation_name(self) -> str:
        """
        str : Name of the correlation
        """
        return 'gurvich1991'

    @property
    def is_injective(self) -> bool:
        """
        bool : `True` if the correlation is injective,
        `False` otherwise.
        """
        return False

    @property
    def range(self) -> List[float]:
        """
        List[float] : Temperature validity range of the specific heat
        capacity correlation function
        """
        return [T_m0, 2000.0]

    @property
    def units(self) -> str:
        """
        str : Specific heat capacity unit
        """
        return "[J/(kg*K)]"

    @property
    def long_name(self) -> str:
        """
        str : Specific heat capacity long name
        """
        return "specific heat capacity"

    @property
    def description(self) -> str:
        """
        str : Specific heat capacity description
        """
        return f"Liquid lead {self.long_name}"


class h(PropertyInterface):
    """
    Liquid lead *specific enthalpy* property class.
    """
    @range_warning
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Returns the value of the *specific enthalpy* by
        applying the property correlation.

        Parameters
        ----------
        T : float
            Temperature in :math:`[K]`
        p : float, optional
            Pressure in :math:`[Pa]`, by default the atmospheric pressure
            value, i.e., :math:`101325.0 Pa`
        verbose : bool, optional
            `True` to tell the decorator to print a warning message in case of
            range check failing, `False` otherwise. By default, `False`

        Returns
        -------
        float:
            specific enthalpy in :math:`[J/kg]`
        """
        return T * (176.2 - T * (2.4615e-2 - 5.147e-6 * T))\
            - T_m0 * (176.2 - T_m0 * (2.4615e-2 - 5.147e-6 * T_m0))\
            + 1.524e6 * (1 / T - 1 / T_m0)

    @property
    def correlation_name(self) -> str:
        """
        str : Name of the correlation
        """
        return 'sobolev2011'

    @property
    def range(self) -> List[float]:
        """
        List[float] : Temperature validity range of the specific enthalpy
        correlation function
        """
        return [T_m0, 2000.0]

    @property
    def units(self) -> str:
        """
        str : Specific enthalpy unit
        """
        return "[J/kg]"

    @property
    def long_name(self) -> str:
        """
        str : Specific enthalpy long name
        """
        return "specific enthalpy"

    @property
    def description(self) -> str:
        """
        str : Specific enthalpy description
        """
        return (f"Liquid lead {self.long_name} "
                "(as difference with respect to "
                "the melting point enthalpy)")


class mu(PropertyInterface):
    """
    Liquid lead *dynamic viscosity* property class.
    """
    @range_warning
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Returns the value of the *dynamic viscosity* by
        applying the property correlation.

        Parameters
        ----------
        T : float
            Temperature in :math:`[K]`
        p : float, optional
            Pressure in :math:`[Pa]`, by default the atmospheric pressure
            value, i.e., :math:`101325.0 Pa`
        verbose : bool, optional
            `True` to tell the decorator to print a warning message in case of
            range check failing, `False` otherwise. By default, `False`

        Returns
        -------
        float:
            dynamic viscosity in :math:`[Pa \\cdot s]`
        """
        return 4.55e-4 * np.exp(1069/T)

    def initialization_helper(self,
                              property_value: float) -> Union[None, float]:
        """
        Returns the temperature guess value according to the value
        of the dynamic viscosity passed as argument.
        It is used by the root finder algorithm.

        Parameters
        ----------
        property_value : float
            dynamic viscosity in :math:`[Pa]`

        Returns
        -------
        float
            Temperature guess value in :math:`[K]`
        """
        if property_value < 2e-3:
            return 800
        return 1600

    @property
    def range(self) -> List[float]:
        """
        List[float] : Temperature validity range of the dynamic viscosity
        correlation function
        """
        return [T_m0, 1473.0]

    @property
    def units(self) -> str:
        """
        str : Dynamic viscosity unit
        """
        return "[Pa*s]"

    @property
    def long_name(self) -> str:
        """
        str : Dynamic viscosity long name
        """
        return "dynamic viscosity"

    @property
    def description(self) -> str:
        """
        str : Dynamic viscosity description
        """
        return f"Liquid lead {self.long_name}"


class r(PropertyInterface):
    """
    Liquid lead *electrical resistivity* property class.
    """
    @range_warning
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Returns the value of the *electrical resistivity* by
        applying the property correlation.

        Parameters
        ----------
        T : float
            Temperature in :math:`[K]`
        p : float, optional
            Pressure in :math:`[Pa]`, by default the atmospheric pressure
            value, i.e., :math:`101325.0 Pa`
        verbose : bool, optional
            `True` to tell the decorator to print a warning message in case of
            range check failing, `False` otherwise. By default, `False`

        Returns
        -------
        float:
            electrical resistivity in :math:`[Ohm \\cdot m]`
        """
        return (67.0 + 0.0471*T)*1e-8

    @property
    def range(self) -> List[float]:
        """
        List[float] : Temperature validity range of the electrical
        resistivity correlation function
        """
        return [T_m0, 1273.0]

    @property
    def units(self) -> str:
        """
        str : Electrical resistivity unit
        """
        return "[Ohm*m]"

    @property
    def long_name(self) -> str:
        """
        str : Electrical resistivity long name
        """
        return "electrical resistivity"

    @property
    def description(self) -> str:
        """
        str : Electrical resistivity description
        """
        return f"Liquid lead {self.long_name}"


class k(PropertyInterface):
    """
    Liquid lead *thermal conductivity* property class.
    """
    @range_warning
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Returns the value of the *thermal conductivity* by
        applying the property correlation.

        Parameters
        ----------
        T : float
            Temperature in :math:`[K]`
        p : float, optional
            Pressure in :math:`[Pa]`, by default the atmospheric pressure
            value, i.e., :math:`101325.0 Pa`
        verbose : bool, optional
            `True` to tell the decorator to print a warning message in case of
            range check failing, `False` otherwise. By default, `False`

        Returns
        -------
        float:
            thermal conductivity in :math:`[W/(m \\cdot K)]`
        """
        return 9.2 + 0.011*T

    @property
    def range(self) -> List[float]:
        """
        List[float] : Temperature validity range of the thermal
        conductivity correlation function
        """
        return [T_m0, 1300.0]

    @property
    def units(self) -> str:
        """
        str : Thermal conductivity unit
        """
        return "[W/(m*K)]"

    @property
    def long_name(self) -> str:
        """
        str : Thermal conductivity long name
        """
        return "thermal conductivity"

    @property
    def description(self) -> str:
        """
        str : Thermal conductivity description
        """
        return f"Liquid lead {self.long_name}"
