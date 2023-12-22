"""Module with the definition of the *diffusivity*
property objects for *lead-bismuth eutectic* (*lbe*)."""
from typing import List
import numpy as np
from scipy.constants import atm, R
from lbh15.properties.interface import PropertyInterface
from ..._decorators import range_warning


class OxygenDiffusivityInterface(PropertyInterface):
    """
    Liquid lbe *Oxygen diffusivity* property abstract class.
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
        return "[cm^2.s^-1]"

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
        return f"{self.long_name} in liquid lbe"


class OxygenDiffusivityGromov1996(OxygenDiffusivityInterface):
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
            diffusivity in :math:`[cm^2 / s]`
        """
        return np.exp(-43073 / R / T) * 2.39e-2

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


class OxygenDiffusivityGanesan2006b(OxygenDiffusivityInterface):
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
            diffusivity in :math:`[cm^2 / s]`
        """
        return np.exp(-69069 / R / T) * 0.154

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


class IronDiffusivity(PropertyInterface):
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
            diffusivity in :math:`[cm^2 / s]`
        """
        return np.power(10, - 2.31 - 2295 / T)

    @property
    def name(self) -> str:
        """
        str : Name of the property
        """
        return "fe_dif"

    @property
    def units(self) -> str:
        """
        str : Iron diffusivity unit
        """
        return "[cm^2.s^-1]"

    @property
    def range(self) -> List[float]:
        """
        List[float] : Temperature validity range of the Iron diffusivity
        correlation function
        """
        return [973.0, 1273.0]

    @property
    def long_name(self) -> str:
        """
        str : Iron diffusivity long name
        """
        return "iron diffusivity"

    @property
    def description(self) -> str:
        """
        str : Iron diffusivity description
        """
        return "f{self.long_name} in liquid lbe"
