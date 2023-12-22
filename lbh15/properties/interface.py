"""Module with the definition of the base class for both the thermo-physical
and the thermo-chemical properties, i.e., :class:`.PropertyInterface`."""
from abc import ABC
from abc import abstractmethod
from typing import List
from typing import Union
from numpy import nan
from scipy.optimize import minimize_scalar
from scipy.constants import atm
from .._decorators import range_warning


class PropertyInterface(ABC):
    """
    Abstract class that defines the interface for both the thermo-physical
    and the thermo-chemical properties.
    Derived classes must override the following attributes:

        - :func:`~PropertyInterface.correlation`
        - :attr:`~.PropertyInterface.range`
        - :attr:`~.PropertyInterface.units`
        - :attr:`~.PropertyInterface.long_name`
        - :attr:`~.PropertyInterface.description`

    Even the following attributes can be overridden, but not mandatorily:

        - :func:`~PropertyInterface.initialization_helper`: override this \
          method if the property correlation is particularly *difficult* to \
          solve in terms of temperature (see \
          :func:`lbh15.properties.lead_properties.p_s.initialization_helper`).\
          If not overridden, it is ignored.
        - :attr:`~.PropertyInterface.name`: override this member to give \
          the property a custom name, otherwise the class name is used.
        - :attr:`~.PropertyInterface.correlation_name`: override this member \
          to give the correlation a name different from the default one.
        - :attr:`~.PropertyInterface.is_injective`: override this member only \
          in case the correlation function is not injective by returning the
          `False` value, otherwise it is considered injective.

    Derived classes are not allowed having either the name starting with
    :attr:`__` or overriding the :attr:`~.PropertyInterface.name` attribute
    for providing a name starting with :attr:`__`.
    """
    def __init__(self):
        self.__min: float = -nan
        self.__max: float = nan
        self.__T_at_min: float = -nan
        self.__T_at_max: float = nan

    def compute_bounds(self) -> None:
        """
        Computes the bounds of the property within the validity range, i.e.,
        the minimum and the maximum values of the correlation function inside
        the validity range, together with the corresponding temperature values.
        If this method is not invoked, the default values are `-nan` for the
        minimum value of the property and for its corresponding temperature,
        and `nan` for the maximum value of the property and for its
        corresponding temperature.
        The bounding values are computed using the
        :func:`scipy.optimize.minimize_scalar` function by adopting the
        "Bounded" method (for more details, please refer to the *scipy*
        documentation).

        Returns
        -------
        None
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

    def initialization_helper(self,
                              property_value: float) -> Union[float, None]:
        """
        Returns the temperature guess value according to the value
        of the property passed as argument. It is used by the root finder
        algorithm in case the return type is not `None`.

        Parameters
        ----------
        property_value : float
            value of the property

        Returns
        -------
        None
        """
        return None

    def info(self, T: float, p: float = atm,
             print_info: bool = True, n_tab: int = 0) -> Union[None, str]:
        """
        Prints the information about the property and about the correlation
        adopted to compute its value.

        Parameters
        ----------
        T : float
            Temperature in :math:`[K]`
        p : float, optional
            Pressure in :math:`[Pa]`, by default the atmospheric
            pressure value, i.e., :math:`101325.0 Pa`
        print_info : bool, optional
            `True` to print to the console, `False` for getting the
            string. By default, `True`
        n_tab : int, optional
            Number of indentation tabs used to format the output,
            by default `0`

        Returns
        -------
        None | str
            Returns `None` if `print_info=True`, otherwise returns the content
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
        Returns the value of the property by applying the
        corresponding correlation.

        Parameters
        ----------
        T : float
            Temperature in :math:`[K]`
        p : float, optional
            Pressure in :math:`[Pa]`, by default the atmospheric pressure,
            i.e., :math:`101325.0 Pa`
        verbose : bool, optional
            `True` to tell the decorator to print a warning message in case of
            range check failing, `False` otherwise. By default, `False`
        
        Returns
        -------
        exception
        """
        raise NotImplementedError(f"{type(self).__name__}.correlation "
                                  "NOT IMPLEMENTED")

    @property
    def name(self) -> str:
        """
        str : Name of the property
        """
        return type(self).__name__

    @property
    def correlation_name(self) -> str:
        """
        str : Name of the correlation
        """
        return "lbh15"

    @property
    def is_injective(self) -> bool:
        """
        bool : `True` if the correlation is injective,
        `False` otherwise
        """
        return True

    @property
    def min(self) -> float:
        """
        float : Minimum value of the property correlation function within
        the validity range
        """
        return self.__min

    @property
    def max(self) -> float:
        """
        float : Maximum value of the property correlation function within
        the validity range
        """
        return self.__max

    @property
    def T_at_min(self) -> float:
        """
        float : Temperature value corresponding to the minimum value of the
        property correlation function within the validity range
        """
        return self.__T_at_min

    @property
    def T_at_max(self) -> float:
        """
        float : Temperature value corresponding to the maximum value of the
        property correlation function within the validity range
        """
        return self.__T_at_max

    @property
    @abstractmethod
    def range(self) -> List[float]:
        """
        List[float] : Validity range of the property correlation function
        identified by the minimum and the maximum values of the temperature
        """
        raise NotImplementedError(f"{type(self).__name__}.range "
                                  "NOT IMPLEMENTED")

    @property
    @abstractmethod
    def units(self) -> str:
        """
        str : Property unit
        """
        raise NotImplementedError(f"{type(self).__name__}.units "
                                  "NOT IMPLEMENTED")

    @property
    @abstractmethod
    def long_name(self) -> str:
        """
        str : Property long name
        """
        raise NotImplementedError(f"{type(self).__name__}.long_name "
                                  "NOT IMPLEMENTED")

    @property
    @abstractmethod
    def description(self) -> str:
        """
        str : Property description
        """
        raise NotImplementedError(f"{type(self).__name__}.description "
                                  "NOT IMPLEMENTED")
