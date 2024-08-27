# This test is used to check initialization from properties
import unittest
import sys
import os
import inspect
sys.path.insert(0, os.path.abspath('..'))
from lbh15.properties.interface import PropertyInterface
from lbh15 import LBE
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
Ts = [125] + list(range(150, 1700, 50))
Ts = list(map(lambda x: convert_temperature(x, 'C', 'K'), Ts))
lbePs = []
for T in Ts:
    lbePs.append(LBE(T=T))


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


if __name__ == "__main__":
    unittest.main()
