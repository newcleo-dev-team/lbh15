"""Module with the definition of some coumpounds properties
for contamination assessment"""
from math import log
from typing import List
from scipy.constants import atm
from ..interface import PropertyInterface
from ..._decorators import range_warning


class LeadPoloniumVapourPressureInterfaceAbakumov1994a(PropertyInterface):
    """
    Liquid lead *Polonium compounds vapour pressure* property class
    implementing the correlation by *abakumov1994a*.
    """
    @range_warning
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Returns the value of the *Polonium compounds vapour pressure* by
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
        return 10**((- 7270 / T) + 9.06)

    @property
    def name(self) -> str:
        """
        str : Name of the property
        """
        return "P_PbPo"

    @property
    def correlation_name(self) -> str:
        """
        str : Name of the correlation
        """
        return "abakumov1994a"

    @property
    def units(self) -> str:
        """
        str : Vapour pressure unit
        """
        return "[Pa]"

    @property
    def long_name(self) -> str:
        """
        str : Polonium vapour pressure long name
        """
        return "Vapour pressure of Polonium in pure lead"

    @property
    def description(self) -> str:
        """
        str : Polonium vapour pressure description
        """
        return f"{self.long_name} in liquid lead"

    @property
    def range(self) -> List[float]:
        """
        List[float] : Temperature validity range of the Polonium
        vapour pressure correlation function
        """
        return [913.0, 1123.0]


class LeadPoloniumHenryConstantInterfaceOhno2006(PropertyInterface):
    """
    Liquid lead *Polonium compounds Henry constant* property class
    implementing the correlation by *ohno2006*.
    """
    @range_warning
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Returns the value of the *Polonium compounds Henry constant* by
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
            Henry constant in :math:`[Pa]`
        """
        return 10**((- 8348 / T) + 10.5357)

    @property
    def name(self) -> str:
        """
        str : Name of the property
        """
        return "K_PbPo"

    @property
    def correlation_name(self) -> str:
        """
        str : Name of the correlation
        """
        return "ohno2006"

    @property
    def units(self) -> str:
        """
        str : Henry constant unit
        """
        return "[Pa]"

    @property
    def long_name(self) -> str:
        """
        str : Polonium Henry constant long name
        """
        return "Henry constant of Polonium in pure lead"

    @property
    def description(self) -> str:
        """
        str : Polonium Henry constant description
        """
        return f"{self.long_name} in liquid lead"

    @property
    def range(self) -> List[float]:
        """
        List[float] : Temperature validity range of the Polonium Henry constant
        correlation function
        """
        return [723.0, 1023.0]

class LeadPoloniumActivityCoefficientInterfaceLi1998(PropertyInterface):
    """
    Liquid lbe *Polonium compounds activity coefficient* property class.
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
        return 10**((- 1830 / T) - 0.40)

    @property
    def name(self) -> str:
        """
        str : Name of the property
        """
        return "gamma_PbPo"

    @property
    def correlation_name(self) -> str:
        """
        str : Name of the correlation
        """
        return "Li1998"

    @property
    def units(self) -> str:
        """
        str : activity coefficient unit
        """
        return "[]"

    @property
    def long_name(self) -> str:
        """
        str : Polonium activity coefficient long name
        """
        return "Activity coefficient of Polonium in pure lead"

    @property
    def description(self) -> str:
        """
        str : Polonium Activity coefficient description
        """
        return f"{self.long_name} in liquid lead"

    @property
    def range(self) -> List[float]:
        """
        List[float] : Temperature validity range of the Polonium activity
        coefficient correlation function.
        """
        return [641.0, 877.0]
