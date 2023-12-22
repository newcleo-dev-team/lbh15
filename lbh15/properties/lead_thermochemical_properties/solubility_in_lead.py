"""Module with the definition of the *solubility*
property objects for *lead*."""
from typing import List
import numpy as np
from scipy.constants import atm
from lbh15.properties.interface import PropertyInterface
from ..._decorators import range_warning


class IronSolubility(PropertyInterface):
    """
    Liquid lead *Iron solubility* property class.
    """
    @range_warning
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Returns the value of the *Iron solubility* by
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
            solubility in :math:`[wt.\\%]`
        """
        return np.power(10, 2.11-5225/T)

    @property
    def name(self) -> str:
        """
        str : Name of the property
        """
        return "fe_sol"

    @property
    def units(self) -> str:
        """
        str : Iron solubility unit
        """
        return "[wt.%]"

    @property
    def correlation_name(self) -> str:
        """
        str : Name of the correlation
        """
        return "gosse2014"

    @property
    def range(self) -> List[float]:
        """
        List[float] : Temperature validity range of the Iron solubility
        correlation function
        """
        return [600.0, 1173.0]

    @property
    def long_name(self) -> str:
        """
        str : Iron solubility long name
        """
        return "iron solubility"

    @property
    def description(self) -> str:
        """
        str : Iron solubility description
        """
        return "f{self.long_name} in liquid lead"


class NickelSolubility(PropertyInterface):
    """
    Liquid lead *Nickel solubility* property class.
    """
    @range_warning
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Returns the value of the *Nickel solubility* by
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
            solubility in :math:`[wt.\\%]`
        """
        return np.power(10, 1.36-1395/T)

    @property
    def name(self) -> str:
        """
        str : Name of the property
        """
        return "ni_sol"

    @property
    def units(self) -> str:
        """
        str : Nickel solubility unit
        """
        return "[wt.%]"

    @property
    def correlation_name(self) -> str:
        """
        str : Name of the correlation
        """
        return "gosse2014"

    @property
    def range(self) -> List[float]:
        """
        List[float] : Temperature validity range of the Nickel solubility
        correlation function
        """
        return [598.0, 917.0]

    @property
    def long_name(self) -> str:
        """
        str : Nickel solubility long name
        """
        return "nickel solubility"

    @property
    def description(self) -> str:
        """
        str : Nickel solubility description
        """
        return "f{self.long_name} in liquid lead"


class ChromiumSolubilityInterface(PropertyInterface):
    """
    Liquid lead *Chromium solubility* property abstract class.
    """
    @property
    def name(self) -> str:
        """
        str : Name of the property
        """
        return "cr_sol"

    @property
    def units(self) -> str:
        """
        str : Chromium solubility unit
        """
        return "[wt.%]"

    @property
    def long_name(self) -> str:
        """
        str : Chromium solubility long name
        """
        return "chromium solubility"

    @property
    def description(self) -> str:
        """
        str : Chromium solubility description
        """
        return f"{self.long_name} in liquid lead"


class ChromiumSolubilityAlden1958(ChromiumSolubilityInterface):
    """
    Liquid lead *Chromium solubility* property class
    implementing the correlation by *alden1958*.
    """
    @range_warning
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Returns the value of the *Chromium solubility* by
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
            solubility in :math:`[wt.\\%]`
        """
        return np.power(10, 3.74-6750/T)

    @property
    def correlation_name(self) -> str:
        """
        str : Name of the correlation
        """
        return "alden1958"

    @property
    def range(self) -> List[float]:
        """
        List[float] : Temperature validity range of the Chromium solubility
        correlation function
        """
        return [1181.0, 1483.0]


class ChromiumSolubilityVenkatraman1988(ChromiumSolubilityInterface):
    """
    Liquid lead *Chromium solubility* property class
    implementing the correlation by *venkatraman1988*.
    """
    @range_warning
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Returns the value of the *Chromium solubility* by
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
            solubility in :math:`[wt.\\%]`
        """
        return np.power(10, 3.7-6720/T)

    @property
    def correlation_name(self) -> str:
        """
        str : Name of the correlation
        """
        return "venkatraman1988"

    @property
    def range(self) -> List[float]:
        """
        List[float] : Temperature validity range of the Chromium solubility
        correlation function
        """
        return [1173.0, 1473.0]


class ChromiumSolubilityGosse2014(ChromiumSolubilityInterface):
    """
    Liquid lead *Chromium solubility* property class
    implementing the correlation by *gosse2014*.
    """
    @range_warning
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Returns the value of the *Chromium solubility* by
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
            solubility in :math:`[wt.\\%]`
        """
        return np.power(10, 3.62-6648/T)

    @property
    def correlation_name(self) -> str:
        """
        str : Name of the correlation
        """
        return "gosse2014"

    @property
    def range(self) -> List[float]:
        """
        List[float] : Temperature validity range of the Chromium solubility
        correlation function
        """
        return [601.0, 1773.0]


class SiliconSolubility(PropertyInterface):
    """
    Liquid lead *Silicon solubility* property class.
    """
    @range_warning
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Returns the value of the *Silicon solubility* by
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
            solubility in :math:`[wt.\\%]`
        """
        return np.power(10, 3.886-7180/T)

    @property
    def name(self) -> str:
        """
        str : Name of the property
        """
        return "si_sol"

    @property
    def units(self) -> str:
        """
        str : Silicon solubility unit
        """
        return "[wt.%]"

    @property
    def range(self) -> List[float]:
        """
        List[float] : Temperature validity range of the Silicon solubility
        correlation function
        """
        return [1323.0, 1523.0]

    @property
    def long_name(self) -> str:
        """
        str : Silicon solubility long name
        """
        return "silicon solubility"

    @property
    def description(self) -> str:
        """
        str : Silicon solubility description
        """
        return "f{self.long_name} in liquid lead"


class OxygenSolubility(PropertyInterface):
    """
    Liquid lead *Oxygen solubility* property class.
    """
    @range_warning
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Returns the value of the *Oxygen solubility* by
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
            solubility in :math:`[wt.\\%]`
        """
        return np.power(10, 3.23-5043/T)

    @property
    def name(self) -> str:
        """
        str : Name of the property
        """
        return "o_sol"

    @property
    def units(self) -> str:
        """
        str : Oxygen solubility unit
        """
        return "[wt.%]"

    @property
    def range(self) -> List[float]:
        """
        List[float] : Temperature validity range of the Oxygen solubility
        correlation function
        """
        return [673.0, 1373.0]

    @property
    def long_name(self) -> str:
        """
        str : Oxygen solubility long name
        """
        return "oxygen solubility"

    @property
    def description(self) -> str:
        """
        str : Oxygen solubility description
        """
        return "f{self.long_name} in liquid lead"
