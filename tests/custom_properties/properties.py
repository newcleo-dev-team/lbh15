from lbh15.properties.interface import PropertyInterface
from lbh15.properties.interface import range_warning


class rho_custom_corr(PropertyInterface):
    def __init__(self):
        super().__init__(use_package_bounds=False)
        self._min = self.correlation(self.range[1])
        self._T_at_min = self.range[1]
        self._max = self.correlation(self.range[0])
        self._T_at_max = self.range[1]

    @range_warning
    def correlation(self, T, verbose=False):
        "Implement here the user-defined correlation."
        return 11400 - 1.2*T
    
    @property
    def range(self):
        return [700.0, 1900.0]
    
    @property
    def units(self):
        return "[kg/m^3]"

    @property
    def name(self):
        return "rho"

    @property
    def long_name(self):
        return "custom density"
    
    @property
    def description(self):
        return "Liquid lead " + self.long_name
    
    @property
    def correlation_name(self):
        return "custom2022"
    
    @property
    def is_injective(self):
        return True

class T_double(PropertyInterface):
    def __init__(self):
        super().__init__(use_package_bounds=False)
        self._min = self.correlation(self.range[0])
        self._T_at_min = self.range[0]
        self._max = self.correlation(self.range[1])
        self._T_at_max = self.range[0]

    @range_warning
    def correlation(self, T, verbose=False):
        "Return the temperature value multiplied by 2."
        return 2*T
    
    @property
    def range(self):
        return [700.0, 1900.0]
    
    @property
    def units(self):
        return "[K]"

    @property
    def name(self):
        return "T_double"

    @property
    def long_name(self):
        return "double of the temperature"
    
    @property
    def description(self):
        return "Liquid lead " + self.long_name
    
    @property
    def correlation_name(self):
        return "double2022"
    
    @property
    def is_injective(self):
        return True
