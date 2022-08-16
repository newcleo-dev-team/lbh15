from abc import ABC, abstractmethod
from numpy import inf


class PropertiesInterface(ABC):
    def __init__(self):
        self._name = type(self).__name__
        self._range = [-inf, inf]
        self._units = "[-]"
        self._long_name = "properties interface"
        self._description = "This is properties interface, override me"

    @abstractmethod
    def correlation(self, T):
        """
        Function that implements the property correlation

        Parameters
        ----------
        T : float
            Temperature in [K]
        """
        raise NotImplementedError("{:s}.correlation NOT IMPLEMENTED"
                                  .format(type(self).__name__))

    @property
    def name(self):
        """
        str : name of the property
        """
        return self._name

    @property
    def range(self):
        """
        list : temperature validity range for property correlation
        """
        return self._range.copy()

    @property
    def units(self):
        """
        str : property units
        """
        return self._units

    @property
    def long_name(self):
        """
        str : property long name
        """
        return self._long_name

    @property
    def description(self):
        """
        str : property description
        """
        return self._description
