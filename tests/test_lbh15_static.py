# This test is used to check lbh15 static methods
import unittest
import sys
sys.path.insert(0, '..')
from lbh15 import Lead
from lbh15 import Bismuth
from lbh15 import LBE

tol = 6


class LeadTester(unittest.TestCase):

    def test_lead_sobolev(self):
        liquid_lead = Lead(T=Lead.T_at_cp_min('sobolev2011'),
                           cp_correlation_to_use='sobolev2011')
        self.assertAlmostEqual(Lead.cp_min('sobolev2011'), liquid_lead.cp, tol)

    def test_lead_gurvich(self):
        liquid_lead = Lead(T=Lead.T_at_cp_min('gurvich1991'),
                           cp_correlation_to_use='gurvich1991')
        self.assertAlmostEqual(Lead.cp_min('gurvich1991'), liquid_lead.cp, tol)


class BismuthTester(unittest.TestCase):

    def test_bismuth(self):
        liquid_bismuth = Bismuth(T=Bismuth.T_at_cp_min())
        self.assertAlmostEqual(Bismuth.cp_min(), liquid_bismuth.cp, tol)


class LBETester(unittest.TestCase):

    def test_lbe(self):
        liquid_lbe = LBE(T=LBE.T_at_cp_min())
        self.assertAlmostEqual(LBE.cp_min(), liquid_lbe.cp, tol)


if __name__ == "__main__":
    unittest.main()
