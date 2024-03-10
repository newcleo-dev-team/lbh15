"""Module with the definition of the *diffusivity*
property objects for *bismuth*."""
from typing import List
import numpy as np
from scipy.constants import atm
from scipy.constants import R
from lbh15.properties.common_interface import OxygenDiffusivityInterface
from ..._decorators import range_warning


class BismuthOxygenDiffusivityInterface(OxygenDiffusivityInterface):
    """
    Liquid bismuth *Oxygen diffusivity* property abstract class.
    """
    @property
    def name(self) -> str:
        """
        str : Name of the property
        """
        return "o_dif"

    @property
    def units(self) -> str:
        """
        str : Oxygen diffusivity unit
        """
        return "[m^2.s^-1]"

    @property
    def long_name(self) -> str:
        """
        str : Oxygen diffusivity long name
        """
        return "oxygen diffusivity"

    @property
    def description(self) -> str:
        """
        str : Oxygen diffusivity description
        """
        return f"{self.long_name} in liquid bismuth"


class OxygenDiffusivityFitzner1980(BismuthOxygenDiffusivityInterface):
    """
    Liquid bismuth *Oxygen diffusivity* property class
    implementing the correlation by *fitzner1980*.
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
        return np.exp(-49229 / R / T) * 1.07e-6

    @property
    def correlation_name(self) -> str:
        """
        str : Name of the correlation
        """
        return "fitzner1980"

    @property
    def range(self) -> List[float]:
        """
        List[float] : Temperature validity range of the Oxygen diffusivity
        correlation function
        """
        return [951, 1100]


class OxygenDiffusivityHeshmatpour1981(BismuthOxygenDiffusivityInterface):
    """
    Liquid bismuth *Oxygen diffusivity* property class
    implementing the correlation by *heshmatpour1981*.
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
        return np.exp(-26610 / R / T) * 1.98e-8

    @property
    def correlation_name(self) -> str:
        """
        str : Name of the correlation
        """
        return "heshmatpour1981"

    @property
    def range(self) -> List[float]:
        """
        List[float] : Temperature validity range of the Oxygen diffusivity
        correlation function
        """
        return [1023, 1273]
