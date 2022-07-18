import unittest
import lbeh15.lead as lead

T = 395
tol = 10
prop = lead.Lead(T, 'degC')


class PropertiesTester(unittest.TestCase):

    def test_p_s(self):
        fromPs = lead.LeadP_s(prop.p_s)
        self.assertAlmostEqual(T, fromPs.T_in_celsius, tol)

    def test_sigma(self):
        fromSigma = lead.LeadSigma(prop.sigma)
        self.assertAlmostEqual(T, fromSigma.T_in_celsius, tol)

    def test_rho(self):
        fromRho = lead.LeadRho(prop.rho)
        self.assertAlmostEqual(T, fromRho.T_in_celsius, tol)

    def test_alpha(self):
        fromAlpha = lead.LeadAlpha(prop.alpha)
        self.assertAlmostEqual(T, fromAlpha.T_in_celsius, tol)

    def test_u_s(self):
        fromU_s = lead.LeadU_s(prop.u_s)
        self.assertAlmostEqual(T, fromU_s.T_in_celsius, tol)

    def test_beta_s(self):
        fromBeta_s = lead.LeadBeta_s(prop.beta_s)
        self.assertAlmostEqual(T, fromBeta_s.T_in_celsius, tol)

    def test_cp(self):
        fromCp = lead.LeadCp(prop.cp)
        self.assertAlmostEqual(T, fromCp.T_in_celsius, tol)

    def test_delta_h(self):
        fromDelta_h = lead.LeadDelta_h(prop.delta_h)
        self.assertAlmostEqual(T, fromDelta_h.T_in_celsius, tol)

    def test_mi(self):
        fromMi = lead.LeadMi(prop.mi)
        self.assertAlmostEqual(T, fromMi.T_in_celsius, tol)

    def test_r(self):
        fromR = lead.LeadR(prop.r)
        self.assertAlmostEqual(T, fromR.T_in_celsius, tol)

    def test_conductivity(self):
        fromConductivity = lead.LeadConductivity(prop.conductivity)
        self.assertAlmostEqual(T, fromConductivity.T_in_celsius, tol)


if __name__ == "__main__":
    unittest.main()
