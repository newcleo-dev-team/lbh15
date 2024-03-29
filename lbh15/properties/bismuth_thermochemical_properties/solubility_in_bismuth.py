"""Module with the definition of the *solubility*
property objects for *bismuth*."""
from typing import List
from typing import Union
import numpy as np
from scipy.constants import atm
from ..tch_common_interface import IronSolubilityInterface
from ..tch_common_interface import NickelSolubilityInterface
from ..tch_common_interface import ChromiumSolubilityInterface
from ..tch_common_interface import OxygenSolubilityInterface
from ..._decorators import range_warning


class BismuthIronSolubilityInterface(IronSolubilityInterface):
    """
    Liquid bismuth *Iron solubility* property abstract class.
    """
    @property
    def description(self) -> str:
        """
        str : Iron solubility description
        """
        return f"{self.long_name} in liquid bismuth"


class IronSolubilityGosse2014(BismuthIronSolubilityInterface):
    """
    Liquid bismuth *Iron solubility* property class
    implementing the correlation by *gosse2014*.
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
        return np.power(10, 2.20-3930/T)

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
        return [545.0, 1173.0]


class IronSolubilityMassalski1990(BismuthIronSolubilityInterface):
    """
    Liquid bismuth *Iron solubility* property class
    implementing the correlation by *massalski1990*.
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
        return np.power(10, 2.18-3980/T)

    @property
    def correlation_name(self) -> str:
        """
        str : Name of the correlation
        """
        return "massalski1990"

    @property
    def range(self) -> List[float]:
        """
        List[float] : Temperature validity range of the Iron solubility
        correlation function
        """
        return [973.0, 1173.0]


class IronSolubilityWeeks1998(BismuthIronSolubilityInterface):
    """
    Liquid bismuth *Iron solubility* property class
    implementing the correlation by *weeks1998*.
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
        return np.power(10, 1.832-3589/T)

    @property
    def correlation_name(self) -> str:
        """
        str : Name of the correlation
        """
        return "weeks1998"

    @property
    def range(self) -> List[float]:
        """
        List[float] : Temperature validity range of the Iron solubility
        correlation function
        """
        return [713.0, 998.0]


class BismuthNickelSolubilityInterface(NickelSolubilityInterface):
    """
    Liquid bismuth *Nickel solubility* property abstract class.
    """
    @property
    def description(self) -> str:
        """
        str : Nickel solubility description
        """
        return f"{self.long_name} in liquid bismuth"


class NickelSolubilityWeeks1998(BismuthNickelSolubilityInterface):
    """
    Liquid bismuth *Nickel solubility* property class
    implementing the correlation by *weeks1998*.
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
        return np.power(10, 2.61-1538/T)

    @property
    def correlation_name(self) -> str:
        """
        str : Name of the correlation
        """
        return "weeks1998"

    @property
    def range(self) -> List[float]:
        """
        List[float] : Temperature validity range of the Nickel solubility
        correlation function
        """
        return [723.0, 903.0]


class NickelSolubilityGosse2014(BismuthNickelSolubilityInterface):
    """
    Liquid bismuth *Nickel solubility* property class
    implementing the correlation by *gosse2014*.
    """
    @range_warning
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> Union[float, np.ndarray]:
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
        return np.where(T <= 738, np.power(10, 3.81-2429/T),
                        np.where(T <= 918, np.power(10, 2.05-1131/T),
                                 np.power(10, 1.35-484/T)))[()]

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
        return [543.0, 1173.0]


class BismuthChromiumSolubilityInterface(ChromiumSolubilityInterface):
    """
    Liquid bismuth *Chromium solubility* property abstract class.
    """
    @property
    def description(self) -> str:
        """
        str : Chromium solubility description
        """
        return f"{self.long_name} in liquid bismuth"


class ChromiumSolubilityVenkatraman1988(BismuthChromiumSolubilityInterface):
    """
    Liquid bismuth *Chromium solubility* property class
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
        return np.power(10, 2.34-3610/T)

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
        return [658.0, 901.0]


class ChromiumSolubilityWeeks1998(BismuthChromiumSolubilityInterface):
    """
    Liquid bismuth *Chromium solubility* property class
    implementing the correlation by *weeks1998*.
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
        return np.power(10, 2.5-3717/T)

    @property
    def correlation_name(self) -> str:
        """
        str : Name of the correlation
        """
        return "weeks1998"

    @property
    def range(self) -> List[float]:
        """
        List[float] : Temperature validity range of the Chromium solubility
        correlation function
        """
        return [663.0, 998.0]


class ChromiumSolubilityGosse2014(BismuthChromiumSolubilityInterface):
    """
    Liquid bismuth *Chromium solubility* property class
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
        return np.power(10, 2.34-3610/T)

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
        return [545.0, 1773.0]


class OxygenSolubility(OxygenSolubilityInterface):
    """
    Liquid bismuth *Oxygen solubility* property class.
    """
    @range_warning
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> Union[float, np.ndarray]:
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
        return np.where(T <= 1002, np.power(10, 2.30-4066/T),
                        np.power(10, 3.04-4810/T))[()]

    @property
    def range(self) -> List[float]:
        """
        List[float] : Temperature validity range of the Oxygen solubility
        correlation function
        """
        return [573.0, 1573.0]

    @property
    def description(self) -> str:
        """
        str : Oxygen solubility description
        """
        return f"{self.long_name} in liquid bismuth"
