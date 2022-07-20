import unittest
import lbeh15.lead as lead
import lbeh15.bismuth as bismuth
import lbeh15.lbe as lbe

T = 395
tol = 9
leadP = lead.Lead(T, 'degC')
bismuthP = bismuth.Bismuth(T, 'degC')
lbeP = lbe.LBE(T, 'degC')


class LeadTester(unittest.TestCase):

    def test_p_s(self):
        fromPs = lead.LeadP_s(leadP.p_s)
        self.assertAlmostEqual(T, fromPs.T_in_celsius, tol)

    def test_sigma(self):
        fromSigma = lead.LeadSigma(leadP.sigma)
        self.assertAlmostEqual(T, fromSigma.T_in_celsius, tol)

    def test_rho(self):
        fromRho = lead.LeadRho(leadP.rho)
        self.assertAlmostEqual(T, fromRho.T_in_celsius, tol)

    def test_alpha(self):
        fromAlpha = lead.LeadAlpha(leadP.alpha)
        self.assertAlmostEqual(T, fromAlpha.T_in_celsius, tol)

    def test_u_s(self):
        fromU_s = lead.LeadU_s(leadP.u_s)
        self.assertAlmostEqual(T, fromU_s.T_in_celsius, tol)

    def test_beta_s(self):
        fromBeta_s = lead.LeadBeta_s(leadP.beta_s)
        self.assertAlmostEqual(T, fromBeta_s.T_in_celsius, tol)

    def test_cp(self):
        fromCp = lead.LeadCp(leadP.cp)
        self.assertAlmostEqual(T, fromCp.T_in_celsius, tol)

    def test_delta_h(self):
        fromDelta_h = lead.LeadDelta_h(leadP.delta_h)
        self.assertAlmostEqual(T, fromDelta_h.T_in_celsius, tol)

    def test_mi(self):
        fromMi = lead.LeadMi(leadP.mi)
        self.assertAlmostEqual(T, fromMi.T_in_celsius, tol)

    def test_r(self):
        fromR = lead.LeadR(leadP.r)
        self.assertAlmostEqual(T, fromR.T_in_celsius, tol)

    def test_conductivity(self):
        fromConductivity = lead.LeadConductivity(leadP.conductivity)
        self.assertAlmostEqual(T, fromConductivity.T_in_celsius, tol)


class BismuthTester(unittest.TestCase):

    def test_p_s(self):
        fromPs = bismuth.BismuthP_s(bismuthP.p_s)
        self.assertAlmostEqual(T, fromPs.T_in_celsius, tol)

    def test_sigma(self):
        fromSigma = bismuth.BismuthSigma(bismuthP.sigma)
        self.assertAlmostEqual(T, fromSigma.T_in_celsius, tol)

    def test_rho(self):
        fromRho = bismuth.BismuthRho(bismuthP.rho)
        self.assertAlmostEqual(T, fromRho.T_in_celsius, tol)

    def test_alpha(self):
        fromAlpha = bismuth.BismuthAlpha(bismuthP.alpha)
        self.assertAlmostEqual(T, fromAlpha.T_in_celsius, tol)

    def test_u_s(self):
        fromU_s = bismuth.BismuthU_s(bismuthP.u_s)
        self.assertAlmostEqual(T, fromU_s.T_in_celsius, tol)

    def test_beta_s(self):
        fromBeta_s = bismuth.BismuthBeta_s(bismuthP.beta_s)
        self.assertAlmostEqual(T, fromBeta_s.T_in_celsius, tol)

    def test_cp(self):
        fromCp = bismuth.BismuthCp(bismuthP.cp)
        self.assertAlmostEqual(T, fromCp.T_in_celsius, tol)

    def test_delta_h(self):
        fromDelta_h = bismuth.BismuthDelta_h(bismuthP.delta_h)
        self.assertAlmostEqual(T, fromDelta_h.T_in_celsius, tol)

    def test_mi(self):
        fromMi = bismuth.BismuthMi(bismuthP.mi)
        self.assertAlmostEqual(T, fromMi.T_in_celsius, tol)

    def test_r(self):
        fromR = bismuth.BismuthR(bismuthP.r)
        self.assertAlmostEqual(T, fromR.T_in_celsius, tol)

    def test_conductivity(self):
        fromConductivity = bismuth.BismuthConductivity(bismuthP.conductivity)
        self.assertAlmostEqual(T, fromConductivity.T_in_celsius, tol)


class LBETester(unittest.TestCase):

    def test_p_s(self):
        fromPs = lbe.LBEP_s(lbeP.p_s)
        self.assertAlmostEqual(T, fromPs.T_in_celsius, tol)

    def test_sigma(self):
        fromSigma = lbe.LBESigma(lbeP.sigma)
        self.assertAlmostEqual(T, fromSigma.T_in_celsius, tol)

    def test_rho(self):
        fromRho = lbe.LBERho(lbeP.rho)
        self.assertAlmostEqual(T, fromRho.T_in_celsius, tol)

    def test_alpha(self):
        fromAlpha = lbe.LBEAlpha(lbeP.alpha)
        self.assertAlmostEqual(T, fromAlpha.T_in_celsius, tol)

    def test_u_s(self):
        fromU_s = lbe.LBEU_s(lbeP.u_s)
        self.assertAlmostEqual(T, fromU_s.T_in_celsius, tol)

    def test_beta_s(self):
        fromBeta_s = lbe.LBEBeta_s(lbeP.beta_s)
        self.assertAlmostEqual(T, fromBeta_s.T_in_celsius, tol)

    def test_cp(self):
        fromCp = lbe.LBECp(lbeP.cp)
        self.assertAlmostEqual(T, fromCp.T_in_celsius, tol)

    def test_delta_h(self):
        fromDelta_h = lbe.LBEDelta_h(lbeP.delta_h)
        self.assertAlmostEqual(T, fromDelta_h.T_in_celsius, tol)

    def test_mi(self):
        fromMi = lbe.LBEMi(lbeP.mi)
        self.assertAlmostEqual(T, fromMi.T_in_celsius, tol)

    def test_r(self):
        fromR = lbe.LBER(lbeP.r)
        self.assertAlmostEqual(T, fromR.T_in_celsius, tol)

    def test_conductivity(self):
        fromConductivity = lbe.LBEConductivity(lbeP.conductivity)
        self.assertAlmostEqual(T, fromConductivity.T_in_celsius, tol)


if __name__ == "__main__":
    unittest.main()
