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
        return np.power(10, - 6790 / T + 8.46)

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
        compound Henry constant correlation function
        """
        return [665.0, 823.0]


class LBEPoloniumActivityCoefficientInterface(PropertyInterface):
    """
    Liquid LBE *elemental Polonium activity coefficient*
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
        return "Activity coefficient of elemental Polonium"

    @property
    def description(self) -> str:
        """
        str : Polonium activity coefficient description
        """
        return f"{self.long_name} in liquid LBE"


class LBEPoloniumActivityCoefficientOhno2006\
        (LBEPoloniumActivityCoefficientInterface):
    """
    Liquid LBE *elemental Polonium activity coefficient* property class
    implementing the correlation by *ohno2006*.
    """
    @range_warning
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Returns the value of the *elemental Polonium activity coefficient* by
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
        List[float] : Temperature validity range of the elemental
        Polonium activity coefficient correlation function
        """
        return [723.0, 877.0]


class LBEPoloniumActivityCoefficient(LBEPoloniumActivityCoefficientInterface):
    """
    Liquid LBE *elemental Polonium activity coefficient* property class
    implementing the correlation by *lbh15*.
    """
    @range_warning
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Returns the value of the *elemental Polonium activity coefficient* by
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
        List[float] : Temperature validity range of the elemental
        Polonium activity coefficient correlation function
        """
        return [913.0, 1123.0]


class LBEMercuryHenryConstant(PropertyInterface):
    """
    Liquid LBE *Mercury Henry constant* property class
    implementing the correlation by *lbh15*.
    """
    @range_warning
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Returns the value of the *Mercury Henry constant* by
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
        return np.power(10, - 3332.7 / T - 0.848 * np.log(T) + 12.9716)

    @property
    def name(self) -> str:
        """
        str : Name of the property
        """
        return "K_Hg"

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
        return [603 - 0.05 * (T_b0 - T_m0),
                603 + 0.05 * (T_b0 - T_m0)]


class LBEMercuryActivityCoefficient(PropertyInterface):
    """
    Liquid LBE *Mercury activity coefficient* property class
    implementing the correlation by *lbh15*.
    """
    @range_warning
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Returns the value of the *Mercury activity coefficient* by
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
        return [603 - 0.05 * (T_b0 - T_m0),
                603 + 0.05 * (T_b0 - T_m0)]


class LBECadmiumHenryConstant(PropertyInterface):
    """
    Liquid LBE *Cadmium Henry constant* property class
    implementing the correlation by *lbh15*.
    """
    @range_warning
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Returns the value of the *Cadmium Henry constant* by
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
        return [773 - 0.05 * (T_b0 - T_m0),
                773 + 0.05 * (T_b0 - T_m0)]


class LBECadmiumActivityCoefficient(PropertyInterface):
    """
    Liquid LBE *Cadmium activity coefficient* property class
    implementing the correlation by *lbh15*.
    """
    @range_warning
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Returns the value of the *Cadmium activity coefficient* by
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
        return [773 - 0.05 * (T_b0 - T_m0),
                773 + 0.05 * (T_b0 - T_m0)]


class LBEThalliumHenryConstant(PropertyInterface):
    """
    Liquid LBE *Thallium Henry constant* property class
    implementing the correlation by *lbh15*.
    """
    @range_warning
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Returns the value of the *Thallium Henry constant* by
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
        return [773 - 0.05 * (T_b0 - T_m0),
                773 + 0.05 * (T_b0 - T_m0)]


class LBEThalliumActivityCoefficient(PropertyInterface):
    """
    Liquid LBE *Thallium activity coefficient* property class
    implementing the correlation by *lbh15*.
    """
    @range_warning
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Returns the value of the *Thallium activity coefficient* by
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
        return [773 - 0.05 * (T_b0 - T_m0),
                773 + 0.05 * (T_b0 - T_m0)]


class LBEIodineVapourPressureInterface(PropertyInterface):
    """
    Liquid LBE *PbI2 Iodine compound vapour pressure*
    abstract class.
    """
    @property
    def name(self) -> str:
        """
        str : Name of the property
        """
        return "P_PbI2"

    @property
    def units(self) -> str:
        """
        str : Vapour pressure unit
        """
        return "[Pa]"

    @property
    def long_name(self) -> str:
        """
        str : PbI2 Iodine vapour pressure long name
        """
        return "Vapour pressure of PbI2 Iodine compound"

    @property
    def description(self) -> str:
        """
        str : PbI2 Iodine compound vapour pressure description
        """
        return f"{self.long_name} in liquid LBE"


class LBEIodineVapourPressureKonings1996(LBEIodineVapourPressureInterface):
    """
    Liquid LBE *PbI2 Iodine compound vapour pressure* property class
    implementing the correlation by *konings1996*.
    """
    @range_warning
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Returns the value of the *PbI2 Iodine compound vapour pressure* by
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
        return np.power(10, - 8691 / T + 13.814)

    @property
    def correlation_name(self) -> str:
        """
        str : Name of the correlation
        """
        return "konings1996"

    @property
    def range(self) -> List[float]:
        """
        List[float] : Temperature validity range of the PbI2
        Iodine compound vapour pressure correlation function.
        """
        return [580.0, 697.0]


class LBEIodineVapourPressureKnacke1991(LBEIodineVapourPressureInterface):
    """
    Liquid LBE *PbI2 Iodine compound vapour pressure* property class
    implementing the correlation by *knacke1991*.
    """
    @range_warning
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Returns the value of the *PbI2 Iodine compound vapour pressure* by
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
        return np.power(10, - 9087 / T - 6.16 * np.log(T) + 31.897)

    @property
    def correlation_name(self) -> str:
        """
        str : Name of the correlation
        """
        return "knacke1991"

    @property
    def range(self) -> List[float]:
        """
        List[float] : Temperature validity range of the PbI2
        Iodine compound vapour pressure correlation function.
        """
        return [697.0, 1120.0]


class LBEIodineActivityCoefficient(PropertyInterface):
    """
    Liquid LBE *PbI2 Iodine compound activity coefficient*
    property class implementing the suggestion by *handbook*.
    """
    @range_warning
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Returns the value of the *PbI2 Iodine compound activity coefficient*
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
        return "gamma_PbI2"

    @property
    def units(self) -> str:
        """
        str : activity coefficient unit
        """
        return "[-]"

    @property
    def long_name(self) -> str:
        """
        str : PbI2 iodine compound activity coefficient long name
        """
        return "Activity coefficient of PbI2 Iodine compound"

    @property
    def description(self) -> str:
        """
        str : PbI2 Iodine compound activity coefficient description
        """
        return f"{self.long_name} in liquid LBE"

    @property
    def range(self) -> List[float]:
        """
        List[float] : Temperature validity range of the PbI2 Iodine
        compound activity coefficient correlation function
        """
        return [580.0, 1120.0]


class LBEIodineHenryConstantInterface(PropertyInterface):
    """
    Liquid LBE *PbI2 Iodine compound Henry constant*
    abstract class.
    """
    @property
    def name(self) -> str:
        """
        str : Name of the property
        """
        return "K_PbI2"

    @property
    def units(self) -> str:
        """
        str : Henry constant unit
        """
        return "[Pa]"

    @property
    def long_name(self) -> str:
        """
        str : PbI2 Iodine compound Henry constant long name
        """
        return "Henry constant of PbI2 Iodine compound"

    @property
    def description(self) -> str:
        """
        str : PbI2 Iodine compound Henry constant description
        """
        return f"{self.long_name} in liquid LBE"


class LBEIodineHenryConstantKonings1996(LBEIodineHenryConstantInterface):
    """
    Liquid LBE *PbI2 Iodine compound Henry constant*
    property class implementing the correlation by *konings1996*.
    """
    @range_warning
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Returns the value of the *PbI2 Iodine compound Henry constant*
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
            Henry constant in :math:`[Pa]`
        """
        return LBEIodineVapourPressureKonings1996().correlation(T, p)

    @property
    def correlation_name(self) -> str:
        """
        str : Name of the correlation
        """
        return "konings1996"

    @property
    def range(self) -> List[float]:
        """
        List[float] : Temperature validity range of the PbI2 Iodine
        compound Henry constant correlation function
        """
        return [580.0, 697.0]


class LBEIodineHenryConstantKnacke1991(LBEIodineHenryConstantInterface):
    """
    Liquid LBE *PbI2 Iodine compound Henry constant*
    property class implementing the correlation by *knacke1991*.
    """
    @range_warning
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Returns the value of the *PbI2 Iodine compound Henry constant*
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
            Henry constant in :math:`[Pa]`
        """
        return LBEIodineVapourPressureKnacke1991().correlation(T, p)

    @property
    def correlation_name(self) -> str:
        """
        str : Name of the correlation
        """
        return "knacke1991"

    @property
    def range(self) -> List[float]:
        """
        List[float] : Temperature validity range of the PbI2 Iodine
        compound Henry constant correlation function
        """
        return [697.0, 1120.0]


class LBEIodineHenryConstantNeuhausen2005(LBEIodineHenryConstantInterface):
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
        return "neuhausen2005"

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
        return [700, 1120.0]


class LBECaesiumHenryConstant(PropertyInterface):
    """
    Liquid LBE *Caesium intermetallic compounds Henry constant*
    property class implementing the correlation by *lbh15*.
    """
    @range_warning
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Returns the value of the *Caesium intermetallic compounds
        Henry constant* by applying the property correlation.

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
        return np.power(10, - 4980 / T - 9.323 * np.log(T)
                        + 0.004473 * T - 8.684e-7 * T**2 + 33.07)

    @property
    def name(self) -> str:
        """
        str : Name of the property
        """
        return "K_Cs"

    @property
    def units(self) -> str:
        """
        str : Henry constant unit
        """
        return "[Pa]"

    @property
    def long_name(self) -> str:
        """
        str : Caesium Henry constant long name
        """
        return "Henry constant of Caesium intermettalic compounds"

    @property
    def description(self) -> str:
        """
        str : Caesium Henry constant description
        """
        return f"{self.long_name} in liquid LBE"

    @property
    def range(self) -> List[float]:
        """
        List[float] : Temperature validity range of the Caesium
        intermettalic compounds Henry constant correlation function.
        """
        return [643, 933]


class LBECaesiumActivityCoefficientInterface(PropertyInterface):
    """
    Liquid LBE *Caesium intermetallic compounds activity coefficient*
    property abstract class.
    """

    @property
    def name(self) -> str:
        """
        str : Name of the property
        """
        return "gamma_Cs"

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
        return f"{self.long_name} in liquid LBE"


class LBECaesiumActivityCoefficient(LBECaesiumActivityCoefficientInterface):
    """
    Liquid LBE *Caesium intermetallic compounds activity coefficient* property
    class implementing the correlation by *lbh15*.
    """
    @range_warning
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Returns the value of the *Caesium intermetallic compounds Henry
        constant* by applying the property correlation.

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
        return np.power(10, -1.5)

    @property
    def range(self) -> List[float]:
        """
        List[float] : Temperature validity range of the Caesium
        intermetallic compounds activity coefficient correlation function.
        """
        return [643, 933]


class LBECaesiumActivityCoefficientOhno2006\
      (LBECaesiumActivityCoefficientInterface):
    """
    Liquid LBE *Caesium intermetallic compounds activity coefficient* property
    class implementing the correlation by *ohno2006*.
    """
    @range_warning
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Returns the value of the *Caesium intermetallic compounds Henry
        constant* by applying the property correlation.

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
    def correlation_name(self) -> str:
        """
        str : Name of the correlation
        """
        return "ohno2006"

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
        return [873 - 0.05 * (T_b0 - T_m0),
                873 + 0.05 * (T_b0 - T_m0)]


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
        return 0.02

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
        return [873 - 0.05 * (T_b0 - T_m0),
                873 + 0.05 * (T_b0 - T_m0)]


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
        return [873 - 0.05 * (T_b0 - T_m0),
                873 + 0.05 * (T_b0 - T_m0)]