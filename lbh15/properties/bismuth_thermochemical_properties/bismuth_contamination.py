"""Module with the definition of some coumpounds properties
for contamination assessment"""
from typing import List
from scipy.constants import atm
import numpy as np
from ..interface import PropertyInterface
from ..._decorators import range_warning
from ..._commons import BISMUTH_MELTING_TEMPERATURE as T_m0
from ..._commons import BISMUTH_BOILING_TEMPERATURE as T_b0


class BismuthPoloniumActivityCoefficientInterface(PropertyInterface):
    """
    Liquid bismuth *dilute Polonium activity coefficient*
    abstract class.
    """
    @property
    def name(self) -> str:
        """
        str : Name of the property
        """
        return "gamma_Po"

    @property
    def units(self) -> str:
        """
        str : Activity coefficient unit
        """
        return "[-]"

    @property
    def long_name(self) -> str:
        """
        str : Polonium activity coefficient long name
        """
        return "Activity coefficient of Polonium"

    @property
    def description(self) -> str:
        """
        str : Polonium activity coefficient description
        """
        return f"{self.long_name} in liquid bismuth"


class BismuthPoloniumActivityCoefficientJoy1963\
        (BismuthPoloniumActivityCoefficientInterface):
    """
    Liquid bismuth *dilute Polonium activity coefficient* property class
    implementing the correlation by *joy1963*.
    """
    @range_warning
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Returns the value of the *dilute Polonium activity coefficient* by
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
            activity coefficient in :math:`[-]`
        """
        return np.power(10, - 2728.3 / T + 1.1176)

    @property
    def correlation_name(self) -> str:
        """
        str : Name of the correlation
        """
        return "joy1963"

    @property
    def range(self) -> List[float]:
        """
        List[float] : Temperature validity range of the dilute Polonium
        activity coefficient correlation function
        """
        return [723.0, 1123.0]


class BismuthPoloniumActivityCoefficient\
        (BismuthPoloniumActivityCoefficientInterface):
    """
    Liquid bismuth *dilute Polonium activity coefficient* property class
    implementing the correlation by *lbh15*.
    """
    @range_warning
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Returns the value of the *dilute Polonium activity coefficient* by
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
            activity coefficient in :math:`[-]`
        """
        return np.power(10, - 2272.7 / T + 0.1316)

    @property
    def range(self) -> List[float]:
        """
        List[float] : Temperature validity range of the dilute Polonium
        activity coefficient correlation function
        """
        return [923.0, 1038.0]


class BismuthIodineVapourPressureCubicciotti1959(PropertyInterface):
    """
    Liquid bismuth *BiI3 Iodide compound vapour pressure* property class
    implementing the correlation by *cubicciotti1959*.
    """
    @range_warning
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Returns the value of the *BiI3 Iodide compound vapour pressure* by
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
        return np.power(10, - 4310 / T + 10.29)

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
        str : BiI3 Iodide vapour pressure long name
        """
        return "Vapour pressure of BiI3 Iodide"

    @property
    def description(self) -> str:
        """
        str : BiI3 Iodide vapour pressure description
        """
        return f"{self.long_name} in liquid bismuth"

    @property
    def range(self) -> List[float]:
        """
        List[float] : Temperature validity range of the BiI3 Iodide
        vapour pressure correlation function
        """
        return [682.0, T_b0]


class BismuthCaesiumActivityCoefficientGverdtsiteli1984(PropertyInterface):
    """
    Liquid bismuth *Caesium intermetallic compounds activity coefficient*
    property class implementing the correlation by *gverdtsiteli1984*.
    """
    @range_warning
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Returns the value of the *Caesium intermetallic compounds
        activity coefficient* by applying the property correlation.

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
            activity coefficient in :math:`[-]`
        """
        return np.power(10, -2.5)

    @property
    def name(self) -> str:
        """
        str : Name of the property
        """
        return "gamma_Cs"

    @property
    def correlation_name(self) -> str:
        """
        str : Name of the correlation
        """
        return "gverdtsiteli1984"

    @property
    def units(self) -> str:
        """
        str : Activity coefficient unit
        """
        return "[-]"

    @property
    def long_name(self) -> str:
        """
        str : Caesium intermetallic compounds activity coefficient long name
        """
        return "Activity coefficient of Caesium intermetallic compounds"

    @property
    def description(self) -> str:
        """
        str : Caesium intermetallic compounds activity coefficient description
        """
        return f"{self.long_name} in liquid bismuth"

    @property
    def range(self) -> List[float]:
        """
        List[float] : Temperature validity range of the Caesium intermetallic
        compounds activity coefficient correlation function
        """
        return [T_m0, 1000]
