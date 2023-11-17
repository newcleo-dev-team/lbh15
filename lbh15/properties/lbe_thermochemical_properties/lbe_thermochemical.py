"""Module with the definition of thermochemical
property objects for lead-bismuth eutectic"""
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
from ..._decorators import typecheck_for_method


class OxygenPartialPressure(PropertyInterface):
    """
    Oxygen partial pressure in liquid lead-bismuth eutectic
    divided by the oxygen concentration in liquid
    lead-bismuth eutectic squared property class
    """
    @typecheck_for_method
    def initialization_helper(self,
                              property_value: float) -> Union[None, float]:
        """
        Returns a temperature guess according to the value
        of the oxygen partial pressure in liquid lead-bismuth eutectic
        divided by the oxygen concentration in liquid
        lead-bismuth eutectic squared

        Parameters
        ----------
        property_value : float
            oxygen partial pressure in liquid lead-bismuth eutectic
            divided by the oxygen concentration in liquid
            lead-bismuth eutectic squared in [atm.wt.%^-2]
        verbose : bool, optional
            True to tell decorator to print warning about
            range check failing, False otherwise. By default False

        Returns
        -------
        rvalue : float
            Temperature guess in [K]
        """
        if property_value < 1e-3:
            return 650
        return 1500

    @range_warning
    @typecheck_for_method
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Correlation used to compute oxygen partial pressure
        in liquid lead-bismuth eutectic divided by the oxygen
        concentration in liquid lead-bismuth eutectic squared

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
        partial pressure divided by concentration
        squared [atm.wt.%^-2] : float
        """
        return np.power(10, 2 / 2.3 / R * (-127398 / T + 27.938))\
            * M * M / M_O / M_O

    @property
    def name(self) -> str:
        """
        str : name of the property
        """
        return "o_pp"

    @property
    def units(self) -> str:
        """
        str : property units
        """
        return "[atm.wt.%^-2]"

    @property
    def range(self) -> List[float]:
        """
        list : temperature validity range for property correlation
        """
        return [812, 1008]

    @property
    def long_name(self) -> str:
        """
        str : property long name
        """
        return ("Oxygen partial pressure divided by the"
                " oxygen concentration squared")

    @property
    def description(self) -> str:
        """
        str : property description
        """
        return f"{self.long_name} in liquid lbe"


class LeadChemicalActivity(PropertyInterface):
    """
    Lead chemical activity in liquid lead-bismuth eutectic
    property class
    """
    @range_warning
    @typecheck_for_method
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Correlation used to compute lead chemical activity
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
        chemical activity [-] : float
        """
        return 0.42206 - 63.2 / T

    @property
    def name(self) -> str:
        """
        str : name of the property
        """
        return "pb_a"

    @property
    def units(self) -> str:
        """
        str : property units
        """
        return "[-]"

    @property
    def correlation_name(self) -> str:
        """
        str : name of the correlation
        """
        return "gosse2014"

    @property
    def range(self) -> List[float]:
        """
        list : temperature validity range for property correlation
        """
        return [399, 1173]

    @property
    def long_name(self) -> str:
        """
        str : property long name
        """
        return "lead chemical activity"

    @property
    def description(self) -> str:
        """
        str : property description
        """
        return f"{self.long_name} in liquid lbe"


class BismuthChemicalActivity(PropertyInterface):
    """
    Bismuth chemical activity in liquid lead-bismuth eutectic
    property class
    """
    @range_warning
    @typecheck_for_method
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Correlation used to compute Bismuth chemical activity
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
        chemical activity [-] : float
        """
        return 0.53381 - 56.2 / T

    @property
    def name(self) -> str:
        """
        str : name of the property
        """
        return "bi_a"

    @property
    def units(self) -> str:
        """
        str : property units
        """
        return "[-]"

    @property
    def correlation_name(self) -> str:
        """
        str : name of the correlation
        """
        return "gosse2014"

    @property
    def range(self) -> List[float]:
        """
        list : temperature validity range for property correlation
        """
        return [399, 1173]

    @property
    def long_name(self) -> str:
        """
        str : property long name
        """
        return "Bismuth chemical activity"

    @property
    def description(self) -> str:
        """
        str : property description
        """
        return f"{self.long_name} in liquid lbe"


class MolarEnthalpy(PropertyInterface):
    """
    Liquid lead-bismuth eutectic molar
    enthalpy variation property class
    """
    @range_warning
    @typecheck_for_method
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Correlation used to compute molar enthalpy variation
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
        molar enthalpy [J/mol] : float
        """
        return h().correlation(T, p) * M / 1000

    @property
    def name(self) -> str:
        """
        str : name of the property
        """
        return "H"

    @property
    def units(self) -> str:
        """
        str : property units
        """
        return "[J.mol^-1]"

    @property
    def range(self) -> List[float]:
        """
        list : temperature validity range for property correlation
        """
        return [400.0, T_b0]

    @property
    def long_name(self) -> str:
        """
        str : property long name
        """
        return "molar enthalpy variation"

    @property
    def description(self) -> str:
        """
        str : property description
        """
        return f"{self.long_name} in liquid lbe"


class MolarEntropy(PropertyInterface):
    """
    Liquid lead-bismuth eutectic molar
    entropy variation property class
    """
    @range_warning
    @typecheck_for_method
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Correlation used to compute molar entropy
        variation in liquid lead-bismuth eutectic

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
        molar entropy [J/(mol*K)] : float
        """
        return M / 1000 * (164.8 * np.log(T / T_m0)
                           - 3.94e-2 * (T - T_m0)
                           + 6.25e-6 * (T * T - T_m0 * T_m0)
                           + 2.28e5 * (1 / T / T - 1 / T_m0 / T_m0))

    @property
    def name(self) -> str:
        """
        str : name of the property
        """
        return "S"

    @property
    def units(self) -> str:
        """
        str : property units
        """
        return "[J/(mol.K)]"

    @property
    def range(self) -> List[float]:
        """
        list : temperature validity range for property correlation
        """
        return [400, T_b0]

    @property
    def long_name(self) -> str:
        """
        str : property long name
        """
        return "molar entropy variation"

    @property
    def description(self) -> str:
        """
        str : property description
        """
        return f"{self.long_name} in liquid lbe"


class GibbsFreeEnergy(PropertyInterface):
    """
    Liquid lead-bimuth eutectic Gibbs free
    energy variation property class
    """
    @range_warning
    @typecheck_for_method
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Correlation used to compute Gibbs free energy
        variation in liquid lead-bismuth eutectic

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
        gibbs free energy [J/mol] : float
        """
        return MolarEnthalpy().correlation(T, p)\
            - T * MolarEntropy().correlation(T, p)

    @property
    def name(self) -> str:
        """
        str : name of the property
        """
        return "G"

    @property
    def units(self) -> str:
        """
        str : property units
        """
        return "[J/mol]"

    @property
    def range(self) -> List[float]:
        """
        list : temperature validity range for property correlation
        """
        return [400, T_b0]

    @property
    def long_name(self) -> str:
        """
        str : property long name
        """
        return "Gibbs free energy variation"

    @property
    def description(self) -> str:
        """
        str : property description
        """
        return f"{self.long_name} in liquid lbe"
