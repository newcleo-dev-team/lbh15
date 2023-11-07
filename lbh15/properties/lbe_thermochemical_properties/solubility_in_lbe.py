"""Module with the definition of solubility
property objects for lead-bismuth eutectic"""
from typing import List
from typing import Union
import numpy as np
from scipy.constants import atm
from lbh15.properties.interface import PropertyInterface
from lbh15.properties.interface import range_warning
from ..._decorators import typecheck_for_method


class IronSolubilityInterface(PropertyInterface):
    """
    Iron solubility in liquid lead-bismuth
    eutectic property class
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
        return f"{self.long_name} in liquid lbe"


class IronSolubilityGosse2014(IronSolubilityInterface):
    """
    Iron solubility in liquid lead-bismuth eutectic
    property class implementing correlation by gosse2014
    """
    @range_warning
    @typecheck_for_method
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Correlation used to compute iron solubility in liquid
        lead-bismuth eutectic

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
        return np.power(10, 2.00-4399/T)

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
        return [399.0, 1173.0]


class IronSolubilityWeeks1969(IronSolubilityInterface):
    """
    Iron solubility in liquid lead-bismuth eutectic
    property class implementing correlation by weeks1969
    """
    @range_warning
    @typecheck_for_method
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Correlation used to compute iron solubility in liquid
        lead-bismuth eutectic

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
        return np.power(10, 1.85-4164/T)

    @property
    def correlation_name(self) -> str:
        """
        str : name of the correlation
        """
        return "weeks1969"

    @property
    def range(self) -> List[float]:
        """
        list : temperature validity range for property correlation
        """
        return [823.0, 1053.0]


class NickelSolubilityInterface(PropertyInterface):
    """
    Nickel solubility in liquid lead-bismuth
    eutectic property class
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
        return f"{self.long_name} in liquid lbe"


class NickelSolubilityMartinelli2010(NickelSolubilityInterface):
    """
    Nickel solubility in liquid lead-bismuth eutectic
    property class implementing correlation by martinelli2010
    """
    @range_warning
    @typecheck_for_method
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> Union[float, np.ndarray]:
        """
        Correlation used to compute nickel solubility in liquid
        lead-bismuth eutectic

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
        return np.where(T <= 712, np.power(10, 5.2-3500/T),
                        np.power(10, 1.7-1009/T))[()]

    @property
    def correlation_name(self) -> str:
        """
        str : name of the correlation
        """
        return "martinelli2010"

    @property
    def range(self) -> List[float]:
        """
        list : temperature validity range for property correlation
        """
        return [603.0, 1173.0]


class NickelSolubilityGosse2014(NickelSolubilityInterface):
    """
    Nickel solubility in liquid lead-bismuth eutectic
    property class implementing correlation by gosse2014
    """
    @range_warning
    @typecheck_for_method
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> Union[float, np.ndarray]:
        """
        Correlation used to compute nickel solubility in liquid
        lead-bismuth eutectic

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
        return np.where(T <= 742, np.power(10, 4.32-2933/T),
                        np.power(10, 1.74-1006/T))[()]

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
        return [528.0, 1173.0]


class ChromiumSolubilityInterface(PropertyInterface):
    """
    Chromium solubility in liquid lead-bismuth
    eutectic property class
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
        return "cr solubility"

    @property
    def description(self) -> str:
        """
        str : property description
        """
        return f"{self.long_name} in liquid lbe"


class ChromiumSolubilityGosse2014(ChromiumSolubilityInterface):
    """
    Chromium solubility in liquid lead-bismuth eutectic
    property class implementing correlation by gosse2014
    """
    @range_warning
    @typecheck_for_method
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Correlation used to compute chromium solubility in liquid
        lead-bismuth eutectic

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
        return np.power(10, 1.12-3056/T)

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
        return [399.0, 1173.0]


class ChromiumSolubilityCourouau2004(ChromiumSolubilityInterface):
    """
    Chromium solubility in liquid lead-bismuth eutectic
    property class implementing correlation by courouau2004
    """
    @range_warning
    @typecheck_for_method
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Correlation used to compute chromium solubility in liquid
        lead-bismuth eutectic

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
        return np.power(10, 1.07-3022/T)

    @property
    def correlation_name(self) -> str:
        """
        str : name of the correlation
        """
        return "courouau2004"

    @property
    def range(self) -> List[float]:
        """
        list : temperature validity range for property correlation
        """
        return [643.0, 813.0]


class ChromiumSolubilityMartynov1998(ChromiumSolubilityInterface):
    """
    Chromium solubility in liquid lead-bismuth eutectic
    property class implementing correlation by martynov1998
    """
    @range_warning
    @typecheck_for_method
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Correlation used to compute chromium solubility in liquid
        lead-bismuth eutectic

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
        return np.power(10, -0.02-2280/T)

    @property
    def correlation_name(self) -> str:
        """
        str : name of the correlation
        """
        return "martynov1998"

    @property
    def range(self) -> List[float]:
        """
        list : temperature validity range for property correlation
        """
        return [673.0, 773.0]


class OxygenSolubility(PropertyInterface):
    """
    Oxygen solubility in liquid lead-bismuth
    eutectic property class
    """
    @range_warning
    @typecheck_for_method
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Correlation used to compute oxygen solubility in
        liquid lead-bismuth eutectic

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
        return np.power(10, 2.25-4125/T)

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
        return [673.0, 1013.0]

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
        return "f{self.long_name} in liquid lbe"
