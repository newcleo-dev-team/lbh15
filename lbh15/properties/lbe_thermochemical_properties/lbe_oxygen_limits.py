"""Module with the definition of oxygen
concentration limits objects for lead-bismuth eutectic"""
import numpy as np
from scipy.constants import atm, R
from ..interface import PropertyInterface, range_warning
from .solubility_in_lbe import OxygenSolubility
from .solubility_in_lbe import ChromiumSolubilityGosse2014
from .solubility_in_lbe import ChromiumSolubilityCourouau2004
from .solubility_in_lbe import ChromiumSolubilityMartynov1998
from .solubility_in_lbe import NickelSolubilityGosse2014
from .solubility_in_lbe import NickelSolubilityMartinelli2010
from .solubility_in_lbe import IronSolubilityGosse2014
from .solubility_in_lbe import IronSolubilityWeeks1969
from .lbe_thermochemical import LeadChemicalActivity


class LowerLimitSaturationIron(PropertyInterface):
    """
    Lower limit of oxygen concentration to promote a
    protective oxide film in liquid lead-bismuth
    eutectic considering iron is at its saturation
    concentration property class
    """
    @range_warning
    def correlation(self, T, p=atm, verbose=False):
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
        o_sol_obj = OxygenSolubility()
        pb_a_obj = LeadChemicalActivity()
        return np.exp((-114380/(2*R*T))-(42.2/(2*R))
                      + np.log(o_sol_obj.correlation(T, p))
                      + np.log(pb_a_obj.correlation(T, p)))

    @property
    def name(self):
        """
        str : name of the property
        """
        return "lim_fe_sat"

    @property
    def units(self):
        """
        str : property units
        """
        return "[wt.%]"

    @property
    def range(self):
        """
        list : temperature validity range for property correlation
        """
        return [673, 1000]

    @property
    def long_name(self):
        """
        str : property long name
        """
        return ("Oxygen concentration lower limit for"
                "iron at its saturation concentration")

    @property
    def description(self):
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
    @range_warning
    def correlation(self, T, p=atm, verbose=False):
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
        o_sol_obj = OxygenSolubility()
        pb_a_obj = LeadChemicalActivity()
        return np.exp((-317800/(2*R*T))-(27.3/(2*R))
                      + np.log(o_sol_obj.correlation(T, p))
                      + np.log(pb_a_obj.correlation(T, p)))

    @property
    def name(self):
        """
        str : name of the property
        """
        return "lim_cr_sat"

    @property
    def units(self):
        """
        str : property units
        """
        return "[wt.%]"

    @property
    def range(self):
        """
        list : temperature validity range for property correlation
        """
        return [673, 1000]

    @property
    def long_name(self):
        """
        str : property long name
        """
        return ("Oxygen concentration lower limit for"
                "chromium at its saturation concentration")

    @property
    def description(self):
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
    def correlation(self, T, p=atm, verbose=False):
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
        o_sol_obj = OxygenSolubility()
        pb_a_obj = LeadChemicalActivity()
        return np.exp((-36080/(2*R*T))-(23.4/(2*R))
                      + np.log(o_sol_obj.correlation(T, p))
                      + np.log(pb_a_obj.correlation(T, p)))

    @property
    def name(self):
        """
        str : name of the property
        """
        return "lim_ni_sat"

    @property
    def units(self):
        """
        str : property units
        """
        return "[wt.%]"

    @property
    def range(self):
        """
        list : temperature validity range for property correlation
        """
        return [673, 1000]

    @property
    def long_name(self):
        """
        str : property long name
        """
        return ("Oxygen concentration lower limit for"
                " nickel at its saturation concentration")

    @property
    def description(self):
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
    @range_warning
    def correlation(self, T, p=atm, verbose=False):
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
        o_sol_obj = OxygenSolubility()
        pb_a_obj = LeadChemicalActivity()
        return np.exp((-471710/(2*R*T))-(19.5/(2*R))
                      + np.log(o_sol_obj.correlation(T, p))
                      + np.log(pb_a_obj.correlation(T, p)))

    @property
    def name(self):
        """
        str : name of the property
        """
        return "lim_si_sat"

    @property
    def units(self):
        """
        str : property units
        """
        return "[wt.%]"

    @property
    def range(self):
        """
        list : temperature validity range for property correlation
        """
        return [673, 1000]

    @property
    def long_name(self):
        """
        str : property long name
        """
        return ("Oxygen concentration lower limit for"
                " silicon at its saturation concentration")

    @property
    def description(self):
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
    @range_warning
    def correlation(self, T, p=atm, verbose=False):
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
        o_sol_obj = OxygenSolubility()
        pb_a_obj = LeadChemicalActivity()
        return np.exp((-679540/(2*R*T))-(-10.7/(2*R))
                      + np.log(o_sol_obj.correlation(T, p))
                      + np.log(pb_a_obj.correlation(T, p)))

    @property
    def name(self):
        """
        str : name of the property
        """
        return "lim_al_sat"

    @property
    def units(self):
        """
        str : property units
        """
        return "[wt.%]"

    @property
    def range(self):
        """
        list : temperature validity range for property correlation
        """
        return [673, 1000]

    @property
    def long_name(self):
        """
        str : property long name
        """
        return ("Oxygen concentration lower limit for"
                " aluminium at its saturation concentration")

    @property
    def description(self):
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
    @property
    def name(self):
        """
        str : name of the property
        """
        return "lim_cr"

    @property
    def units(self):
        """
        str : property units
        """
        return "[wt.%]"

    @property
    def long_name(self):
        """
        str : property long name
        """
        return ("Oxygen concentration lower limit times"
                " chromium concentration raised to 2/3")

    @property
    def description(self):
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
    def correlation(self, T, p=atm, verbose=False):
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
        lim_cr_sat_obj = LowerLimitSaturationChromium()
        cr_sol_obj = ChromiumSolubilityGosse2014()
        return (np.exp((2/3)*np.log(cr_sol_obj.correlation(T, p)))
                * lim_cr_sat_obj.correlation(T, p))

    @property
    def correlation_name(self):
        """
        str : name of the correlation
        """
        return "gosse2014"

    @property
    def range(self):
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
    def correlation(self, T, p=atm, verbose=False):
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
        lim_cr_sat_obj = LowerLimitSaturationChromium()
        cr_sol_obj = ChromiumSolubilityCourouau2004()
        return (np.exp((2/3)*np.log(cr_sol_obj.correlation(T, p)))
                * lim_cr_sat_obj.correlation(T, p))

    @property
    def correlation_name(self):
        """
        str : name of the correlation
        """
        return "courouau2004"

    @property
    def range(self):
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
    def correlation(self, T, p=atm, verbose=False):
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
        lim_cr_sat_obj = LowerLimitSaturationChromium()
        cr_sol_obj = ChromiumSolubilityMartynov1998()
        return (np.exp((2/3)*np.log(cr_sol_obj.correlation(T, p)))
                * lim_cr_sat_obj.correlation(T, p))

    @property
    def correlation_name(self):
        """
        str : name of the correlation
        """
        return "martynov1998"

    @property
    def range(self):
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
    def name(self):
        """
        str : name of the property
        """
        return "lim_ni"

    @property
    def units(self):
        """
        str : property units
        """
        return "[wt.%]"

    @property
    def long_name(self):
        """
        str : property long name
        """
        return ("Oxygen concentration lower limit times"
                "nickel concentration")

    @property
    def description(self):
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
    def correlation(self, T, p=atm, verbose=False):
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
        lim_ni_sat_obj = LowerLimitSaturationNickel()
        ni_sol_obj = NickelSolubilityMartinelli2010()
        return (np.exp(np.log(ni_sol_obj.correlation(T, p)))
                * lim_ni_sat_obj.correlation(T, p))

    @property
    def correlation_name(self):
        """
        str : name of the correlation
        """
        return "martinelli2010"

    @property
    def range(self):
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
    def correlation(self, T, p=atm, verbose=False):
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
        lim_ni_sat_obj = LowerLimitSaturationNickel()
        ni_sol_obj = NickelSolubilityGosse2014()
        return (np.exp(np.log(ni_sol_obj.correlation(T, p)))
                * lim_ni_sat_obj.correlation(T, p))

    @property
    def correlation_name(self):
        """
        str : name of the correlation
        """
        return "gosse2014"

    @property
    def range(self):
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
    @property
    def name(self):
        """
        str : name of the property
        """
        return "lim_fe"

    @property
    def units(self):
        """
        str : property units
        """
        return "[wt.%]"

    @property
    def long_name(self):
        """
        str : property long name
        """
        return ("Oxygen concentration lower limit times"
                " iron concentration raised to 3/4")

    @property
    def description(self):
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
    def correlation(self, T, p=atm, verbose=False):
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
        lim_fe_sat_obj = LowerLimitSaturationIron()
        fe_sol_obj = IronSolubilityGosse2014()
        return (np.exp((3/4)*np.log(fe_sol_obj.correlation(T, p)))
                * lim_fe_sat_obj.correlation(T, p))

    @property
    def correlation_name(self):
        """
        str : name of the correlation
        """
        return "gosse2014"

    @property
    def range(self):
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
    def correlation(self, T, p=atm, verbose=False):
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
        lim_fe_sat_obj = LowerLimitSaturationIron()
        fe_sol_obj = IronSolubilityWeeks1969()
        return (np.exp((3/4)*np.log(fe_sol_obj.correlation(T, p)))
                * lim_fe_sat_obj.correlation(T, p))

    @property
    def correlation_name(self):
        """
        str : name of the correlation
        """
        return "weeks1969"

    @property
    def range(self):
        """
        list : temperature validity range for property correlation
        """
        return [673, 1000]
