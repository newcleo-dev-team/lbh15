from scipy.constants import atm
from lbh15.properties.interface import PropertyInterface
from lbh15.properties.interface import range_warning


class rho_custom_corr(PropertyInterface):
    @range_warning
    def correlation(self, T, p=atm, verbose=False):
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
        return "Liquid Lead " + self.long_name

    @property
    def correlation_name(self):
        return "custom2022"


class T_double(PropertyInterface):
    @range_warning
    def correlation(self, T, p=atm, verbose=False):
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
