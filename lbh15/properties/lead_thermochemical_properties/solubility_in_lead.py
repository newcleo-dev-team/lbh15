"""Module with the definition of solubility
property objects for bismuth"""
from typing import List
import numpy as np
from scipy.constants import atm
from lbh15.properties.interface import PropertyInterface
from lbh15.properties.interface import range_warning
from ..._decorators import typecheck_for_method


class IronSolubility(PropertyInterface):
    """
    Iron solubility in liquid lead property class
    """
    @range_warning
    @typecheck_for_method
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Correlation used to compute iron solubility in liquid lead

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
        return np.exp((2.11-5225/T)*np.log(10))

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
        return [600.0, 1173.0]

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
        return "f{self.long_name} in liquid lead"


class NickelSolubility(PropertyInterface):
    """
    Nickel solubility in liquid lead property class
    """
    @range_warning
    @typecheck_for_method
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Correlation used to compute nickel solubility in liquid lead

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
        return np.exp((1.36-1395/T)*np.log(10))

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
        return [598.0, 917.0]

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
        return "f{self.long_name} in liquid lead"


class ChromiumSolubilityInterface(PropertyInterface):
    """
    Chromium solubility in liquid lead property class
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
        return f"{self.long_name} in liquid lead"


class ChromiumSolubilityAlden1958(ChromiumSolubilityInterface):
    """
    Chromium solubility in liquid lead property class
    implementing correlation by alden1958
    """
    @range_warning
    @typecheck_for_method
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Correlation used to compute chromium solubility in liquid lead

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

        return np.exp((3.74-6750/T)*np.log(10))

    @property
    def correlation_name(self) -> str:
        """
        str : name of the correlation
        """
        return "alden1958"

    @property
    def range(self) -> List[float]:
        """
        list : temperature validity range for property correlation
        """
        return [1181.0, 1483.0]


class ChromiumSolubilityVenkatraman1988(ChromiumSolubilityInterface):
    """
    Chromium solubility in liquid lead property class
    implementing correlation by venkatraman1988
    """
    @range_warning
    @typecheck_for_method
    def correlation(self, T: float, p: float = atm,
                    verbose: bool =False) -> float:
        """
        Correlation used to compute chromium solubility in liquid lead

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

        return np.exp((3.7-6720/T)*np.log(10))

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
        return [1173.0, 1473.0]


class ChromiumSolubilityGosse2014(ChromiumSolubilityInterface):
    """
    Chromium solubility in liquid lead property class
    implementing correlation by gosse2014
    """
    @range_warning
    @typecheck_for_method
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Correlation used to compute chromium solubility in liquid lead

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

        return np.exp((3.62-6648/T)*np.log(10))

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
        return [601.0, 1773.0]


class SiliconSolubility(PropertyInterface):
    """
    Silicon solubility in liquid lead property class
    """
    @range_warning
    @typecheck_for_method
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Correlation used to compute silicon solubility in liquid lead

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
        return np.exp((3.886-7180/T)*np.log(10))

    @property
    def name(self) -> str:
        """
        str : name of the property
        """
        return "si_sol"

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
        return [1323.0, 1523.0]

    @property
    def long_name(self) -> str:
        """
        str : property long name
        """
        return "silicon solubility"

    @property
    def description(self) -> str:
        """
        str : property description
        """
        return "f{self.long_name} in liquid lead"


class OxygenSolubility(PropertyInterface):
    """
    Oxygen solubility in liquid lead property class
    """
    @range_warning
    @typecheck_for_method
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Correlation used to compute oxygen solubility in liquid lead

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
        return np.exp((3.23-5043/T)*np.log(10))

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
        return [673.0, 1373.0]

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
        return "f{self.long_name} in liquid lead"
