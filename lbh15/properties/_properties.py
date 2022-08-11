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
        raise NotImplementedError("{:s}.correlation NOT IMPLEMENTED"
                                  .format(type(self).__name__))

    @property
    def name(self):
        return self._name
    
    @property
    def range(self):
        return self._range.copy()
    
    @property
    def units(self):
        return self._units
    
    @property
    def long_name(self):
        return self._long_name
    
    @property
    def description(self):
        return self._description