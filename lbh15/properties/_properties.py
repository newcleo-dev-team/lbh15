from abc import ABC, abstractmethod
from numpy import inf


class PropertyInterface(ABC):
    def __init__(self):
        self._name = type(self).__name__ #this is the name of the variable
        self._range = [-inf, inf]
        self._correlation_name = "lbh15"
        self._units = "[-]"
        self._long_name = "long name of the property interface"
        self._description = "description of the property interface"

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

    def initialization_helper(self, property_value):
        return None

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
    def correlation_name(self):
        """
        str : name of the correlation
        """
        return self._correlation_name

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
