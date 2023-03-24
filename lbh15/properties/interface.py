"""Module with the definition of thermophysical property object base class,
i.e., PropertyInterface. Definition of decorator
for validity range check as well."""
import warnings
from abc import ABC, abstractmethod
from .._constants import P_ATM


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
            if len(args) == 4:
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
        from numpy import nan
        self.__min = -nan
        self.__max = nan
        self.__T_at_min = -nan
        self.__T_at_max = nan

    def compute_bounds(self):
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
        from scipy.optimize import minimize_scalar
        min_vals = minimize_scalar(self.correlation,
                                   bounds=self.range,
                                   method="Bounded")
        self.__min = min_vals.fun
        self.__T_at_min = min_vals.x
        if self.__T_at_min - self.range[0] < 5e-4:
            self.__T_at_min = self.range[0]
            self.__min = self.correlation(self.__T_at_min)

        def corr_reciprocal(T):
            return 1/self.correlation(T)

        max_vals = minimize_scalar(corr_reciprocal,
                                   bounds=self.range,
                                   method="Bounded")
        self.__max = self.correlation(max_vals.x)
        self.__T_at_max = max_vals.x
        if self.range[1] - self.__T_at_max < 5e-4:
            self.__T_at_max = self.range[1]
            self.__max = self.correlation(self.__T_at_max)

    def initialization_helper(self, property_value):
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
        return None

    def info(self, T, p=P_ATM, print_info=True, n_tab=0):
        """
        Method used to print information about the property
        and the correlation used to compute its value.

        Parameters
        ----------
        T : float
            Temperature in [K]
        p : float, optional
            Pressure in [Pa], by default P_ATM, i.e., 101325.0 Pa
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
        name = self.name
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

        all_info = "{:s}{:s}:\n".format(n_tab*"\t", name)
        all_info += "{:s}{:s}\n".format((n_tab+1)*"\t", value)
        all_info += "{:s}{:s}\n".format((n_tab+1)*"\t", validity)
        all_info += "{:s}{:s}\n".format((n_tab+1)*"\t", corr_name)
        all_info += "{:s}{:s}\n".format((n_tab+1)*"\t", long_name)
        all_info += "{:s}{:s}\n".format((n_tab+1)*"\t", units)
        all_info += "{:s}{:s}".format((n_tab+1)*"\t", description)

        rvalue = None
        if print_info:
            print(all_info)
        else:
            rvalue = all_info
        return rvalue

    @abstractmethod
    @range_warning
    def correlation(self, T, p=P_ATM, verbose=False):
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
    def name(self):
        """
        str : name of the property
        """
        return type(self).__name__

    @property
    def correlation_name(self):
        """
        str : name of the correlation
        """
        return "lbh15"

    @property
    def is_injective(self):
        """
        bool : True if correlation is injective,
        False otherwise
        """
        return True

    @property
    def min(self):
        """
        float : minimum of property correlation in validity
        range
        """
        return self.__min

    @property
    def max(self):
        """
        float : maximum of property correlation in validity
        range
        """
        return self.__max

    @property
    def T_at_min(self):
        """
        float : temperature corresponding to the minimum of
        property correlation in validity range
        """
        return self.__T_at_min

    @property
    def T_at_max(self):
        """
        float : temperature corresponding to the maximum of
        property correlation in validity range
        """
        return self.__T_at_max

    @property
    @abstractmethod
    def range(self):
        """
        list : temperature validity range for property correlation
        """
        raise NotImplementedError(f"{type(self).__name__}.range "
                                  "NOT IMPLEMENTED")

    @property
    @abstractmethod
    def units(self):
        """
        str : property units
        """
        raise NotImplementedError(f"{type(self).__name__}.units "
                                  "NOT IMPLEMENTED")

    @property
    @abstractmethod
    def long_name(self):
        """
        str : property long name
        """
        raise NotImplementedError(f"{type(self).__name__}.long_name "
                                  "NOT IMPLEMENTED")

    @property
    @abstractmethod
    def description(self):
        """
        str : property description
        """
        raise NotImplementedError(f"{type(self).__name__}.description "
                                  "NOT IMPLEMENTED")
