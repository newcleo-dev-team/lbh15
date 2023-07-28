"""Module with the definition of chemical property objects
for lead"""
import numpy as np
from scipy.constants import atm, R
from lbh15.properties.interface import PropertyInterface, range_warning


class OxygenDiffusivityInterface(PropertyInterface):
    """
    Oxygen diffusivity in liquid lead property class
    """
    @property
    def name(self):
        """
        str : name of the property
        """
        return "o_dif"

    @property
    def units(self):
        """
        str : property units
        """
        return "[cm^2.s^-1]"

    @property
    def long_name(self):
        """
        str : property long name
        """
        return "oxygen diffusivity"

    @property
    def description(self):
        """
        str : property description
        """
        return f"{self.long_name} in liquid lead"


class OxygenDiffusivityArcella1968(OxygenDiffusivityInterface):
    """
    Oxygen diffusivity in liquid lead property class
    implementing correlation by arcella1968
    """
    @range_warning
    def correlation(self, T, p=atm, verbose=False):
        """
        Correlation used to compute oxygen diffusivity in liquid lead

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
        diffusivity [cm^2.s^-1] : float
        """

        return np.exp(-14979/(R*T))*6.32e-5

    @property
    def correlation_name(self):
        """
        str : name of the correlation
        """
        return "arcella1968"

    @property
    def range(self):
        """
        list : temperature validity range for property correlation
        """
        return [973, 1173]


class OxygenDiffusivityHomna1971(OxygenDiffusivityInterface):
    """
    Oxygen diffusivity in liquid lead property class
    implementing correlation by homna1971
    """
    @range_warning
    def correlation(self, T, p=atm, verbose=False):
        """
        Correlation used to compute oxygen diffusivity in liquid lead

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
        diffusivity [cm^2.s^-1] : float
        """

        return np.exp(-20083/(R*T))*9.65e-5

    @property
    def correlation_name(self):
        """
        str : name of the correlation
        """
        return "homna1971"

    @property
    def range(self):
        """
        list : temperature validity range for property correlation
        """
        return [1073, 1373]


class OxygenDiffusivitySwzarc1972(OxygenDiffusivityInterface):
    """
    Oxygen diffusivity in liquid lead property class
    implementing correlation by swzarc1972
    """
    @range_warning
    def correlation(self, T, p=atm, verbose=False):
        """
        Correlation used to compute oxygen diffusivity in liquid lead

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
        diffusivity [cm^2.s^-1] : float
        """

        return np.exp(-25942/(R*T))*1.44e-3

    @property
    def correlation_name(self):
        """
        str : name of the correlation
        """
        return "swzarc1972"

    @property
    def range(self):
        """
        list : temperature validity range for property correlation
        """
        return [1013, 1353]


class OxygenDiffusivityOtsuka1975(OxygenDiffusivityInterface):
    """
    Oxygen diffusivity in liquid lead property class
    implementing correlation by otsuka1975
    """
    @range_warning
    def correlation(self, T, p=atm, verbose=False):
        """
        Correlation used to compute oxygen diffusivity in liquid lead

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
        diffusivity [cm^2.s^-1] : float
        """

        return np.exp(-19497/(R*T))*1.48e-3

    @property
    def correlation_name(self):
        """
        str : name of the correlation
        """
        return "otsuka1975"

    @property
    def range(self):
        """
        list : temperature validity range for property correlation
        """
        return [1173, 1373]


class OxygenDiffusivityCharle1976(OxygenDiffusivityInterface):
    """
    Oxygen diffusivity in liquid lead property class
    implementing correlation by charle1976
    """
    @range_warning
    def correlation(self, T, p=atm, verbose=False):
        """
        Correlation used to compute oxygen diffusivity in liquid lead

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
        diffusivity [cm^2.s^-1] : float
        """

        return np.exp(-20927/(R*T))*1.90e-3

    @property
    def correlation_name(self):
        """
        str : name of the correlation
        """
        return "charle1976"

    @property
    def range(self):
        """
        list : temperature validity range for property correlation
        """
        return [1173, 1373]


class OxygenDiffusivityGromov1996(OxygenDiffusivityInterface):
    """
    Oxygen diffusivity in liquid lead property class
    implementing correlation by gromov1996
    """
    @range_warning
    def correlation(self, T, p=atm, verbose=False):
        """
        Correlation used to compute oxygen diffusivity in liquid lead

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
        diffusivity [cm^2.s^-1] : float
        """

        return np.exp(-16158/(R*T))*6.6e-5

    @property
    def correlation_name(self):
        """
        str : name of the correlation
        """
        return "gromov1996"

    @property
    def range(self):
        """
        list : temperature validity range for property correlation
        """
        return [673, 1273]


class OxygenDiffusivityGanesan2006b(OxygenDiffusivityInterface):
    """
    Oxygen diffusivity in liquid lead property class
    implementing correlation by ganesan2006b
    """
    @range_warning
    def correlation(self, T, p=atm, verbose=False):
        """
        Correlation used to compute oxygen diffusivity in liquid lead

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
        diffusivity [cm^2.s^-1] : float
        """

        return np.exp(-45587/(R*T))*2.79e-3

    @property
    def correlation_name(self):
        """
        str : name of the correlation
        """
        return "ganesan2006b"

    @property
    def range(self):
        """
        list : temperature validity range for property correlation
        """
        return [823, 1053]


class IronDiffusivity(PropertyInterface):
    """
    Iron diffusivity in liquid lead
    property class
    """
    @range_warning
    def correlation(self, T, p=atm, verbose=False):
        """
        Correlation used to compute iron diffusivity
        in liquid lead

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
        diffusivity [cm^2.s^-1] : float
        """
        return np.exp((-2.31-2295/T)*np.log(10))

    @property
    def name(self):
        """
        str : name of the property
        """
        return "fe_dif"

    @property
    def units(self):
        """
        str : property units
        """
        return "[cm^2.s^-1]"

    @property
    def range(self):
        """
        list : temperature validity range for property correlation
        """
        return [973.0, 1273.0]

    @property
    def long_name(self):
        """
        str : property long name
        """
        return "iron diffusivity"

    @property
    def description(self):
        """
        str : property description
        """
        return "f{self.long_name} in liquid lead"


class CobaltDiffusivity(PropertyInterface):
    """
    Cobalt diffusivity in liquid lead
    property class
    """
    @range_warning
    def correlation(self, T, p=atm, verbose=False):
        """
        Correlation used to compute cobalt diffusivity
        in liquid lead

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
        diffusivity [cm^2.s^-1] : float
        """
        return np.exp(-22154/(R*T))*4.6e-4

    @property
    def name(self):
        """
        str : name of the property
        """
        return "co_dif"

    @property
    def units(self):
        """
        str : property units
        """
        return "[cm^2.s^-1]"

    @property
    def range(self):
        """
        list : temperature validity range for property correlation
        """
        return [1023.0, 1273.0]

    @property
    def long_name(self):
        """
        str : property long name
        """
        return "cobalt diffusivity"

    @property
    def description(self):
        """
        str : property description
        """
        return "f{self.long_name} in liquid lead"


class SeleniumDiffusivity(PropertyInterface):
    """
    Selenium diffusivity in liquid lead
    property class
    """
    @range_warning
    def correlation(self, T, p=atm, verbose=False):
        """
        Correlation used to compute selenium diffusivity
        in liquid lead

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
        diffusivity [cm^2.s^-1] : float
        """
        return np.exp(-12958/(R*T))*3.4e-4

    @property
    def name(self):
        """
        str : name of the property
        """
        return "se_dif"

    @property
    def units(self):
        """
        str : property units
        """
        return "[cm^2.s^-1]"

    @property
    def range(self):
        """
        list : temperature validity range for property correlation
        """
        return [823.0, 1173.0]

    @property
    def long_name(self):
        """
        str : property long name
        """
        return "selenium diffusivity"

    @property
    def description(self):
        """
        str : property description
        """
        return "f{self.long_name} in liquid lead"


class IndiumDiffusivity(PropertyInterface):
    """
    Indium diffusivity in liquid lead
    property class
    """
    @range_warning
    def correlation(self, T, p=atm, verbose=False):
        """
        Correlation used to compute indium diffusivity
        in liquid lead

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
        diffusivity [cm^2.s^-1] : float
        """
        return np.exp(-13794/(R*T))*3.1e-4

    @property
    def name(self):
        """
        str : name of the property
        """
        return "in_dif"

    @property
    def units(self):
        """
        str : property units
        """
        return "[cm^2.s^-1]"

    @property
    def range(self):
        """
        list : temperature validity range for property correlation
        """
        return [723.0, 1173.0]

    @property
    def long_name(self):
        """
        str : property long name
        """
        return "indium diffusivity"

    @property
    def description(self):
        """
        str : property description
        """
        return "f{self.long_name} in liquid lead"


class TelluriumDiffusivity(PropertyInterface):
    """
    Tellurium diffusivity in liquid lead
    property class
    """
    @range_warning
    def correlation(self, T, p=atm, verbose=False):
        """
        Correlation used to compute tellurium diffusivity
        in liquid lead

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
        diffusivity [cm^2.s^-1] : float
        """
        return np.exp(-15884/(R*T))*3.1e-4

    @property
    def name(self):
        """
        str : name of the property
        """
        return "te_dif"

    @property
    def units(self):
        """
        str : property units
        """
        return "[cm^2.s^-1]"

    @property
    def range(self):
        """
        list : temperature validity range for property correlation
        """
        return [723.0, 1173.0]

    @property
    def long_name(self):
        """
        str : property long name
        """
        return "tellurium diffusivity"

    @property
    def description(self):
        """
        str : property description
        """
        return "f{self.long_name} in liquid lead"
