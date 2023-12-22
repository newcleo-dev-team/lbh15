"""Module with the definition of the *diffusivity*
property objects for *lead*."""
from typing import List
import numpy as np
from scipy.constants import atm
from scipy.constants import R
from lbh15.properties.interface import PropertyInterface
from ..._decorators import range_warning


class OxygenDiffusivityInterface(PropertyInterface):
    """
    Liquid lead *Oxygen diffusivity* property abstract class.
    """
    @property
    def name(self) -> str:
        """
        str : Name of the property
        """
        return "o_dif"

    @property
    def units(self) -> str:
        """
        str : Oxygen diffusivity unit
        """
        return "[cm^2.s^-1]"

    @property
    def long_name(self) -> str:
        """
        str : Oxygen diffusivity long name
        """
        return "oxygen diffusivity"

    @property
    def description(self) -> str:
        """
        str : Oxygen diffusivity description
        """
        return f"{self.long_name} in liquid lead"


class OxygenDiffusivityArcella1968(OxygenDiffusivityInterface):
    """
    Liquid lead *Oxygen diffusivity* property class
    implementing the correlation by *arcella1968*.
    """
    @range_warning
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Returns the value of the *Oxygen diffusivity* by
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
            diffusivity in :math:`[cm^2 / s]`
        """
        return np.exp(-14979 / R / T) * 6.32e-5

    @property
    def correlation_name(self) -> str:
        """
        str : Name of the correlation
        """
        return "arcella1968"

    @property
    def range(self) -> List[float]:
        """
        List[float] : Temperature validity range of the Oxygen diffusivity
        correlation function
        """
        return [973, 1173]


class OxygenDiffusivityHomna1971(OxygenDiffusivityInterface):
    """
    Liquid lead *Oxygen diffusivity* property class
    implementing the correlation by *homna1971*.
    """
    @range_warning
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Returns the value of the *Oxygen diffusivity* by
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
            diffusivity in :math:`[cm^2 / s]`
        """
        return np.exp(-20083 / R / T) * 9.65e-5

    @property
    def correlation_name(self) -> str:
        """
        str : Name of the correlation
        """
        return "homna1971"

    @property
    def range(self) -> List[float]:
        """
        List[float] : Temperature validity range of the Oxygen diffusivity
        correlation function
        """
        return [1073, 1373]


class OxygenDiffusivitySwzarc1972(OxygenDiffusivityInterface):
    """
    Liquid lead *Oxygen diffusivity* property class
    implementing the correlation by *swzarc1972*.
    """
    @range_warning
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Returns the value of the *Oxygen diffusivity* by
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
            diffusivity in :math:`[cm^2 / s]`
        """
        return np.exp(-25942 / R / T) * 1.44e-3

    @property
    def correlation_name(self) -> str:
        """
        str : Name of the correlation
        """
        return "swzarc1972"

    @property
    def range(self) -> List[float]:
        """
        List[float] : Temperature validity range of the Oxygen diffusivity
        correlation function
        """
        return [1013, 1353]


class OxygenDiffusivityOtsuka1975(OxygenDiffusivityInterface):
    """
    Liquid lead *Oxygen diffusivity* property class
    implementing the correlation by *otsuka1975*.
    """
    @range_warning
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Returns the value of the *Oxygen diffusivity* by
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
            diffusivity in :math:`[cm^2 / s]`
        """
        return np.exp(-19497 / R / T) * 1.48e-3

    @property
    def correlation_name(self) -> str:
        """
        str : Name of the correlation
        """
        return "otsuka1975"

    @property
    def range(self) -> List[float]:
        """
        List[float] : Temperature validity range of the Oxygen diffusivity
        correlation function
        """
        return [1173, 1373]


class OxygenDiffusivityCharle1976(OxygenDiffusivityInterface):
    """
    Liquid lead *Oxygen diffusivity* property class
    implementing the correlation by *charle1976*.
    """
    @range_warning
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Returns the value of the *Oxygen diffusivity* by
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
            diffusivity in :math:`[cm^2 / s]`
        """
        return np.exp(-20927 / R / T) * 1.90e-3

    @property
    def correlation_name(self) -> str:
        """
        str : Name of the correlation
        """
        return "charle1976"

    @property
    def range(self) -> List[float]:
        """
        List[float] : Temperature validity range of the Oxygen diffusivity
        correlation function
        """
        return [1173, 1373]


class OxygenDiffusivityGromov1996(OxygenDiffusivityInterface):
    """
    Liquid lead *Oxygen diffusivity* property class
    implementing the correlation by *gromov1996*.
    """
    @range_warning
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Returns the value of the *Oxygen diffusivity* by
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
            diffusivity in :math:`[cm^2 / s]`
        """
        return np.exp(-16158 / R / T) * 6.6e-5

    @property
    def correlation_name(self) -> str:
        """
        str : Name of the correlation
        """
        return "gromov1996"

    @property
    def range(self) -> List[float]:
        """
        List[float] : Temperature validity range of the Oxygen diffusivity
        correlation function
        """
        return [673, 1273]


class OxygenDiffusivityGanesan2006b(OxygenDiffusivityInterface):
    """
    Liquid lead *Oxygen diffusivity* property class
    implementing the correlation by *ganesan2006b*.
    """
    @range_warning
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Returns the value of the *Oxygen diffusivity* by
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
            diffusivity in :math:`[cm^2 / s]`
        """
        return np.exp(-45587 / R / T) * 2.79e-3

    @property
    def correlation_name(self) -> str:
        """
        str : Name of the correlation
        """
        return "ganesan2006b"

    @property
    def range(self) -> List[float]:
        """
        List[float] : Temperature validity range of the Oxygen diffusivity
        correlation function
        """
        return [823, 1053]


class IronDiffusivity(PropertyInterface):
    """
    Liquid lead *Iron diffusivity* property class.
    """
    @range_warning
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Returns the value of the *Iron diffusivity* by
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
            diffusivity in :math:`[cm^2 / s]`
        """
        return np.power(10, - 2.31 - 2295 / T)

    @property
    def name(self) -> str:
        """
        str : Name of the property
        """
        return "fe_dif"

    @property
    def units(self) -> str:
        """
        str : Iron diffusivity unit
        """
        return "[cm^2.s^-1]"

    @property
    def range(self) -> List[float]:
        """
        List[float] : Temperature validity range of the Iron diffusivity
        correlation function
        """
        return [973.0, 1273.0]

    @property
    def long_name(self) -> str:
        """
        str : Iron diffusivity long name
        """
        return "iron diffusivity"

    @property
    def description(self) -> str:
        """
        str : Iron diffusivity description
        """
        return "f{self.long_name} in liquid lead"


class CobaltDiffusivity(PropertyInterface):
    """
    Liquid lead *Cobalt diffusivity* property class.
    """
    @range_warning
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Returns the value of the *Cobalt diffusivity* by
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
            diffusivity in :math:`[cm^2 / s]`
        """
        return np.exp(-22154 / R / T) * 4.6e-4

    @property
    def name(self) -> str:
        """
        str : Name of the property
        """
        return "co_dif"

    @property
    def units(self) -> str:
        """
        str : Cobalt diffusivity unit
        """
        return "[cm^2.s^-1]"

    @property
    def range(self) -> List[float]:
        """
        List[float] : Temperature validity range of the Cobalt diffusivity
        correlation function
        """
        return [1023.0, 1273.0]

    @property
    def long_name(self) -> str:
        """
        str : Cobalt diffusivity long name
        """
        return "cobalt diffusivity"

    @property
    def description(self) -> str:
        """
        str : Cobalt diffusivity description
        """
        return "f{self.long_name} in liquid lead"


class SeleniumDiffusivity(PropertyInterface):
    """
    Liquid lead *Selenium diffusivity* property class.
    """
    @range_warning
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Returns the value of the *Selenium diffusivity* by
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
            diffusivity in :math:`[cm^2 / s]`
        """
        return np.exp(-12958 / R / T) * 3.4e-4

    @property
    def name(self) -> str:
        """
        str : Name of the property
        """
        return "se_dif"

    @property
    def units(self) -> str:
        """
        str : Selenium diffusivity unit
        """
        return "[cm^2.s^-1]"

    @property
    def range(self) -> List[float]:
        """
        List[float] : Temperature validity range of the Selenium diffusivity
        correlation function
        """
        return [823.0, 1173.0]

    @property
    def long_name(self) -> str:
        """
        str : Selenium diffusivity long name
        """
        return "selenium diffusivity"

    @property
    def description(self) -> str:
        """
        str : Selenium diffusivity description
        """
        return "f{self.long_name} in liquid lead"


class IndiumDiffusivity(PropertyInterface):
    """
    Liquid lead *Indium diffusivity* property class.
    """
    @range_warning
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Returns the value of the *Indium diffusivity* by
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
            diffusivity in :math:`[cm^2 / s]`
        """
        return np.exp(-13794 / R / T) * 3.1e-4

    @property
    def name(self) -> str:
        """
        str : Name of the property
        """
        return "in_dif"

    @property
    def units(self) -> str:
        """
        str : Indium diffusivity unit
        """
        return "[cm^2.s^-1]"

    @property
    def range(self) -> List[float]:
        """
        List[float] : Temperature validity range of the Indium diffusivity
        correlation function
        """
        return [723.0, 1173.0]

    @property
    def long_name(self) -> str:
        """
        str : Indium diffusivity long name
        """
        return "indium diffusivity"

    @property
    def description(self) -> str:
        """
        str : Indium diffusivity description
        """
        return "f{self.long_name} in liquid lead"


class TelluriumDiffusivity(PropertyInterface):
    """
    Liquid lead *Tellurium diffusivity* property class.
    """
    @range_warning
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Returns the value of the *Tellurium diffusivity* by
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
            diffusivity in :math:`[cm^2 / s]`
        """
        return np.exp(-15884 / R / T) * 3.1e-4

    @property
    def name(self) -> str:
        """
        str : Name of the property
        """
        return "te_dif"

    @property
    def units(self) -> str:
        """
        str : Tellurium diffusivity unit
        """
        return "[cm^2.s^-1]"

    @property
    def range(self) -> List[float]:
        """
        List[float] : Temperature validity range of the Tellurium diffusivity
        correlation function
        """
        return [723.0, 1173.0]

    @property
    def long_name(self) -> str:
        """
        str : Tellurium diffusivity long name
        """
        return "tellurium diffusivity"

    @property
    def description(self) -> str:
        """
        str : Tellurium diffusivity description
        """
        return "f{self.long_name} in liquid lead"
