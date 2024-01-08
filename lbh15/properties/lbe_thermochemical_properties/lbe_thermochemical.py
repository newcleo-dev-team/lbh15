"""Module with the definition of the *thermo-chemical*
property objects for *lead-bismuth eutectic* (*lbe*)."""
from typing import List
from typing import Union
import numpy as np
from scipy.constants import atm
from scipy.constants import R
from ..interface import PropertyInterface
from ..lbe_properties import h
from ..._commons import LBE_BOILING_TEMPERATURE as T_b0
from ..._commons import LBE_MELTING_TEMPERATURE as T_m0
from ..._commons import LBE_MOLAR_MASS as M
from ..._commons import OXYGEN_MOLAR_MASS as M_O
from ..._decorators import range_warning


class OxygenPartialPressure(PropertyInterface):
    """
    *Oxygen partial pressure in liquid lbe divided by the
    Oxygen concentration in liquid lbe squared* property class.
    """
    def initialization_helper(self,
                              property_value: float) -> Union[None, float]:
        """
        Returns the temperature guess value according to the value
        of the Oxygen partial pressure in liquid lbe divided by the
        Oxygen concentration in liquid lbe squared passed as argument.
        It is used by the root finder algorithm.

        Parameters
        ----------
        property_value : float
            oxygen partial pressure in liquid lbe divided by the
            oxygen concentration in liquid lbe squared
            in :math:`[atm. /wt.\\%^2]`

        Returns
        -------
        float
            Temperature guess value in :math:`[K]`
        """
        return 1600

    @range_warning
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Returns the value of the *Oxygen partial pressure in liquid lbe
        divided by the Oxygen concentration in liquid lbe squared* by
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
        return np.power(10, 2 / 2.3 / R * (-127398 / T + 27.938))\
            * M * M / M_O / M_O

    @property
    def name(self) -> str:
        """
        str : Name of the property
        """
        return "o_pp"

    @property
    def units(self) -> str:
        """
        str : Oxygen partial pressure in liquid lbe divided by the
        Oxygen concentration in liquid lbe squared unit
        """
        return "[atm.wt.%^-2]"

    @property
    def range(self) -> List[float]:
        """
        List[float] : Temperature validity range of the Oxygen partial
        pressure divided by the Oxygen concentration squared
        correlation function
        """
        return [812, 1008]

    @property
    def long_name(self) -> str:
        """
        str : Oxygen partial pressure in liquid lbe divided by the
        Oxygen concentration in liquid lbe squared long name
        """
        return ("Oxygen partial pressure divided by the"
                " oxygen concentration squared")

    @property
    def description(self) -> str:
        """
        str : Oxygen partial pressure in liquid lbe divided by the
        Oxygen concentration in liquid lbe squared description
        """
        return f"{self.long_name} in liquid lbe"


class LeadChemicalActivity(PropertyInterface):
    """
    *Lead chemical activity* in liquid lbe property class.
    """
    @range_warning
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Returns the value of the *lead chemical activity* in liquid lbe
        by applying the property correlation.

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
            Lead chemical activity in :math:`[-]`
        """
        return 0.42206 - 63.2 / T

    @property
    def name(self) -> str:
        """
        str : Name of the property
        """
        return "pb_a"

    @property
    def units(self) -> str:
        """
        str : Lead chemical activity unit
        """
        return "[-]"

    @property
    def correlation_name(self) -> str:
        """
        str : Name of the correlation
        """
        return "gosse2014"

    @property
    def range(self) -> List[float]:
        """
        List[float] : Temperature validity range of the lead chemical
        activity correlation function
        """
        return [399, 1173]

    @property
    def long_name(self) -> str:
        """
        str : Lead chemical activity long name
        """
        return "lead chemical activity"

    @property
    def description(self) -> str:
        """
        str : Lead chemical activity description
        """
        return f"{self.long_name} in liquid lbe"


class BismuthChemicalActivity(PropertyInterface):
    """
    *Bismuth chemical activity* in liquid lbe property class.
    """
    @range_warning
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Returns the value of the *bismuth chemical activity* in liquid lbe
        by applying the property correlation.

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
            Bismuth chemical activity in :math:`[-]`
        """
        return 0.53381 - 56.2 / T

    @property
    def name(self) -> str:
        """
        str : Name of the property
        """
        return "bi_a"

    @property
    def units(self) -> str:
        """
        str : Bismuth chemical activity unit
        """
        return "[-]"

    @property
    def correlation_name(self) -> str:
        """
        str : Name of the correlation
        """
        return "gosse2014"

    @property
    def range(self) -> List[float]:
        """
        List[float] : Temperature validity range of the bismuth chemical
        activity correlation function
        """
        return [399, 1173]

    @property
    def long_name(self) -> str:
        """
        str : Bismuth chemical activity long name
        """
        return "Bismuth chemical activity"

    @property
    def description(self) -> str:
        """
        str : Bismuth chemical activity description
        """
        return f"{self.long_name} in liquid lbe"


class MolarEnthalpy(PropertyInterface):
    """
    Liquid lbe *molar enthalpy variation* property class.
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
        return [400.0, T_b0]

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
        return f"{self.long_name} in liquid lbe"


class MolarEntropy(PropertyInterface):
    """
    Liquid lbe *molar entropy variation* property class.
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
        return M / 1000 * (164.8 * np.log(T / T_m0)
                           - 3.94e-2 * (T - T_m0)
                           + 6.25e-6 * (T * T - T_m0 * T_m0)
                           + 2.28e5 * (1 / T / T - 1 / T_m0 / T_m0))

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
        return [400, T_b0]

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
        return f"{self.long_name} in liquid lbe"


class GibbsFreeEnergy(PropertyInterface):
    """
    Liquid lbe *Gibbs free energy variation* property class.
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
        return [400, T_b0]

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
        return f"{self.long_name} in liquid lbe"
