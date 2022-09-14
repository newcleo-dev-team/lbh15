# This test is used to check initialization from properties
import unittest
from scipy.constants import convert_temperature
import sys
import os
sys.path.insert(0, os.path.abspath('..'))
from lbh15 import Lead
from lbh15 import Bismuth
from lbh15 import LBE

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

    def test_p_s(self):
        for leadP in leadPs:
            fromPs = Lead(p_s=leadP.p_s)
            self.assertAlmostEqual(leadP.T, fromPs.T, tol)

    def test_sigma(self):
        for leadP in leadPs:
            fromSigma = Lead(sigma=leadP.sigma)
            self.assertAlmostEqual(leadP.T, fromSigma.T, tol)

    def test_rho(self):
        for leadP in leadPs:
            fromRho = Lead(rho=leadP.rho)
            self.assertAlmostEqual(leadP.T, fromRho.T, tol)

    def test_alpha(self):
        for leadP in leadPs:
            fromAlpha = Lead(alpha=leadP.alpha)
            self.assertAlmostEqual(leadP.T, fromAlpha.T, tol)

    def test_u_s(self):
        for leadP in leadPs:
            fromU_s = Lead(u_s=leadP.u_s)
            self.assertAlmostEqual(leadP.T, fromU_s.T, tol)

    def test_beta_s(self):
        for leadP in leadPs:
            fromBeta_s = Lead(beta_s=leadP.beta_s)
            self.assertAlmostEqual(leadP.T, fromBeta_s.T, tol)

    def test_cp(self):
        first = True
        for leadP in leadPs:
            if first:
                fromCp = Lead(cp=leadP.cp)
            else:
                Lead.set_root_to_use('cp', 1)
                fromCp = Lead(cp=leadP.cp)
            first = False
        self.assertAlmostEqual(leadP.T, fromCp.T, tol)

    def test_h(self):
        for leadP in leadPs:
            fromH = Lead(h=leadP.h)
            self.assertAlmostEqual(leadP.T, fromH.T, tol)

    def test_mu(self):
        for leadP in leadPs:
            fromMu = Lead(mu=leadP.mu)
            self.assertAlmostEqual(leadP.T, fromMu.T, tol)

    def test_r(self):
        for leadP in leadPs:
            fromR = Lead(r=leadP.r)
            self.assertAlmostEqual(leadP.T,  fromR.T, tol)

    def test_k(self):
        for leadP in leadPs:
            fromK = Lead(k=leadP.k)
            self.assertAlmostEqual(leadP.T, fromK.T, tol)


class BismuthTester(unittest.TestCase):

    def test_p_s(self):
        for bismuthP in bismuthPs:
            fromPs = Bismuth(p_s=bismuthP.p_s)
            self.assertAlmostEqual(bismuthP.T, fromPs.T, tol)

    def test_sigma(self):
        for bismuthP in bismuthPs:
            fromSigma = Bismuth(sigma=bismuthP.sigma)
            self.assertAlmostEqual(bismuthP.T, fromSigma.T, tol)

    def test_rho(self):
        for bismuthP in bismuthPs:
            fromRho = Bismuth(rho=bismuthP.rho)
            self.assertAlmostEqual(bismuthP.T, fromRho.T, tol)

    def test_alpha(self):
        for bismuthP in bismuthPs:
            fromAlpha = Bismuth(alpha=bismuthP.alpha)
            self.assertAlmostEqual(bismuthP.T, fromAlpha.T, tol)

    def test_u_s(self):
        for bismuthP in bismuthPs:
            fromU_s = Bismuth(u_s=bismuthP.u_s)
            self.assertAlmostEqual(bismuthP.T, fromU_s.T, tol)

    def test_beta_s(self):
        for bismuthP in bismuthPs:
            fromBeta_s = Bismuth(beta_s=bismuthP.beta_s)
            self.assertAlmostEqual(bismuthP.T, fromBeta_s.T, tol)

    def test_cp(self):
        first = True
        for bismuthP in bismuthPs:
            if first:
                fromCp = Bismuth(cp=bismuthP.cp)
            else:
                Bismuth.set_root_to_use('cp', 1)
                fromCp = Bismuth(cp=bismuthP.cp)
            first = False
        self.assertAlmostEqual(bismuthP.T, fromCp.T, tol)

    def test_h(self):
        for bismuthP in bismuthPs:
            fromH = Bismuth(h=bismuthP.h)
            self.assertAlmostEqual(bismuthP.T, fromH.T, tol)

    def test_mu(self):
        for bismuthP in bismuthPs:
            fromMu = Bismuth(mu=bismuthP.mu)
            self.assertAlmostEqual(bismuthP.T, fromMu.T, tol)

    def test_r(self):
        for bismuthP in bismuthPs:
            fromR = Bismuth(r=bismuthP.r)
            self.assertAlmostEqual(bismuthP.T, fromR.T, tol)

    def test_k(self):
        for bismuthP in bismuthPs:
            fromK = Bismuth(k=bismuthP.k)
            self.assertAlmostEqual(bismuthP.T, fromK.T, tol)


class LBETester(unittest.TestCase):

    def test_p_s(self):
        for lbeP in lbePs:
            fromPs = LBE(p_s=lbeP.p_s)
            self.assertAlmostEqual(lbeP.T, fromPs.T, tol)

    def test_sigma(self):
        for lbeP in lbePs:
            fromSigma = LBE(sigma=lbeP.sigma)
            self.assertAlmostEqual(lbeP.T, fromSigma.T, tol)

    def test_rho(self):
        for lbeP in lbePs:
            fromRho = LBE(rho=lbeP.rho)
            self.assertAlmostEqual(lbeP.T, fromRho.T, tol)

    def test_alpha(self):
        for lbeP in lbePs:
            fromAlpha = LBE(alpha=lbeP.alpha)
            self.assertAlmostEqual(lbeP.T, fromAlpha.T, tol)

    def test_u_s(self):
        for lbeP in lbePs:
            fromU_s = LBE(u_s=lbeP.u_s)
            self.assertAlmostEqual(lbeP.T, fromU_s.T, tol)

    def test_beta_s(self):
        for lbeP in lbePs:
            fromBeta_s = LBE(beta_s=lbeP.beta_s)
            self.assertAlmostEqual(lbeP.T, fromBeta_s.T, tol)

    def test_cp(self):
        first = True
        for lbeP in lbePs:
            if first:
                fromCp = LBE(cp=lbeP.cp)
            else:
                LBE.set_root_to_use('cp', 1)
                fromCp = LBE(cp=lbeP.cp)
            first = False
            self.assertAlmostEqual(lbeP.T, fromCp.T, tol)

    def test_h(self):
        for lbeP in lbePs:
            fromH = LBE(h=lbeP.h)
            self.assertAlmostEqual(lbeP.T, fromH.T, tol)

    def test_mu(self):
        for lbeP in lbePs:
            fromMu = LBE(mu=lbeP.mu)
            self.assertAlmostEqual(lbeP.T, fromMu.T, tol)

    def test_r(self):
        for lbeP in lbePs:
            fromR = LBE(r=lbeP.r)
            self.assertAlmostEqual(lbeP.T, fromR.T, tol)

    def test_k(self):
        for lbeP in lbePs:
            fromK = LBE(k=lbeP.k)
            self.assertAlmostEqual(lbeP.T, fromK.T, tol)


if __name__ == "__main__":
    unittest.main()
