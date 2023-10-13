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
        o_sol_obj = OxygenSolubility()
        return np.exp((-114380/(2*R*T))-(42.2/(2*R))
                      + np.log(o_sol_obj.correlation(T, p)))

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
            rvalue = 650
        else:
            rvalue = 1700

        return rvalue

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
        o_sol_obj = OxygenSolubility()
        return np.exp((-317800/(2*R*T))-(27.3/(2*R))
                      + np.log(o_sol_obj.correlation(T, p)))

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
        o_sol_obj = OxygenSolubility()
        return np.exp((-36080/(2*R*T))-(23.4/(2*R))
                      + np.log(o_sol_obj.correlation(T, p)))

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
            rvalue = 650
        else:
            rvalue = 1700

        return rvalue

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
        o_sol_obj = OxygenSolubility()
        return np.exp((-471710/(2*R*T))-(19.5/(2*R))
                      + np.log(o_sol_obj.correlation(T, p)))

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
            rvalue = 650
        else:
            rvalue = 1700

        return rvalue

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
        o_sol_obj = OxygenSolubility()
        return np.exp((-679540/(2*R*T))-(-10.7/(2*R))
                      + np.log(o_sol_obj.correlation(T, p)))

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
            rvalue = 650
        else:
            rvalue = 1700

        return rvalue

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
        lim_cr_sat_obj = LowerLimitSaturationChromium()
        cr_sol_obj = ChromiumSolubilityGosse2014()
        return (np.exp((2/3)*np.log(cr_sol_obj.correlation(T, p)))
                * lim_cr_sat_obj.correlation(T, p))

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
        lim_cr_sat_obj = LowerLimitSaturationChromium()
        cr_sol_obj = ChromiumSolubilityVenkatraman1988()
        return (np.exp((2/3)*np.log(cr_sol_obj.correlation(T, p)))
                * lim_cr_sat_obj.correlation(T, p))

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
        lim_cr_sat_obj = LowerLimitSaturationChromium()
        cr_sol_obj = ChromiumSolubilityAlden1958()
        return (np.exp((2/3)*np.log(cr_sol_obj.correlation(T, p)))
                * lim_cr_sat_obj.correlation(T, p))

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
        lim_ni_sat_obj = LowerLimitSaturationNickel()
        ni_sol_obj = NickelSolubility()
        return (np.exp(np.log(ni_sol_obj.correlation(T, p)))
                * lim_ni_sat_obj.correlation(T, p))

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
            rvalue = 650
        else:
            rvalue = 1700

        return rvalue

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
        lim_fe_sat_obj = LowerLimitSaturationIron()
        fe_sol_obj = IronSolubility()
        return (np.exp((3/4)*np.log(fe_sol_obj.correlation(T, p)))
                * lim_fe_sat_obj.correlation(T, p))

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
            rvalue = 650
        else:
            rvalue = 1700

        return rvalue

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
        lim_si_sat_obj = LowerLimitSaturationSilicon()
        si_sol_obj = SiliconSolubility()
        return (np.exp((1/2)*np.log(si_sol_obj.correlation(T, p)))
                * lim_si_sat_obj.correlation(T, p))

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
