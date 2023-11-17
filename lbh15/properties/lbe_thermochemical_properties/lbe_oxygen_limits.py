"""Module with the definition of oxygen
concentration limits objects for lead-bismuth eutectic"""
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
from ..._decorators import typecheck_for_method


class LowerLimitSaturationIron(PropertyInterface):
    """
    Lower limit of oxygen concentration to promote a
    protective oxide film in liquid lead-bismuth
    eutectic considering iron is at its saturation
    concentration property class
    """
    @range_warning
    @typecheck_for_method
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Correlation used to compute oxygen concentration lower
        limit to promote a protective oxide film in liquid
        lead-bismuth eutectic considering iron is at its
        saturation concentration

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
        concentration [wt.%] : float
        """
        return np.exp(-57190 / R / T - 21.1 / R
                      + np.log(OxygenSolubility().correlation(T, p))
                      + np.log(LeadChemicalActivity().correlation(T, p)))

    @property
    def name(self) -> str:
        """
        str : name of the property
        """
        return "lim_fe_sat"

    @property
    def units(self) -> str:
        """
        str : property units
        """
        return "[wt.%]"

    @property
    def range(self) -> List[float]:
        """
        list : temperature validity range for property correlation
        """
        return [673, 1000]

    @property
    def long_name(self) -> str:
        """
        str : property long name
        """
        return ("Oxygen concentration lower limit for"
                "iron at its saturation concentration")

    @property
    def description(self) -> str:
        """
        str : property description
        """
        return f"{self.long_name} in liquid lbe"


class LowerLimitSaturationChromium(PropertyInterface):
    """
    Lower limit of oxygen concentration to promote a
    protective oxide film in liquid lead-bismuth
    eutectic considering chromium is at its saturation
    concentration property class
    """
    @typecheck_for_method
    def initialization_helper(self,
                              property_value: float) -> Union[None, float]:
        """
        Returns a temperature guess according to the value
        of the lower limit of oxygen concentration to promote a
        protective oxide film in liquid lead-bismuth eutectic considering
        chromium is at its saturation concentration

        Parameters
        ----------
        property_value : float
            lower limit of oxygen concentration to promote a
            protective oxide film in liquid lead-bismuth eutectic considering
            chromium is at its saturation concentration in [wt.%]
        verbose : bool, optional
            True to tell decorator to print warning about
            range check failing, False otherwise. By default False

        Returns
        -------
        rvalue : float
            Temperature guess in [K]
        """
        if property_value < 1e-7:
            return 650
        return 1700

    @range_warning
    @typecheck_for_method
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Correlation used to compute oxygen concentration lower
        limit to promote a protective oxide film in liquid
        lead-bismuth eutectic considering chromium is at
        its saturation concentration

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
        concentration [wt.%] : float
        """
        return np.exp(-158900 / R / T - 13.65 / R
                      + np.log(OxygenSolubility().correlation(T, p))
                      + np.log(LeadChemicalActivity().correlation(T, p)))

    @property
    def name(self) -> str:
        """
        str : name of the property
        """
        return "lim_cr_sat"

    @property
    def units(self) -> str:
        """
        str : property units
        """
        return "[wt.%]"

    @property
    def range(self) -> List[float]:
        """
        list : temperature validity range for property correlation
        """
        return [673, 1000]

    @property
    def long_name(self) -> str:
        """
        str : property long name
        """
        return ("Oxygen concentration lower limit for"
                "chromium at its saturation concentration")

    @property
    def description(self) -> str:
        """
        str : property description
        """
        return f"{self.long_name} in lbe"


class LowerLimitSaturationNickel(PropertyInterface):
    """
    Lower limit of oxygen concentration to promote a
    protective oxide film in liquid lead-bismuth
    eutectic considering nickel is at its saturation
    concentration property class
    """
    @range_warning
    @typecheck_for_method
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Correlation used to compute oxygen concentration lower
        limit to promote a protective oxide film in liquid
        lead-bismuth eutectic considering nickel is at its
        saturation concentration

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
        concentration [wt.%] : float
        """
        return np.exp(-18040 / R / T - 11.7 / R
                      + np.log(OxygenSolubility().correlation(T, p))
                      + np.log(LeadChemicalActivity().correlation(T, p)))

    @property
    def name(self) -> str:
        """
        str : name of the property
        """
        return "lim_ni_sat"

    @property
    def units(self) -> str:
        """
        str : property units
        """
        return "[wt.%]"

    @property
    def range(self) -> List[float]:
        """
        list : temperature validity range for property correlation
        """
        return [673, 1000]

    @property
    def long_name(self) -> str:
        """
        str : property long name
        """
        return ("Oxygen concentration lower limit for"
                " nickel at its saturation concentration")

    @property
    def description(self) -> str:
        """
        str : property description
        """
        return f"{self.long_name} in liquid lbe"


class LowerLimitSaturationSilicon(PropertyInterface):
    """
    Lower limit of oxygen concentration to promote a
    protective oxide film in liquid lead-bismuth
    eutectic considering silicon is at its saturation
    concentration property class
    """
    @typecheck_for_method
    def initialization_helper(self,
                              property_value: float) -> Union[None, float]:
        """
        Returns a temperature guess according to the value
        of the lower limit of oxygen concentration to promote a
        protective oxide film in liquid lead-bismuth eutectic considering
        silicon is at its saturation concentration

        Parameters
        ----------
        property_value : float
            lower limit of oxygen concentration to promote a
            protective oxide film in liquid lead-bismuth eutectic considering
            silicon is at its saturation concentration in [wt.%]
        verbose : bool, optional
            True to tell decorator to print warning about
            range check failing, False otherwise. By default False

        Returns
        -------
        rvalue : float
            Temperature guess in [K]
        """
        if property_value < 1e-9:
            return 650
        return 1700

    @range_warning
    @typecheck_for_method
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Correlation used to compute oxygen concentration lower
        limit to promote a protective oxide film in liquid
        lead-bismuth eutectic considering silicon is at its
        saturation concentration

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
        concentration [wt.%] : float
        """
        return np.exp(-235855 / R / T - 9.75 / R
                      + np.log(OxygenSolubility().correlation(T, p))
                      + np.log(LeadChemicalActivity().correlation(T, p)))

    @property
    def name(self) -> str:
        """
        str : name of the property
        """
        return "lim_si_sat"

    @property
    def units(self) -> str:
        """
        str : property units
        """
        return "[wt.%]"

    @property
    def range(self) -> List[float]:
        """
        list : temperature validity range for property correlation
        """
        return [673, 1000]

    @property
    def long_name(self) -> str:
        """
        str : property long name
        """
        return ("Oxygen concentration lower limit for"
                " silicon at its saturation concentration")

    @property
    def description(self) -> str:
        """
        str : property description
        """
        return f"{self.long_name} in liquid lbe"


class LowerLimitSaturationAluminium(PropertyInterface):
    """
    Lower limit of oxygen concentration to promote a
    protective oxide film in liquid lead-bismuth
    eutectic considering aluminium is at its saturation
    concentration property class
    """
    @typecheck_for_method
    def initialization_helper(self,
                              property_value: float) -> Union[None, float]:
        """
        Returns a temperature guess according to the value
        of the lower limit of oxygen concentration to promote a
        protective oxide film in liquid lead-bismuth eutectic considering
        aluminium is at its saturation concentration

        Parameters
        ----------
        property_value : float
            lower limit of oxygen concentration to promote a
            protective oxide film in liquid lead-bismuth eutectic considering
            aluminium is at its saturation concentration in [wt.%]
        verbose : bool, optional
            True to tell decorator to print warning about
            range check failing, False otherwise. By default False

        Returns
        -------
        rvalue : float
            Temperature guess in [K]
        """
        if property_value < 1e-11:
            return 650
        return 1700

    @range_warning
    @typecheck_for_method
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Correlation used to compute oxygen concentration lower
        limit to promote a protective oxide film in liquid
        lead-bismuth eutectic considering aluminium is at its
        saturation concentration

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
        concentration [wt.%] : float
        """
        return np.exp(-339770 / R / T + 5.35 / R
                      + np.log(OxygenSolubility().correlation(T, p))
                      + np.log(LeadChemicalActivity().correlation(T, p)))

    @property
    def name(self) -> str:
        """
        str : name of the property
        """
        return "lim_al_sat"

    @property
    def units(self) -> str:
        """
        str : property units
        """
        return "[wt.%]"

    @property
    def range(self) -> List[float]:
        """
        list : temperature validity range for property correlation
        """
        return [673, 1000]

    @property
    def long_name(self) -> str:
        """
        str : property long name
        """
        return ("Oxygen concentration lower limit for"
                " aluminium at its saturation concentration")

    @property
    def description(self) -> str:
        """
        str : property description
        """
        return f"{self.long_name} in liquid lbe"


class LowerLimitChromiumInterface(PropertyInterface):
    """
    Lower limit of oxygen concentration to promote a
    protective oxide film times the chromium concentration
    raised to 2/3 in liquid lead-bismuth eutectic property class
    """
    @typecheck_for_method
    def initialization_helper(self,
                              property_value: float) -> Union[None, float]:
        """
        Returns a temperature guess according to the value
        of the lower limit of oxygen concentration to promote a
        protective oxide film times the chromium concentration
        raised to 2/3 in liquid lead-bismuth eutectic

        Parameters
        ----------
        property_value : float
            lower limit of oxygen concentration to promote a
            protective oxide film times the chromium concentration
            raised to 2/3 in liquid lead-bismuth eutectic in [wt.%]
        verbose : bool, optional
            True to tell decorator to print warning about
            range check failing, False otherwise. By default False

        Returns
        -------
        rvalue : float
            Temperature guess in [K]
        """
        if property_value < 1e-7:
            return 650
        return 1700

    @property
    def name(self) -> str:
        """
        str : name of the property
        """
        return "lim_cr"

    @property
    def units(self) -> str:
        """
        str : property units
        """
        return "[wt.%]"

    @property
    def long_name(self) -> str:
        """
        str : property long name
        """
        return ("Oxygen concentration lower limit times"
                " chromium concentration raised to 2/3")

    @property
    def description(self) -> str:
        """
        str : property description
        """
        return f"{self.long_name} in lbe"


class LowerLimitChromiumGosse2014(LowerLimitChromiumInterface):
    """
    Lower limit of oxygen concentration to promote a
    protective oxide film times the chromium concentration
    raised to 2/3 in liquid lead-bismuth eutectic property class
    implementing correlation by gosse2014
    """
    @range_warning
    @typecheck_for_method
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Correlation used to compute oxygen concentration lower
        limit to promote a protective oxide film times
        chromium concentration raised to 2/3 in liquid lead-bismuth eutectic

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
        concentration [wt.%] : float
        """
        return np.exp(
            2 / 3 *
            np.log(ChromiumSolubilityGosse2014().correlation(T, p)))\
            * LowerLimitSaturationChromium().correlation(T, p)

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
        return [673, 1000]


class LowerLimitChromiumCourouau2004(LowerLimitChromiumInterface):
    """
    Lower limit of oxygen concentration to promote a
    protective oxide film times the chromium concentration
    raised to 2/3 in liquid lead-bismuth eutectic property class
    implementing correlation by courouau2004
    """
    @range_warning
    @typecheck_for_method
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Correlation used to compute oxygen concentration lower
        limit to promote a protective oxide film times
        chromium concentration raised to 2/3 in liquid lead-bismuth eutectic

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
        concentration [wt.%] : float
        """
        return np.exp(
            2 / 3 *
            np.log(ChromiumSolubilityCourouau2004().correlation(T, p)))\
            * LowerLimitSaturationChromium().correlation(T, p)

    @property
    def correlation_name(self) -> str:
        """
        str : name of the correlation
        """
        return "courouau2004"

    @property
    def range(self) -> List[float]:
        """
        list : temperature validity range for property correlation
        """
        return [673, 813]


class LowerLimitChromiumMartynov1998(LowerLimitChromiumInterface):
    """
    Lower limit of oxygen concentration to promote a
    protective oxide film times the chromium concentration
    raised to 2/3 in liquid lead-bismuth eutectic property class
    implementing correlation by martynov1998
    """
    @range_warning
    @typecheck_for_method
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Correlation used to compute oxygen concentration lower
        limit to promote a protective oxide film times
        chromium concentration raised to 2/3 in liquid lead-bismuth eutectic

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
        concentration [wt.%] : float
        """
        return np.exp(
            2 / 3 *
            np.log(ChromiumSolubilityMartynov1998().correlation(T, p)))\
            * LowerLimitSaturationChromium().correlation(T, p)

    @property
    def correlation_name(self) -> str:
        """
        str : name of the correlation
        """
        return "martynov1998"

    @property
    def range(self) -> List[float]:
        """
        list : temperature validity range for property correlation
        """
        return [673, 773]


class LowerLimitNickelInterface(PropertyInterface):
    """
    Lower limit of oxygen concentration to promote a
    protective oxide film times the nickel concentration
    in liquid lead-bismuth eutectic property class
    """
    @property
    def name(self) -> str:
        """
        str : name of the property
        """
        return "lim_ni"

    @property
    def units(self) -> str:
        """
        str : property units
        """
        return "[wt.%]"

    @property
    def long_name(self) -> str:
        """
        str : property long name
        """
        return ("Oxygen concentration lower limit times"
                "nickel concentration")

    @property
    def description(self) -> str:
        """
        str : property description
        """
        return f"{self.long_name} in lbe"


class LowerLimitNickelMartinelli2010(LowerLimitNickelInterface):
    """
    Lower limit of oxygen concentration to promote a
    protective oxide film times the nickel concentration
    in liquid lead-bismuth eutectic property class
    implementing correlation by martinelli2010
    """
    @range_warning
    @typecheck_for_method
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Correlation used to compute oxygen concentration lower
        limit to promote a protective oxide film times
        nickel concentration in liquid lead-bismuth eutectic

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
        concentration [wt.%] : float
        """
        return np.exp(
            np.log(NickelSolubilityMartinelli2010().correlation(T, p)))\
            * LowerLimitSaturationNickel().correlation(T, p)

    @property
    def correlation_name(self) -> str:
        """
        str : name of the correlation
        """
        return "martinelli2010"

    @property
    def range(self) -> List[float]:
        """
        list : temperature validity range for property correlation
        """
        return [673, 1000]


class LowerLimitNickelGosse2014(LowerLimitNickelInterface):
    """
    Lower limit of oxygen concentration to promote a
    protective oxide film times the nickel concentration
    in liquid lead-bismuth eutectic property class
    implementing correlation by gosse2014
    """
    @range_warning
    @typecheck_for_method
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Correlation used to compute oxygen concentration lower
        limit to promote a protective oxide film times
        nickel concentration in liquid lead-bismuth eutectic

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
        concentration [wt.%] : float
        """
        return np.exp(
            np.log(NickelSolubilityGosse2014().correlation(T, p)))\
            * LowerLimitSaturationNickel().correlation(T, p)

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
        return [673, 1000]


class LowerLimitIronInterface(PropertyInterface):
    """
    Lower limit of oxygen concentration to promote a
    protective oxide film times the iron concentration
    raised to 3/4 in liquid lead-bismuth eutectic property class
    """
    @typecheck_for_method
    def initialization_helper(self,
                              property_value: float) -> Union[None, float]:
        """
        Returns a temperature guess according to the value
        of the lower limit of oxygen concentration to promote a
        protective oxide film times the iron concentration
        raised to 3/4 in liquid lead-bismuth eutectic

        Parameters
        ----------
        property_value : float
            lower limit of oxygen concentration to promote a
            protective oxide film times the iron concentration
            raised to 3/4 in liquid lead-bismuth eutectic in [wt.%]
        verbose : bool, optional
            True to tell decorator to print warning about
            range check failing, False otherwise. By default False

        Returns
        -------
        rvalue : float
            Temperature guess in [K]
        """
        if property_value < 1e-6:
            return 650
        return 1700

    @property
    def name(self) -> str:
        """
        str : name of the property
        """
        return "lim_fe"

    @property
    def units(self) -> str:
        """
        str : property units
        """
        return "[wt.%]"

    @property
    def long_name(self) -> str:
        """
        str : property long name
        """
        return ("Oxygen concentration lower limit times"
                " iron concentration raised to 3/4")

    @property
    def description(self) -> str:
        """
        str : property description
        """
        return f"{self.long_name} in lbe"


class LowerLimitIronGosse2014(LowerLimitIronInterface):
    """
    Lower limit of oxygen concentration to promote a
    protective oxide film times the iron concentration
    raised to 3/4 in liquid lead-bismuth eutectic property class
    implementing correlation by gosse2014
    """
    @range_warning
    @typecheck_for_method
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Correlation used to compute oxygen concentration lower
        limit to promote a protective oxide film times
        iron concentration raised to 3/4 in liquid lead-bismuth
        eutectic

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
        concentration [wt.%] : float
        """
        return np.exp(
            0.75 * np.log(IronSolubilityGosse2014().correlation(T, p)))\
            * LowerLimitSaturationIron().correlation(T, p)

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
        return [673, 1000]


class LowerLimitIronWeeks1969(LowerLimitIronInterface):
    """
    Lower limit of oxygen concentration to promote a
    protective oxide film times the iron concentration
    raised to 3/4 in liquid lead-bismuth eutectic property class
    implementing correlation by weeks1969
    """
    @range_warning
    @typecheck_for_method
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Correlation used to compute oxygen concentration lower
        limit to promote a protective oxide film times
        iron concentration raised to 3/4 in liquid lead-bismuth
        eutectic

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
        concentration [wt.%] : float
        """
        return np.exp(
            0.75 * np.log(IronSolubilityWeeks1969().correlation(T, p)))\
            * LowerLimitSaturationIron().correlation(T, p)

    @property
    def correlation_name(self) -> str:
        """
        str : name of the correlation
        """
        return "weeks1969"

    @property
    def range(self) -> List[float]:
        """
        list : temperature validity range for property correlation
        """
        return [673, 1000]
