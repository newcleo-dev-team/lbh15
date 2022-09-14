from abc import ABC, abstractmethod


class PropertyInterface(ABC):
    """
    Abstract class that defines thermo-physical property interface.
    Derived classes must implement :func:`~PropertyInterface.correlation`,
    and must override members returned by:

        - :attr:`~.PropertyInterface.range`
        - :attr:`~.PropertyInterface.units`
        - :attr:`~.PropertyInterface.long_name`
        - :attr:`~.PropertyInterface.description`

    Instead, it is not mandatory to override the following attributes:

        - :func:`~PropertyInterface.initialization_helper`, override this \
          method if roots of the function are particulary 'difficult' to find \
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
        self._name = type(self).__name__
        self._range = [-inf, inf]
        self._correlation_name = "lbh15"
        self._units = "[-]"
        self._long_name = "long name of the property interface"
        self._description = "description of the property interface"
        self._is_injective = True

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

    @property
    def is_injective(self):
        """
        bool : True if correlation is injective,
        False otherwise
        """
        return self._is_injective
