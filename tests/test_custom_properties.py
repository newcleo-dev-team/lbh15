import unittest
import sys
import os
sys.path.insert(0, '..')
from lbh15 import Lead

custom_property_path = os.getcwd() + '/custom_properties/properties.py'
Lead.set_custom_properties_path(custom_property_path)


class CustomPropertiesTester(unittest.TestCase):

    def test_custom_rho(self):
        Lead.set_correlation_to_use('rho', 'custom2022')
        liquid_lead = Lead(T=1000)
        self.assertTrue(hasattr(liquid_lead, 'rho'))

    def test_T_double(self):
        liquid_lead = Lead(T=1000)
        self.assertEqual(2000, liquid_lead.T_double)


if __name__ == "__main__":
    unittest.main()
