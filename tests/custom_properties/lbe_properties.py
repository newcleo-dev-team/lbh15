from scipy.constants import atm
from lbh15.properties.interface import PropertyInterface
from lbh15.properties.interface import range_warning


class rho_custom_corr(PropertyInterface):
    @range_warning
    def correlation(self, T, p=atm, verbose=False):
        "Implement here the user-defined correlation."
        return 11500 - 1.3*T

    @property
    def range(self):
        return [800.0, 2000.0]

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
        return "Liquid LBE " + self.long_name

    @property
    def correlation_name(self):
        return "custom2022"
