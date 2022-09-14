from lbh15.properties.interface import PropertyInterface


class rho_custom_corr(PropertyInterface):
    def __init__(self):
        super().__init__()
        self._range = [700.0, 1900.0]
        self._units = "[kg/m^3]"
        self._name = "rho"
        self._long_name = "custom density"
        self._description = "Liquid lead " + self._long_name
        self._correlation_name = "custom2022"
        self._is_injective = True

    def correlation(self, T):
        "Implement here the user-defined correlation."
        return 11400 - 1.2*T


class T_double(PropertyInterface):
    def __init__(self):
        super().__init__()
        self._range = [700.0, 1900.0]
        self._units = "[K]"
        self._name = "T_double"
        self._long_name = "double of the temperature"
        self._description = "Liquid lead " + self._long_name
        self._correlation_name = "double2022"
        self._is_injective = True

    def correlation(self, T):
        "Return the temperature value multiplied by 2."
        return 2*T
