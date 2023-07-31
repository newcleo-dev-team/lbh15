# This test is used to check lbh15 static methods
import unittest
import sys
import os
import json
import inspect
sys.path.insert(0, os.path.abspath('..'))
import lbh15
from lbh15.properties.interface import PropertyInterface


def load_prop(module_name):
    propertyObjectList = []
    module = module_name
    for name, obj in inspect.getmembers(sys.modules[module]):
        if (inspect.isclass(obj) and obj is not PropertyInterface
                and not inspect.isabstract(obj)):
            if issubclass(obj, PropertyInterface):
                propertyObjectList.append(obj())
    return propertyObjectList


def get_val(prop_object, what):
    key = (prop_object.name + "_"
           + prop_object.correlation_name + "_"
           + prop_object.description)
    key = key.replace(" ", "_")
    return file_bounds[key][what], key


with open("properties_bounds.json", "r") as json_file:
    file_bounds = json.load(json_file)


tol = 6


class LeadTester(unittest.TestCase):

    properties = load_prop('lbh15.properties.lead_properties')

    def test_min(self):
        for prop in self.properties:
            prop.compute_bounds()
            val, key = get_val(prop, "min")
            self.assertAlmostEqual(val, prop.min, tol, key+" FAILED")

    def test_T_at_min(self):
        for prop in self.properties:
            prop.compute_bounds()
            val, key = get_val(prop, "T_at_min")
            self.assertAlmostEqual(val, prop.T_at_min, tol, key+" FAILED")

    def test_max(self):
        for prop in self.properties:
            prop.compute_bounds()
            val, key = get_val(prop, "max")
            self.assertAlmostEqual(val, prop.max, tol, key+" FAILED")

    def test_T_at_max(self):
        for prop in self.properties:
            prop.compute_bounds()
            val, key = get_val(prop, "T_at_max")
            self.assertAlmostEqual(val, prop.T_at_max, tol, key+" FAILED")


class LeadSolubilityTester(unittest.TestCase):

    properties = load_prop('lbh15.properties.lead_thermochemical_properties.solubility_in_lead')

    def test_min(self):
        for prop in self.properties:
            prop.compute_bounds()
            val, key = get_val(prop, "min")
            self.assertAlmostEqual(val, prop.min, tol, key+" FAILED")

    def test_T_at_min(self):
        for prop in self.properties:
            prop.compute_bounds()
            val, key = get_val(prop, "T_at_min")
            self.assertAlmostEqual(val, prop.T_at_min, tol, key+" FAILED")

    def test_max(self):
        for prop in self.properties:
            prop.compute_bounds()
            val, key = get_val(prop, "max")
            self.assertAlmostEqual(val, prop.max, tol, key+" FAILED")

    def test_T_at_max(self):
        for prop in self.properties:
            prop.compute_bounds()
            val, key = get_val(prop, "T_at_max")
            self.assertAlmostEqual(val, prop.T_at_max, tol, key+" FAILED")


class LeadDiffusivityTester(unittest.TestCase):

    properties = load_prop('lbh15.properties.lead_thermochemical_properties.diffusivity_in_lead')

    def test_min(self):
        for prop in self.properties:
            prop.compute_bounds()
            val, key = get_val(prop, "min")
            self.assertAlmostEqual(val, prop.min, tol, key+" FAILED")

    def test_T_at_min(self):
        for prop in self.properties:
            prop.compute_bounds()
            val, key = get_val(prop, "T_at_min")
            self.assertAlmostEqual(val, prop.T_at_min, tol, key+" FAILED")

    def test_max(self):
        for prop in self.properties:
            prop.compute_bounds()
            val, key = get_val(prop, "max")
            self.assertAlmostEqual(val, prop.max, tol, key+" FAILED")

    def test_T_at_max(self):
        for prop in self.properties:
            prop.compute_bounds()
            val, key = get_val(prop, "T_at_max")
            self.assertAlmostEqual(val, prop.T_at_max, tol, key+" FAILED")


class LeadThermochemicalTester(unittest.TestCase):

    properties = load_prop('lbh15.properties.lead_thermochemical_properties.lead_thermochemical')

    def test_min(self):
        for prop in self.properties:
            prop.compute_bounds()
            val, key = get_val(prop, "min")
            self.assertAlmostEqual(val, prop.min, tol, key+" FAILED")

    def test_T_at_min(self):
        for prop in self.properties:
            prop.compute_bounds()
            val, key = get_val(prop, "T_at_min")
            self.assertAlmostEqual(val, prop.T_at_min, tol, key+" FAILED")

    def test_max(self):
        for prop in self.properties:
            prop.compute_bounds()
            val, key = get_val(prop, "max")
            self.assertAlmostEqual(val, prop.max, tol, key+" FAILED")

    def test_T_at_max(self):
        for prop in self.properties:
            prop.compute_bounds()
            val, key = get_val(prop, "T_at_max")
            self.assertAlmostEqual(val, prop.T_at_max, tol, key+" FAILED")


class LeadLimitsTester(unittest.TestCase):

    properties = load_prop('lbh15.properties.lead_thermochemical_properties.lead_oxygen_limits')

    def test_min(self):
        for prop in self.properties:
            prop.compute_bounds()
            val, key = get_val(prop, "min")
            self.assertAlmostEqual(val, prop.min, tol, key+" FAILED")

    def test_T_at_min(self):
        for prop in self.properties:
            prop.compute_bounds()
            val, key = get_val(prop, "T_at_min")
            self.assertAlmostEqual(val, prop.T_at_min, tol, key+" FAILED")

    def test_max(self):
        for prop in self.properties:
            prop.compute_bounds()
            val, key = get_val(prop, "max")
            self.assertAlmostEqual(val, prop.max, tol, key+" FAILED")

    def test_T_at_max(self):
        for prop in self.properties:
            prop.compute_bounds()
            val, key = get_val(prop, "T_at_max")
            self.assertAlmostEqual(val, prop.T_at_max, tol, key+" FAILED")


class BismuthTester(unittest.TestCase):

    properties = load_prop('lbh15.properties.bismuth_properties')

    def test_min(self):
        for prop in self.properties:
            prop.compute_bounds()
            val, key = get_val(prop, "min")
            self.assertAlmostEqual(val, prop.min, tol, key+" FAILED")

    def test_T_at_min(self):
        for prop in self.properties:
            prop.compute_bounds()
            val, key = get_val(prop, "T_at_min")
            self.assertAlmostEqual(val, prop.T_at_min, tol, key+" FAILED")

    def test_max(self):
        for prop in self.properties:
            prop.compute_bounds()
            val, key = get_val(prop, "max")
            self.assertAlmostEqual(val, prop.max, tol, key+" FAILED")

    def test_T_at_max(self):
        for prop in self.properties:
            prop.compute_bounds()
            val, key = get_val(prop, "T_at_max")
            self.assertAlmostEqual(val, prop.T_at_max, tol, key+" FAILED")


class BismuthSolubilityTester(unittest.TestCase):

    properties = load_prop('lbh15.properties.bismuth_thermochemical_properties.solubility_in_bismuth')

    def test_min(self):
        for prop in self.properties:
            prop.compute_bounds()
            val, key = get_val(prop, "min")
            self.assertAlmostEqual(val, prop.min, tol, key+" FAILED")

    def test_T_at_min(self):
        for prop in self.properties:
            prop.compute_bounds()
            val, key = get_val(prop, "T_at_min")
            self.assertAlmostEqual(val, prop.T_at_min, tol, key+" FAILED")

    def test_max(self):
        for prop in self.properties:
            prop.compute_bounds()
            val, key = get_val(prop, "max")
            self.assertAlmostEqual(val, prop.max, tol, key+" FAILED")

    def test_T_at_max(self):
        for prop in self.properties:
            prop.compute_bounds()
            val, key = get_val(prop, "T_at_max")
            self.assertAlmostEqual(val, prop.T_at_max, tol, key+" FAILED")


class BismuthDiffusivityTester(unittest.TestCase):

    properties = load_prop('lbh15.properties.bismuth_thermochemical_properties.diffusivity_in_bismuth')

    def test_min(self):
        for prop in self.properties:
            prop.compute_bounds()
            val, key = get_val(prop, "min")
            self.assertAlmostEqual(val, prop.min, tol, key+" FAILED")

    def test_T_at_min(self):
        for prop in self.properties:
            prop.compute_bounds()
            val, key = get_val(prop, "T_at_min")
            self.assertAlmostEqual(val, prop.T_at_min, tol, key+" FAILED")

    def test_max(self):
        for prop in self.properties:
            prop.compute_bounds()
            val, key = get_val(prop, "max")
            self.assertAlmostEqual(val, prop.max, tol, key+" FAILED")

    def test_T_at_max(self):
        for prop in self.properties:
            prop.compute_bounds()
            val, key = get_val(prop, "T_at_max")
            self.assertAlmostEqual(val, prop.T_at_max, tol, key+" FAILED")


class BismuthThermochemicalTester(unittest.TestCase):

    properties = load_prop('lbh15.properties.bismuth_thermochemical_properties.bismuth_thermochemical')

    def test_min(self):
        for prop in self.properties:
            prop.compute_bounds()
            val, key = get_val(prop, "min")
            self.assertAlmostEqual(val, prop.min, tol, key+" FAILED")

    def test_T_at_min(self):
        for prop in self.properties:
            prop.compute_bounds()
            val, key = get_val(prop, "T_at_min")
            self.assertAlmostEqual(val, prop.T_at_min, tol, key+" FAILED")

    def test_max(self):
        for prop in self.properties:
            prop.compute_bounds()
            val, key = get_val(prop, "max")
            self.assertAlmostEqual(val, prop.max, tol, key+" FAILED")

    def test_T_at_max(self):
        for prop in self.properties:
            prop.compute_bounds()
            val, key = get_val(prop, "T_at_max")
            self.assertAlmostEqual(val, prop.T_at_max, tol, key+" FAILED")


class LBETester(unittest.TestCase):

    properties = load_prop('lbh15.properties.lbe_properties')

    def test_min(self):
        for prop in self.properties:
            prop.compute_bounds()
            val, key = get_val(prop, "min")
            self.assertAlmostEqual(val, prop.min, tol, key+" FAILED")

    def test_T_at_min(self):
        for prop in self.properties:
            prop.compute_bounds()
            val, key = get_val(prop, "T_at_min")
            self.assertAlmostEqual(val, prop.T_at_min, tol, key+" FAILED")

    def test_max(self):
        for prop in self.properties:
            prop.compute_bounds()
            val, key = get_val(prop, "max")
            self.assertAlmostEqual(val, prop.max, tol, key+" FAILED")

    def test_T_at_max(self):
        for prop in self.properties:
            prop.compute_bounds()
            val, key = get_val(prop, "T_at_max")
            self.assertAlmostEqual(val, prop.T_at_max, tol, key+" FAILED")


class LBESolubilityTester(unittest.TestCase):

    properties = load_prop('lbh15.properties.lbe_thermochemical_properties.solubility_in_lbe')

    def test_min(self):
        for prop in self.properties:
            prop.compute_bounds()
            val, key = get_val(prop, "min")
            self.assertAlmostEqual(val, prop.min, tol, key+" FAILED")

    def test_T_at_min(self):
        for prop in self.properties:
            prop.compute_bounds()
            val, key = get_val(prop, "T_at_min")
            self.assertAlmostEqual(val, prop.T_at_min, tol, key+" FAILED")

    def test_max(self):
        for prop in self.properties:
            prop.compute_bounds()
            val, key = get_val(prop, "max")
            self.assertAlmostEqual(val, prop.max, tol, key+" FAILED")

    def test_T_at_max(self):
        for prop in self.properties:
            prop.compute_bounds()
            val, key = get_val(prop, "T_at_max")
            self.assertAlmostEqual(val, prop.T_at_max, tol, key+" FAILED")


class LBEDiffusivityTester(unittest.TestCase):

    properties = load_prop('lbh15.properties.lbe_thermochemical_properties.diffusivity_in_lbe')

    def test_min(self):
        for prop in self.properties:
            prop.compute_bounds()
            val, key = get_val(prop, "min")
            self.assertAlmostEqual(val, prop.min, tol, key+" FAILED")

    def test_T_at_min(self):
        for prop in self.properties:
            prop.compute_bounds()
            val, key = get_val(prop, "T_at_min")
            self.assertAlmostEqual(val, prop.T_at_min, tol, key+" FAILED")

    def test_max(self):
        for prop in self.properties:
            prop.compute_bounds()
            val, key = get_val(prop, "max")
            self.assertAlmostEqual(val, prop.max, tol, key+" FAILED")

    def test_T_at_max(self):
        for prop in self.properties:
            prop.compute_bounds()
            val, key = get_val(prop, "T_at_max")
            self.assertAlmostEqual(val, prop.T_at_max, tol, key+" FAILED")


class LBEThermochemicalTester(unittest.TestCase):

    properties = load_prop('lbh15.properties.lbe_thermochemical_properties.lbe_thermochemical')

    def test_min(self):
        for prop in self.properties:
            prop.compute_bounds()
            val, key = get_val(prop, "min")
            self.assertAlmostEqual(val, prop.min, tol, key+" FAILED")

    def test_T_at_min(self):
        for prop in self.properties:
            prop.compute_bounds()
            val, key = get_val(prop, "T_at_min")
            self.assertAlmostEqual(val, prop.T_at_min, tol, key+" FAILED")

    def test_max(self):
        for prop in self.properties:
            prop.compute_bounds()
            val, key = get_val(prop, "max")
            self.assertAlmostEqual(val, prop.max, tol, key+" FAILED")

    def test_T_at_max(self):
        for prop in self.properties:
            prop.compute_bounds()
            val, key = get_val(prop, "T_at_max")
            self.assertAlmostEqual(val, prop.T_at_max, tol, key+" FAILED")


class LBELimitsTester(unittest.TestCase):

    properties = load_prop('lbh15.properties.lbe_thermochemical_properties.lbe_oxygen_limits')

    def test_min(self):
        for prop in self.properties:
            prop.compute_bounds()
            val, key = get_val(prop, "min")
            self.assertAlmostEqual(val, prop.min, tol, key+" FAILED")

    def test_T_at_min(self):
        for prop in self.properties:
            prop.compute_bounds()
            val, key = get_val(prop, "T_at_min")
            self.assertAlmostEqual(val, prop.T_at_min, tol, key+" FAILED")

    def test_max(self):
        for prop in self.properties:
            prop.compute_bounds()
            val, key = get_val(prop, "max")
            self.assertAlmostEqual(val, prop.max, tol, key+" FAILED")

    def test_T_at_max(self):
        for prop in self.properties:
            prop.compute_bounds()
            val, key = get_val(prop, "T_at_max")
            self.assertAlmostEqual(val, prop.T_at_max, tol, key+" FAILED")


if __name__ == "__main__":
    unittest.main()
