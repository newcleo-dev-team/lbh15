import warnings
import json
import pathlib
from abc import ABC, abstractmethod, abstractproperty


PROP_PATH = str(pathlib.Path(__file__).parent.resolve())


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
    Derived classes must implement :func:`~PropertyInterface.correlation`,
    and must override:

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
    def __init__(self, use_package_bounds=True):
        from numpy import inf
        self._min = -inf
        self._max = inf
        self._T_at_min = self.range[0]
        self._T_at_max = self.range[1]
        if use_package_bounds:
            self.__read_bounds()

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
        return self._min

    @property
    def max(self):
        """
        float : maximum of property correlation in validity
        range
        """
        return self._max

    @property
    def T_at_min(self):
        """
        float : temperature corresponding to the minimum of
        property correlation in validity range
        """
        return self._T_at_min

    @property
    def T_at_max(self):
        """
        float : temperature corresponding to the maximum of
        property correlation in validity range
        """
        return self._T_at_max

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

    def __read_bounds(self):
        """
        Computes the bound of property in validity range, i.e.,
        the minimum and the maximum of the correlation, together with the
        corresponding temperature
        """
        with open(PROP_PATH + '/properties_bounds.json') as json_file:
            bounds = json.load(json_file)
        json_file.close()

        key = self.name + "_" + self.correlation_name + "_" + self.description
        key = key.replace(" ", "_")
        bounds = bounds[key]
        self._min = bounds['min']
        self._T_at_min = bounds["T_at_min"]
        self._max = bounds["max"]
        self._T_at_max = bounds["T_at_max"]
