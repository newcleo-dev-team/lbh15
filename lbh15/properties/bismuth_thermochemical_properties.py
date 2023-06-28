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
