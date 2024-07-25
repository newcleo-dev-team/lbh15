"""Module with the definition of some coumpounds properties
for contamination assessment"""
from math import log
from typing import List
from scipy.constants import atm
from ..interface import PropertyInterface
from ..._decorators import range_warning


class LeadPoloniumVapourPressureAbakumov1994a(PropertyInterface):
    """
    Liquid lead *PbPo Polonium compounds vapour pressure* property class
    implementing the correlation by *abakumov1994a*.
    """
    @range_warning
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Returns the value of the *PbPo Polonium compounds vapour pressure* by
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
        return 10**((- 7270 / T) + 9.06)

    @property
    def name(self) -> str:
        """
        str : Name of the property
        """
        return "P_PbPo"

    @property
    def correlation_name(self) -> str:
        """
        str : Name of the correlation
        """
        return "abakumov1994a"

    @property
    def units(self) -> str:
        """
        str : Vapour pressure unit
        """
        return "[Pa]"

    @property
    def long_name(self) -> str:
        """
        str : PbPo Polonium compound vapour pressure long name
        """
        return "Vapour pressure of PbPo compound in pure lead"

    @property
    def description(self) -> str:
        """
        str : PbPo Polonium compound vapour pressure description
        """
        return f"{self.long_name} in liquid lead"

    @property
    def range(self) -> List[float]:
        """
        List[float] : Temperature validity range of the PbPo Polonium 
        compound vapour pressure correlation function
        """
        return [913.0, 1123.0]


class LeadPoloniumActivityCoefficientLi1998(PropertyInterface):
    """
    Liquid lead *PbPo Polonium compounds activity coefficient* 
    property class implementing the correlation by *li1998*.
    """
    @range_warning
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Returns the value of the *PbPo Polonium compounds activity coefficient*
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
            activity coefficient in :math:`[]`
        """
        return 1

    @property
    def name(self) -> str:
        """
        str : Name of the property
        """
        return "gamma_PbPo"

    @property
    def correlation_name(self) -> str:
        """
        str : Name of the correlation
        """
        return "li1998"

    @property
    def units(self) -> str:
        """
        str : activity coefficient unit
        """
        return "[]"

    @property
    def long_name(self) -> str:
        """
        str : PbPo Polonium compound activity coefficient long name
        """
        return "Activity coefficient of PbPo compound in pure lead"

    @property
    def description(self) -> str:
        """
        str : PbPo Polonium compound activity coefficient description
        """
        return f"{self.long_name} in liquid lead"

    @property
    def range(self) -> List[float]:
        """
        List[float] : Temperature validity range of the PbPo Polonium 
        compound activity coefficient correlation function
        """
        return [913.0, 1123.0]


class LeadPoloniumHenryConstantHandbook(PropertyInterface):
    """
    Liquid lead *PbPo Polonium compounds Henry constant* 
    property class implementing the correlation by *handbook*.
    """
    @range_warning
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Returns the value of the *PbPo Polonium compounds Henry constant*
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
        return LeadPoloniumVapourPressureAbakumov1994a.correlation(T,p)

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
        return "handbook"

    @property
    def units(self) -> str:
        """
        str : Henry constant unit
        """
        return "[Pa]"

    @property
    def long_name(self) -> str:
        """
        str : PbPo Polonium compound Henry constant long name
        """
        return "Henry constant of PbPo compound in pure lead"

    @property
    def description(self) -> str:
        """
        str : PbPo Polonium compound Henry constant description
        """
        return f"{self.long_name} in liquid lead"

    @property
    def range(self) -> List[float]:
        """
        List[float] : Temperature validity range of the PbPo Polonium 
        compound Henry constant correlation function
        """
        return [913.0, 1123.0]


class LeadIodineVapourPressureKonings1996(PropertyInterface):
    """
    Liquid lead *PbI2 Iodine compounds vapour pressure* property class
    implementing the correlation by *konings1996*.
    """
    @range_warning
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Returns the value of the *PbI2 Iodine compounds vapour pressure* by
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
        return 10**((- 8691 / T) + 13.814)

    @property
    def name(self) -> str:
        """
        str : Name of the property
        """
        return "P_PbI2_a"

    @property
    def correlation_name(self) -> str:
        """
        str : Name of the correlation
        """
        return "konings1994"

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
        return "Vapour pressure of PbI2 Iodine in pure lead"

    @property
    def description(self) -> str:
        """
        str : PbI2 Iodine vapour pressure description
        """
        return f"{self.long_name} in liquid lead"

    @property
    def range(self) -> List[float]:
        """
        List[float] : Temperature validity range of the PbI2 
        Iodine vapour pressure correlation function.
        """
        return [600.6, 697.0]   


class LeadIodineVapourPressureKnacke1991(PropertyInterface):
    """
    Liquid lead *PbI2 Iodine compounds vapour pressure* property class
    implementing the correlation by *knacke1991*.
    """
    @range_warning
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Returns the value of the *PbI2 Iodine compounds vapour pressure* by
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
        return 10**((- 9087 / T) + 31.897 - 6.16 * log(T))

    @property
    def name(self) -> str:
        """
        str : Name of the property
        """
        return "P_PbI2_b"

    @property
    def correlation_name(self) -> str:
        """
        str : Name of the correlation
        """
        return "knacke1991"

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
        return "Vapour pressure of PbI2 Iodine in pure lead"

    @property
    def description(self) -> str:
        """
        str : PbI2 Iodine vapour pressure description
        """
        return f"{self.long_name} in liquid lead"

    @property
    def range(self) -> List[float]:
        """
        List[float] : Temperature validity range of the PbI2
        Iodine vapour pressure correlation function.
        """
        return [697.1, 2021.1]


class LeadIodineActivityCoefficientHandbook(PropertyInterface):
    """
    Liquid lead *PbI2 Iodine compounds activity coefficient* 
    property class implementing the correlation by *handbook*.
    """
    @range_warning
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Returns the value of the *PbI2 Iodine compounds activity coefficient*
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
            activity coefficient in :math:`[]`
        """
        return 1

    @property
    def name(self) -> str:
        """
        str : Name of the property
        """
        return "gamma_PbI2"

    @property
    def correlation_name(self) -> str:
        """
        str : Name of the correlation
        """
        return "handbook"

    @property
    def units(self) -> str:
        """
        str : activity coefficient unit
        """
        return "[]"

    @property
    def long_name(self) -> str:
        """
        str : PbI2 iodine compound activity coefficient long name
        """
        return "Activity coefficient of PbI2 compound in pure lead"

    @property
    def description(self) -> str:
        """
        str : PbI2 Iodine compound activity coefficient description
        """
        return f"{self.long_name} in liquid lead"

    @property
    def range(self) -> List[float]:
        """
        List[float] : Temperature validity range of the PbI2 Iodine
        compound activity coefficient correlation function
        """
        return [600.6, 2021.1]


class LeadIodineHenryConstantKonings1996(PropertyInterface):
    """
    Liquid lead *PbI2 Iodine compounds Henry constant* 
    property class implementing the correlation by *konings1996*.
    """
    @range_warning
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Returns the value of the *PbI2 Iodine compounds Henry constant*
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
        return LeadIodineVapourPressureKonings1996.correlation(T,p)

    @property
    def name(self) -> str:
        """
        str : Name of the property
        """
        return "K_PbI2_a"

    @property
    def correlation_name(self) -> str:
        """
        str : Name of the correlation
        """
        return "konings1996"

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
        return "Henry constant of PbI2 compound in pure lead"

    @property
    def description(self) -> str:
        """
        str : PbI2 iodine compound Henry constant description
        """
        return f"{self.long_name} in liquid lead"

    @property
    def range(self) -> List[float]:
        """
        List[float] : Temperature validity range of the PbI2 Iodine
        compound Henry constant correlation function
        """
        return [600.6, 697.0] 


class LeadIodineHenryConstantKnacke1991(PropertyInterface):
    """
    Liquid lead *PbI2 Iodine compounds Henry constant* 
    property class implementing the correlation by *knacke1991*.
    """
    @range_warning
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Returns the value of the *PbI2 Iodine compounds Henry constant*
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
        return LeadIodineVapourPressureKnacke1991.correlation(T,p)

    @property
    def name(self) -> str:
        """
        str : Name of the property
        """
        return "K_PbI2_b"

    @property
    def correlation_name(self) -> str:
        """
        str : Name of the correlation
        """
        return "knacke1991"

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
        return "Henry constant of PbI2 compound in pure lead"

    @property
    def description(self) -> str:
        """
        str : PbI2 iodine compound Henry constant description
        """
        return f"{self.long_name} in liquid lead"

    @property
    def range(self) -> List[float]:
        """
        List[float] : Temperature validity range of the PbI2 Iodine
        compound Henry constant correlation function
        """
        return [697.1, 2021.1] 


class LeadCaesiumHenryConstantYamshchikov2001(PropertyInterface):
    """
    Liquid lead *Cs-Pb Caesium intermetallic compound Henry constant* property class
    implementing the correlation by *yamshchikov2001*.
    """
    @range_warning
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Returns the value of the *Cs-Pb Caesium intermetallic compound
        Henry Constant* by applying the property correlation.

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
        return 10**((- 4979.5799 / T) - 9.3234247 * log(T) + 0.0044733132 * T
                    - 8.684092 * 10**(-7) * T**(2) + 34.573234)

    @property
    def name(self) -> str:
        """
        str : Name of the property
        """
        return "K_PbCs"

    @property
    def correlation_name(self) -> str:
        """
        str : Name of the correlation
        """
        return "yamshchikov2001"

    @property
    def units(self) -> str:
        """
        str : Henry constant unit
        """
        return "[Pa]"

    @property
    def long_name(self) -> str:
        """
        str : Cs-Pb Caesium intermetallic compound Henry constant long name
        """
        return "Cs-Pb Caesium intermetallic compound Henry Constant in pure lead"

    @property
    def description(self) -> str:
        """
        str : Cs-Pb Caesium intermetallic compound Henry constant description
        """
        return f"{self.long_name} in liquid lead"

    @property
    def range(self) -> List[float]:
        """
        List[float] : Temperature validity range of the Cs-Pb Caesium 
        intermetallic compound Henry constant correlation function
        """
        return [643.0, 933.0]


class LeadCaesiumActivityCoefficientHandbook(PropertyInterface):
    """
    Liquid lead *Cs-Pb Caesium intermetallic compound activity coefficient* 
    property class implementing the correlation by *handbook*.
    """
    @range_warning
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Returns the value of the *Cs-Pb Caesium intermetallic compound activity coefficient*
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
            activity coefficient in :math:`[]`
        """
        return 10**(-1.5)

    @property
    def name(self) -> str:
        """
        str : Name of the property
        """
        return "gamma_PbCs"

    @property
    def correlation_name(self) -> str:
        """
        str : Name of the correlation
        """
        return "handbook"

    @property
    def units(self) -> str:
        """
        str : activity coefficient unit
        """
        return "[]"

    @property
    def long_name(self) -> str:
        """
        str : Cs-Pb Caesium intermetallic compound activity coefficient long name
        """
        return "Activity coefficient of Cs-Pb Caesium intermetallic compound in pure lead"

    @property
    def description(self) -> str:
        """
        str : Cs-Pb Caesium intermetallic compound activity coefficient description
        """
        return f"{self.long_name} in liquid lead"

    @property
    def range(self) -> List[float]:
        """
        List[float] : Temperature validity range of the Cs-Pb Caesium 
        intermetallic compound compound activity coefficient correlation function
        """
        return [643.0, 933.0]


class LeadCaesiumVapourPressureYamshchikov2001(PropertyInterface):
    """
    Liquid lead *Cs-Pb Caesium intermetallic compound vapour pressure* 
    property class implementing the correlation by *yamshchikov2001*.
    """
    @range_warning
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Returns the value of the *Cs-Pb Caesium intermetallic compounds
        vapour pressure* by applying the property correlation.

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
        return LeadCaesiumActivityCoefficientHandbook.correlation(T,p) * LeadCaesiumHenryConstantYamshchikov2001.correlation(T,p)

    @property
    def name(self) -> str:
        """
        str : Name of the property
        """
        return "P_PbCs"

    @property
    def correlation_name(self) -> str:
        """
        str : Name of the correlation
        """
        return "yamshchikov2001"

    @property
    def units(self) -> str:
        """
        str : Vapour pressure unit
        """
        return "[Pa]"

    @property
    def long_name(self) -> str:
        """
        str : Cs-Pb Caesium intermetallic compound vapour pressure long name
        """
        return "Cs-Pb Caesium intermetallic compound vapour pressure in pure lead"

    @property
    def description(self) -> str:
        """
        str : Cs-Pb Caesium intermetallic compound vapour pressure description
        """
        return f"{self.long_name} in liquid lead"

    @property
    def range(self) -> List[float]:
        """
        List[float] : Temperature validity range of the Cs-Pb Caesium 
        intermetallic compound vapour pressure correlation function
        """
        return [643.0, 933.0]
