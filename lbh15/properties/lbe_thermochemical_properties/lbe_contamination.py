"""Module with the definition of some coumpounds properties
for contamination assessment"""
from typing import List
import numpy as np
from scipy.constants import atm
from ..interface import PropertyInterface
from ..._decorators import range_warning
from ..._commons import LBE_MELTING_TEMPERATURE as T_m0
from ..._commons import LBE_BOILING_TEMPERATURE as T_b0


class LBEPoloniumHenryConstantInterface(PropertyInterface):
    """
    Liquid LBE *Polonium compound Henry constant*
    abstract class.
    """
    @property
    def units(self) -> str:
        """
        str : Henry constant unit
        """
        return "[Pa]"

    @property
    def long_name(self) -> str:
        """
        str : Polonium Henry constant long name
        """
        return "Henry constant of Polonium"

    @property
    def description(self) -> str:
        """
        str : Polonium Henry constant description
        """
        return f"{self.long_name} in liquid LBE"


class LBEPoloniumHenryConstantOhno2006(LBEPoloniumHenryConstantInterface):
    """
    Liquid LBE *elemental Polonium Henry constant* property class
    implementing the correlation by *ohno2006*.
    """
    @range_warning
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Returns the value of the *elemental Polonium Henry constant* by
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
            Henry constant in :math:`[Pa]`
        """
        return np.power(10, - 8348 / T + 10.5357)

    @property
    def name(self) -> str:
        """
        str : Name of the property
        """
        return "K_Po"

    @property
    def correlation_name(self) -> str:
        """
        str : Name of the correlation
        """
        return "ohno2006"

    @property
    def range(self) -> List[float]:
        """
        List[float] : Temperature validity range of the Polonium
        Henry constant correlation function
        """
        return [723.0, 1023.0]


class LBEPoloniumHenryConstantBuongiorno2003\
        (LBEPoloniumHenryConstantInterface):
    """
    Liquid LBE *Polonium compound Henry constant* property class
    implementing the correlation by *buongiorno2003*.
    """
    @range_warning
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Returns the value of the *Polonium compound Henry constant* by
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
            Henry constant in :math:`[Pa]`
        """
        return np.power(10, - 6790 / T + 1.26)

    @property
    def name(self) -> str:
        """
        str : Name of the property
        """
        return "K_PbPo"

    @property
    def correlation_name(self) -> str:
        """
        str : Name of the correlation
        """
        return "buongiorno2003"

    @property
    def range(self) -> List[float]:
        """
        List[float] : Temperature validity range of the Polonium
        Henry constant correlation function
        """
        return [665.0, 823.0]


class LBEPoloniumActivityCoefficientInterface(PropertyInterface):
    """
    Liquid LBE *Polonium compound activity coefficient*
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
        return "activity coefficient of Polonium"

    @property
    def description(self) -> str:
        """
        str : Polonium activity coefficient description
        """
        return f"{self.long_name} in liquid LBE"


class LBEPoloniumActivityCoefficientOhno2006\
        (LBEPoloniumActivityCoefficientInterface):
    """
    Liquid LBE *Polonium compound activity coefficient* property class
    implementing the correlation by *ohno2006*.
    """
    @range_warning
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Returns the value of the *Polonium compound activity coefficient* by
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
        return np.power(10, - 2908 / T + 1.079)

    @property
    def correlation_name(self) -> str:
        """
        str : Name of the correlation
        """
        return "ohno2006"

    @property
    def range(self) -> List[float]:
        """
        List[float] : Temperature validity range of the Polonium
        activity coefficient correlation function
        """
        return [723.0, 877.0]


class LBEPoloniumActivityCoefficient(LBEPoloniumActivityCoefficientInterface):
    """
    Liquid LBE *Polonium compound activity coefficient* property class
    implementing the correlation by *lbh15*.
    """
    @range_warning
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Returns the value of the *Polonium compound activity coefficient* by
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
        return np.power(10, - 1830 / T + 0.40)

    @property
    def range(self) -> List[float]:
        """
        List[float] : Temperature validity range of the Polonium
        activity coefficient correlation function
        """
        return [913.0, 1123.0]


class LBEMercuryHenryConstant(PropertyInterface):
    """
    Liquid LBE *dilute Mercury Henry constant* property class
    implementing the correlation by *lbh15*.
    """
    @range_warning
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Returns the value of the *dilute Mercury Henry constant* by
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
            Henry constant in :math:`[Pa]`
        """
        return np.power(10, - 3332.7 / T - 0.848 * np.log(T) + 12.6706)

    @property
    def name(self) -> str:
        """
        str : Name of the property
        """
        return "K_LBEHg"

    @property
    def units(self) -> str:
        """
        str : Henry constant unit
        """
        return "[Pa]"

    @property
    def long_name(self) -> str:
        """
        str : Mercury Henry constant long name
        """
        return "Henry constant of Mercury"

    @property
    def description(self) -> str:
        """
        str : Mercury Henry constant description
        """
        return f"{self.long_name} in liquid LBE"

    @property
    def range(self) -> List[float]:
        """
        List[float] : Temperature validity range of the Mercury
        Henry constant correlation function
        """
        return [629.73, T_b0]


class LBEMercuryActivityCoefficient(PropertyInterface):
    """
    Liquid LBE *dilute Mercury activity coefficient* property class
    implementing the correlation by *lbh15*.
    """
    @range_warning
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Returns the value of the *dilute Mercury activity coefficient* by
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
        return 2

    @property
    def name(self) -> str:
        """
        str : Name of the property
        """
        return "gamma_Hg"

    @property
    def units(self) -> str:
        """
        str : activity coefficient unit
        """
        return "[-]"

    @property
    def long_name(self) -> str:
        """
        str : Mercury activity coefficient long name
        """
        return "Activity coefficient of Mercury"

    @property
    def description(self) -> str:
        """
        str : Mercury activity coefficient description
        """
        return f"{self.long_name} in liquid LBE"

    @property
    def range(self) -> List[float]:
        """
        List[float] : Temperature validity range of the Mercury
        activity coefficient correlation function
        """
        return [629.73, T_b0]


class LBEMercuryVapourPressure(PropertyInterface):
    """
    Liquid LBE *dilute Mercury vapour pressure* property class
    implementing the correlation by *lbh15*.
    """
    @range_warning
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Returns the value of the *dilute Mercury vapour pressure* by
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
            Vapour pressure in :math:`[Pa]`
        """
        return LBEMercuryHenryConstant().correlation(T, p) /\
            LBEMercuryActivityCoefficient().correlation(T, p)

    @property
    def name(self) -> str:
        """
        str : Name of the property
        """
        return "P_Hg"

    @property
    def units(self) -> str:
        """
        str : Vapour pressure unit
        """
        return "[Pa]"

    @property
    def long_name(self) -> str:
        """
        str : Mercury vapour pressure long name
        """
        return "Vapour pressure of Mercury"

    @property
    def description(self) -> str:
        """
        str : Mercury vapour pressure description
        """
        return f"{self.long_name} in liquid LBE"

    @property
    def range(self) -> List[float]:
        """
        List[float] : Temperature validity range of the Mercury
        vapour pressure correlation function
        """
        return [629.73, T_b0]


class LBECadmiumHenryConstant(PropertyInterface):
    """
    Liquid LBE *dilute Cadmium Henry constant* property class
    implementing the correlation by *lbh15*.
    """
    @range_warning
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Returns the value of the *dilute Cadmium Henry constant* by
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
            Henry constant in :math:`[Pa]`
        """
        return np.power(10, - 5711 / T - 1.0867 * np.log(T) + 14.38)

    @property
    def name(self) -> str:
        """
        str : Name of the property
        """
        return "K_Cd"

    @property
    def units(self) -> str:
        """
        str : Henry constant unit
        """
        return "[Pa]"

    @property
    def long_name(self) -> str:
        """
        str : Cadmium Henry constant long name
        """
        return "Henry constant of Cadmium"

    @property
    def description(self) -> str:
        """
        str : Cadmium Henry constant description
        """
        return f"{self.long_name} in liquid LBE"

    @property
    def range(self) -> List[float]:
        """
        List[float] : Temperature validity range of the Cadmium Henry constant
        correlation function
        """
        return [T_m0, T_b0]


class LBECadmiumActivityCoefficient(PropertyInterface):
    """
    Liquid LBE *dilute Cadmium activity coefficient* property class
    implementing the correlation by *lbh15*.
    """
    @range_warning
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Returns the value of the *dilute Cadmium activity coefficient* by
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
        return 4

    @property
    def name(self) -> str:
        """
        str : Name of the property
        """
        return "gamma_Cd"

    @property
    def units(self) -> str:
        """
        str : activity coefficient unit
        """
        return "[-]"

    @property
    def long_name(self) -> str:
        """
        str : Cadmium activity coefficient long name
        """
        return "Activity coefficient of Cadmium"

    @property
    def description(self) -> str:
        """
        str : Cadmium activity coefficient description
        """
        return f"{self.long_name} in liquid LBE"

    @property
    def range(self) -> List[float]:
        """
        List[float] : Temperature validity range of the Cadmium
        activity coefficient correlation function
        """
        return [T_m0, T_b0]


class LBECadmiumVapourPressure(PropertyInterface):
    """
    Liquid LBE *dilute Cadmium vapour pressure* property class
    implementing the correlation by *lbh15*.
    """
    @range_warning
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Returns the value of the *dilute Cadmium vapour pressure* by
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
            vapour pressure in :math:`[Pa]`
        """
        return LBECadmiumHenryConstant().correlation(T, p) /\
            LBECadmiumActivityCoefficient().correlation(T, p)

    @property
    def name(self) -> str:
        """
        str : Name of the property
        """
        return "P_Cd"

    @property
    def units(self) -> str:
        """
        str : vapour pressure unit
        """
        return "[Pa]"

    @property
    def long_name(self) -> str:
        """
        str : Cadmium vapour pressure long name
        """
        return "Vapour pressure of Cadmium"

    @property
    def description(self) -> str:
        """
        str : Cadmium vapour pressure description
        """
        return f"{self.long_name} in liquid LBE"

    @property
    def range(self) -> List[float]:
        """
        List[float] : Temperature validity range of the Cadmium
        vapour pressure correlation function
        """
        return [T_m0, T_b0]


class LBEThalliumHenryConstant(PropertyInterface):
    """
    Liquid LBE *dilute Thallium Henry constant* property class
    implementing the correltion by *lbh15*.
    """
    @range_warning
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Returns the value of the *dilute Thallium Henry constant* by
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
            Henry constant in :math:`[Pa]`
        """
        return np.power(10, - 9463 / T - 0.892 * np.log(T) + 13.264)

    @property
    def name(self) -> str:
        """
        str : Name of the property
        """
        return "K_Tl"

    @property
    def units(self) -> str:
        """
        str : Henry constant unit
        """
        return "[Pa]"

    @property
    def long_name(self) -> str:
        """
        str : Thallium Henry constant long name
        """
        return "Henry constant of Thallium"

    @property
    def description(self) -> str:
        """
        str : Thallium Henry constant description
        """
        return f"{self.long_name} in liquid LBE"

    @property
    def range(self) -> List[float]:
        """
        List[float] : Temperature validity range of the Thallium Henry
        constant correlation function.
        """
        return [577.0, T_b0]


class LBEThalliumActivityCoefficient(PropertyInterface):
    """
    Liquid LBE *dilute Thallium activity coefficient* property class
    implementing the correlation by *lbh15*.
    """
    @range_warning
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Returns the value of the *dilute Thallium activity coefficient* by
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
        return 0.8

    @property
    def name(self) -> str:
        """
        str : Name of the property
        """
        return "gamma_Tl"

    @property
    def units(self) -> str:
        """
        str : activity coefficient unit
        """
        return "[-]"

    @property
    def long_name(self) -> str:
        """
        str : Thallium activity coefficient long name
        """
        return "Activity coefficient of Thallium"

    @property
    def description(self) -> str:
        """
        str : Thallium activity coefficient description
        """
        return f"{self.long_name} in liquid LBE"

    @property
    def range(self) -> List[float]:
        """
        List[float] : Temperature validity range of the Thallium
        activity coefficient correlation function
        """
        return [577.0, T_b0]


class LBEThalliumVapourPressure(PropertyInterface):
    """
    Liquid LBE *dilute Thallium vapour pressure* property class
    implementing the correlation by *lbh15*.
    """
    @range_warning
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Returns the value of the *dilute Thallium vapour pressure* by
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
            vapour pressure in :math:`[Pa]`
        """
        return LBEThalliumHenryConstant().correlation(T, p) /\
            LBEThalliumActivityCoefficient().correlation(T, p)

    @property
    def name(self) -> str:
        """
        str : Name of the property
        """
        return "P_Tl"

    @property
    def units(self) -> str:
        """
        str : vapour pressure unit
        """
        return "[Pa]"

    @property
    def long_name(self) -> str:
        """
        str : Thallium vapour pressure long name
        """
        return "Vapour pressure of Thallium"

    @property
    def description(self) -> str:
        """
        str : Thallium vapour pressure description
        """
        return f"{self.long_name} in liquid LBE"

    @property
    def range(self) -> List[float]:
        """
        List[float] : Temperature validity range of the Thallium
        vapour pressure correlation function
        """
        return [577.0, T_b0]


class LBEIodineHenryConstantNeuhausen2005(PropertyInterface):
    """
    Liquid LBE *monoatomic Iodine Henry constant* property class
    implementing the correlation by *neuhausen2005*.
    """
    @range_warning
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Returns the value of the *monoatomic Iodine Henry constant* by
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
            Henry constant in :math:`[Pa]`
        """
        return np.power(10, - 10407 / T + 14.56)

    @property
    def name(self) -> str:
        """
        str : Name of the property
        """
        return "K_I"

    @property
    def correlation_name(self) -> str:
        """
        str : Name of the correlation
        """
        return "neuheusen2005"

    @property
    def units(self) -> str:
        """
        str : Henry constant unit
        """
        return "[Pa]"

    @property
    def long_name(self) -> str:
        """
        str : monoatomic Iodine Henry constant long name
        """
        return "Henry constant of monoatomic Iodine"

    @property
    def description(self) -> str:
        """
        str : monoatomic Iodine Henry constant description
        """
        return f"{self.long_name} in liquid LBE"

    @property
    def range(self) -> List[float]:
        """
        List[float] : Temperature validity range of the monoatomic Iodine
        Henry constant correlation function
        """
        return [700, T_b0]


class LBEIodineActivityCoefficientNeuhasen2005c(PropertyInterface):
    """
    Liquid LBE *monoatomic Iodine activity coefficient* property class
    implementing the correlation by *neuhasen2005c*.
    """
    @range_warning
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Returns the value of the *monoatomic Iodine activity coefficient*
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
            activity coefficient in :math:`[-]`
        """
        return 1

    @property
    def name(self) -> str:
        """
        str : Name of the property
        """
        return "gamma_I"

    @property
    def correlation_name(self) -> str:
        """
        str : Name of the correlation
        """
        return "neuhasen2005c"

    @property
    def units(self) -> str:
        """
        str : activity coefficient unit
        """
        return "[-]"

    @property
    def long_name(self) -> str:
        """
        str : monoatomic Iodine activity coefficient long name
        """
        return "Activity coefficient of monoatomic Iodine"

    @property
    def description(self) -> str:
        """
        str : monoatomic Iodine activity coefficient description
        """
        return f"{self.long_name} in liquid LBE"

    @property
    def range(self) -> List[float]:
        """
        List[float] : Temperature validity range of the monoatomic Iodine
        activity coefficient correlation function
        """
        return [700, T_b0]


class LBEIodineVapourPressure(PropertyInterface):
    """
    Liquid LBE *monoatomic Iodine vapour pressure* property class
    implementing the correlation by *lbh15*.
    """
    @range_warning
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Returns the value of the *monoatomic Iodine vapour pressure* by
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
            vapour pressure in :math:`[Pa]`
        """
        return LBEIodineHenryConstantNeuhausen2005().correlation(T, p) /\
            LBEIodineActivityCoefficientNeuhasen2005c().correlation(T, p)

    @property
    def name(self) -> str:
        """
        str : Name of the property
        """
        return "P_I"

    @property
    def units(self) -> str:
        """
        str : vapour pressure unit
        """
        return "[Pa]"

    @property
    def long_name(self) -> str:
        """
        str : monoatomic Iodine vapour pressure long name
        """
        return "Vapour pressure of monoatomic Iodine"

    @property
    def description(self) -> str:
        """
        str : monoatomic Iodine vapour pressure description
        """
        return f"{self.long_name} in liquid LBE"

    @property
    def range(self) -> List[float]:
        """
        List[float] : Temperature validity range of the monoatomic Iodine
        vapour pressure correlation function
        """
        return [700, T_b0]


class LBECaesiumActivityCoefficientOhno2006(PropertyInterface):
    """
    Liquid LBE *Caesium intermetallic compounds activity coefficient* property class
    implementing the correlation by *ohno2006*.
    """
    @range_warning
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Returns the value of the *Caesium intermetallic compounds Henry constant* by
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
        return np.power(10, - 2677 / T + 0.75)

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
        return "ohno2006"

    @property
    def units(self) -> str:
        """
        str : activity coefficient unit
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
        return f"{self.long_name} in liquid lead"

    @property
    def range(self) -> List[float]:
        """
        List[float] : Temperature validity range of the Caesium
        intermetallic compounds activity coefficient correlation function.
        """
        return [723.0, 1023.0]


class LBERubidiumVapourPressureInterfaceLandolt1960(PropertyInterface):
    """
    Liquid LBE *Rubidium vapour pressure* property class
    implementing the correlation by *landolt1960*.
    """
    @range_warning
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Returns the value of the *Rubidium vapour pressure* by
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
        return np.power(10, - 4588 / T - 1.45 * np.log(T) + 14.110)

    @property
    def name(self) -> str:
        """
        str : Name of the property
        """
        return "P_Rb"

    @property
    def correlation_name(self) -> str:
        """
        str : Name of the correlation
        """
        return "landolt1960"

    @property
    def units(self) -> str:
        """
        str : Vapour pressure unit
        """
        return "[Pa]"

    @property
    def long_name(self) -> str:
        """
        str : Rubidium vapour pressure long name
        """
        return "Vapour pressure of Rubidium"

    @property
    def description(self) -> str:
        """
        str : Rubidium vapour pressure description
        """
        return f"{self.long_name} in liquid LBE"

    @property
    def range(self) -> List[float]:
        """
        List[float] : Temperature validity range of the Rubidium
        vapour pressure correlation function.
        """
        return [800, T_b0]


class LBERubidiumActivityCoefficient(PropertyInterface):
    """
    Liquid LBE *Rubidium activity coefficient* property class
    implementing the correlation by *lbh15*.
    """
    @range_warning
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Returns the value of the *Rubidium activity coefficient* by
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
        return np.power(10, -1.7)

    @property
    def name(self) -> str:
        """
        str : Name of the property
        """
        return "gamma_Rb"

    @property
    def units(self) -> str:
        """
        str : activity coefficient unit
        """
        return "[-]"

    @property
    def long_name(self) -> str:
        """
        str : Rubidium activity coefficient long name
        """
        return "Activity coefficient of Rubidium"

    @property
    def description(self) -> str:
        """
        str : Rubidium activity coefficient description
        """
        return f"{self.long_name} in liquid LBE"

    @property
    def range(self) -> List[float]:
        """
        List[float] : Temperature validity range of the Rubidium
        activity coefficient correlation function
        """
        return [800, T_b0]


class LBERubidiumHenryConstant(PropertyInterface):
    """
    Liquid LBE *Rubidium Henry constant* property class
    implementing the correlation by *lbh15*.
    """
    @range_warning
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Returns the value of the *Rubidium Henry constant* by
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
            Henry constant in :math:`[Pa]`
        """
        return LBERubidiumVapourPressureInterfaceLandolt1960()\
            .correlation(T, p) * LBERubidiumActivityCoefficient()\
            .correlation(T, p)

    @property
    def name(self) -> str:
        """
        str : Name of the property
        """
        return "K_Rb"

    @property
    def units(self) -> str:
        """
        str : Henry constant unit
        """
        return "[Pa]"

    @property
    def long_name(self) -> str:
        """
        str : Rubidium Henry constant long name
        """
        return "Henry constant of Rubidium"

    @property
    def description(self) -> str:
        """
        str : Rubidium Henry constant description
        """
        return f"{self.long_name} in liquid LBE"

    @property
    def range(self) -> List[float]:
        """
        List[float] : Temperature validity range of the Rubidium
        Henry constant correlation function.
        """
        return [800, T_b0]
