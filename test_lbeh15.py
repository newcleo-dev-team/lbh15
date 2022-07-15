import unittest
import lbeh15.lead as lead

T = 395
tol = 10
prop = lead.Lead(T, 'degC')
print(prop.T)


class PropertiesTester(unittest.TestCase):

    def test_p_s(self):
        fromPs = lead.LeadPropertiesP_s(prop.p_s)
        self.assertAlmostEqual(T, fromPs.T_in_celsius, tol)

   #def test_sigma(self):
   #    fromSigma = lead.LeadPropertiesSigma(prop.sigma)
   #    self.assertAlmostEqual(T, fromSigma.T_in_celsius, tol)

   #def test_rho(self):
   #    fromRho = lead.LeadPropertiesRho(prop.rho)
   #    self.assertAlmostEqual(T, fromRho.T_in_celsius, tol)

   #def test_alpha(self):
   #    fromAlpha = lead.LeadPropertiesAlpha(prop.alpha)
   #    self.assertAlmostEqual(T, fromAlpha.T_in_celsius, tol)

   #def test_u_s(self):
   #    fromU_s = lead.LeadPropertiesU_s(prop.u_s)
   #    self.assertAlmostEqual(T, fromU_s.T_in_celsius, tol)

   #def test_beta_s(self):
   #    fromBeta_s = lead.LeadPropertiesBeta_s(prop.beta_s)
   #    self.assertAlmostEqual(T, fromBeta_s.T_in_celsius, tol)

   #def test_cp(self):
   #    fromCp = lead.LeadPropertiesCp(prop.cp)
   #    self.assertAlmostEqual(T, fromCp.T_in_celsius, tol)

   #def test_delta_h(self):
   #    fromDelta_h = lead.LeadPropertiesDelta_h(prop.delta_h)
   #    self.assertAlmostEqual(T, fromDelta_h.T_in_celsius, tol)

   #def test_mi(self):
   #    fromMi = lead.LeadPropertiesMi(prop.mi)
   #    self.assertAlmostEqual(T, fromMi.T_in_celsius, tol)


if __name__ == "__main__":
    unittest.main()
