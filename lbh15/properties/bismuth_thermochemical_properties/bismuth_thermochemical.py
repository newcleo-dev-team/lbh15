"""Module with the definition of chemical property objects
for bismuth"""
import numpy as np
from scipy.constants import atm, R
from ..interface import PropertyInterface, range_warning
from ..bismuth_properties import h
from ..._commons import BISMUTH_BOILING_TEMPERATURE as T_b0
from ..._commons import BISMUTH_MELTING_TEMPERATURE as T_m0
from ..._commons import BISMUTH_MOLAR_MASS as M
from ..._commons import OXYGEN_MOLAR_MASS as M_O


class OxygenPartialPressureInterface(PropertyInterface):
    """
    Oxygen partial pressure in liquid bismuth divided by the
    oxygen concentration in liquid bismuth squared property class
    """
    @property
    def name(self):
        """
        str : name of the property
        """
        return "o_pp"

    @property
    def units(self):
        """
        str : property units
        """
        return "[atm.wt.%^-2]"

    @property
    def long_name(self):
        """
        str : property long name
        """
        return "oxygen partial pressure divided by the oxygen \
              concentration squared"

    @property
    def description(self):
        """
        str : property description
        """
        return f"{self.long_name} in liquid bismuth"


class OxygenPartialPressureFitzner1980(OxygenPartialPressureInterface):
    """
    Oxygen partial pressure in liquid bismuth divided by the
    oxygen concentration in liquid bismuth squared property
    class implementing correlation by fitzner1980
    """
    @range_warning
    def correlation(self, T, p=atm, verbose=False):
        """
        Correlation used to compute oxygen partial pressure in liquid
        bismuth divided by the oxygen concentration in liquid bismuth squared

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
        partial pressure divided by concentration
        squared [atm.wt.%^-2] : float
        """
        return np.exp((2/R)*((-95502/T)+9.69))*(M/M_O)**2

    @property
    def correlation_name(self):
        """
        str : name of the correlation
        """
        return "fitzner1980"

    @property
    def range(self):
        """
        list : temperature validity range for property correlation
        """
        return [988, 1181]


class OxygenPartialPressureIsecke1979(OxygenPartialPressureInterface):
    """
    Oxygen partial pressure in liquid bismuth divided by the
    oxygen concentration in liquid bismuth squared property
    class implementing correlation by isecke1979
    """
    @range_warning
    def correlation(self, T, p=atm, verbose=False):
        """
        Correlation used to compute oxygen partial pressure in liquid
        bismuth divided by the oxygen concentration in liquid bismuth squared

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
        partial pressure divided by concentration
        squared [atm.wt.%^-2] : float
        """

        return np.exp((2/R)*((-101098/T)+15.66))*(M/M_O)**2

    @property
    def correlation_name(self):
        """
        str : name of the correlation
        """
        return "isecke1979"

    @property
    def range(self):
        """
        list : temperature validity range for property correlation
        """
        return [973, 1473]


class OxygenPartialPressureHahn1979(OxygenPartialPressureInterface):
    """
    Oxygen partial pressure in liquid bismuth divided by the
    oxygen concentration in liquid bismuth squared property
    class implementing correlation by hahn1979
    """
    @range_warning
    def correlation(self, T, p=atm, verbose=False):
        """
        Correlation used to compute oxygen partial pressure in liquid
        bismuth divided by the oxygen concentration in liquid bismuth squared

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
        partial pressure divided by concentration
        squared [atm.wt.%^-2] : float
        """

        return np.exp((2/R)*((-68156/T)+14.14))*(M/M_O)**2

    @property
    def correlation_name(self):
        """
        str : name of the correlation
        """
        return "hahn1979"

    @property
    def range(self):
        """
        list : temperature validity range for property correlation
        """
        return [1073, 1223]


class OxygenPartialPressureHeshmatpour1981(OxygenPartialPressureInterface):
    """
    Oxygen partial pressure in liquid bismuth divided by the
    oxygen concentration in liquid bismuth squared property
    class implementing correlation by heshmatpour1981
    """
    @range_warning
    def correlation(self, T, p=atm, verbose=False):
        """
        Correlation used to compute oxygen partial pressure in liquid
        bismuth divided by the oxygen concentration in liquid bismuth squared

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
        partial pressure divided by concentration
        squared [atm.wt.%^-2] : float
        """

        return np.exp((2/R)*((-95437/T)+3.78))*(M/M_O)**2

    @property
    def correlation_name(self):
        """
        str : name of the correlation
        """
        return "heshmatpour1981"

    @property
    def range(self):
        """
        list : temperature validity range for property correlation
        """
        return [1023, 1273]


class MolarEnthalpy(PropertyInterface):
    """
    Liquid bismuth molar enthalpy variation
    property class
    """
    @range_warning
    def correlation(self, T, p=atm, verbose=False):
        """
        Correlation used to compute molar enthalpy variation
        in liquid bismuth

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
        molar enthalpy [J/mol] : float
        """
        h_obj = h()
        return h_obj.correlation(T, p)*(M*10**(-3))

    @property
    def name(self):
        """
        str : name of the property
        """
        return "H"

    @property
    def units(self):
        """
        str : property units
        """
        return "[J.mol^-1]"

    @property
    def range(self):
        """
        list : temperature validity range for property correlation
        """
        return [T_m0, T_b0]

    @property
    def long_name(self):
        """
        str : property long name
        """
        return "molar enthalpy variation"

    @property
    def description(self):
        """
        str : property description
        """
        return f"{self.long_name} in liquid bismuth"


class MolarEntropy(PropertyInterface):
    """
    Liquid bismuth molar entropy variation
    property class
    """
    @range_warning
    def correlation(self, T, p=atm, verbose=False):
        """
        Correlation used to compute molar entropy
        variation in liquid bismuth

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
        molar entropy [J/(mol*K)] : float
        """
        return ((M*10**-3)*(
                118.2*np.log(T/T_m0)
                + 5.934e-3*(T - T_m0)
                + ((7.183e6)/-2)*((1/(T*T)) - T_m0**-2)))

    @property
    def name(self):
        """
        str : name of the property
        """
        return "S"

    @property
    def units(self):
        """
        str : property units
        """
        return "[J/(mol.K)]"

    @property
    def range(self):
        """
        list : temperature validity range for property correlation
        """
        return [T_m0, T_b0]

    @property
    def long_name(self):
        """
        str : property long name
        """
        return "molar entropy variation"

    @property
    def description(self):
        """
        str : property description
        """
        return f"{self.long_name} in liquid bismuth"


class GibbsFreeEnergy(PropertyInterface):
    """
    Liquid bismuth Gibbs free energy variation
    property class
    """
    @range_warning
    def correlation(self, T, p=atm, verbose=False):
        """
        Correlation used to compute Gibbs free energy
        variation in liquid bismuth

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
        gibbs free energy [J/mol] : float
        """
        H_obj = MolarEnthalpy()
        S_obj = MolarEntropy()
        return H_obj.correlation(T, p) - T*S_obj.correlation(T, p)

    @property
    def name(self):
        """
        str : name of the property
        """
        return "G"

    @property
    def units(self):
        """
        str : property units
        """
        return "[J/mol]"

    @property
    def range(self):
        """
        list : temperature validity range for property correlation
        """
        return [T_m0, T_b0]

    @property
    def long_name(self):
        """
        str : property long name
        """
        return "Gibbs free energy variation"

    @property
    def description(self):
        """
        str : property description
        """
        return f"{self.long_name} in liquid bismuth"
