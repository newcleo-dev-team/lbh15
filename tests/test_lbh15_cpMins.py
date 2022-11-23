# This test is used to check lbh15 static methods
import unittest
import sys
import os
sys.path.insert(0, os.path.abspath('..'))
from lbh15 import Lead
from lbh15 import Bismuth
from lbh15 import LBE
from lbh15.properties.lead_properties import cp_gurvich1991, cp_sobolev2011
from lbh15.properties.bismuth_properties import cp as cp_bmth
from lbh15.properties.lbe_properties import cp as cp_lbe


LEAD_T_AT_CP_MIN_GURVICH = 1682.522  # [K]
LEAD_T_AT_CP_MIN_SOBOLEV = 1568.665  # [K]
LEAD_CP_MIN_GURVICH = 137.287133  # [J/(kg*K)]
LEAD_CP_MIN_SOBOLEV = 136.348649  # [J/(kg*K)]
BISMUTH_T_AT_CP_MIN = 1342.753  # [K]
BISMUTH_CP_MIN = 130.151844  # [J/(kg*K)]
LBE_T_AT_CP_MIN = 1566.510  # [K]
LBE_CP_MIN = 133.568103  # [J/(kg*K)]


tol = 6


class LeadTester(unittest.TestCase):

    def test_lead_sobolev(self):
        cp_ll = cp_sobolev2011()
        self.assertAlmostEqual(LEAD_CP_MIN_SOBOLEV, cp_ll.min, tol)

    def test_lead_gurvich(self):
        cp_ll = cp_gurvich1991()
        self.assertAlmostEqual(LEAD_CP_MIN_GURVICH, cp_ll.min, tol)


class BismuthTester(unittest.TestCase):

    def test_bismuth(self):
        cp_lb = cp_bmth()
        self.assertAlmostEqual(BISMUTH_CP_MIN, cp_lb.min, tol)


class LBETester(unittest.TestCase):

    def test_lbe(self):
        cp_l_lbe = cp_lbe()
        self.assertAlmostEqual(LBE_CP_MIN, cp_l_lbe.min, tol)


if __name__ == "__main__":
    unittest.main()
