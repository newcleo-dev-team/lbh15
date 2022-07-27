import unittest
import lbeh15.lead as lead
import lbeh15.bismuth as bismuth
import lbeh15.lbe as lbe

tol = 8
Ts = [395+273.15, 1500+273.15]
leadPs = []
bismuthPs = []
lbePs = []
for T in Ts:
    leadPs.append(lead.Lead(T))
    bismuthPs.append(bismuth.Bismuth(T))
    lbePs.append(lbe.LBE(T))


class LeadTester(unittest.TestCase):

    def test_p_s(self):
        for leadP in leadPs:
            fromPs = lead.LeadP_s(leadP.p_s)
            self.assertAlmostEqual(leadP.T, fromPs.T, tol)

    def test_sigma(self):
        for leadP in leadPs:
            fromSigma = lead.LeadSigma(leadP.sigma)
            self.assertAlmostEqual(leadP.T, fromSigma.T, tol)

    def test_rho(self):
        for leadP in leadPs:
            fromRho = lead.LeadRho(leadP.rho)
            self.assertAlmostEqual(leadP.T, fromRho.T, tol)

    def test_alpha(self):
        for leadP in leadPs:
            fromAlpha = lead.LeadAlpha(leadP.alpha)
            self.assertAlmostEqual(leadP.T, fromAlpha.T, tol)

    def test_u_s(self):
        for leadP in leadPs:
            fromU_s = lead.LeadU_s(leadP.u_s)
            self.assertAlmostEqual(leadP.T, fromU_s.T, tol)

    def test_beta_s(self):
        for leadP in leadPs:
            fromBeta_s = lead.LeadBeta_s(leadP.beta_s)
            self.assertAlmostEqual(leadP.T, fromBeta_s.T, tol)

    def test_cp(self):
        first = True
        for leadP in leadPs:
            if first:
                fromCp = lead.LeadCp(leadP.cp)
            else:
                fromCp = lead.LeadCp(leadP.cp, second_root=True)
            first = False
        self.assertAlmostEqual(leadP.T, fromCp.T, tol)

    def test_delta_h(self):
        for leadP in leadPs:
            fromDelta_h = lead.LeadDelta_h(leadP.delta_h)
            self.assertAlmostEqual(leadP.T, fromDelta_h.T, tol)

    def test_mu(self):
        for leadP in leadPs:
            fromMu = lead.LeadMu(leadP.mu)
            self.assertAlmostEqual(leadP.T, fromMu.T, tol)

    def test_r(self):
        for leadP in leadPs:
            fromR = lead.LeadR(leadP.r)
            self.assertAlmostEqual(leadP.T,  fromR.T, tol)

    def test_k(self):
        for leadP in leadPs:
            fromK = lead.LeadK(leadP.k)
            self.assertAlmostEqual(leadP.T, fromK.T, tol)


class BismuthTester(unittest.TestCase):

    def test_p_s(self):
        for bismuthP in bismuthPs:
            fromPs = bismuth.BismuthP_s(bismuthP.p_s)
            self.assertAlmostEqual(bismuthP.T, fromPs.T, tol)

    def test_sigma(self):
        for bismuthP in bismuthPs:
            fromSigma = bismuth.BismuthSigma(bismuthP.sigma)
            self.assertAlmostEqual(bismuthP.T, fromSigma.T, tol)

    def test_rho(self):
        for bismuthP in bismuthPs:
            fromRho = bismuth.BismuthRho(bismuthP.rho)
            self.assertAlmostEqual(bismuthP.T, fromRho.T, tol)

    def test_alpha(self):
        for bismuthP in bismuthPs:
            fromAlpha = bismuth.BismuthAlpha(bismuthP.alpha)
            self.assertAlmostEqual(bismuthP.T, fromAlpha.T, tol)

    def test_u_s(self):
        for bismuthP in bismuthPs:
            fromU_s = bismuth.BismuthU_s(bismuthP.u_s)
            self.assertAlmostEqual(bismuthP.T, fromU_s.T, tol)

    def test_beta_s(self):
        for bismuthP in bismuthPs:
            fromBeta_s = bismuth.BismuthBeta_s(bismuthP.beta_s)
            self.assertAlmostEqual(bismuthP.T, fromBeta_s.T, tol)

    def test_cp(self):
        first = True
        for bismuthP in bismuthPs:
            if first:
                fromCp = bismuth.BismuthCp(bismuthP.cp)
            else:
                fromCp = bismuth.BismuthCp(bismuthP.cp, second_root=True)
            first = False
        self.assertAlmostEqual(bismuthP.T, fromCp.T, tol)

    def test_delta_h(self):
        for bismuthP in bismuthPs:
            fromDelta_h = bismuth.BismuthDelta_h(bismuthP.delta_h)
            self.assertAlmostEqual(bismuthP.T, fromDelta_h.T, tol)

    def test_mu(self):
        for bismuthP in bismuthPs:
            fromMu = bismuth.BismuthMu(bismuthP.mu)
            self.assertAlmostEqual(bismuthP.T, fromMu.T, tol)

    def test_r(self):
        for bismuthP in bismuthPs:
            fromR = bismuth.BismuthR(bismuthP.r)
            self.assertAlmostEqual(bismuthP.T, fromR.T, tol)

    def test_k(self):
        for bismuthP in bismuthPs:
            fromK = bismuth.BismuthK(bismuthP.k)
            self.assertAlmostEqual(bismuthP.T, fromK.T, tol)


class LBETester(unittest.TestCase):

    def test_p_s(self):
        for lbeP in lbePs:
            fromPs = lbe.LBEP_s(lbeP.p_s)
            self.assertAlmostEqual(lbeP.T, fromPs.T, tol)

    def test_sigma(self):
        for lbeP in lbePs:
            fromSigma = lbe.LBESigma(lbeP.sigma)
            self.assertAlmostEqual(lbeP.T, fromSigma.T, tol)

    def test_rho(self):
        for lbeP in lbePs:
            fromRho = lbe.LBERho(lbeP.rho)
            self.assertAlmostEqual(lbeP.T, fromRho.T, tol)

    def test_alpha(self):
        for lbeP in lbePs:
            fromAlpha = lbe.LBEAlpha(lbeP.alpha)
            self.assertAlmostEqual(lbeP.T, fromAlpha.T, tol)

    def test_u_s(self):
        for lbeP in lbePs:
            fromU_s = lbe.LBEU_s(lbeP.u_s)
            self.assertAlmostEqual(lbeP.T, fromU_s.T, tol)

    def test_beta_s(self):
        for lbeP in lbePs:
            fromBeta_s = lbe.LBEBeta_s(lbeP.beta_s)
            self.assertAlmostEqual(lbeP.T, fromBeta_s.T, tol)

    def test_cp(self):
        first = True
        for lbeP in lbePs:
            if first:
                fromCp = lbe.LBECp(lbeP.cp)
            else:
                fromCp = lbe.LBECp(lbeP.cp, second_root=True)
            first = False
            self.assertAlmostEqual(lbeP.T, fromCp.T, tol)

    def test_delta_h(self):
        for lbeP in lbePs:
            fromDelta_h = lbe.LBEDelta_h(lbeP.delta_h)
            self.assertAlmostEqual(lbeP.T, fromDelta_h.T, tol)

    def test_mu(self):
        for lbeP in lbePs:
            fromMu = lbe.LBEMu(lbeP.mu)
            self.assertAlmostEqual(lbeP.T, fromMu.T, tol)

    def test_r(self):
        for lbeP in lbePs:
            fromR = lbe.LBER(lbeP.r)
            self.assertAlmostEqual(lbeP.T, fromR.T, tol)

    def test_k(self):
        for lbeP in lbePs:
            fromK = lbe.LBEK(lbeP.k)
            self.assertAlmostEqual(lbeP.T, fromK.T, tol)


if __name__ == "__main__":
    unittest.main()
