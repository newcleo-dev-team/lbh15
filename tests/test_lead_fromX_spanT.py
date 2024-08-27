# This test is used to check initialization from properties
import unittest
import sys
import os
import inspect
import numpy as np
sys.path.insert(0, os.path.abspath('..'))
from lbh15.properties.interface import PropertyInterface
from lbh15 import Lead
from lbh15 import lead_properties
from lbh15 import lead_contamination
from scipy.constants import convert_temperature


def load_prop(module_name):
    propertyObjectList = []

    def is_valid(obj):
        return inspect.isclass(obj) and obj is not PropertyInterface \
            and not inspect.isabstract(obj) \
            and issubclass(obj, PropertyInterface)

    for _, obj in inspect.getmembers(sys.modules[module_name], is_valid):
        propertyObjectList.append(obj())
    return propertyObjectList


tol = 8
Ts = [330.0] + list((range(350, 1750, 50))) + [1745.0]
Ts = list(map(lambda x: convert_temperature(x, 'C', 'K'), Ts))
leadPs = []
for T in Ts:
    leadPs.append(Lead(T=T))

# Compute temperature discriminants for cp, P_PbI2 and K_PbI2 root index identification
cp_sobolev2011 = lead_properties.cp_sobolev2011()
cp_sobolev2011.compute_bounds()
T_change_sobolev2011 = cp_sobolev2011.T_at_min
cp_gurvich1991 = lead_properties.cp_gurvich1991()
cp_gurvich1991.compute_bounds()
T_change_gurvich1991 = cp_gurvich1991.T_at_min
P_PbI2 = lead_contamination.LeadIodineVapourPressureKnacke1991()
P_PbI2.compute_bounds()
T_change_P_PbI2 = P_PbI2.T_at_max
K_PbI2 = lead_contamination.LeadIodineHenryConstantKnacke1991()
K_PbI2.compute_bounds()
T_change_K_PbI2 = K_PbI2.T_at_max

class LeadTester(unittest.TestCase):

    def test_init_fromX(self):
        for leadP in leadPs:
            properties = load_prop('lbh15.properties.lead_properties')
            for prop in properties:
                name = prop.name
                if name == 'cp' and\
                        ((prop.correlation_name == 'sobolev2011' \
                        and leadP.T > T_change_sobolev2011) \
                        or \
                        (prop.correlation_name == 'gurvich1991' \
                        and leadP.T > T_change_gurvich1991)):
                    Lead.set_root_to_use('cp', 1)
                val = getattr(leadP, name)
                init_dict = {name: val}
                fromX = Lead(**init_dict)
                self.assertAlmostEqual(leadP.T, fromX.T, tol, name+" FAILED")


class LeadSolubilityTester(unittest.TestCase):

    def test_init_fromX(self):
        for leadP in leadPs:
            properties = load_prop('lbh15.properties.lead_thermochemical_properties.solubility_in_lead')
            for prop in properties:
                name = prop.name
                val = getattr(leadP, name)
                init_dict = {name: val}
                fromX = Lead(**init_dict)
                self.assertAlmostEqual(leadP.T, fromX.T, tol, name+" FAILED")


class LeadDiffusivityTester(unittest.TestCase):

    def test_init_fromX(self):
        for leadP in leadPs:
            properties = load_prop('lbh15.properties.lead_thermochemical_properties.diffusivity_in_lead')
            for prop in properties:
                name = prop.name
                val = getattr(leadP, name)
                init_dict = {name: val}
                fromX = Lead(**init_dict)
                self.assertAlmostEqual(leadP.T, fromX.T, tol, name+" FAILED")


class LeadThermochemicalTester(unittest.TestCase):

    def test_init_fromX(self):
        for leadP in leadPs:
            properties = load_prop('lbh15.properties.lead_thermochemical_properties.lead_thermochemical')
            for prop in properties:
                name = prop.name
                val = getattr(leadP, name)
                init_dict = {name: val}
                fromX = Lead(**init_dict)
                self.assertAlmostEqual(leadP.T, fromX.T, tol, name+" FAILED")


class LeadLimitsTester(unittest.TestCase):

    def test_init_fromX(self):
        for leadP in leadPs:
            properties = load_prop('lbh15.properties.lead_thermochemical_properties.lead_oxygen_limits')
            for prop in properties:
                name = prop.name
                val = getattr(leadP, name)
                init_dict = {name: val}
                fromX = Lead(**init_dict)
                self.assertAlmostEqual(leadP.T, fromX.T, tol, name+" FAILED")

class LeadContaminationTester(unittest.TestCase):

    def test_init_fromX(self):
        for leadP in leadPs:
            properties = load_prop('lbh15.properties.lead_thermochemical_properties.lead_contamination')
            for prop in properties:
                name = prop.name
                if name == 'P_PbI2' and\
                    (prop.correlation_name == 'knacke1991'\
                     and leadP.T > T_change_P_PbI2):
                    Lead.set_root_to_use('P_PbI2', 1)
                if name == 'K_PbI2' and\
                    (prop.correlation_name == 'knacke1991'\
                     and leadP.T > T_change_K_PbI2):
                    Lead.set_root_to_use('K_PbI2', 1)
                val = getattr(leadP, name)
                init_dict = {name: val}
                fromX = Lead(**init_dict)
                if np.isnan(fromX.T):
                    print(f"Test passed for {name} because it is a constant.")
                    continue  
                self.assertAlmostEqual(leadP.T, fromX.T, tol, name+" FAILED")

if __name__ == "__main__":
    unittest.main()
