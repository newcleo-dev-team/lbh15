"""Module with the definition of oxygen
concentration limits objects for lead"""
from typing import List
from typing import Union
import numpy as np
from scipy.constants import atm
from scipy.constants import R
from ..interface import PropertyInterface
from ..interface import range_warning
from .solubility_in_lead import OxygenSolubility
from .solubility_in_lead import ChromiumSolubilityGosse2014
from .solubility_in_lead import ChromiumSolubilityAlden1958
from .solubility_in_lead import ChromiumSolubilityVenkatraman1988
from .solubility_in_lead import NickelSolubility
from .solubility_in_lead import IronSolubility
from .solubility_in_lead import SiliconSolubility
from ..._decorators import typecheck_for_method


class LowerLimitSaturationIron(PropertyInterface):
    """
    Lower limit of oxygen concentration to promote a
    protective oxide film in liquid lead considering
    iron is at its saturation concentration property class
    """
    @range_warning
    @typecheck_for_method
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Correlation used to compute oxygen concentration lower
        limit to promote a protective oxide film in liquid lead
        considering iron is at its saturation concentration

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
                      + np.log(OxygenSolubility().correlation(T, p)))

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
                " iron at its saturation concentration")

    @property
    def description(self) -> str:
        """
        str : property description
        """
        return f"{self.long_name} in liquid lead"


class LowerLimitSaturationChromium(PropertyInterface):
    """
    Lower limit of oxygen concentration to promote a
    protective oxide film in liquid lead considering
    chromium is at its saturation concentration property class
    """
    @typecheck_for_method
    def initialization_helper(self,
                              property_value: float) -> Union[None, float]:
        """
        Returns a temperature guess according to the value
        of the lower limit of oxygen concentration to promote a
        protective oxide film in liquid lead considering
        chromium is at its saturation concentration

        Parameters
        ----------
        property_value : float
            lower limit of oxygen concentration to promote a
            protective oxide film in liquid lead considering
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
        limit to promote a protective oxide film in liquid lead
        considering chromium is at its saturation concentration

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
                      + np.log(OxygenSolubility().correlation(T, p)))

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
                " chromium at its saturation concentration")

    @property
    def description(self) -> str:
        """
        str : property description
        """
        return f"{self.long_name} in liquid lead"


class LowerLimitSaturationNickel(PropertyInterface):
    """
    Lower limit of oxygen concentration to promote a
    protective oxide film in liquid lead considering
    nickel is at its saturation concentration property class
    """
    @range_warning
    @typecheck_for_method
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Correlation used to compute oxygen concentration lower
        limit to promote a protective oxide film in liquid lead
        considering nickel is at its saturation concentration

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
                      + np.log(OxygenSolubility().correlation(T, p)))

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
        return f"{self.long_name} in liquid lead"


class LowerLimitSaturationSilicon(PropertyInterface):
    """
    Lower limit of oxygen concentration to promote a
    protective oxide film in liquid lead considering
    silicon is at its saturation concentration property class
    """
    @typecheck_for_method
    def initialization_helper(self,
                              property_value: float) -> Union[None, float]:
        """
        Returns a temperature guess according to the value
        of the lower limit of oxygen concentration to promote a
        protective oxide film in liquid lead considering
        silicon is at its saturation concentration

        Parameters
        ----------
        property_value : float
            lower limit of oxygen concentration to promote a
            protective oxide film in liquid lead considering
            silicon is at its saturation concentration in [wt.%]
        verbose : bool, optional
            True to tell decorator to print warning about
            range check failing, False otherwise. By default False

        Returns
        -------
        rvalue : float
            Temperature guess in [K]
        """
        if property_value < 1e-8:
            return 650
        return 1700

    @range_warning
    @typecheck_for_method
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Correlation used to compute oxygen concentration lower
        limit to promote a protective oxide film in liquid lead
        considering silicon is at its saturation concentration

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
                      + np.log(OxygenSolubility().correlation(T, p)))

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
        return f"{self.long_name} in liquid lead"


class LowerLimitSaturationAluminium(PropertyInterface):
    """
    Lower limit of oxygen concentration to promote a
    protective oxide film in liquid lead considering
    aluminium is at its saturation concentration property class
    """
    @typecheck_for_method
    def initialization_helper(self,
                              property_value: float) -> Union[None, float]:
        """
        Returns a temperature guess according to the value
        of the lower limit of oxygen concentration to promote a
        protective oxide film in liquid lead considering
        aluminium is at its saturation concentration

        Parameters
        ----------
        property_value : float
            lower limit of oxygen concentration to promote a
            protective oxide film in liquid lead considering
            aluminium is at its saturation concentration in [wt.%]
        verbose : bool, optional
            True to tell decorator to print warning about
            range check failing, False otherwise. By default False

        Returns
        -------
        rvalue : float
            Temperature guess in [K]
        """
        if property_value < 1e-10:
            return 650
        return 1700

    @range_warning
    @typecheck_for_method
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Correlation used to compute oxygen concentration lower
        limit to promote a protective oxide film in liquid lead
        considering aluminium is at its saturation concentration

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
                      + np.log(OxygenSolubility().correlation(T, p)))

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
        return f"{self.long_name} in liquid lead"


class LowerLimitChromiumInterface(PropertyInterface):
    """
    Lower limit of oxygen concentration to promote a
    protective oxide film times the chromium concentration
    raised to 2/3 in liquid lead property class
    """
    @typecheck_for_method
    def initialization_helper(self,
                              property_value: float) -> Union[None, float]:
        """
        Returns a temperature guess according to the value
        of the lower limit of oxygen concentration to promote a
        protective oxide film times the chromium concentration
        raised to 2/3 in liquid lead

        Parameters
        ----------
        property_value : float
            lower limit of oxygen concentration to promote a
            protective oxide film times the chromium concentration
            raised to 2/3 in liquid lead in [wt.%]
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
        return f"{self.long_name} in lead"


class LowerLimitChromiumGosse2014(LowerLimitChromiumInterface):
    """
    Lower limit of oxygen concentration to promote a
    protective oxide film times the chromium concentration
    raised to 2/3 in liquid lead property class
    implementing correlation by gosse2014
    """
    @range_warning
    @typecheck_for_method
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Correlation used to compute oxygen concentration lower
        limit to promote a protective oxide film times
        chromium concentration raised to 2/3 in liquid lead

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


class LowerLimitChromiumVenkatraman1988(LowerLimitChromiumInterface):
    """
    Lower limit of oxygen concentration to promote a
    protective oxide film times the chromium concentration
    raised to 2/3 in liquid lead property class
    implementing correlation by venkatraman1988
    """
    @range_warning
    @typecheck_for_method
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Correlation used to compute oxygen concentration lower
        limit to promote a protective oxide film times
        chromium concentration raised to 2/3 in liquid lead

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
            np.log(ChromiumSolubilityVenkatraman1988().correlation(T, p)))\
            * LowerLimitSaturationChromium().correlation(T, p)

    @property
    def correlation_name(self) -> str:
        """
        str : name of the correlation
        """
        return "venkatraman1988"

    @property
    def range(self) -> List[float]:
        """
        list : temperature validity range for property correlation
        """
        return [673, 1000]


class LowerLimitChromiumAlden1958(LowerLimitChromiumInterface):
    """
    Lower limit of oxygen concentration to promote a
    protective oxide film times the chromium concentration
    raised to 2/3 in liquid lead property class
    implementing correlation by alden1958
    """
    @range_warning
    @typecheck_for_method
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Correlation used to compute oxygen concentration lower
        limit to promote a protective oxide film times
        chromium concentration raised to 2/3 in liquid lead

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
            np.log(ChromiumSolubilityAlden1958().correlation(T, p)))\
            * LowerLimitSaturationChromium().correlation(T, p)

    @property
    def correlation_name(self) -> str:
        """
        str : name of the correlation
        """
        return "alden1958"

    @property
    def range(self) -> List[float]:
        """
        list : temperature validity range for property correlation
        """
        return [673, 1000]


class LowerLimitNickel(PropertyInterface):
    """
    Lower limit of oxygen concentration to promote a
    protective oxide film times the nickel concentration
    in liquid lead property class
    """
    @range_warning
    @typecheck_for_method
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Correlation used to compute oxygen concentration lower
        limit to promote a protective oxide film times
        nickel concentration in liquid lead

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
            np.log(NickelSolubility().correlation(T, p)))\
            * LowerLimitSaturationNickel().correlation(T, p)

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
    def range(self) -> List[float]:
        """
        list : temperature validity range for property correlation
        """
        return [673, 917]

    @property
    def long_name(self) -> str:
        """
        str : property long name
        """
        return ("Oxygen concentration lower limit times"
                " nickel concentration")

    @property
    def description(self) -> str:
        """
        str : property description
        """
        return f"{self.long_name} in lead"


class LowerLimitIron(PropertyInterface):
    """
    Lower limit of oxygen concentration to promote a
    protective oxide film times the iron concentration
    raised to 3/4 in liquid lead property class
    """
    @typecheck_for_method
    def initialization_helper(self,
                              property_value: float) -> Union[None, float]:
        """
        Returns a temperature guess according to the value
        of the lower limit of oxygen concentration to promote a
        protective oxide film times the iron concentration
        raised to 3/4 in liquid lead

        Parameters
        ----------
        property_value : float
            lower limit of oxygen concentration to promote a
            protective oxide film times the iron concentration
            raised to 3/4 in liquid lead in [wt.%]
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
        return 1700

    @range_warning
    @typecheck_for_method
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Correlation used to compute oxygen concentration lower
        limit to promote a protective oxide film times
        iron concentration raised to 3/4 in liquid lead

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
            0.75 * np.log(IronSolubility().correlation(T, p)))\
            * LowerLimitSaturationIron().correlation(T, p)

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
        return ("Oxygen concentration lower limit times"
                " iron concentration raised to 3/4")

    @property
    def description(self) -> str:
        """
        str : property description
        """
        return f"{self.long_name} in lead"


class LowerLimitSilicon(PropertyInterface):
    """
    Lower limit of oxygen concentration to promote a
    protective oxide film times the silicon concentration
    raised to 1/2 in liquid lead property class
    """
    @typecheck_for_method
    def initialization_helper(self,
                              property_value: float) -> Union[None, float]:
        """
        Returns a temperature guess according to the value
        of the lower limit of oxygen concentration to promote a
        protective oxide film times the silicon concentration
        raised to 1/2 in liquid lead

        Parameters
        ----------
        property_value : float
            lower limit of oxygen concentration to promote a
            protective oxide film times the silicon concentration
            raised to 1/2 in liquid lead in [wt.%]
        verbose : bool, optional
            True to tell decorator to print warning about
            range check failing, False otherwise. By default False

        Returns
        -------
        rvalue : float
            Temperature guess in [K]
        """
        if property_value < 1e-8:
            return 650
        return 1700

    @range_warning
    @typecheck_for_method
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Correlation used to compute oxygen concentration lower
        limit to promote a protective oxide film times
        silicon concentration raised to 1/2 in liquid lead

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
            0.5 * np.log(SiliconSolubility().correlation(T, p)))\
            * LowerLimitSaturationSilicon().correlation(T, p)

    @property
    def name(self) -> str:
        """
        str : name of the property
        """
        return "lim_si"

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
        return ("Oxygen concentration lower limit times"
                " silicon concentration raised to 1/2")

    @property
    def description(self) -> str:
        """
        str : property description
        """
        return f"{self.long_name} in lead"
