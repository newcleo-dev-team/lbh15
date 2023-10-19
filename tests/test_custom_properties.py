import unittest
import sys
import os
import io
from typing import Union
sys.path.insert(0, os.path.abspath('..'))
from lbh15 import Lead
from lbh15 import LBE
from lbh15 import Bismuth

lead_custom_property_path = os.getcwd() \
    + '/custom_properties/lead_properties.py'
lbe_custom_property_path = os.getcwd() \
    + '/custom_properties/lbe_properties.py'
bismuth_custom_property_path = os.getcwd() \
    + '/custom_properties/bismuth_properties.py'
Lead.set_custom_properties_path(lead_custom_property_path)
LBE.set_custom_properties_path(lbe_custom_property_path)
Bismuth.set_custom_properties_path(bismuth_custom_property_path)


def infoOf(metal_object: Union[Lead, LBE, Bismuth]) -> str:
    """
    Function for capturing the printed info string of
    the liquid metal object passed as argument
    """
    # Freeze the stdout so far
    prev_stdout = sys.stdout
    # Redirect to the stdout the I/O flux
    sys.stdout = buffer = io.StringIO()
    metal_object.rho_info()
    # Restore the right stdout
    sys.stdout = prev_stdout
    # Return the string printed in the meanwhile
    return buffer.getvalue()


##################
# Expected results
# Lead
lead_ref_string = "rho:\n"
lead_ref_string += "\tValue: 9240.00 [kg/m^3]\n"
lead_ref_string += "\tValidity range: [700.00, 1900.00] K\n"
lead_ref_string += "\tCorrelation name: 'custom2022'\n"
lead_ref_string += "\tLong name: custom density\n"
lead_ref_string += "\tUnits: [kg/m^3]\n"
lead_ref_string += "\tDescription:\n"
lead_ref_string += "\t\tLiquid Lead custom density\n"
# LBE
lbe_ref_string = "rho:\n"
lbe_ref_string += "\tValue: 9160.00 [kg/m^3]\n"
lbe_ref_string += "\tValidity range: [800.00, 2000.00] K\n"
lbe_ref_string += "\tCorrelation name: 'custom2022'\n"
lbe_ref_string += "\tLong name: custom density\n"
lbe_ref_string += "\tUnits: [kg/m^3]\n"
lbe_ref_string += "\tDescription:\n"
lbe_ref_string += "\t\tLiquid LBE custom density\n"
# Bismuth
bismuth_ref_string = "rho:\n"
bismuth_ref_string += "\tValue: 9080.00 [kg/m^3]\n"
bismuth_ref_string += "\tValidity range: [900.00, 2100.00] K\n"
bismuth_ref_string += "\tCorrelation name: 'custom2022'\n"
bismuth_ref_string += "\tLong name: custom density\n"
bismuth_ref_string += "\tUnits: [kg/m^3]\n"
bismuth_ref_string += "\tDescription:\n"
bismuth_ref_string += "\t\tLiquid Bismuth custom density\n"


class CustomPropertiesTester(unittest.TestCase):

    def test_custom_rho_lead(self):
        Lead.set_correlation_to_use('rho', 'custom2022')
        liquid_lead = Lead(T=1800)
        self.assertEqual(infoOf(liquid_lead), lead_ref_string, "Lead \
                         properties not loaded properly!")

    def test_custom_rho_lbe(self):
        LBE.set_correlation_to_use('rho', 'custom2022')
        liquid_lbe = LBE(T=1800)
        self.assertEqual(infoOf(liquid_lbe), lbe_ref_string, "LBE \
                         properties not loaded properly!")

    def test_custom_rho_bismuth(self):
        Bismuth.set_correlation_to_use('rho', 'custom2022')
        liquid_bismuth = Bismuth(T=1800)
        self.assertEqual(infoOf(liquid_bismuth), bismuth_ref_string, "Bismuth \
                         properties not loaded properly!")

    def test_T_double(self):
        liquid_lead = Lead(T=1000)
        self.assertEqual(2000, liquid_lead.T_double)


if __name__ == "__main__":
    unittest.main()
