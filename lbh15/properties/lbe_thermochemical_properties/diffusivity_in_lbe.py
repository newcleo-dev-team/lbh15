"""Module with the definition of the *diffusivity*
property objects for *lead-bismuth eutectic* (*lbe*)."""
from typing import List
import numpy as np
from scipy.constants import atm, R
from ..tch_common_interface import OxygenDiffusivityInterface
from ..tch_common_interface import IronDiffusivityInterface
from ..._decorators import range_warning


class LBEOxygenDiffusivityInterface(OxygenDiffusivityInterface):
    """
    Liquid lbe *Oxygen diffusivity* property abstract class.
    """
    @property
    def description(self) -> str:
        """
        str : Oxygen diffusivity description
        """
        return f"{self.long_name} in liquid lbe"


class OxygenDiffusivityGromov1996(LBEOxygenDiffusivityInterface):
    """
    Liquid lbe *Oxygen diffusivity* property class
    implementing the correlation by *gromov1996*.
    """
    @range_warning
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Returns the value of the *Oxygen diffusivity* by
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
            diffusivity in :math:`[m^2 / s]`
        """
        return np.exp(-43073 / R / T) * 2.39e-6

    @property
    def correlation_name(self) -> str:
        """
        str : Name of the correlation
        """
        return "gromov1996"

    @property
    def range(self) -> List[float]:
        """
        List[float] : Temperature validity range of the Oxygen diffusivity
        correlation function
        """
        return [473, 1273]


class OxygenDiffusivityGanesan2006b(LBEOxygenDiffusivityInterface):
    """
    Liquid lbe *Oxygen diffusivity* property class
    implementing the correlation by *ganesan2006b*.
    """
    @range_warning
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Returns the value of the *Oxygen diffusivity* by
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
            diffusivity in :math:`[m^2 / s]`
        """
        return np.exp(-69069 / R / T) * 0.154e-4

    @property
    def correlation_name(self) -> str:
        """
        str : Name of the correlation
        """
        return "ganesan2006b"

    @property
    def range(self) -> List[float]:
        """
        List[float] : Temperature validity range of the Oxygen diffusivity
        correlation function
        """
        return [813, 973]


class IronDiffusivity(IronDiffusivityInterface):
    """
    Liquid lbe *Iron diffusivity* property class.
    """
    @range_warning
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Returns the value of the *Iron diffusivity* by
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
            diffusivity in :math:`[m^2 / s]`
        """
        return np.power(10, - 2.31 - 2295 / T) * 1.0e-4

    @property
    def range(self) -> List[float]:
        """
        List[float] : Temperature validity range of the Iron diffusivity
        correlation function
        """
        return [973.0, 1273.0]

    @property
    def description(self) -> str:
        """
        str : Iron diffusivity description
        """
        return f"{self.long_name} in liquid lbe"
