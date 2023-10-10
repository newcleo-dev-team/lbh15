"""Module with the definition of thermophysical property object base class,
i.e., PropertyInterface. Definition of decorator
for validity range check as well."""
import warnings
from abc import ABC
from abc import abstractmethod
from typing import List
from typing import Union
from numpy import nan
from scipy.optimize import minimize_scalar
from scipy.constants import atm
from .._decorators import typecheck_for_method


def range_warning(function):
    """
    Decorator used to check validity range
    of correlation
    """
    def wrapper(*args):
        range_lim = args[0].range
        p_name = args[0].long_name
        temp = args[1]
        if hasattr(temp, "__len__"):
            temp = temp[0]
        if temp < range_lim[0] or temp > range_lim[1]:
            if (len(args) == 4) and args[3]:
                warnings.warn(f"The {p_name} is requested at "
                              f"temperature value of {temp:.2f} K "
                              "that is not in validity range "
                              f"[{range_lim[0]:.2f}, {range_lim[1]:.2f}] K",
                              stacklevel=3)
        return function(*args)
    return wrapper


class PropertyInterface(ABC):
    """
    Abstract class that defines thermo-physical property interface.
    Derived classes must override:

        - :func:`~PropertyInterface.correlation`
        - :attr:`~.PropertyInterface.range`
        - :attr:`~.PropertyInterface.units`
        - :attr:`~.PropertyInterface.long_name`
        - :attr:`~.PropertyInterface.description`

    Instead, it is not mandatory to override the following attributes:

        - :func:`~PropertyInterface.initialization_helper`, override this \
          method if function's roots are particularly 'difficult' to find \
          (see \
          :func:`lbh15.properties.lead_properties.p_s.initialization_helper`).\
           If not overridden it will be ignored.
        - :attr:`~.PropertyInterface.name`, override this member to use \
          a custom name for the property, otherwise the class name will be used
        - :attr:`~.PropertyInterface.correlation_name` override this member \
          to set a correlation name different from default one
        - :attr:`~.PropertyInterface.is_injective` override this member \
          if the function is not injective, othwerise it will \
          be considered injective
    """
    def __init__(self):
        self.__min: float = -nan
        self.__max: float = nan
        self.__T_at_min: float = -nan
        self.__T_at_max: float = nan

    def compute_bounds(self) -> None:
        """
        Computes the bound of property in validity range, i.e.,
        the minimum and the maximum of the correlation inside
        the validity range, together with the corresponding temperature.
        If this method is not invoked their default value is
        -nan and nan respectively.
        Values are computed using :func:`scipy.optimize.minimize_scalar`
        with "Bounded" solver (for more details please refer to scipy
        documentation)
        """
        res = minimize_scalar(self.correlation,
                              bounds=self.range,
                              method="Bounded",
                              options={'xatol': 1e-10})
        if res.success:
            self.__min = res.fun
            self.__T_at_min = res.x
        else:
            raise RuntimeError("Unable to find the minimum point: "
                               + res.message)

        def corr_opposite(T: float) -> float:
            return -self.correlation(T)

        res = minimize_scalar(corr_opposite,
                              bounds=self.range,
                              method="Bounded",
                              options={'xatol': 1e-10})
        if res.success:
            self.__max = -res.fun
            self.__T_at_max = res.x
        else:
            raise RuntimeError("Unable to find the maximum point: "
                               + res.message)

    @typecheck_for_method
    def initialization_helper(self,
                              property_value: float) -> float:
        """
        Returns a temperature guess according to the value
        of the property. Used by root finder algorithm if
        return type is not None.

        Parameters
        ----------
        property_value : float
            value of the property

        Returns
        -------
        None
        """
        return 0

    @typecheck_for_method
    def info(self, T: float, p: float = atm,
             print_info: bool = True, n_tab: int = 0) -> Union[None, str]:
        """
        Method used to print information about the property
        and the correlation used to compute its value.

        Parameters
        ----------
        T : float
            Temperature in [K]
        p : float, optional
            Pressure in [Pa], by default atm, i.e., 101325.0 Pa
        print_info : bool, optional
            True to print to console, False for getting the
            string, by default True
        n_tab : int, optional
            Number of tabs used to format the information, by default 0

        Returns
        -------
        str, None
            Returns None id print_info=True, otherwise returns the content
            of the information.
        """
        property_val = self.correlation(T, p)
        if property_val < 1e-2:
            value = f"Value: {property_val:.2e} {self.units}"
        else:
            value = f"Value: {property_val:.2f} {self.units}"
        validity = ("Validity range: "
                    f"[{self.range[0]:.2f}, {self.range[1]:.2f}] K")
        corr_name = f"Correlation name: '{self.correlation_name}'"
        long_name = f"Long name: {self.long_name}"
        units = f"Units: {self.units}"
        description = ("Description:\n{:s}{:s}"
                       .format((n_tab+2)*"\t", self.description))

        all_info = "{:s}{:s}:\n".format(n_tab*"\t", self.name)
        all_info += "{:s}{:s}\n".format((n_tab+1)*"\t", value)
        all_info += "{:s}{:s}\n".format((n_tab+1)*"\t", validity)
        all_info += "{:s}{:s}\n".format((n_tab+1)*"\t", corr_name)
        all_info += "{:s}{:s}\n".format((n_tab+1)*"\t", long_name)
        all_info += "{:s}{:s}\n".format((n_tab+1)*"\t", units)
        all_info += "{:s}{:s}".format((n_tab+1)*"\t", description)

        if print_info:
            return print(all_info)
        return all_info

    @abstractmethod
    @range_warning
    def correlation(self, T: float, p: float = atm,
                    verbose: bool = False) -> float:
        """
        Function that implements the property correlation

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
        """
        raise NotImplementedError(f"{type(self).__name__}.correlation "
                                  "NOT IMPLEMENTED")

    @property
    def name(self) -> str:
        """
        str : name of the property
        """
        return type(self).__name__

    @property
    def correlation_name(self) -> str:
        """
        str : name of the correlation
        """
        return "lbh15"

    @property
    def is_injective(self) -> bool:
        """
        bool : True if correlation is injective,
        False otherwise
        """
        return True

    @property
    def min(self) -> float:
        """
        float : minimum of property correlation in validity
        range
        """
        return self.__min

    @property
    def max(self) -> float:
        """
        float : maximum of property correlation in validity
        range
        """
        return self.__max

    @property
    def T_at_min(self) -> float:
        """
        float : temperature corresponding to the minimum of
        property correlation in validity range
        """
        return self.__T_at_min

    @property
    def T_at_max(self) -> float:
        """
        float : temperature corresponding to the maximum of
        property correlation in validity range
        """
        return self.__T_at_max

    @property
    @abstractmethod
    def range(self) -> List[float]:
        """
        list : temperature validity range for property correlation
        """
        raise NotImplementedError(f"{type(self).__name__}.range "
                                  "NOT IMPLEMENTED")

    @property
    @abstractmethod
    def units(self) -> str:
        """
        str : property units
        """
        raise NotImplementedError(f"{type(self).__name__}.units "
                                  "NOT IMPLEMENTED")

    @property
    @abstractmethod
    def long_name(self) -> str:
        """
        str : property long name
        """
        raise NotImplementedError(f"{type(self).__name__}.long_name "
                                  "NOT IMPLEMENTED")

    @property
    @abstractmethod
    def description(self) -> str:
        """
        str : property description
        """
        raise NotImplementedError(f"{type(self).__name__}.description "
                                  "NOT IMPLEMENTED")
