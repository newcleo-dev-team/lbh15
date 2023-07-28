"""Module with the definition of thermochemical
property objects for lead-bismuth eutectic"""
import numpy as np
from scipy.constants import atm, R
from ..interface import PropertyInterface, range_warning
from ..lbe_properties import h
from ..._commons import LBE_BOILING_TEMPERATURE as T_b0
from ..._commons import LBE_MELTING_TEMPERATURE as T_m0
from ..._commons import LBE_MOLAR_MASS as M
from ..._commons import OXYGEN_MOLAR_MASS as M_o


class OxygenPartialPressure(PropertyInterface):
    """
    Oxygen partial pressure in liquid lead-bismuth eutectic
    divided by the oxygen concentration in liquid
    lead-bismuth eutectic squared property class
    """
    @range_warning
    def correlation(self, T, p=atm, verbose=False):
        """
        Correlation used to compute oxygen partial pressure
        in liquid lead-bismuth eutectic divided by the oxygen
        concentration in liquid lead-bismuth eutectic squared

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
        return np.exp((2/R)*((-127398/T)+27.938))*(M/M_o)**2

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
    def range(self):
        """
        list : temperature validity range for property correlation
        """
        return [812, 1008]

    @property
    def long_name(self):
        """
        str : property long name
        """
        return "oxygen partial pressure divided by the \
                oxygen concentration squared"

    @property
    def description(self):
        """
        str : property description
        """
        return f"{self.long_name} in liquid lbe"


class LeadChemicalActivity(PropertyInterface):
    """
    Lead chemical activity in liquid lead-bismuth eutectic
    property class
    """
    @range_warning
    def correlation(self, T, p=atm, verbose=False):
        """
        Correlation used to compute lead chemical activity
        in liquid lead-bismuth eutectic

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
        chemical activity [-] : float
        """
        return 0.42206-63.2/T

    @property
    def name(self):
        """
        str : name of the property
        """
        return "pb_a"

    @property
    def units(self):
        """
        str : property units
        """
        return "[-]"

    @property
    def range(self):
        """
        list : temperature validity range for property correlation
        """
        return [399, 1173]

    @property
    def long_name(self):
        """
        str : property long name
        """
        return "lead chemical activity"

    @property
    def description(self):
        """
        str : property description
        """
        return f"{self.long_name} in liquid lbe"


class BismuthChemicalActivity(PropertyInterface):
    """
    Bismuth chemical activity in liquid lead-bismuth eutectic
    property class
    """
    @range_warning
    def correlation(self, T, p=atm, verbose=False):
        """
        Correlation used to compute Bismuth chemical activity
        in liquid lead-bismuth eutectic

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
        chemical activity [-] : float
        """
        return 0.53381-56.2/T

    @property
    def name(self):
        """
        str : name of the property
        """
        return "bi_a"

    @property
    def units(self):
        """
        str : property units
        """
        return "[-]"

    @property
    def range(self):
        """
        list : temperature validity range for property correlation
        """
        return [399, 1173]

    @property
    def long_name(self):
        """
        str : property long name
        """
        return "Bismuth chemical activity"

    @property
    def description(self):
        """
        str : property description
        """
        return f"{self.long_name} in liquid lbe"


class MolarEnthalpy(PropertyInterface):
    """
    Liquid lead-bismuth eutectic molar
    enthalpy variation property class
    """
    @range_warning
    def correlation(self, T, p=atm, verbose=False):
        """
        Correlation used to compute molar enthalpy variation
        in liquid lead-bismuth eutectic

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
        return [400.0, T_b0]

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
        return f"{self.long_name} in liquid lbe"


class MolarEntropy(PropertyInterface):
    """
    Liquid lead-bismuth eutectic molar
    entropy variation property class
    """
    @range_warning
    def correlation(self, T, p=atm, verbose=False):
        """
        Correlation used to compute molar entropy
        variation in liquid lead-bismuth eutectic

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
                164.8*np.log(T/T_m0)
                - 3.94e-2*(T - T_m0)
                + ((1.25e-5)/2)*((T*T) - T_m0**2)
                - ((4.56e5)/-2)*((1/(T*T)) - T_m0**-2)))

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
        return [400, T_b0]

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
        return f"{self.long_name} in liquid lbe"


class GibbsFreeEnergy(PropertyInterface):
    """
    Liquid lead-bimuth eutectic Gibbs free
    energy variation property class
    """
    @range_warning
    def correlation(self, T, p=atm, verbose=False):
        """
        Correlation used to compute Gibbs free energy
        variation in liquid lead-bismuth eutectic

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
        return [400, T_b0]

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
        return f"{self.long_name} in liquid lbe"
