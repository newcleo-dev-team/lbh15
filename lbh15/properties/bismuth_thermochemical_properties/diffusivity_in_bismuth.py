"""Module with the definition of diffusivity
property objects for bismuth"""
from typing import List
import numpy as np
from scipy.constants import atm
from scipy.constants import R
from lbh15.properties.interface import PropertyInterface
from ..._decorators import range_warning
from ..._decorators import typecheck_for_method


class OxygenDiffusivityInterface(PropertyInterface):
    """
    Oxygen diffusivity in liquid bismuth property class
    """
    @property
    def name(self) -> str:
        """
        str : name of the property
        """
        return "o_dif"

    @property
    def units(self) -> str:
        """
        str : property units
        """
        return "[cm^2.s^-1]"

    @property
    def long_name(self) -> str:
        """
        str : property long name
        """
        return "oxygen diffusivity"

    @property
    def description(self) -> str:
        """
        str : property description
        """
        return f"{self.long_name} in liquid bismuth"


class OxygenDiffusivityFitzner1980(OxygenDiffusivityInterface):
    """
    Oxygen diffusivity in liquid bismuth property class
    implementing correlation by fitzner1980
    """
    @range_warning
    @typecheck_for_method
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Correlation used to compute oxygen diffusivity in liquid bismuth

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
        diffusivity [cm^2.s^-1] : float
        """
        return np.exp(-49229 / R / T) * 1.07e-2

    @property
    def correlation_name(self) -> str:
        """
        str : name of the correlation
        """
        return "fitzner1980"

    @property
    def range(self) -> List[float]:
        """
        list : temperature validity range for property correlation
        """
        return [951, 1100]


class OxygenDiffusivityHeshmatpour1981(OxygenDiffusivityInterface):
    """
    Oxygen diffusivity in liquid bismuth property class
    implementing correlation by heshmatpour1981
    """
    @range_warning
    @typecheck_for_method
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Correlation used to compute oxygen diffusivity in liquid bismuth

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
        diffusivity [cm^2.s^-1] : float
        """
        return np.exp(-26610 / R / T) * 1.98e-4

    @property
    def correlation_name(self) -> str:
        """
        str : name of the correlation
        """
        return "heshmatpour1981"

    @property
    def range(self) -> List[float]:
        """
        list : temperature validity range for property correlation
        """
        return [1023, 1273]
