"""Module with the definition of some coumpounds properties
for contamination assessment"""
from typing import List
from scipy.constants import atm
from ..interface import PropertyInterface
from ..._decorators import range_warning


class BismuthPoloniumActivityCoefficientInterfaceJoy1963(PropertyInterface):
    """
    Liquid lead *Polonium compounds activity coeffcient* property class
    implementing the correlation by *joy1963*.
    """
    @range_warning
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Returns the value of the *Polonium compounds activity coefficient* by
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
            activity coefficient in :math:`[]`
        """
        return 10**((- 2272.7 / T) + 0.1316)

    @property
    def name(self) -> str:
        """
        str : Name of the property
        """
        return "gamma_BiPo"

    @property
    def correlation_name(self) -> str:
        """
        str : Name of the correlation
        """
        return "joy1963"

    @property
    def units(self) -> str:
        """
        str : Activity coefficient unit
        """
        return "[]"

    @property
    def long_name(self) -> str:
        """
        str : Polonium activity coefficient long name
        """
        return "Activity coefficient of Polonium in pure bismuth"

    @property
    def description(self) -> str:
        """
        str : Polonium activity coefficient description
        """
        return f"{self.long_name} in liquid bismuth"

    @property
    def range(self) -> List[float]:
        """
        List[float] : Temperature validity range of the activity coefficient
        correlation function
        """
        return [723.0, 1123.0]


class BismuthIodineVapourPressureInterfaceCubicciotti1959(PropertyInterface):
    """
    Liquid bismuth *Iodine compounds vapour pressure* property class
    implementing the correlation by *cubicciotti1959*.
    """
    @range_warning
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Returns the value of the *Iodine compounds vapour pressure* by
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
            pressure in :math:`[Pa]`
        """
        return 10**((- 4310 / T) + 10.29)

    @property
    def name(self) -> str:
        """
        str : Name of the property
        """
        return "P_BiI3"

    @property
    def correlation_name(self) -> str:
        """
        str : Name of the correlation
        """
        return "cubicciotti1959"

    @property
    def units(self) -> str:
        """
        str : Vapour pressure unit
        """
        return "[Pa]"

    @property
    def long_name(self) -> str:
        """
        str : Iodine vapour pressure long name
        """
        return "Vapour pressure of Iodine in pure bismuth"

    @property
    def description(self) -> str:
        """
        str : Iodine vapour pressure description
        """
        return f"{self.long_name} in liquid bismuth"

    @property
    def range(self) -> List[float]:
        """
        List[float] : Temperature validity range of the Iodine vapour pressure
        correlation function
        """
        return [544.6, 1831.0]
