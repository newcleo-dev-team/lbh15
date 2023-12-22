"""Module with the definition of the *Oxygen concentration lower limits*
objects for *lead-bismuth eutectic* (*lbe*)."""
from typing import List
from typing import Union
import numpy as np
from scipy.constants import atm
from scipy.constants import R
from ..interface import PropertyInterface
from .solubility_in_lbe import OxygenSolubility
from .solubility_in_lbe import ChromiumSolubilityGosse2014
from .solubility_in_lbe import ChromiumSolubilityCourouau2004
from .solubility_in_lbe import ChromiumSolubilityMartynov1998
from .solubility_in_lbe import NickelSolubilityGosse2014
from .solubility_in_lbe import NickelSolubilityMartinelli2010
from .solubility_in_lbe import IronSolubilityGosse2014
from .solubility_in_lbe import IronSolubilityWeeks1969
from .lbe_thermochemical import LeadChemicalActivity
from ..._decorators import range_warning


class LowerLimitSaturationIron(PropertyInterface):
    """
    *Lower limit of Oxygen concentration* to promote a
    protective oxide film in liquid lbe considering
    *Iron at its saturation concentration* property class.
    """
    def initialization_helper(self,
                              property_value: float) -> Union[None, float]:
        """
        Returns the temperature guess value according to the value
        of the lower limit of Oxygen concentration to promote a protective
        oxide film in liquid lbe considering Iron at its saturation
        concentration passed as argument.
        It is used by the root finder algorithm.

        Parameters
        ----------
        property_value : float
            lower limit of Oxygen concentration to promote a
            protective oxide film in liquid lbe considering
            Iron at its saturation concentration
            in :math:`[wt.\\%]`

        Returns
        -------
        float
            Temperature guess value in :math:`[K]`
        """
        return 1700

    @range_warning
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Returns the value of the *Oxygen concentration lower
        limit* to promote a protective oxide film in liquid lbe
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
            * OxygenSolubility().correlation(T, p)\
            * LeadChemicalActivity().correlation(T, p)

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
                "iron at its saturation concentration")

    @property
    def description(self) -> str:
        """
        str : Oxygen concentration lower limit description
        """
        return f"{self.long_name} in liquid lbe"


class LowerLimitSaturationChromium(PropertyInterface):
    """
    *Lower limit of Oxygen concentration* to promote a
    protective oxide film in liquid lbe considering
    *Chromium at its saturation concentration* property class.
    """
    def initialization_helper(self,
                              property_value: float) -> Union[None, float]:
        """
        Returns the temperature guess value according to the value
        of the lower limit of Oxygen concentration to promote a protective
        oxide film in liquid lbe considering Chromium at its saturation
        concentration passed as argument.
        It is used by the root finder algorithm.

        Parameters
        ----------
        property_value : float
            lower limit of Oxygen concentration to promote a
            protective oxide film in liquid lbe considering
            Chromium at its saturation concentration
            in :math:`[wt.\\%]`

        Returns
        -------
        float
            Temperature guess value in :math:`[K]`
        """
        return 1700

    @range_warning
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Returns the value of the *Oxygen concentration lower
        limit* to promote a protective oxide film in liquid lbe
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
            * OxygenSolubility().correlation(T, p)\
            * LeadChemicalActivity().correlation(T, p)

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
                "chromium at its saturation concentration")

    @property
    def description(self) -> str:
        """
        str : Oxygen concentration lower limit description
        """
        return f"{self.long_name} in lbe"


class LowerLimitSaturationNickel(PropertyInterface):
    """
    *Lower limit of Oxygen concentration* to promote a
    protective oxide film in liquid lbe considering
    *Nickel at its saturation concentration* property class.
    """
    @range_warning
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Returns the value of the *Oxygen concentration lower
        limit* to promote a protective oxide film in liquid lbe
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
            * OxygenSolubility().correlation(T, p)\
            * LeadChemicalActivity().correlation(T, p)

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
        return f"{self.long_name} in liquid lbe"


class LowerLimitSaturationSilicon(PropertyInterface):
    """
    *Lower limit of Oxygen concentration* to promote a
    protective oxide film in liquid lbe considering
    *Silicon at its saturation concentration* property class.
    """
    def initialization_helper(self,
                              property_value: float) -> Union[None, float]:
        """
        Returns the temperature guess value according to the value
        of the lower limit of Oxygen concentration to promote a protective
        oxide film in liquid lbe considering Silicon at its saturation
        concentration passed as argument.
        It is used by the root finder algorithm.

        Parameters
        ----------
        property_value : float
            lower limit of Oxygen concentration to promote a
            protective oxide film in liquid lbe considering
            Silicon at its saturation concentration
            in :math:`[wt.\\%]`

        Returns
        -------
        float
            Temperature guess value in :math:`[K]`
        """
        if property_value < 1e-9:
            return 1400
        return 1700

    @range_warning
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Returns the value of the *Oxygen concentration lower
        limit* to promote a protective oxide film in liquid lbe
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
            * OxygenSolubility().correlation(T, p)\
            * LeadChemicalActivity().correlation(T, p)

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
        return f"{self.long_name} in liquid lbe"


class LowerLimitSaturationAluminium(PropertyInterface):
    """
    *Lower limit of Oxygen concentration* to promote a
    protective oxide film in liquid lbe considering
    *Aluminium at its saturation concentration* property class.
    """
    def initialization_helper(self,
                              property_value: float) -> Union[None, float]:
        """
        Returns the temperature guess value according to the value
        of the lower limit of Oxygen concentration to promote a protective
        oxide film in liquid lbe considering Aluminium at its saturation
        concentration passed as argument.
        It is used by the root finder algorithm.

        Parameters
        ----------
        property_value : float
            lower limit of Oxygen concentration to promote a
            protective oxide film in liquid lbe considering
            Aluminium at its saturation concentration
            in :math:`[wt.\\%]`

        Returns
        -------
        float
            Temperature guess value in :math:`[K]`
        """
        if property_value < 1e-11:
            return 1500
        return 1800

    @range_warning
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Returns the value of the *Oxygen concentration lower
        limit* to promote a protective oxide film in liquid lbe
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
            * OxygenSolubility().correlation(T, p)\
            * LeadChemicalActivity().correlation(T, p)

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
        return f"{self.long_name} in liquid lbe"


class LowerLimitChromiumInterface(PropertyInterface):
    """
    *Lower limit of oxygen concentration* to promote a
    protective oxide film times the *Chromium concentration*
    raised to :math:`2/3` in liquid lbe property abstract class.
    """
    def initialization_helper(self,
                              property_value: float) -> Union[None, float]:
        """
        Returns the temperature guess value according to the value
        of the lower limit of Oxygen concentration to promote a protective
        oxide film times the Chromium concentration raised to :math:`2/3`
        in liquid lbe passed as argument.
        It is used by the root finder algorithm.

        Parameters
        ----------
        property_value : float
            lower limit of Oxygen concentration to promote a
            protective oxide film times the Chromium concentration
            raised to :math:`2/3` in liquid lbe
            in :math:`[wt.\\%]`

        Returns
        -------
        float
            Temperature guess value in :math:`[K]`
        """
        if property_value < 1e-7:
            return 1400
        return 1700

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
        return f"{self.long_name} in lbe"


class LowerLimitChromiumGosse2014(LowerLimitChromiumInterface):
    """
    *Lower limit of oxygen concentration* to promote a
    protective oxide film times the *Chromium concentration*
    raised to :math:`2/3` in liquid lbe property class
    implementing the correlation by *gosse2014*.
    """
    @range_warning
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Returns the value of the *Oxygen concentration lower
        limit* to promote a protective oxide film times Chromium
        concentration raised to :math:`2/3` in liquid lbe
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


class LowerLimitChromiumCourouau2004(LowerLimitChromiumInterface):
    """
    *Lower limit of oxygen concentration* to promote a
    protective oxide film times the *Chromium concentration*
    raised to :math:`2/3` in liquid lbe property class
    implementing the correlation by *courouau2004*.
    """
    @range_warning
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Returns the value of the *Oxygen concentration lower
        limit* to promote a protective oxide film times Chromium
        concentration raised to :math:`2/3` in liquid lbe
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
            * np.power(ChromiumSolubilityCourouau2004().correlation(T, p),
                       2 / 3)

    @property
    def correlation_name(self) -> str:
        """
        str : Name of the correlation
        """
        return "courouau2004"

    @property
    def range(self) -> List[float]:
        """
        List[float] : Temperature validity range of the Oxygen concentration
        lower limit correlation function
        """
        return [673, 813]


class LowerLimitChromiumMartynov1998(LowerLimitChromiumInterface):
    """
    *Lower limit of oxygen concentration* to promote a
    protective oxide film times the *Chromium concentration*
    raised to :math:`2/3` in liquid lbe property class
    implementing the correlation by *martynov1998*.
    """
    @range_warning
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Returns the value of the *Oxygen concentration lower
        limit* to promote a protective oxide film times Chromium
        concentration raised to :math:`2/3` in liquid lbe
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
            * np.power(ChromiumSolubilityMartynov1998().correlation(T, p),
                       2 / 3)

    @property
    def correlation_name(self) -> str:
        """
        str : Name of the correlation
        """
        return "martynov1998"

    @property
    def range(self) -> List[float]:
        """
        List[float] : Temperature validity range of the Oxygen concentration
        lower limit correlation function
        """
        return [673, 773]


class LowerLimitNickelInterface(PropertyInterface):
    """
    *Lower limit of oxygen concentration* to promote a
    protective oxide film times the *Nickel concentration*
    in liquid lbe property abstract class.
    """
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
    def long_name(self) -> str:
        """
        str : Oxygen concentration lower limit long name
        """
        return ("Oxygen concentration lower limit times"
                "nickel concentration")

    @property
    def description(self) -> str:
        """
        str : Oxygen concentration lower limit description
        """
        return f"{self.long_name} in lbe"


class LowerLimitNickelMartinelli2010(LowerLimitNickelInterface):
    """
    *Lower limit of oxygen concentration* to promote a
    protective oxide film times the *Nickel concentration*
    in liquid lbe property class
    implementing the correlation by *martinelli2010*.
    """
    @range_warning
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> Union[float, np.ndarray]:
        """
        Returns the value of the *Oxygen concentration lower
        limit* to promote a protective oxide film times Nickel
        concentration in liquid lbe
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
            * NickelSolubilityMartinelli2010().correlation(T, p)

    @property
    def correlation_name(self) -> str:
        """
        str : Name of the correlation
        """
        return "martinelli2010"

    @property
    def range(self) -> List[float]:
        """
        List[float] : Temperature validity range of the Oxygen concentration
        lower limit correlation function
        """
        return [673, 1000]


class LowerLimitNickelGosse2014(LowerLimitNickelInterface):
    """
    *Lower limit of oxygen concentration* to promote a
    protective oxide film times the *Nickel concentration*
    in liquid lbe property class
    implementing the correlation by *gosse2014*.
    """
    @range_warning
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> Union[float, np.ndarray]:
        """
        Returns the value of the *Oxygen concentration lower
        limit* to promote a protective oxide film times Nickel
        concentration in liquid lbe
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
            * NickelSolubilityGosse2014().correlation(T, p)

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


class LowerLimitIronInterface(PropertyInterface):
    """
    *Lower limit of oxygen concentration* to promote a
    protective oxide film times the *Iron concentration*
    raised to :math:`3/4` in liquid lbe property abstract class.
    """
    def initialization_helper(self,
                              property_value: float) -> Union[None, float]:
        """
        Returns the temperature guess value according to the value
        of the lower limit of Oxygen concentration to promote a protective
        oxide film times the Iron concentration raised to :math:`3/4`
        in liquid lbe passed as argument.
        It is used by the root finder algorithm.

        Parameters
        ----------
        property_value : float
            lower limit of Oxygen concentration to promote a
            protective oxide film times the Iron concentration
            raised to :math:`3/4` in liquid lbe
            in :math:`[wt.\\%]`

        Returns
        -------
        float
            Temperature guess value in :math:`[K]`
        """
        if property_value < 1e-6:
            return 1200
        return 1700

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
        return f"{self.long_name} in lbe"


class LowerLimitIronGosse2014(LowerLimitIronInterface):
    """
    *Lower limit of oxygen concentration* to promote a
    protective oxide film times the *Iron concentration*
    raised to :math:`3/4` in liquid lbe property class
    implementing the correlation by *gosse2014*.
    """
    @range_warning
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Returns the value of the *Oxygen concentration lower
        limit* to promote a protective oxide film times Iron
        concentration raised to :math:`3/4` in liquid lbe
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
            * np.power(IronSolubilityGosse2014().correlation(T, p), 0.75)

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


class LowerLimitIronWeeks1969(LowerLimitIronInterface):
    """
    *Lower limit of oxygen concentration* to promote a
    protective oxide film times the *Iron concentration*
    raised to :math:`3/4` in liquid lbe property class
    implementing the correlation by *weeks1969*.
    """
    @range_warning
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Returns the value of the *Oxygen concentration lower
        limit* to promote a protective oxide film times Iron
        concentration raised to :math:`3/4` in liquid lbe
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
            * np.power(IronSolubilityWeeks1969().correlation(T, p), 0.75)

    @property
    def correlation_name(self) -> str:
        """
        str : Name of the correlation
        """
        return "weeks1969"

    @property
    def range(self) -> List[float]:
        """
        List[float] : Temperature validity range of the Oxygen concentration
        lower limit correlation function
        """
        return [673, 1000]
