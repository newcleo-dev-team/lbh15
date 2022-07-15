import unittest
import pyll.properties as leadP

T = 395
tol = 10
prop = leadP.LeadProperties(T, '°C')


class PropertiesTester(unittest.TestCase):

    def test_p_s(self):
        fromPs = leadP.LeadPropertiesP_s(prop.p_s)
        self.assertAlmostEqual(T, fromPs.T_in_celsius, tol)

    def test_sigma(self):
        fromSigma = leadP.LeadPropertiesSigma(prop.sigma)
        self.assertAlmostEqual(T, fromSigma.T_in_celsius, tol)

    def test_rho(self):
        fromRho = leadP.LeadPropertiesRho(prop.rho)
        self.assertAlmostEqual(T, fromRho.T_in_celsius, tol)

    def test_alpha(self):
        fromAlpha = leadP.LeadPropertiesAlpha(prop.alpha)
        self.assertAlmostEqual(T, fromAlpha.T_in_celsius, tol)

    def test_u_s(self):
        fromU_s = leadP.LeadPropertiesU_s(prop.u_s)
        self.assertAlmostEqual(T, fromU_s.T_in_celsius, tol)

    def test_beta_s(self):
        fromBeta_s = leadP.LeadPropertiesBeta_s(prop.beta_s)
        self.assertAlmostEqual(T, fromBeta_s.T_in_celsius, tol)

    def test_cp(self):
        fromCp = leadP.LeadPropertiesCp(prop.cp)
        self.assertAlmostEqual(T, fromCp.T_in_celsius, tol)

    def test_delta_h(self):
        fromDelta_h = leadP.LeadPropertiesDelta_h(prop.delta_h)
        self.assertAlmostEqual(T, fromDelta_h.T_in_celsius, tol)

    def test_mi(self):
        fromMi = leadP.LeadPropertiesMi(prop.mi)
        self.assertAlmostEqual(T, fromMi.T_in_celsius, tol)


if __name__ == "__main__":
    unittest.main()
