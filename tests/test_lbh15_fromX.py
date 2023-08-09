# This test is used to check initialization from properties
import unittest
import sys
import os
import inspect
sys.path.insert(0, os.path.abspath('..'))
from lbh15.properties.interface import PropertyInterface
from lbh15 import Lead
from lbh15 import Bismuth
from lbh15 import LBE
from scipy.constants import convert_temperature


def load_prop(module_name):
    propertyObjectList = []
    module = module_name
    for obj in inspect.getmembers(sys.modules[module]):
        if (inspect.isclass(obj) and obj is not PropertyInterface
                and not inspect.isabstract(obj)):
            if issubclass(obj, PropertyInterface):
                propertyObjectList.append(obj())
    return propertyObjectList


tol = 8
Ts = [convert_temperature(395, 'C', 'K'), convert_temperature(1500, 'C', 'K')]
leadPs = []
bismuthPs = []
lbePs = []
for T in Ts:
    leadPs.append(Lead(T=T))
    bismuthPs.append(Bismuth(T=T))
    lbePs.append(LBE(T=T))


class LeadTester(unittest.TestCase):

    def test_init_fromX(self):
        first = True
        for leadP in leadPs:
            properties = load_prop('lbh15.properties.lead_properties')
            for prop in properties:
                name = prop.name
                val = getattr(leadP, name)
                init_dict = {name: val}
                if not first and name == 'cp':
                    Lead.set_root_to_use('cp', 1)
                fromX = Lead(**init_dict)
                self.assertAlmostEqual(leadP.T, fromX.T, tol, name+" FAILED")
            first = False


class LeadSolubilityTester(unittest.TestCase):

    def test_init_fromX(self):
        first = True
        for leadP in leadPs:
            properties = load_prop('lbh15.properties.lead_thermochemical_properties.solubility_in_lead')
            for prop in properties:
                name = prop.name
                val = getattr(leadP, name)
                init_dict = {name: val}
                fromX = Lead(**init_dict)
                self.assertAlmostEqual(leadP.T, fromX.T, tol, name+" FAILED")
            first = False


class LeadDiffusivityTester(unittest.TestCase):

    def test_init_fromX(self):
        first = True
        for leadP in leadPs:
            properties = load_prop('lbh15.properties.lead_thermochemical_properties.diffusivity_in_lead')
            for prop in properties:
                name = prop.name
                val = getattr(leadP, name)
                init_dict = {name: val}
                fromX = Lead(**init_dict)
                self.assertAlmostEqual(leadP.T, fromX.T, tol, name+" FAILED")
            first = False


class LeadThermochemicalTester(unittest.TestCase):

    def test_init_fromX(self):
        first = True
        for leadP in leadPs:
            properties = load_prop('lbh15.properties.lead_thermochemical_properties.lead_thermochemical')
            for prop in properties:
                name = prop.name
                val = getattr(leadP, name)
                init_dict = {name: val}
                fromX = Lead(**init_dict)
                self.assertAlmostEqual(leadP.T, fromX.T, tol, name+" FAILED")
            first = False


class LeadLimitsTester(unittest.TestCase):

    def test_init_fromX(self):
        first = True
        for leadP in leadPs:
            properties = load_prop('lbh15.properties.lead_thermochemical_properties.lead_oxygen_limits')
            for prop in properties:
                name = prop.name
                val = getattr(leadP, name)
                init_dict = {name: val}
                fromX = Lead(**init_dict)
                self.assertAlmostEqual(leadP.T, fromX.T, tol, name+" FAILED")
            first = False


class BismuthTester(unittest.TestCase):

    def test_init_fromX(self):
        first = True
        for bismuthP in bismuthPs:
            properties = load_prop('lbh15.properties.bismuth_properties')
            for prop in properties:
                name = prop.name
                val = getattr(bismuthP, name)
                init_dict = {name: val}
                if not first and name == 'cp':
                    Bismuth.set_root_to_use('cp', 1)
                fromX = Bismuth(**init_dict)
                self.assertAlmostEqual(bismuthP.T, fromX.T, tol, name+" FAILED")
            first = False


class BismuthSolubilityTester(unittest.TestCase):

    def test_init_fromX(self):
        first = True
        for bismuthP in bismuthPs:
            properties = load_prop('lbh15.properties.bismuth_thermochemical_properties.solubility_in_bismuth')
            for prop in properties:
                name = prop.name
                val = getattr(bismuthP, name)
                init_dict = {name: val}
                fromX = Bismuth(**init_dict)
                self.assertAlmostEqual(bismuthP.T, fromX.T, tol, name+" FAILED")
            first = False


class BismuthDiffusivityTester(unittest.TestCase):

    def test_init_fromX(self):
        first = True
        for bismuthP in bismuthPs:
            properties = load_prop('lbh15.properties.bismuth_thermochemical_properties.diffusivity_in_bismuth')
            for prop in properties:
                name = prop.name
                val = getattr(bismuthP, name)
                init_dict = {name: val}
                fromX = Bismuth(**init_dict)
                self.assertAlmostEqual(bismuthP.T, fromX.T, tol, name+" FAILED")
            first = False


class BismuthThermochemicalTester(unittest.TestCase):

    def test_init_fromX(self):
        first = True
        for bismuthP in bismuthPs:
            properties = load_prop('lbh15.properties.bismuth_thermochemical_properties.bismuth_thermochemical')
            for prop in properties:
                name = prop.name
                val = getattr(bismuthP, name)
                init_dict = {name: val}
                fromX = Bismuth(**init_dict)
                self.assertAlmostEqual(bismuthP.T, fromX.T, tol, name+" FAILED")
            first = False


class LBETester(unittest.TestCase):

    def test_init_fromX(self):
        first = True
        for lbeP in lbePs:
            properties = load_prop('lbh15.properties.lbe_properties')
            for prop in properties:
                name = prop.name
                val = getattr(lbeP, name)
                init_dict = {name: val}
                if not first and name == 'cp':
                    LBE.set_root_to_use('cp', 1)
                fromX = LBE(**init_dict)
                self.assertAlmostEqual(lbeP.T, fromX.T, tol, name+" FAILED")
            first = False


class LBESolubilityTester(unittest.TestCase):

    def test_init_fromX(self):
        first = True
        for lbeP in lbePs:
            properties = load_prop('lbh15.properties.lbe_thermochemical_properties.solubility_in_lbe')
            for prop in properties:
                name = prop.name
                val = getattr(lbeP, name)
                init_dict = {name: val}
                fromX = LBE(**init_dict)
                self.assertAlmostEqual(lbeP.T, fromX.T, tol, name+" FAILED")
            first = False


class LBEDiffusivityTester(unittest.TestCase):

    def test_init_fromX(self):
        first = True
        for lbeP in lbePs:
            properties = load_prop('lbh15.properties.lbe_thermochemical_properties.diffusivity_in_lbe')
            for prop in properties:
                name = prop.name
                val = getattr(lbeP, name)
                init_dict = {name: val}
                fromX = LBE(**init_dict)
                self.assertAlmostEqual(lbeP.T, fromX.T, tol, name+" FAILED")
            first = False


class LBEThermochemicalTester(unittest.TestCase):

    def test_init_fromX(self):
        first = True
        for lbeP in lbePs:
            properties = load_prop('lbh15.properties.lbe_thermochemical_properties.lbe_thermochemical')
            for prop in properties:
                name = prop.name
                val = getattr(lbeP, name)
                init_dict = {name: val}
                fromX = LBE(**init_dict)
                self.assertAlmostEqual(lbeP.T, fromX.T, tol, name+" FAILED")
            first = False


class LBELimitsTester(unittest.TestCase):

    def test_init_fromX(self):
        first = True
        for lbeP in lbePs:
            properties = load_prop('lbh15.properties.lbe_thermochemical_properties.lbe_oxygen_limits')
            for prop in properties:
                name = prop.name
                val = getattr(lbeP, name)
                init_dict = {name: val}
                fromX = LBE(**init_dict)
                self.assertAlmostEqual(lbeP.T, fromX.T, tol, name+" FAILED")
            first = False


if __name__ == "__main__":
    unittest.main()
