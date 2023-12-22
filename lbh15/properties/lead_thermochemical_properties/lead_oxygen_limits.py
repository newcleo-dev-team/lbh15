"""Module with the definition of the *Oxygen concentration lower limits*
objects for *lead*."""
from typing import List
from typing import Union
import numpy as np
from scipy.constants import atm
from scipy.constants import R
from ..interface import PropertyInterface
from .solubility_in_lead import OxygenSolubility
from .solubility_in_lead import ChromiumSolubilityGosse2014
from .solubility_in_lead import ChromiumSolubilityAlden1958
from .solubility_in_lead import ChromiumSolubilityVenkatraman1988
from .solubility_in_lead import NickelSolubility
from .solubility_in_lead import IronSolubility
from .solubility_in_lead import SiliconSolubility
from ..._decorators import range_warning


class LowerLimitSaturationIron(PropertyInterface):
    """
    *Lower limit of Oxygen concentration* to promote a
    protective oxide film in liquid lead considering
    *Iron at its saturation concentration* property class.
    """
    def initialization_helper(self,
                              property_value: float) -> Union[None, float]:
        """
        Returns the temperature guess value according to the value
        of the lower limit of Oxygen concentration to promote a protective
        oxide film in liquid lead considering Chromium at its saturation
        concentration passed as argument.
        It is used by the root finder algorithm.

        Parameters
        ----------
        property_value : float
            lower limit of Oxygen concentration to promote a
            protective oxide film in liquid lead considering
            Chromium at its saturation concentration
            in :math:`[wt.\\%]`

        Returns
        -------
        float
            Temperature guess value in :math:`[K]`
        """
        if property_value < 1e-4:
            return 1000
        return 1700

    @range_warning
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Returns the value of the *Oxygen concentration lower
        limit* to promote a protective oxide film in liquid lead
        considering *Iron at its saturation concentration* by
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
            Oxygen concentration in :math:`[wt.\\%]`
        """
        return np.exp(-57190 / R / T - 21.1 / R)\
            * OxygenSolubility().correlation(T, p)

    @property
    def name(self) -> str:
        """
        str : Name of the property
        """
        return "lim_fe_sat"

    @property
    def units(self) -> str:
        """
        str : Oxygen concentration lower limit unit
        """
        return "[wt.%]"

    @property
    def range(self) -> List[float]:
        """
        List[float] : Temperature validity range of the Oxygen concentration
        lower limit correlation function
        """
        return [673, 1000]

    @property
    def long_name(self) -> str:
        """
        str : Oxygen concentration lower limit long name
        """
        return ("Oxygen concentration lower limit for"
                " iron at its saturation concentration")

    @property
    def description(self) -> str:
        """
        str : Oxygen concentration lower limit description
        """
        return f"{self.long_name} in liquid lead"


class LowerLimitSaturationChromium(PropertyInterface):
    """
    *Lower limit of Oxygen concentration* to promote a
    protective oxide film in liquid lead considering
    *Chromium at its saturation concentration* property class.
    """
    def initialization_helper(self,
                              property_value: float) -> Union[None, float]:
        """
        Returns the temperature guess value according to the value
        of the lower limit of Oxygen concentration to promote a protective
        oxide film in liquid lead considering Chromium at its saturation
        concentration passed as argument.
        It is used by the root finder algorithm.

        Parameters
        ----------
        property_value : float
            lower limit of Oxygen concentration to promote a
            protective oxide film in liquid lead considering
            Chromium at its saturation concentration
            in :math:`[wt.\\%]`

        Returns
        -------
        float
            Temperature guess value in :math:`[K]`
        """
        if property_value < 1e-7:
            return 1200
        return 1700

    @range_warning
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Returns the value of the *Oxygen concentration lower
        limit* to promote a protective oxide film in liquid lead
        considering *Chromium at its saturation concentration* by
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
            Oxygen concentration in :math:`[wt.\\%]`
        """
        return np.exp(-158900 / R / T - 13.65 / R)\
            * OxygenSolubility().correlation(T, p)

    @property
    def name(self) -> str:
        """
        str : Name of the property
        """
        return "lim_cr_sat"

    @property
    def units(self) -> str:
        """
        str : Oxygen concentration lower limit unit
        """
        return "[wt.%]"

    @property
    def range(self) -> List[float]:
        """
        List[float] : Temperature validity range of the Oxygen concentration
        lower limit correlation function
        """
        return [673, 1000]

    @property
    def long_name(self) -> str:
        """
        str : Oxygen concentration lower limit long name
        """
        return ("Oxygen concentration lower limit for"
                " chromium at its saturation concentration")

    @property
    def description(self) -> str:
        """
        str : Oxygen concentration lower limit description
        """
        return f"{self.long_name} in liquid lead"


class LowerLimitSaturationNickel(PropertyInterface):
    """
    *Lower limit of Oxygen concentration* to promote a
    protective oxide film in liquid lead considering
    *Nickel at its saturation concentration* property class.
    """
    @range_warning
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Returns the value of the *Oxygen concentration lower
        limit* to promote a protective oxide film in liquid lead
        considering *Nickel at its saturation concentration* by
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
            Oxygen concentration in :math:`[wt.\\%]`
        """
        return np.exp(-18040 / R / T - 11.7 / R)\
            * OxygenSolubility().correlation(T, p)

    @property
    def name(self) -> str:
        """
        str : Name of the property
        """
        return "lim_ni_sat"

    @property
    def units(self) -> str:
        """
        str : Oxygen concentration lower limit unit
        """
        return "[wt.%]"

    @property
    def range(self) -> List[float]:
        """
        List[float] : Temperature validity range of the Oxygen concentration
        lower limit correlation function
        """
        return [673, 1000]

    @property
    def long_name(self) -> str:
        """
        str : Oxygen concentration lower limit long name
        """
        return ("Oxygen concentration lower limit for"
                " nickel at its saturation concentration")

    @property
    def description(self) -> str:
        """
        str : Oxygen concentration lower limit description
        """
        return f"{self.long_name} in liquid lead"


class LowerLimitSaturationSilicon(PropertyInterface):
    """
    *Lower limit of Oxygen concentration* to promote a
    protective oxide film in liquid lead considering
    *Silicon at its saturation concentration* property class.
    """
    def initialization_helper(self,
                              property_value: float) -> Union[None, float]:
        """
        Returns the temperature guess value according to the value
        of the lower limit of Oxygen concentration to promote a protective
        oxide film in liquid lead considering Silicon at its saturation
        concentration passed as argument.
        It is used by the root finder algorithm.

        Parameters
        ----------
        property_value : float
            lower limit of Oxygen concentration to promote a
            protective oxide film in liquid lead considering
            Silicon at its saturation concentration
            in :math:`[wt.\\%]`

        Returns
        -------
        float
            Temperature guess value in :math:`[K]`
        """
        if property_value < 1e-8:
            return 1400
        return 1800

    @range_warning
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Returns the value of the *Oxygen concentration lower
        limit* to promote a protective oxide film in liquid lead
        considering *Silicon at its saturation concentration* by
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
            Oxygen concentration in :math:`[wt.\\%]`
        """
        return np.exp(-235855 / R / T - 9.75 / R)\
            * OxygenSolubility().correlation(T, p)

    @property
    def name(self) -> str:
        """
        str : Name of the property
        """
        return "lim_si_sat"

    @property
    def units(self) -> str:
        """
        str : Oxygen concentration lower limit unit
        """
        return "[wt.%]"

    @property
    def range(self) -> List[float]:
        """
        List[float] : Temperature validity range of the Oxygen concentration
        lower limit correlation function
        """
        return [673, 1000]

    @property
    def long_name(self) -> str:
        """
        str : Oxygen concentration lower limit long name
        """
        return ("Oxygen concentration lower limit for"
                " silicon at its saturation concentration")

    @property
    def description(self) -> str:
        """
        str : Oxygen concentration lower limit description
        """
        return f"{self.long_name} in liquid lead"


class LowerLimitSaturationAluminium(PropertyInterface):
    """
    *Lower limit of Oxygen concentration* to promote a
    protective oxide film in liquid lead considering
    *Aluminium at its saturation concentration* property class.
    """
    def initialization_helper(self,
                              property_value: float) -> Union[None, float]:
        """
        Returns the temperature guess value according to the value
        of the lower limit of Oxygen concentration to promote a protective
        oxide film in liquid lead considering Aluminium at its saturation
        concentration passed as argument.
        It is used by the root finder algorithm.

        Parameters
        ----------
        property_value : float
            lower limit of Oxygen concentration to promote a
            protective oxide film in liquid lead considering
            Aluminium at its saturation concentration
            in :math:`[wt.\\%]`

        Returns
        -------
        float
            Temperature guess value in :math:`[K]`
        """
        return 1800

    @range_warning
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Returns the value of the *Oxygen concentration lower
        limit* to promote a protective oxide film in liquid lead
        considering *Aluminium at its saturation concentration* by
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
            Oxygen concentration in :math:`[wt.\\%]`
        """
        return np.exp(-339770 / R / T + 5.35 / R)\
            * OxygenSolubility().correlation(T, p)

    @property
    def name(self) -> str:
        """
        str : Name of the property
        """
        return "lim_al_sat"

    @property
    def units(self) -> str:
        """
        str : Oxygen concentration lower limit unit
        """
        return "[wt.%]"

    @property
    def range(self) -> List[float]:
        """
        List[float] : Temperature validity range of the Oxygen concentration
        lower limit correlation function
        """
        return [673, 1000]

    @property
    def long_name(self) -> str:
        """
        str : Oxygen concentration lower limit long name
        """
        return ("Oxygen concentration lower limit for"
                " aluminium at its saturation concentration")

    @property
    def description(self) -> str:
        """
        str : Oxygen concentration lower limit description
        """
        return f"{self.long_name} in liquid lead"


class LowerLimitChromiumInterface(PropertyInterface):
    """
    *Lower limit of oxygen concentration* to promote a
    protective oxide film times the *Chromium concentration*
    raised to :math:`2/3` in liquid lead property abstract class.
    """
    def initialization_helper(self,
                              property_value: float) -> Union[None, float]:
        """
        Returns the temperature guess value according to the value
        of the lower limit of Oxygen concentration to promote a protective
        oxide film times the Chromium concentration raised to :math:`2/3`
        in liquid lead passed as argument.
        It is used by the root finder algorithm.

        Parameters
        ----------
        property_value : float
            lower limit of Oxygen concentration to promote a
            protective oxide film times the Chromium concentration
            raised to :math:`2/3` in liquid lead
            in :math:`[wt.\\%]`

        Returns
        -------
        float
            Temperature guess value in :math:`[K]`
        """
        if property_value < 1e-6:
            return 1500
        return 1800

    @property
    def name(self) -> str:
        """
        str : Name of the property
        """
        return "lim_cr"

    @property
    def units(self) -> str:
        """
        str : Oxygen concentration lower limit unit
        """
        return "[wt.%]"

    @property
    def long_name(self) -> str:
        """
        str : Oxygen concentration lower limit long name
        """
        return ("Oxygen concentration lower limit times"
                " chromium concentration raised to 2/3")

    @property
    def description(self) -> str:
        """
        str : Oxygen concentration lower limit description
        """
        return f"{self.long_name} in lead"


class LowerLimitChromiumGosse2014(LowerLimitChromiumInterface):
    """
    *Lower limit of oxygen concentration* to promote a
    protective oxide film times the *Chromium concentration*
    raised to :math:`2/3` in liquid lead property class
    implementing the correlation by *gosse2014*.
    """
    @range_warning
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Returns the value of the *Oxygen concentration lower
        limit* to promote a protective oxide film times Chromium
        concentration raised to :math:`2/3` in liquid lead
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
            Oxygen concentration in :math:`[wt.\\%]`
        """
        return LowerLimitSaturationChromium().correlation(T, p)\
            * np.power(ChromiumSolubilityGosse2014().correlation(T, p), 2 / 3)

    @property
    def correlation_name(self) -> str:
        """
        str : Name of the correlation
        """
        return "gosse2014"

    @property
    def range(self) -> List[float]:
        """
        List[float] : Temperature validity range of the Oxygen concentration
        lower limit correlation function
        """
        return [673, 1000]


class LowerLimitChromiumVenkatraman1988(LowerLimitChromiumInterface):
    """
    *Lower limit of oxygen concentration* to promote a
    protective oxide film times the *Chromium concentration*
    raised to :math:`2/3` in liquid lead property class
    implementing the correlation by *venkatraman1988*.
    """
    @range_warning
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Returns the value of the *Oxygen concentration lower
        limit* to promote a protective oxide film times Chromium
        concentration raised to :math:`2/3` in liquid lead
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
            Oxygen concentration in :math:`[wt.\\%]`
        """
        return LowerLimitSaturationChromium().correlation(T, p)\
            * np.power(ChromiumSolubilityVenkatraman1988().correlation(T, p),
                       2 / 3)

    @property
    def correlation_name(self) -> str:
        """
        str : Name of the correlation
        """
        return "venkatraman1988"

    @property
    def range(self) -> List[float]:
        """
        List[float] : Temperature validity range of the Oxygen concentration
        lower limit correlation function
        """
        return [673, 1000]


class LowerLimitChromiumAlden1958(LowerLimitChromiumInterface):
    """
    *Lower limit of oxygen concentration* to promote a
    protective oxide film times the *Chromium concentration*
    raised to :math:`2/3` in liquid lead property class
    implementing the correlation by *alden1958*.
    """
    @range_warning
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Returns the value of the *Oxygen concentration lower
        limit* to promote a protective oxide film times Chromium
        concentration raised to :math:`2/3` in liquid lead
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
            Oxygen concentration in :math:`[wt.\\%]`
        """
        return LowerLimitSaturationChromium().correlation(T, p)\
            * np.power(ChromiumSolubilityAlden1958().correlation(T, p), 2 / 3)

    @property
    def correlation_name(self) -> str:
        """
        str : Name of the correlation
        """
        return "alden1958"

    @property
    def range(self) -> List[float]:
        """
        List[float] : Temperature validity range of the Oxygen concentration
        lower limit correlation function
        """
        return [673, 1000]


class LowerLimitNickel(PropertyInterface):
    """
    *Lower limit of oxygen concentration* to promote a
    protective oxide film times the *Nickel concentration*
    in liquid lead property class.
    """
    @range_warning
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Returns the value of the *Oxygen concentration lower
        limit* to promote a protective oxide film times Nickel
        concentration in liquid lead
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
            Oxygen concentration in :math:`[wt.\\%]`
        """
        return LowerLimitSaturationNickel().correlation(T, p)\
            * NickelSolubility().correlation(T, p)

    @property
    def name(self) -> str:
        """
        str : Name of the property
        """
        return "lim_ni"

    @property
    def units(self) -> str:
        """
        str : Oxygen concentration lower limit unit
        """
        return "[wt.%]"

    @property
    def range(self) -> List[float]:
        """
        List[float] : Temperature validity range of the Oxygen concentration
        lower limit correlation function
        """
        return [673, 917]

    @property
    def long_name(self) -> str:
        """
        str : Oxygen concentration lower limit long name
        """
        return ("Oxygen concentration lower limit times"
                " nickel concentration")

    @property
    def description(self) -> str:
        """
        str : Oxygen concentration lower limit description
        """
        return f"{self.long_name} in lead"


class LowerLimitIron(PropertyInterface):
    """
    *Lower limit of oxygen concentration* to promote a
    protective oxide film times the *Iron concentration*
    raised to :math:`3/4` in liquid lead property class.
    """
    def initialization_helper(self,
                              property_value: float) -> Union[None, float]:
        """
        Returns the temperature guess value according to the value
        of the lower limit of Oxygen concentration to promote a protective
        oxide film times the Iron concentration raised to :math:`3/4`
        in liquid lead passed as argument.
        It is used by the root finder algorithm.

        Parameters
        ----------
        property_value : float
            lower limit of Oxygen concentration to promote a
            protective oxide film times the Iron concentration
            raised to :math:`3/4` in liquid lead
            in :math:`[wt.\\%]`

        Returns
        -------
        float
            Temperature guess value in :math:`[K]`
        """
        if property_value < 1e-4:
            return 1300
        return 1700

    @range_warning
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Returns the value of the *Oxygen concentration lower
        limit* to promote a protective oxide film times Iron
        concentration raised to :math:`3/4` in liquid lead
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
            Oxygen concentration in :math:`[wt.\\%]`
        """
        return LowerLimitSaturationIron().correlation(T, p)\
            * np.power(IronSolubility().correlation(T, p), 0.75)

    @property
    def name(self) -> str:
        """
        str : Name of the property
        """
        return "lim_fe"

    @property
    def units(self) -> str:
        """
        str : Oxygen concentration lower limit unit
        """
        return "[wt.%]"

    @property
    def range(self) -> List[float]:
        """
        List[float] : Temperature validity range of the Oxygen concentration
        lower limit correlation function
        """
        return [673, 1000]

    @property
    def long_name(self) -> str:
        """
        str : Oxygen concentration lower limit long name
        """
        return ("Oxygen concentration lower limit times"
                " iron concentration raised to 3/4")

    @property
    def description(self) -> str:
        """
        str : Oxygen concentration lower limit description
        """
        return f"{self.long_name} in lead"


class LowerLimitSilicon(PropertyInterface):
    """
    *Lower limit of oxygen concentration* to promote a
    protective oxide film times the *Silicon concentration*
    raised to :math:`1/2` in liquid lead property class.
    """
    def initialization_helper(self,
                              property_value: float) -> Union[None, float]:
        """
        Returns the temperature guess value according to the value
        of the lower limit of Oxygen concentration to promote a protective
        oxide film times the Silicon concentration raised to :math:`1/2`
        in liquid lead passed as argument.
        It is used by the root finder algorithm.

        Parameters
        ----------
        property_value : float
            lower limit of Oxygen concentration to promote a
            protective oxide film times the Silicon concentration
            raised to :math:`1/2` in liquid lead
            in :math:`[wt.\\%]`

        Returns
        -------
        float
            Temperature guess value in :math:`[K]`
        """
        if property_value < 1e-8:
            return 1500
        return 1800

    @range_warning
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Returns the value of the *Oxygen concentration lower
        limit* to promote a protective oxide film times Silicon
        concentration raised to :math:`1/2` in liquid lead
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
            Oxygen concentration in :math:`[wt.\\%]`
        """
        return LowerLimitSaturationSilicon().correlation(T, p)\
            * np.power(SiliconSolubility().correlation(T, p), 0.5)

    @property
    def name(self) -> str:
        """
        str : Name of the property
        """
        return "lim_si"

    @property
    def units(self) -> str:
        """
        str : Oxygen concentration lower limit unit
        """
        return "[wt.%]"

    @property
    def range(self) -> List[float]:
        """
        List[float] : Temperature validity range of the Oxygen concentration
        lower limit correlation function
        """
        return [673, 1000]

    @property
    def long_name(self) -> str:
        """
        str : Oxygen concentration lower limit long name
        """
        return ("Oxygen concentration lower limit times"
                " silicon concentration raised to 1/2")

    @property
    def description(self) -> str:
        """
        str : Oxygen concentration lower limit description
        """
        return f"{self.long_name} in lead"
