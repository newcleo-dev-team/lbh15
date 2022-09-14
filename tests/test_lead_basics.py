# This test is used to check correct implementation of some lead properties
# comparing the Lead class output with data.dat
import unittest
from scipy.constants import convert_temperature
import numpy
import sys
import os
sys.path.insert(0, os.path.abspath('..'))
from lbh15 import Lead

# Specify the correlation to use for cp
Lead.set_correlation_to_use('cp', 'gurvich1991')

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
            liquid_lead = Lead(T=convert_temperature(celsius_array[i],
                                                     'C', 'K'))
            self.assertAlmostEqual(liquid_lead.rho, rho_array[i], tol)
            self.assertAlmostEqual(liquid_lead.k, k_array[i], tol)
            self.assertAlmostEqual(liquid_lead.cp, cp_array[i], tol)
            self.assertAlmostEqual(liquid_lead.mu, mu_array[i], tol)


if __name__ == "__main__":
    unittest.main()
