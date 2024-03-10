"""Module with the definition of the *thermo-chemical*
property objects for *lead*."""
from typing import List
from typing import Union
import numpy as np
from scipy.constants import atm
from scipy.constants import R
from lbh15.properties.common_interface import OxygenPartialPressureInterface
from lbh15.properties.common_interface import MolarEnthalpyInterface
from lbh15.properties.common_interface import MolarEntropyInterface
from lbh15.properties.common_interface import GibbsFreeEnergyInterface
from ..lead_properties import h
from ..._commons import LEAD_MELTING_TEMPERATURE as T_m0
from ..._commons import LEAD_MOLAR_MASS as M
from ..._commons import OXYGEN_MOLAR_MASS as M_O
from ..._decorators import range_warning


class LeadOxygenPartialPressureInterface(OxygenPartialPressureInterface):
    """
    *Oxygen partial pressure in liquid lead divided by the
    Oxygen concentration in liquid lead squared* property abstract class.
    """
    def initialization_helper(self,
                              property_value: float) -> Union[None, float]:
        """
        Returns the temperature guess value according to the value
        of the Oxygen partial pressure in liquid lead divided by the
        Oxygen concentration in liquid lead squared passed as argument.
        It is used by the root finder algorithm.

        Parameters
        ----------
        property_value : float
            oxygen partial pressure in liquid lead divided by the
            oxygen concentration in liquid lead squared
            in :math:`[Pa /wt.\\%^2]`

        Returns
        -------
        float
            Temperature guess value in :math:`[K]`
        """
        return 1600

    @property
    def description(self) -> str:
        """
        str : Oxygen partial pressure in liquid lead divided by the
        Oxygen concentration in liquid lead squared description
        """
        return f"{self.long_name} in liquid lead"


class OxygenPartialPressureOtsuka1979(LeadOxygenPartialPressureInterface):
    """
    *Oxygen partial pressure in liquid lead divided by the
    Oxygen concentration in liquid lead squared* property class
    implementing the correlation by *otsuka1979*.
    """
    @range_warning
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Returns the value of the *Oxygen partial pressure in liquid lead
        divided by the Oxygen concentration in liquid lead squared* by
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
            squared in :math:`[Pa / wt.\\%^2]`
        """
        return np.power(10, 2 / 2.3 / R * (-118600 / T + 14.1))\
            * M * M / M_O / M_O * 101325

    @property
    def correlation_name(self) -> str:
        """
        str : Name of the correlation
        """
        return "otsuka1979"

    @property
    def range(self) -> List[float]:
        """
        List[float] : Temperature validity range of the Oxygen partial
        pressure divided by the Oxygen concentration squared
        correlation function
        """
        return [1073, 1673]


class OxygenPartialPressureOtsuka1981(LeadOxygenPartialPressureInterface):
    """
    *Oxygen partial pressure in liquid lead divided by the
    Oxygen concentration in liquid lead squared* property class
    implementing the correlation by *otsuka1981*.
    """
    @range_warning
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Returns the value of the *Oxygen partial pressure in liquid lead
        divided by the Oxygen concentration in liquid lead squared* by
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
            squared in :math:`[Pa / wt.\\%^2]`
        """
        return np.power(10, 2 / 2.3 / R * (-117170 / T + 12.9))\
            * M * M / M_O / M_O * 101325

    @property
    def correlation_name(self) -> str:
        """
        str : Name of the correlation
        """
        return "otsuka1981"

    @property
    def range(self) -> List[float]:
        """
        List[float] : Temperature validity range of the Oxygen partial
        pressure divided by the Oxygen concentration squared
        correlation function
        """
        return [1023, 1273]


class OxygenPartialPressureGanesan2006(LeadOxygenPartialPressureInterface):
    """
    *Oxygen partial pressure in liquid lead divided by the
    Oxygen concentration in liquid lead squared* property class
    implementing the correlation by *ganesan2006*.
    """
    @range_warning
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Returns the value of the *Oxygen partial pressure in liquid lead
        divided by the Oxygen concentration in liquid lead squared* by
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
            squared in :math:`[Pa / wt.\\%^2]`
        """
        return np.power(10, 2 / 2.3 / R * (-121349 / T + 16.906))\
            * M * M / M_O / M_O * 101325

    @property
    def correlation_name(self) -> str:
        """
        str : Name of the correlation
        """
        return "ganesan2006"

    @property
    def range(self) -> List[float]:
        """
        List[float] : Temperature validity range of the Oxygen partial
        pressure divided by the Oxygen concentration squared
        correlation function
        """
        return [815, 1090]


class OxygenPartialPressureAlcock1964(LeadOxygenPartialPressureInterface):
    """
    *Oxygen partial pressure in liquid lead divided by the
    Oxygen concentration in liquid lead squared* property class
    implementing the correlation by *alcock1964*.
    """
    @range_warning
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Returns the value of the *Oxygen partial pressure in liquid lead
        divided by the Oxygen concentration in liquid lead squared* by
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
            squared in :math:`[Pa / wt.\\%^2]`
        """
        return np.power(10, 2 / 2.3 / R * (-119411 / T + 12.222))\
            * M * M / M_O / M_O * 101325

    @property
    def correlation_name(self) -> str:
        """
        str : Name of the correlation
        """
        return "alcock1964"

    @property
    def range(self) -> List[float]:
        """
        List[float] : Temperature validity range of the Oxygen partial
        pressure divided by the Oxygen concentration squared
        correlation function
        """
        return [783, 973]


class OxygenPartialPressureSzwarc1972(LeadOxygenPartialPressureInterface):
    """
    *Oxygen partial pressure in liquid lead divided by the
    Oxygen concentration in liquid lead squared* property class
    implementing the correlation by *szwarc1972*.
    """
    @range_warning
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Returns the value of the *Oxygen partial pressure in liquid lead
        divided by the Oxygen concentration in liquid lead squared* by
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
            squared in :math:`[Pa / wt.\\%^2]`
        """
        return np.power(10, 2 / 2.3 / R * (-105855 / T + 18.661))\
            * M * M / M_O / M_O * 101325

    @property
    def correlation_name(self) -> str:
        """
        str : Name of the correlation
        """
        return "szwarc1972"

    @property
    def range(self) -> List[float]:
        """
        List[float] : Temperature validity range of the Oxygen partial
        pressure divided by the Oxygen concentration squared
        correlation function
        """
        return [1012, 1353]


class OxygenPartialPressureCharle1976(LeadOxygenPartialPressureInterface):
    """
    *Oxygen partial pressure in liquid lead divided by the
    Oxygen concentration in liquid lead squared* property class
    implementing the correlation by *charle1976*.
    """
    @range_warning
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Returns the value of the *Oxygen partial pressure in liquid lead
        divided by the Oxygen concentration in liquid lead squared* by
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
            squared in :math:`[Pa / wt.\\%^2]`
        """
        return np.power(10, 2 / 2.3 / R * (-119840 / T + 15.794))\
            * M * M / M_O / M_O * 101325

    @property
    def correlation_name(self) -> str:
        """
        str : Name of the correlation
        """
        return "charle1976"

    @property
    def range(self) -> List[float]:
        """
        List[float] : Temperature validity range of the Oxygen partial
        pressure divided by the Oxygen concentration squared
        correlation function
        """
        return [1173, 1373]


class OxygenPartialPressureIsecke1977(LeadOxygenPartialPressureInterface):
    """
    *Oxygen partial pressure in liquid lead divided by the
    Oxygen concentration in liquid lead squared* property class
    implementing the correlation by *isecke1977*.
    """
    @range_warning
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Returns the value of the *Oxygen partial pressure in liquid lead
        divided by the Oxygen concentration in liquid lead squared* by
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
            squared in :math:`[Pa / wt.\\%^2]`
        """
        return np.power(10, 2 / 2.3 / R * (-120376 / T + 16.255))\
            * M * M / M_O / M_O * 101325

    @property
    def correlation_name(self) -> str:
        """
        str : Name of the correlation
        """
        return "isecke1977"

    @property
    def range(self) -> List[float]:
        """
        List[float] : Temperature validity range of the Oxygen partial
        pressure divided by the Oxygen concentration squared
        correlation function
        """
        return [1173, 1373]


class OxygenPartialPressureTaskinen1979(LeadOxygenPartialPressureInterface):
    """
    *Oxygen partial pressure in liquid lead divided by the
    Oxygen concentration in liquid lead squared* property class
    implementing the correlation by *taskinen1979*.
    """
    @range_warning
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Returns the value of the *Oxygen partial pressure in liquid lead
        divided by the Oxygen concentration in liquid lead squared* by
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
            squared in :math:`[Pa / wt.\\%^2]`
        """
        return np.power(10, 2 / 2.3 / R * (-116717 / T + 12.699))\
            * M * M / M_O / M_O * 101325

    @property
    def correlation_name(self) -> str:
        """
        str : Name of the correlation
        """
        return "taskinen1979"

    @property
    def range(self) -> List[float]:
        """
        List[float] : Temperature validity range of the Oxygen partial
        pressure divided by the Oxygen concentration squared
        correlation function
        """
        return [1073, 1203]


class OxygenPartialPressureFisher1966(LeadOxygenPartialPressureInterface):
    """
    *Oxygen partial pressure in liquid lead divided by the
    Oxygen concentration in liquid lead squared* property class
    implementing the correlation by *fisher1966*.
    """
    @range_warning
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Returns the value of the *Oxygen partial pressure in liquid lead
        divided by the Oxygen concentration in liquid lead squared* by
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
            squared in :math:`[Pa / wt.\\%^2]`
        """
        return np.power(10, 2 / 2.3 / R * (-106395 / T + 10.254))\
            * M * M / M_O / M_O * 101325

    @property
    def correlation_name(self) -> str:
        """
        str : Name of the correlation
        """
        return "fisher1966"

    @property
    def range(self) -> List[float]:
        """
        List[float] : Temperature validity range of the Oxygen partial
        pressure divided by the Oxygen concentration squared
        correlation function
        """
        return [903, 1253]


class MolarEnthalpy(MolarEnthalpyInterface):
    """
    Liquid lead *molar enthalpy variation* property class.
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
    def range(self) -> List[float]:
        """
        List[float] : Temperature validity range of the molar enthalpy
        variation correlation function
        """
        return [T_m0, 2000]

    @property
    def description(self) -> str:
        """
        str : Molar enthalpy variation description
        """
        return f"{self.long_name} in liquid lead"


class MolarEntropy(MolarEntropyInterface):
    """
    Liquid lead *molar entropy variation* property class.
    """
    @range_warning
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Returns the value of the *molar entropy variation* by
        applying the property correlation. Specific heat capacity correlation
        by *sobolev2011* is adopted.

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
        return M / 1000 * (176.2 * np.log(T / T_m0)
                           - 4.923e-2 * (T - T_m0)
                           + 7.72e-6 * (T * T - T_m0 * T_m0)
                           + 7.62e5 * (1 / T / T - 1 / T_m0 / T_m0))

    @property
    def range(self) -> List[float]:
        """
        List[float] : Temperature validity range of the molar entropy
        variation correlation function
        """
        return [T_m0, 2000]

    @property
    def description(self) -> str:
        """
        str : Molar entropy variation description
        """
        return f"{self.long_name} in liquid lead"


class GibbsFreeEnergy(GibbsFreeEnergyInterface):
    """
    Liquid lead *Gibbs free energy variation* property class.
    """
    @range_warning
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Returns the value of the *Gibbs free energy variation* by
        applying the property correlation. Specific heat capacity correlation
        by *sobolev2011* is adopted.

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
    def range(self) -> List[float]:
        """
        List[float] : Temperature validity range of the Gibbs free energy
        variation correlation function
        """
        return [T_m0, 2000]

    @property
    def description(self) -> str:
        """
        str : Gibbs free energy description
        """
        return f"{self.long_name} in liquid lead"
