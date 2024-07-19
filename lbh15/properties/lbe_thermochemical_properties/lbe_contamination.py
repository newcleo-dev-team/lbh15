"""Module with the definition of some coumpounds properties
for contamination assessment"""
from math import log
from typing import List
from scipy.constants import atm
from ..interface import PropertyInterface
from ..._decorators import range_warning


class LBEPoloniumHenryConstantInterfaceOhno2006(PropertyInterface):
    """
    Liquid LBE *Polonium compounds Henry constant* property class
    implementing the correlation by *ohno2006*.
    """
    @range_warning
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Returns the value of the *Polonium compounds Henry constant* by
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
        return 10**((- 8348 / T) + 10.5357)

    @property
    def name(self) -> str:
        """
        str : Name of the property
        """
        return "K_LBEPo"

    @property
    def correlation_name(self) -> str:
        """
        str : Name of the correlation
        """
        return "ohno2006"

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
        return "Henry constant of Polonium in LBE"

    @property
    def description(self) -> str:
        """
        str : Polonium Henry constant description
        """
        return f"{self.long_name} in liquid LBE"

    @property
    def range(self) -> List[float]:
        """
        List[float] : Temperature validity range of the Polonium Henry constant
        correlation function
        """
        return [723.0, 1023.0]


class LBEMercuryHenryConstantInterfaceLandolt1991(PropertyInterface):
    """
    Liquid LBE *Mercury compounds Henry constant* property class
    implementing the correlation by *landolt1991*.
    """
    @range_warning
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Returns the value of the *Mercury compounds Henry constant* by
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
        return 10**((- 3332.7 / T) + 12.6706 - 0.848 * log(T))

    @property
    def name(self) -> str:
        """
        str : Name of the property
        """
        return "K_LBEHg"

    @property
    def correlation_name(self) -> str:
        """
        str : Name of the correlation
        """
        return "landolt1991"

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
        return "Henry constant of Mercury in LBE"

    @property
    def description(self) -> str:
        """
        str : Mercury Henry constant description
        """
        return f"{self.long_name} in liquid LBE"

    @property
    def range(self) -> List[float]:
        """
        List[float] : Temperature validity range of the Mercury Henry constant
        correlation function
        """
        return [625.0, 1927.0]
    

class LBECadmiumHenryConstantInterfaceLandolt1991(PropertyInterface):
    """
    Liquid LBE *Cadmium compounds Henry constant* property class
    implementing the correlation by *landolt1991*.
    """
    @range_warning
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Returns the value of the *Cadmium compounds Henry constant* by
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
        return 10**((- 5711 / T) + 14.38 - 1.0867 * log(T))

    @property
    def name(self) -> str:
        """
        str : Name of the property
        """
        return "K_LBECd"

    @property
    def correlation_name(self) -> str:
        """
        str : Name of the correlation
        """
        return "landolt1991"

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
        return "Henry constant of Cadmium in LBE"

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
        return [398.0, 1927.0]


class LBECadmiumVapourPressureInterfaceLandolt1991(PropertyInterface):
    """
    Liquid LBE *Cadmium compounds vapour pressure* property class
    implementing the correlation by *landolt1991*.
    """
    @range_warning
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Returns the value of the *Cadmium compounds vapour pressure* by
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
        return 0.25 * 10**((- 5711 / T) + 14.38 - 1.0867 * log(T))

    @property
    def name(self) -> str:
        """
        str : Name of the property
        """
        return "P_LBECd"

    @property
    def correlation_name(self) -> str:
        """
        str : Name of the correlation
        """
        return "landolt1991"

    @property
    def units(self) -> str:
        """
        str : Vapour pressure unit
        """
        return "[Pa]"

    @property
    def long_name(self) -> str:
        """
        str : Cadmium Vapour pressure long name
        """
        return "Vapour pressure of Cadmium in LBE"

    @property
    def description(self) -> str:
        """
        str : Cadmium Vapour pressure description
        """
        return f"{self.long_name} in liquid LBE"

    @property
    def range(self) -> List[float]:
        """
        List[float] : Temperature validity range of the Cadmium vapour
        pressure correlation function.
        """
        return [398.0, 1927.0]


class LBEThalliumHenryConstantInterfaceLandolt1991(PropertyInterface):
    """
    Liquid LBE *Thallium compounds Henry constant* property class
    implementing the correltion by *landolt1991*.
    """
    @range_warning
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Returns the value of the *Thallium compounds Henry constant* by
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
        return 10**((- 9463 / T) + 13.264 - 0.892 * log(T))

    @property
    def name(self) -> str:
        """
        str : Name of the property
        """
        return "K_LBETl"

    @property
    def correlation_name(self) -> str:
        """
        str : Name of the correlation
        """
        return "landolt1991"

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
        return "Henry constant of Thallium in LBE"

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
        return [398.0, 1927.0]


class LBEThalliumVapourPressureInterfaceLandolt1991(PropertyInterface):
    """
    Liquid LBE *Thallium compounds vapour pressure* property class
    implementing the correltion by *landolt1991*.
    """
    @range_warning
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Returns the value of the *Thallium compounds vapour pressure* by
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
        return 1.25 * 10**((- 9463 / T) + 13.264 - 0.892 * log(T))

    @property
    def name(self) -> str:
        """
        str : Name of the property
        """
        return "P_LBETl"

    @property
    def correlation_name(self) -> str:
        """
        str : Name of the correlation
        """
        return "landolt1991"

    @property
    def units(self) -> str:
        """
        str : Vapour pressure unit
        """
        return "[Pa]"

    @property
    def long_name(self) -> str:
        """
        str : Thallium vapour pressure long name
        """
        return "Vapour pressure of Thallium in LBE"

    @property
    def description(self) -> str:
        """
        str : Thallium vapour pressure description
        """
        return f"{self.long_name} in liquid LBE"

    @property
    def range(self) -> List[float]:
        """
        List[float] : Temperature validity range of the thallium
        vapour pressure correlation function.
        """
        return [398.0, 1927.0]


class LBEIodineHenryConstantInterfaceNeuhausen2005(PropertyInterface):
    """
    Liquid LBE *Iodine compounds Henry constant* property class
    implementing the correlation by *neuhausen2005*.
    """
    @range_warning
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Returns the value of the *Iodine compounds Henry constant* by
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
        return 10**((- 10407 / T) + 14.56)

    @property
    def name(self) -> str:
        """
        str : Name of the property
        """
        return "K_LBEI"

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
        str : Iodine Henry constant long name
        """
        return "Henry constant of Iodine in LBE"

    @property
    def description(self) -> str:
        """
        str : Iodine Henry constant description
        """
        return f"{self.long_name} in liquid LBE"

    @property
    def range(self) -> List[float]:
        """
        List[float] : Temperature validity range of the Iodine Henry constant
        correlation function
        """
        return [398.0, 1927.0]
