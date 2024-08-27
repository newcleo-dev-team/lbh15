# This test is used to check initialization from properties
import unittest
import sys
import os
import inspect
import numpy as np
sys.path.insert(0, os.path.abspath('..'))
from lbh15.properties.interface import PropertyInterface
from lbh15 import Bismuth
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
Ts = [275] + list(range(300, 1600, 50))
Ts = list(map(lambda x: convert_temperature(x, 'C', 'K'), Ts))
bismuthPs = []
for T in Ts:
    bismuthPs.append(Bismuth(T=T))


class BismuthTester(unittest.TestCase):

    def test_init_fromX(self):
        for bismuthP in bismuthPs:
            properties = load_prop('lbh15.properties.bismuth_properties')
            for prop in properties:
                name = prop.name
                if name in Bismuth.roots_to_use().keys():
                    continue
                val = getattr(bismuthP, name)
                init_dict = {name: val}
                fromX = Bismuth(**init_dict)
                self.assertAlmostEqual(bismuthP.T, fromX.T, tol, name+" FAILED")


class BismuthSolubilityTester(unittest.TestCase):

    def test_init_fromX(self):
        for bismuthP in bismuthPs:
            properties = load_prop('lbh15.properties.bismuth_thermochemical_properties.solubility_in_bismuth')
            for prop in properties:
                name = prop.name
                val = getattr(bismuthP, name)
                init_dict = {name: val}
                fromX = Bismuth(**init_dict)
                self.assertAlmostEqual(bismuthP.T, fromX.T, tol, name+" FAILED")


class BismuthDiffusivityTester(unittest.TestCase):

    def test_init_fromX(self):
        for bismuthP in bismuthPs:
            properties = load_prop('lbh15.properties.bismuth_thermochemical_properties.diffusivity_in_bismuth')
            for prop in properties:
                name = prop.name
                val = getattr(bismuthP, name)
                init_dict = {name: val}
                fromX = Bismuth(**init_dict)
                self.assertAlmostEqual(bismuthP.T, fromX.T, tol, name+" FAILED")


class BismuthThermochemicalTester(unittest.TestCase):

    def test_init_fromX(self):
        for bismuthP in bismuthPs:
            properties = load_prop('lbh15.properties.bismuth_thermochemical_properties.bismuth_thermochemical')
            for prop in properties:
                name = prop.name
                val = getattr(bismuthP, name)
                init_dict = {name: val}
                fromX = Bismuth(**init_dict)
                self.assertAlmostEqual(bismuthP.T, fromX.T, tol, name+" FAILED")


if __name__ == "__main__":
    unittest.main()
