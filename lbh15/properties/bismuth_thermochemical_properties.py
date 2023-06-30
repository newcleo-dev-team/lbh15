"""Module with the definition of chemical property objects
for bismuth"""
import numpy as np
from scipy.constants import atm, R
from lbh15.properties.interface import PropertyInterface, range_warning


class IronSolubilityInterface(PropertyInterface):
    """
    Iron solubility in liquid bismuth property class
    """
    @property
    def name(self):
        """
        str : name of the property
        """
        return "fe_sol"

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
        return "iron solubility"

    @property
    def description(self):
        """
        str : property description
        """
        return f"{self.long_name} in liquid bismuth"


class fe_sol_gosse2014(IronSolubilityInterface):
    """
    Iron solubility in liquid bismuth property class
    implementing correlation by gosse2014
    """
    @range_warning
    def correlation(self, T, p=atm, verbose=False):
        """
        Correlation used to compute iron solubility in liquid bismuth

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
        solubility [wt.%] : float
        """

        return np.exp((2.20-3930/T)*np.log(10))

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
        return [545.0, 1173.0]


class fe_sol_massalski1990(IronSolubilityInterface):
    """
    Iron solubility in liquid bismuth property class
    implementing correlation by massalski1990
    """
    @range_warning
    def correlation(self, T, p=atm, verbose=False):
        """
        Correlation used to compute iron solubility in liquid bismuth

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
        solubility [wt.%] : float
        """

        return np.exp((2.18-3980/T)*np.log(10))

    @property
    def correlation_name(self):
        """
        str : name of the correlation
        """
        return "massalski1990"

    @property
    def range(self):
        """
        list : temperature validity range for property correlation
        """
        return [973.0, 1173.0]


class fe_sol_weeks1998(IronSolubilityInterface):
    """
    Iron solubility in liquid bismuth property class
    implementing correlation by weeks1998
    """
    @range_warning
    def correlation(self, T, p=atm, verbose=False):
        """
        Correlation used to compute iron solubility in liquid bismuth

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
        solubility [wt.%] : float
        """

        return np.exp((1.832-3589/T)*np.log(10))

    @property
    def correlation_name(self):
        """
        str : name of the correlation
        """
        return "weeks1998"

    @property
    def range(self):
        """
        list : temperature validity range for property correlation
        """
        return [713.0, 998.0]


class NickelSolubilityInterface(PropertyInterface):
    """
    Nickel solubility in liquid bismuth property class
    """
    @property
    def name(self):
        """
        str : name of the property
        """
        return "ni_sol"

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
        return "nickel solubility"

    @property
    def description(self):
        """
        str : property description
        """
        return f"{self.long_name} in liquid bismuth"


class ni_sol_weeks1998(NickelSolubilityInterface):
    """
    Nickel solubility in liquid bismuth property class
    implementing correlation by weeks1998
    """
    @range_warning
    def correlation(self, T, p=atm, verbose=False):
        """
        Correlation used to compute nickel solubility in liquid bismuth

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
        solubility [wt.%] : float
        """

        return np.exp((2.61-1538/T)*np.log(10))

    @property
    def correlation_name(self):
        """
        str : name of the correlation
        """
        return "weeks1998"

    @property
    def range(self):
        """
        list : temperature validity range for property correlation
        """
        return [723.0, 903.0]


class ni_sol_gosse2014(NickelSolubilityInterface):
    """
    Nickel solubility in liquid bismuth property class
    implementing correlation by gosse2014
    """
    @range_warning
    def correlation(self, T, p=atm, verbose=False):
        """
        Correlation used to compute nickel solubility in liquid bismuth

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
        solubility [wt.%] : float
        """
        if T <= 738:
            rvalue = np.exp((3.81-2429/T)*np.log(10))
        elif 738 < T <= 918:
            rvalue = np.exp((2.05-1131/T)*np.log(10))
        else:
            rvalue = np.exp((1.35-484/T)*np.log(10))
        return rvalue

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
        return [543.0, 1173.0]


class ChromiumSolubilityInterface(PropertyInterface):
    """
    Chromium solubility in liquid bismuth property class
    """
    @property
    def name(self):
        """
        str : name of the property
        """
        return "cr_sol"

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
        return "chromium solubility"

    @property
    def description(self):
        """
        str : property description
        """
        return f"{self.long_name} in liquid bismuth"


class cr_sol_venkatraman1988(ChromiumSolubilityInterface):
    """
    Chromium solubility in liquid bismuth property class
    implementing correlation by venkatraman1988
    """
    @range_warning
    def correlation(self, T, p=atm, verbose=False):
        """
        Correlation used to compute chromium solubility in liquid bismuth

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
        solubility [wt.%] : float
        """

        return np.exp((2.34-3610/T)*np.log(10))

    @property
    def correlation_name(self):
        """
        str : name of the correlation
        """
        return "venkatraman1988"

    @property
    def range(self):
        """
        list : temperature validity range for property correlation
        """
        return [658.0, 901.0]


class cr_sol_weeks1998(ChromiumSolubilityInterface):
    """
    Chromium solubility in liquid bismuth property class
    implementing correlation by weeks1998
    """
    @range_warning
    def correlation(self, T, p=atm, verbose=False):
        """
        Correlation used to compute chromium solubility in liquid bismuth

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
        solubility [wt.%] : float
        """

        return np.exp((2.5-3717/T)*np.log(10))

    @property
    def correlation_name(self):
        """
        str : name of the correlation
        """
        return "weeks1998"

    @property
    def range(self):
        """
        list : temperature validity range for property correlation
        """
        return [663.0, 998.0]


class cr_sol_gosse2014(ChromiumSolubilityInterface):
    """
    Chromium solubility in liquid bismuth property class
    implementing correlation by gosse2014
    """
    @range_warning
    def correlation(self, T, p=atm, verbose=False):
        """
        Correlation used to compute chromium solubility in liquid bismuth

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
        solubility [wt.%] : float
        """

        return np.exp((2.34-3610/T)*np.log(10))

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
        return [545.0, 1773.0]
