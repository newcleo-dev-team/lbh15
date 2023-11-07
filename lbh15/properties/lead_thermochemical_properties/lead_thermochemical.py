"""Module with the definition of thermochemical property
objects for lead"""
from typing import List
from typing import Union
import numpy as np
from scipy.constants import atm
from scipy.constants import R
from lbh15.properties.interface import PropertyInterface
from lbh15.properties.interface import range_warning
from ..lead_properties import h
from ..._commons import LEAD_MELTING_TEMPERATURE as T_m0
from ..._commons import LEAD_MOLAR_MASS as M
from ..._commons import OXYGEN_MOLAR_MASS as M_O
from ..._decorators import typecheck_for_method


class OxygenPartialPressureInterface(PropertyInterface):
    """
    Oxygen partial pressure in liquid lead divided by the
    oxygen concentration in liquid lead squared property class
    """
    @typecheck_for_method
    def initialization_helper(self,
                              property_value: float) -> Union[None, float]:
        """
        Returns a temperature guess according to the value
        of the oxygen partial pressure in liquid lead divided by the
        oxygen concentration in liquid lead squared

        Parameters
        ----------
        property_value : float
            oxygen partial pressure in liquid lead divided by the
            oxygen concentration in liquid lead squared in [atm.wt.%^-2]
        verbose : bool, optional
            True to tell decorator to print warning about
            range check failing, False otherwise. By default False

        Returns
        -------
        rvalue : float
            Temperature guess in [K]
        """
        if property_value < 1e-4:
            return 650
        return 1500

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
        return f"{self.long_name} in liquid lead"


class OxygenPartialPressureOtsuka1979(OxygenPartialPressureInterface):
    """
    Oxygen partial pressure in liquid lead divided by the
    oxygen concentration in liquid lead squared property
    class implementing correlation by otsuka1979
    """
    @range_warning
    @typecheck_for_method
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Correlation used to compute oxygen partial pressure in liquid
        lead divided by the oxygen concentration in liquid lead squared

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
        return np.power(10, 2 / 2.3 / R * (-118600 / T + 14.1))\
            * M * M / M_O / M_O

    @property
    def correlation_name(self) -> str:
        """
        str : name of the correlation
        """
        return "otsuka1979"

    @property
    def range(self) -> List[float]:
        """
        list : temperature validity range for property correlation
        """
        return [1073, 1673]


class OxygenPartialPressureOtsuka1981(OxygenPartialPressureInterface):
    """
    Oxygen partial pressure in liquid lead divided by the
    oxygen concentration in liquid lead squared property
    class implementing correlation by otsuka1981
    """
    @range_warning
    @typecheck_for_method
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Correlation used to compute oxygen partial pressure in liquid
        lead divided by the oxygen concentration in liquid lead squared

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
        return np.power(10, 2 / 2.3 / R * (-117170 / T + 12.9))\
            * M * M / M_O / M_O

    @property
    def correlation_name(self) -> str:
        """
        str : name of the correlation
        """
        return "otsuka1981"

    @property
    def range(self) -> List[float]:
        """
        list : temperature validity range for property correlation
        """
        return [1023, 1273]


class OxygenPartialPressureGanesan2006(OxygenPartialPressureInterface):
    """
    Oxygen partial pressure in liquid lead divided by the
    oxygen concentration in liquid lead squared property
    class implementing correlation by ganesan2006
    """
    @range_warning
    @typecheck_for_method
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Correlation used to compute oxygen partial pressure in liquid
        lead divided by the oxygen concentration in liquid lead squared

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
        return np.power(10, 2 / 2.3 / R * (-121349 / T + 16.906))\
            * M * M / M_O / M_O

    @property
    def correlation_name(self) -> str:
        """
        str : name of the correlation
        """
        return "ganesan2006"

    @property
    def range(self) -> List[float]:
        """
        list : temperature validity range for property correlation
        """
        return [815, 1090]


class OxygenPartialPressureAlcock1964(OxygenPartialPressureInterface):
    """
    Oxygen partial pressure in liquid lead divided by the
    oxygen concentration in liquid lead squared property
    class implementing correlation by alcock1964
    """
    @range_warning
    @typecheck_for_method
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Correlation used to compute oxygen partial pressure in liquid
        lead divided by the oxygen concentration in liquid lead squared

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
        return np.power(10, 2 / 2.3 / R * (-119411 / T + 12.222))\
            * M * M / M_O / M_O

    @property
    def correlation_name(self) -> str:
        """
        str : name of the correlation
        """
        return "alcock1964"

    @property
    def range(self) -> List[float]:
        """
        list : temperature validity range for property correlation
        """
        return [783, 973]


class OxygenPartialPressureSzwarc1972(OxygenPartialPressureInterface):
    """
    Oxygen partial pressure in liquid lead divided by the
    oxygen concentration in liquid lead squared property
    class implementing correlation by szwarc1972
    """
    @range_warning
    @typecheck_for_method
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Correlation used to compute oxygen partial pressure in liquid
        lead divided by the oxygen concentration in liquid lead squared

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
        return np.power(10, 2 / 2.3 / R * (-105855 / T + 18.661))\
            * M * M / M_O / M_O

    @property
    def correlation_name(self) -> str:
        """
        str : name of the correlation
        """
        return "szwarc1972"

    @property
    def range(self) -> List[float]:
        """
        list : temperature validity range for property correlation
        """
        return [1012, 1353]


class OxygenPartialPressureCharle1976(OxygenPartialPressureInterface):
    """
    Oxygen partial pressure in liquid lead divided by the
    oxygen concentration in liquid lead squared property
    class implementing correlation by charle1976
    """
    @range_warning
    @typecheck_for_method
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Correlation used to compute oxygen partial pressure in liquid
        lead divided by the oxygen concentration in liquid lead squared

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
        return np.power(10, 2 / 2.3 / R * (-119840 / T + 15.794))\
            * M * M / M_O / M_O

    @property
    def correlation_name(self) -> str:
        """
        str : name of the correlation
        """
        return "charle1976"

    @property
    def range(self) -> List[float]:
        """
        list : temperature validity range for property correlation
        """
        return [1173, 1373]


class OxygenPartialPressureIsecke1977(OxygenPartialPressureInterface):
    """
    Oxygen partial pressure in liquid lead divided by the
    oxygen concentration in liquid lead squared property
    class implementing correlation by isecke1977
    """
    @range_warning
    @typecheck_for_method
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Correlation used to compute oxygen partial pressure in liquid
        lead divided by the oxygen concentration in liquid lead squared

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
        return np.power(10, 2 / 2.3 / R * (-120376 / T + 16.255))\
            * M * M / M_O / M_O

    @property
    def correlation_name(self) -> str:
        """
        str : name of the correlation
        """
        return "isecke1977"

    @property
    def range(self) -> List[float]:
        """
        list : temperature validity range for property correlation
        """
        return [1173, 1373]


class OxygenPartialPressureTaskinen1979(OxygenPartialPressureInterface):
    """
    Oxygen partial pressure in liquid lead divided by the
    oxygen concentration in liquid lead squared property
    class implementing correlation by taskinen1979
    """
    @range_warning
    @typecheck_for_method
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Correlation used to compute oxygen partial pressure in liquid
        lead divided by the oxygen concentration in liquid lead squared

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
        return np.power(10, 2 / 2.3 / R * (-116717 / T + 12.699))\
            * M * M / M_O / M_O

    @property
    def correlation_name(self) -> str:
        """
        str : name of the correlation
        """
        return "taskinen1979"

    @property
    def range(self) -> List[float]:
        """
        list : temperature validity range for property correlation
        """
        return [1073, 1203]


class OxygenPartialPressureFisher1966(OxygenPartialPressureInterface):
    """
    Oxygen partial pressure in liquid lead divided by the
    oxygen concentration in liquid lead squared property
    class implementing correlation by fisher1966
    """
    @range_warning
    @typecheck_for_method
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Correlation used to compute oxygen partial pressure in liquid
        lead divided by the oxygen concentration in liquid lead squared

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
        return np.power(10, 2 / 2.3 / R * (-106395 / T + 10.254))\
            * M * M / M_O / M_O

    @property
    def correlation_name(self) -> str:
        """
        str : name of the correlation
        """
        return "fisher1966"

    @property
    def range(self) -> List[float]:
        """
        list : temperature validity range for property correlation
        """
        return [903, 1253]


class MolarEnthalpy(PropertyInterface):
    """
    Liquid lead molar enthalpy variation
    property class
    """
    @range_warning
    @typecheck_for_method
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Correlation used to compute molar enthalpy variation
        in liquid lead

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
        return [T_m0, 2000]

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
        return f"{self.long_name} in liquid lead"


class MolarEntropy(PropertyInterface):
    """
    Liquid lead molar entropy variation
    property class
    """
    @range_warning
    @typecheck_for_method
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Correlation used to compute molar entropy
        variation in liquid lead. Heat capacity correlation
        by Sobolev2011 is adopted

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
        return M / 1000 * (176.2 * np.log(T / T_m0)
                           - 4.923e-2 * (T - T_m0)
                           + 1.544e-5 / 2 * (T * T - T_m0 * T_m0)
                           + 1.524e6 / 2 * (1 / T / T - 1 / T_m0 / T_m0))

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
        return [T_m0, 2000]

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
        return f"{self.long_name} in liquid lead"


class GibbsFreeEnergy(PropertyInterface):
    """
    Liquid lead Gibbs free energy variation
    property class
    """
    @range_warning
    @typecheck_for_method
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Correlation used to compute Gibbs free energy
        variation in liquid lead. Heat capacity correlation
        by Sobolev2011 is adopted

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
        return [T_m0, 2000]

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
        return f"{self.long_name} in liquid lead"
