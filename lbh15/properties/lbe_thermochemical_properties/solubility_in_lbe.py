"""Module with the definition of the *solubility*
property objects for *lead-bismuth eutectic* (*lbe*)."""
from typing import List
from typing import Union
import numpy as np
from scipy.constants import atm
from lbh15.properties.interface import PropertyInterface
from ..._decorators import range_warning


class IronSolubilityInterface(PropertyInterface):
    """
    Liquid lbe *Iron solubility* property abstract class.
    """
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
        return f"{self.long_name} in liquid lbe"


class IronSolubilityGosse2014(IronSolubilityInterface):
    """
    Liquid lbe *Iron solubility* property class
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
        return np.power(10, 2.00-4399/T)

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
        return [399.0, 1173.0]


class IronSolubilityWeeks1969(IronSolubilityInterface):
    """
    Liquid lbe *Iron solubility* property class
    implementing the correlation by *weeks1969*.
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
        return np.power(10, 1.85-4164/T)

    @property
    def correlation_name(self) -> str:
        """
        str : Name of the correlation
        """
        return "weeks1969"

    @property
    def range(self) -> List[float]:
        """
        List[float] : Temperature validity range of the Iron solubility
        correlation function
        """
        return [823.0, 1053.0]


class NickelSolubilityInterface(PropertyInterface):
    """
    Liquid lbe *Nickel solubility* property abstract class.
    """
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
        return f"{self.long_name} in liquid lbe"


class NickelSolubilityMartinelli2010(NickelSolubilityInterface):
    """
    Liquid lbe *Nickel solubility* property class
    implementing the correlation by *martinelli2010*.
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
        return np.where(T <= 712, np.power(10, 5.2-3500/T),
                        np.power(10, 1.7-1009/T))[()]

    @property
    def correlation_name(self) -> str:
        """
        str : Name of the correlation
        """
        return "martinelli2010"

    @property
    def range(self) -> List[float]:
        """
        List[float] : Temperature validity range of the Nickel solubility
        correlation function
        """
        return [603.0, 1173.0]


class NickelSolubilityGosse2014(NickelSolubilityInterface):
    """
    Liquid lbe *Nickel solubility* property class
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
        return np.where(T <= 742, np.power(10, 4.32-2933/T),
                        np.power(10, 1.74-1006/T))[()]

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
        return [528.0, 1173.0]


class ChromiumSolubilityInterface(PropertyInterface):
    """
    Liquid lbe *Chromium solubility* property abstract class.
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
        return "cr solubility"

    @property
    def description(self) -> str:
        """
        str : Chromium solubility description
        """
        return f"{self.long_name} in liquid lbe"


class ChromiumSolubilityGosse2014(ChromiumSolubilityInterface):
    """
    Liquid lbe *Chromium solubility* property class
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
        return np.power(10, 1.12-3056/T)

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
        return [399.0, 1173.0]


class ChromiumSolubilityCourouau2004(ChromiumSolubilityInterface):
    """
    Liquid lbe *Chromium solubility* property class
    implementing the correlation by *courouau2004*.
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
        return np.power(10, 1.07-3022/T)

    @property
    def correlation_name(self) -> str:
        """
        str : Name of the correlation
        """
        return "courouau2004"

    @property
    def range(self) -> List[float]:
        """
        List[float] : Temperature validity range of the Chromium solubility
        correlation function
        """
        return [643.0, 813.0]


class ChromiumSolubilityMartynov1998(ChromiumSolubilityInterface):
    """
    Liquid lbe *Chromium solubility* property class
    implementing the correlation by *martynov1998*.
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
        return np.power(10, -0.02-2280/T)

    @property
    def correlation_name(self) -> str:
        """
        str : Name of the correlation
        """
        return "martynov1998"

    @property
    def range(self) -> List[float]:
        """
        List[float] : Temperature validity range of the Chromium solubility
        correlation function
        """
        return [673.0, 773.0]


class OxygenSolubility(PropertyInterface):
    """
    Liquid lbe *Oxygen solubility* property class.
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
        return np.power(10, 2.25-4125/T)

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
        return [673.0, 1013.0]

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
        return "f{self.long_name} in liquid lbe"
