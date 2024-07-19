"""Module with the definition of some coumpounds properties
for contamination assessment"""
from math import log
from typing import List
from scipy.constants import atm
from ..interface import PropertyInterface
from ..._decorators import range_warning


class LBEPoloniumHenryConstantInterfaceOhno2006(PropertyInterface):
    """
    Liquid LBE *Polonium compounds Henry constant* property class
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
        return "K_LBEPo"

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
        return "Henry constant of Polonium in LBE"

    @property
    def description(self) -> str:
        """
        str : Polonium Henry constant description
        """
        return f"{self.long_name} in liquid LBE"

    @property
    def range(self) -> List[float]:
        """
        List[float] : Temperature validity range of the Polonium Henry constant
        correlation function
        """
        return [723.0, 1023.0]
