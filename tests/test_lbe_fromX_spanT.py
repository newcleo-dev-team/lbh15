# This test is used to check initialization from properties
import unittest
import sys
import os
import inspect
sys.path.insert(0, os.path.abspath('..'))
from lbh15.properties.interface import PropertyInterface
from lbh15 import LBE
from lbh15 import lead_contamination
from scipy.constants import convert_temperature


def load_prop(module_name):
    propertyObjectList = []

    def is_valid(obj):
        return inspect.isclass(obj) and obj is not PropertyInterface \
            and not inspect.isabstract(obj) \
            and issubclass(obj, PropertyInterface) \
            and not obj.__module__.endswith("lead_contamination")

    for _, obj in inspect.getmembers(sys.modules[module_name], is_valid):
        propertyObjectList.append(obj())
    return propertyObjectList


tol = 8
Ts = [125] + list(range(150, 1700, 50))
Ts = list(map(lambda x: convert_temperature(x, 'C', 'K'), Ts))
lbePs = []
for T in Ts:
    lbePs.append(LBE(T=T))

# Compute temperature discriminants for P_PbI2 and K_PbI2 root index identification
P_PbI2 = lead_contamination.LeadIodineVapourPressureKnacke1991()
P_PbI2.compute_bounds()
T_change_P_PbI2 = P_PbI2.T_at_max
K_PbI2 = lead_contamination.LeadIodineHenryConstantKnacke1991()
K_PbI2.compute_bounds()
T_change_K_PbI2 = K_PbI2.T_at_max
K_Cs = lead_contamination.LeadCaesiumHenryConstantYamshchikov2001()
K_Cs.compute_bounds()
T_change_K_Cs = K_Cs.T_at_max

class LBETester(unittest.TestCase):

    def test_init_fromX(self):
        for lbeP in lbePs:
            properties = load_prop('lbh15.properties.lbe_properties')
            for prop in properties:
                name = prop.name
                if name in LBE.roots_to_use().keys():
                    continue
                val = getattr(lbeP, name)
                init_dict = {name: val}
                fromX = LBE(**init_dict)
                self.assertAlmostEqual(lbeP.T, fromX.T, tol, name+" FAILED")


class LBESolubilityTester(unittest.TestCase):

    def test_init_fromX(self):
        for lbeP in lbePs:
            properties = load_prop('lbh15.properties.lbe_thermochemical_properties.solubility_in_lbe')
            for prop in properties:
                name = prop.name
                val = getattr(lbeP, name)
                init_dict = {name: val}
                fromX = LBE(**init_dict)
                self.assertAlmostEqual(lbeP.T, fromX.T, tol, name+" FAILED")


class LBEDiffusivityTester(unittest.TestCase):

    def test_init_fromX(self):
        for lbeP in lbePs:
            properties = load_prop('lbh15.properties.lbe_thermochemical_properties.diffusivity_in_lbe')
            for prop in properties:
                name = prop.name
                val = getattr(lbeP, name)
                init_dict = {name: val}
                fromX = LBE(**init_dict)
                self.assertAlmostEqual(lbeP.T, fromX.T, tol, name+" FAILED")


class LBEThermochemicalTester(unittest.TestCase):

    def test_init_fromX(self):
        for lbeP in lbePs:
            properties = load_prop('lbh15.properties.lbe_thermochemical_properties.lbe_thermochemical')
            for prop in properties:
                name = prop.name
                val = getattr(lbeP, name)
                init_dict = {name: val}
                fromX = LBE(**init_dict)
                self.assertAlmostEqual(lbeP.T, fromX.T, tol, name+" FAILED")


class LBELimitsTester(unittest.TestCase):

    def test_init_fromX(self):
        for lbeP in lbePs:
            properties = load_prop('lbh15.properties.lbe_thermochemical_properties.lbe_oxygen_limits')
            for prop in properties:
                name = prop.name
                val = getattr(lbeP, name)
                init_dict = {name: val}
                fromX = LBE(**init_dict)
                self.assertAlmostEqual(lbeP.T, fromX.T, tol, name+" FAILED")


class LBEContaminationTester(unittest.TestCase):

    def test_init_fromX(self):
        for lbeP in lbePs:
            properties = load_prop('lbh15.properties.lbe_thermochemical_properties.lbe_contamination')
            for prop in properties:
                name = prop.name
                if name == 'gamma_Cs' and prop.correlation_name == 'ohno2006':
                    lbeP.change_correlation_to_use(name, prop.correlation_name)
                    LBE.set_correlation_to_use(name, prop.correlation_name)
                if prop.is_constant():
                    continue
                if name == 'P_PbI2' and\
                    (prop.correlation_name == 'knacke1991'\
                     and lbeP.T > T_change_P_PbI2):
                    LBE.set_root_to_use('P_PbI2', 1)
                if name == 'K_PbI2' and\
                    (prop.correlation_name == 'knacke1991'\
                     and lbeP.T > T_change_K_PbI2):
                    LBE.set_root_to_use('K_PbI2', 1)
                if name == 'K_Cs' and\
                    lbeP.T > T_change_K_Cs:
                    LBE.set_root_to_use('K_Cs', 1)
                val = getattr(lbeP, name)
                init_dict = {name: val}
                fromX = LBE(**init_dict)
                self.assertAlmostEqual(lbeP.T, fromX.T, tol,
                                       name+" FAILED")


if __name__ == "__main__":
    unittest.main()
