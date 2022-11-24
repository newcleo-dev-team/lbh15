import warnings
from abc import ABC, abstractmethod, abstractproperty


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
            if len(args) == 3:
                warnings.warn("The {:s} is requested at "
                              "temperature value of {:.2f} K "
                              "that is not in validity range "
                              "[{:.2f}, {:.2f}] K"
                              .format(p_name, temp,
                                      range_lim[0], range_lim[1]),
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
        from numpy import inf
        self.__min = -inf
        self.__max = inf
        self.__T_at_min = -inf
        self.__T_at_max = inf

    def compute_bounds(self):
        """
        Computes the bound of property in validity range, i.e.,
        the minimum and the maximum of the correlation inside
        the validity range, together with the corresponding temperature.
        If this method is not invoked their default value is
        -inf and inf respectively.
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

    @abstractmethod
    @range_warning
    def correlation(self, T, verbose=False):
        """
        Function that implements the property correlation

        Parameters
        ----------
        T : float
            Temperature in [K]
        verbose : bool, optional
            True to tell decorator to print warning about
            range check failing, False otherwise. By default False
        """
        raise NotImplementedError("{:s}.correlation NOT IMPLEMENTED"
                                  .format(type(self).__name__))

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

    @abstractproperty
    def range(self):
        """
        list : temperature validity range for property correlation
        """
        raise NotImplementedError("{:s}.range NOT IMPLEMENTED"
                                  .format(type(self).__name__))

    @abstractproperty
    def units(self):
        """
        str : property units
        """
        raise NotImplementedError("{:s}.units NOT IMPLEMENTED"
                                  .format(type(self).__name__))

    @abstractproperty
    def long_name(self):
        """
        str : property long name
        """
        raise NotImplementedError("{:s}.long_name NOT IMPLEMENTED"
                                  .format(type(self).__name__))

    @abstractproperty
    def description(self):
        """
        str : property description
        """
        raise NotImplementedError("{:s}.description NOT IMPLEMENTED"
                                  .format(type(self).__name__))
