"""Module with the definition of diffusivity
property objects for lead-bismuth eutectic"""
from typing import List
import numpy as np
from scipy.constants import atm, R
from lbh15.properties.interface import PropertyInterface
from lbh15.properties.interface import range_warning


class OxygenDiffusivityInterface(PropertyInterface):
    """
    Oxygen diffusivity in liquid lead-bismuth
    eutectic property class
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
        return f"{self.long_name} in liquid lbe"


class OxygenDiffusivityGromov1996(OxygenDiffusivityInterface):
    """
    Oxygen diffusivity in liquid lead-bismuth eutectic
    property class implementing correlation by gromov1996
    """
    @range_warning
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Correlation used to compute oxygen diffusivity in
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
        diffusivity [cm^2.s^-1] : float
        """
        return np.exp(-43073/(R*T))*2.39e-2

    @property
    def correlation_name(self) -> str:
        """
        str : name of the correlation
        """
        return "gromov1996"

    @property
    def range(self) -> List[float]:
        """
        list : temperature validity range for property correlation
        """
        return [473, 1273]


class OxygenDiffusivityGanesan2006b(OxygenDiffusivityInterface):
    """
    Oxygen diffusivity in liquid lead-bismuth eutectic
    property class implementing correlation by ganesan2006b
    """
    @range_warning
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Correlation used to compute oxygen diffusivity in
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
        diffusivity [cm^2.s^-1] : float
        """
        return np.exp(-69069/(R*T))*0.154

    @property
    def correlation_name(self) -> str:
        """
        str : name of the correlation
        """
        return "ganesan2006b"

    @property
    def range(self) -> List[float]:
        """
        list : temperature validity range for property correlation
        """
        return [813, 973]


class IronDiffusivity(PropertyInterface):
    """
    Iron diffusivity in liquid lead-bismuth
    eutectic property class
    """
    @range_warning
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Correlation used to compute iron diffusivity
        in liquid lead-bismuth eutectic

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
        return np.exp((-2.31-2295/T)*np.log(10))

    @property
    def name(self) -> str:
        """
        str : name of the property
        """
        return "fe_dif"

    @property
    def units(self) -> str:
        """
        str : property units
        """
        return "[cm^2.s^-1]"

    @property
    def range(self) -> List[float]:
        """
        list : temperature validity range for property correlation
        """
        return [973.0, 1273.0]

    @property
    def long_name(self) -> str:
        """
        str : property long name
        """
        return "iron diffusivity"

    @property
    def description(self) -> str:
        """
        str : property description
        """
        return "f{self.long_name} in liquid lbe"
