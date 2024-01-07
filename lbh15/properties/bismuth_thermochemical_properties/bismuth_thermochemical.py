"""Module with the definition of the *thermo-chemical*
property objects for *bismuth*."""
from typing import List
from typing import Union
import numpy as np
from scipy.constants import atm
from scipy.constants import R
from ..interface import PropertyInterface
from ..bismuth_properties import h
from ..._commons import BISMUTH_BOILING_TEMPERATURE as T_b0
from ..._commons import BISMUTH_MELTING_TEMPERATURE as T_m0
from ..._commons import BISMUTH_MOLAR_MASS as M
from ..._commons import OXYGEN_MOLAR_MASS as M_O
from ..._decorators import range_warning


class OxygenPartialPressureInterface(PropertyInterface):
    """
    *Oxygen partial pressure in liquid bismuth divided by the
    Oxygen concentration in liquid bismuth squared* property abstract class.
    """
    def initialization_helper(self,
                              property_value: float) -> Union[None, float]:
        """
        Returns the temperature guess value according to the value
        of the Oxygen partial pressure in liquid bismuth divided by the
        Oxygen concentration in liquid bismuth squared passed as argument.
        It is used by the root finder algorithm.

        Parameters
        ----------
        property_value : float
            oxygen partial pressure in liquid bismuth divided by the
            oxygen concentration in liquid bismuth squared
            in :math:`[atm. /wt.\\%^2]`

        Returns
        -------
        float
            Temperature guess value in :math:`[K]`
        """
        if property_value < 1e-4:
            return 1200
        return 1500

    @property
    def name(self) -> str:
        """
        str : Name of the property
        """
        return "o_pp"

    @property
    def units(self) -> str:
        """
        str : Oxygen partial pressure in liquid bismuth divided by the
        Oxygen concentration in liquid bismuth squared unit
        """
        return "[atm.wt.%^-2]"

    @property
    def long_name(self) -> str:
        """
        str : Oxygen partial pressure in liquid bismuth divided by the
        Oxygen concentration in liquid bismuth squared long name
        """
        return ("Oxygen partial pressure divided by the"
                " oxygen concentration squared")

    @property
    def description(self) -> str:
        """
        str : Oxygen partial pressure in liquid bismuth divided by the
        Oxygen concentration in liquid bismuth squared description
        """
        return f"{self.long_name} in liquid bismuth"


class OxygenPartialPressureFitzner1980(OxygenPartialPressureInterface):
    """
    *Oxygen partial pressure in liquid bismuth divided by the
    Oxygen concentration in liquid bismuth squared* property class
    implementing the correlation by *fitzner1980*.
    """
    @range_warning
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Returns the value of the *Oxygen partial pressure in liquid bismuth
        divided by the Oxygen concentration in liquid bismuth squared* by
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
            Oxygen partial pressure divided by Oxygen concentration
            squared in :math:`[atm. / wt.\\%^2]`
        """
        return np.power(10, 2 / 2.3 / R * (-95502 / T + 9.69))\
            * M * M / M_O / M_O

    @property
    def correlation_name(self) -> str:
        """
        str : Name of the correlation
        """
        return "fitzner1980"

    @property
    def range(self) -> List[float]:
        """
        List[float] : Temperature validity range of the Oxygen partial
        pressure divided by the Oxygen concentration squared
        correlation function
        """
        return [988, 1181]


class OxygenPartialPressureIsecke1979(OxygenPartialPressureInterface):
    """
    *Oxygen partial pressure in liquid bismuth divided by the
    Oxygen concentration in liquid bismuth squared* property class
    implementing the correlation by *isecke1979*.
    """
    @range_warning
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Returns the value of the *Oxygen partial pressure in liquid bismuth
        divided by the Oxygen concentration in liquid bismuth squared* by
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
            Oxygen partial pressure divided by Oxygen concentration
            squared in :math:`[atm. / wt.\\%^2]`
        """
        return np.power(10, 2 / 2.3 / R * (-101098 / T + 15.66))\
            * M * M / M_O / M_O

    @property
    def correlation_name(self) -> str:
        """
        str : Name of the correlation
        """
        return "isecke1979"

    @property
    def range(self) -> List[float]:
        """
        List[float] : Temperature validity range of the Oxygen partial
        pressure divided by the Oxygen concentration squared
        correlation function
        """
        return [973, 1473]


class OxygenPartialPressureHahn1979(OxygenPartialPressureInterface):
    """
    *Oxygen partial pressure in liquid bismuth divided by the
    Oxygen concentration in liquid bismuth squared* property class
    implementing the correlation by *hahn1979*.
    """
    @range_warning
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Returns the value of the *Oxygen partial pressure in liquid bismuth
        divided by the Oxygen concentration in liquid bismuth squared* by
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
            Oxygen partial pressure divided by Oxygen concentration
            squared in :math:`[atm. / wt.\\%^2]`
        """
        return np.power(10, 2 / 2.3 / R * (-68156 / T + 14.14))\
            * M * M / M_O / M_O

    @property
    def correlation_name(self) -> str:
        """
        str : Name of the correlation
        """
        return "hahn1979"

    @property
    def range(self) -> List[float]:
        """
        List[float] : Temperature validity range of the Oxygen partial
        pressure divided by the Oxygen concentration squared
        correlation function
        """
        return [1073, 1223]


class OxygenPartialPressureHeshmatpour1981(OxygenPartialPressureInterface):
    """
    *Oxygen partial pressure in liquid bismuth divided by the
    Oxygen concentration in liquid bismuth squared* property class
    implementing the correlation by *heshmatpour1981*.
    """
    @range_warning
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Returns the value of the *Oxygen partial pressure in liquid bismuth
        divided by the Oxygen concentration in liquid bismuth squared* by
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
            Oxygen partial pressure divided by Oxygen concentration
            squared in :math:`[atm. / wt.\\%^2]`
        """
        return np.power(10, 2 / 2.3 / R * (-95437 / T + 3.78))\
            * M * M / M_O / M_O

    @property
    def correlation_name(self) -> str:
        """
        str : Name of the correlation
        """
        return "heshmatpour1981"

    @property
    def range(self) -> List[float]:
        """
        List[float] : Temperature validity range of the Oxygen partial
        pressure divided by the Oxygen concentration squared
        correlation function
        """
        return [1023, 1273]


class MolarEnthalpy(PropertyInterface):
    """
    Liquid bismuth *molar enthalpy variation* property class.
    """
    @range_warning
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Returns the value of the *molar enthalpy variation* by
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
            molar enthalpy in :math:`[J/mol]`
        """
        return h().correlation(T, p) * M / 1000

    @property
    def name(self) -> str:
        """
        str : Name of the property
        """
        return "H"

    @property
    def units(self) -> str:
        """
        str : Molar enthalpy variation unit
        """
        return "[J.mol^-1]"

    @property
    def range(self) -> List[float]:
        """
        List[float] : Temperature validity range of the molar enthalpy
        variation correlation function
        """
        return [T_m0, T_b0]

    @property
    def long_name(self) -> str:
        """
        str : Molar enthalpy variation long name
        """
        return "molar enthalpy variation"

    @property
    def description(self) -> str:
        """
        str : Molar enthalpy variation description
        """
        return f"{self.long_name} in liquid bismuth"


class MolarEntropy(PropertyInterface):
    """
    Liquid bismuth *molar entropy variation* property class.
    """
    @range_warning
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Returns the value of the *molar entropy variation* by
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
            molar entropy in :math:`[J/(mol \\cdot K)]`
        """
        return M / 1000 * (118.2 * np.log(T / T_m0)
                           + 5.934e-3 * (T - T_m0)
                           - 7.183e6 / 2 * (1 / T / T - 1 / T_m0 / T_m0))

    @property
    def name(self) -> str:
        """
        str : Name of the property
        """
        return "S"

    @property
    def units(self) -> str:
        """
        str : Molar entropy variation unit
        """
        return "[J/(mol.K)]"

    @property
    def range(self) -> List[float]:
        """
        List[float] : Temperature validity range of the molar entropy
        variation correlation function
        """
        return [T_m0, T_b0]

    @property
    def long_name(self) -> str:
        """
        str : Molar entropy variation long name
        """
        return "molar entropy variation"

    @property
    def description(self) -> str:
        """
        str : Molar entropy variation description
        """
        return f"{self.long_name} in liquid bismuth"


class GibbsFreeEnergy(PropertyInterface):
    """
    Liquid bismuth *Gibbs free energy variation* property class.
    """
    @range_warning
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Returns the value of the *Gibbs free energy variation* by
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
            Gibbs free energy in :math:`[J/mol]`
        """
        return MolarEnthalpy().correlation(T, p)\
            - T * MolarEntropy().correlation(T, p)

    @property
    def name(self) -> str:
        """
        str : Name of the property
        """
        return "G"

    @property
    def units(self) -> str:
        """
        str : Gibbs free energy unit
        """
        return "[J/mol]"

    @property
    def range(self) -> List[float]:
        """
        List[float] : Temperature validity range of the Gibbs free energy
        variation correlation function
        """
        return [T_m0, T_b0]

    @property
    def long_name(self) -> str:
        """
        str : Gibbs free energy long name
        """
        return "Gibbs free energy variation"

    @property
    def description(self) -> str:
        """
        str : Gibbs free energy description
        """
        return f"{self.long_name} in liquid bismuth"
