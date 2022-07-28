import unittest
from scipy.constants import convert_temperature
import numpy
from lbeh15.lead import Lead

properties_table = numpy.loadtxt("data.dat", comments='#',
                                 skiprows=2, dtype=float)
celsius_array = properties_table[:, 0]
rho_array = properties_table[:, 1]
k_array = properties_table[:, 2]
cp_array = properties_table[:, 3]
mu_array = properties_table[:, 4]
tol = 4


class LeadComparisonTester(unittest.TestCase):

    def test_vs_data(self):
        for i in range(len(celsius_array)):
            liquid_lead = Lead(convert_temperature(celsius_array[i], 'C', 'K'),
                               cp_compact=False)
            self.assertAlmostEqual(liquid_lead.rho, rho_array[i], tol)
            self.assertAlmostEqual(liquid_lead.k, k_array[i], tol)
            self.assertAlmostEqual(liquid_lead.cp, cp_array[i], tol)
            self.assertAlmostEqual(liquid_lead.mu, mu_array[i], tol)


if __name__ == "__main__":
    unittest.main()
