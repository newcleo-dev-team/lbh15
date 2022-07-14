import pyll.pyll as pyll

prop = pyll.LeadProperties(391, "°C")
print(prop.sigma)
print(prop.rho)
print(prop.alpha)
print(prop.u_s)

sigma = prop.sigma
fromSigma = pyll.LeadPropertiesSigma(sigma)
print(fromSigma.T - 273.15)

rho = prop.rho
fromRho = pyll.LeadPropertiesRho(rho)
print(fromRho.T-273.15)


alpha = prop.alpha
fromAlpha = pyll.LeadPropertiesAlpha(alpha)
print(fromAlpha.T - 273.15)

u_s = prop.u_s
fromUs = pyll.LeadPropertiesU_s(u_s)
print(fromUs.T - 273.15)