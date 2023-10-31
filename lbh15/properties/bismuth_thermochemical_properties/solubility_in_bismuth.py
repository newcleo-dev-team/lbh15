"""Module with the definition of solubility
property objects for bismuth"""
from typing import List
import numpy as np
from scipy.constants import atm
from lbh15.properties.interface import PropertyInterface
from lbh15.properties.interface import range_warning
from ..._decorators import typecheck_for_method


class IronSolubilityInterface(PropertyInterface):
    """
    Iron solubility in liquid bismuth property class
    """
    @property
    def name(self) -> str:
        """
        str : name of the property
        """
        return "fe_sol"

    @property
    def units(self) -> str:
        """
        str : property units
        """
        return "[wt.%]"

    @property
    def long_name(self) -> str:
        """
        str : property long name
        """
        return "iron solubility"

    @property
    def description(self) -> str:
        """
        str : property description
        """
        return f"{self.long_name} in liquid bismuth"


class IronSolubilityGosse2014(IronSolubilityInterface):
    """
    Iron solubility in liquid bismuth property class
    implementing correlation by gosse2014
    """
    @range_warning
    @typecheck_for_method
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Correlation used to compute iron solubility in liquid bismuth

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
        solubility [wt.%] : float
        """
        return np.power(10, 2.20-3930/T)

    @property
    def correlation_name(self) -> str:
        """
        str : name of the correlation
        """
        return "gosse2014"

    @property
    def range(self) -> List[float]:
        """
        list : temperature validity range for property correlation
        """
        return [545.0, 1173.0]


class IronSolubilityMassalski1990(IronSolubilityInterface):
    """
    Iron solubility in liquid bismuth property class
    implementing correlation by massalski1990
    """
    @range_warning
    @typecheck_for_method
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Correlation used to compute iron solubility in liquid bismuth

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
        solubility [wt.%] : float
        """
        return np.power(10, 2.18-3980/T)

    @property
    def correlation_name(self) -> str:
        """
        str : name of the correlation
        """
        return "massalski1990"

    @property
    def range(self) -> List[float]:
        """
        list : temperature validity range for property correlation
        """
        return [973.0, 1173.0]


class IronSolubilityWeeks1998(IronSolubilityInterface):
    """
    Iron solubility in liquid bismuth property class
    implementing correlation by weeks1998
    """
    @range_warning
    @typecheck_for_method
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Correlation used to compute iron solubility in liquid bismuth

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
        solubility [wt.%] : float
        """
        return np.power(10, 1.832-3589/T)

    @property
    def correlation_name(self) -> str:
        """
        str : name of the correlation
        """
        return "weeks1998"

    @property
    def range(self) -> List[float]:
        """
        list : temperature validity range for property correlation
        """
        return [713.0, 998.0]


class NickelSolubilityInterface(PropertyInterface):
    """
    Nickel solubility in liquid bismuth property class
    """
    @property
    def name(self) -> str:
        """
        str : name of the property
        """
        return "ni_sol"

    @property
    def units(self) -> str:
        """
        str : property units
        """
        return "[wt.%]"

    @property
    def long_name(self) -> str:
        """
        str : property long name
        """
        return "nickel solubility"

    @property
    def description(self) -> str:
        """
        str : property description
        """
        return f"{self.long_name} in liquid bismuth"


class NickelSolubilityWeeks1998(NickelSolubilityInterface):
    """
    Nickel solubility in liquid bismuth property class
    implementing correlation by weeks1998
    """
    @range_warning
    @typecheck_for_method
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Correlation used to compute nickel solubility in liquid bismuth

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
        solubility [wt.%] : float
        """
        return np.power(10, 2.61-1538/T)

    @property
    def correlation_name(self) -> str:
        """
        str : name of the correlation
        """
        return "weeks1998"

    @property
    def range(self) -> List[float]:
        """
        list : temperature validity range for property correlation
        """
        return [723.0, 903.0]


class NickelSolubilityGosse2014(NickelSolubilityInterface):
    """
    Nickel solubility in liquid bismuth property class
    implementing correlation by gosse2014
    """
    @range_warning
    @typecheck_for_method
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Correlation used to compute nickel solubility in liquid bismuth

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
        solubility [wt.%] : float
        """
        if T <= 738:
            return np.power(10, 3.81-2429/T)
        if 738 < T <= 918:
            return np.power(10, 2.05-1131/T)
        return np.power(10, 1.35-484/T)

    @property
    def correlation_name(self) -> str:
        """
        str : name of the correlation
        """
        return "gosse2014"

    @property
    def range(self) -> List[float]:
        """
        list : temperature validity range for property correlation
        """
        return [543.0, 1173.0]


class ChromiumSolubilityInterface(PropertyInterface):
    """
    Chromium solubility in liquid bismuth property class
    """
    @property
    def name(self) -> str:
        """
        str : name of the property
        """
        return "cr_sol"

    @property
    def units(self) -> str:
        """
        str : property units
        """
        return "[wt.%]"

    @property
    def long_name(self) -> str:
        """
        str : property long name
        """
        return "chromium solubility"

    @property
    def description(self) -> str:
        """
        str : property description
        """
        return f"{self.long_name} in liquid bismuth"


class ChromiumSolubilityVenkatraman1988(ChromiumSolubilityInterface):
    """
    Chromium solubility in liquid bismuth property class
    implementing correlation by venkatraman1988
    """
    @range_warning
    @typecheck_for_method
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Correlation used to compute chromium solubility in liquid bismuth

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
        solubility [wt.%] : float
        """
        return np.power(10, 2.34-3610/T)

    @property
    def correlation_name(self) -> str:
        """
        str : name of the correlation
        """
        return "venkatraman1988"

    @property
    def range(self) -> List[float]:
        """
        list : temperature validity range for property correlation
        """
        return [658.0, 901.0]


class ChromiumSolubilityWeeks1998(ChromiumSolubilityInterface):
    """
    Chromium solubility in liquid bismuth property class
    implementing correlation by weeks1998
    """
    @range_warning
    @typecheck_for_method
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Correlation used to compute chromium solubility in liquid bismuth

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
        solubility [wt.%] : float
        """
        return np.power(10, 2.5-3717/T)

    @property
    def correlation_name(self) -> str:
        """
        str : name of the correlation
        """
        return "weeks1998"

    @property
    def range(self) -> List[float]:
        """
        list : temperature validity range for property correlation
        """
        return [663.0, 998.0]


class ChromiumSolubilityGosse2014(ChromiumSolubilityInterface):
    """
    Chromium solubility in liquid bismuth property class
    implementing correlation by gosse2014
    """
    @range_warning
    @typecheck_for_method
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Correlation used to compute chromium solubility in liquid bismuth

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
        solubility [wt.%] : float
        """
        return np.power(10, 2.34-3610/T)

    @property
    def correlation_name(self) -> str:
        """
        str : name of the correlation
        """
        return "gosse2014"

    @property
    def range(self) -> List[float]:
        """
        list : temperature validity range for property correlation
        """
        return [545.0, 1773.0]


class OxygenSolubility(PropertyInterface):
    """
    Oxygen solubility in liquid bismuth property class
    """
    @range_warning
    @typecheck_for_method
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Correlation used to compute oxygen solubility in liquid bismuth

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
        solubility [wt.%] : float
        """
        if T <= 1002:
            return np.power(10, 2.30-4066/T)
        return np.power(10, 3.04-4810/T)

    @property
    def name(self) -> str:
        """
        str : name of the property
        """
        return "o_sol"

    @property
    def units(self) -> str:
        """
        str : property units
        """
        return "[wt.%]"

    @property
    def range(self) -> List[float]:
        """
        list : temperature validity range for property correlation
        """
        return [573.0, 1573.0]

    @property
    def long_name(self) -> str:
        """
        str : property long name
        """
        return "oxygen solubility"

    @property
    def description(self) -> str:
        """
        str : property description
        """
        return "f{self.long_name} in liquid bismuth"
