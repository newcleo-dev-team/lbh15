import pyll.properties as pprop

prop = pprop.LeadProperties(391, "°C")
print(prop.sigma)
print(prop.rho)
print(prop.alpha)
print(prop.u_s)

sigma = prop.sigma
fromSigma = pprop.LeadPropertiesSigma(sigma)
print(fromSigma.T - 273.15)

rho = prop.rho
fromRho = pprop.LeadPropertiesRho(rho)
print(fromRho.T-273.15)


alpha = prop.alpha
fromAlpha = pprop.LeadPropertiesAlpha(alpha)
print(fromAlpha.T - 273.15)

u_s = prop.u_s
fromUs = pprop.LeadPropertiesU_s(u_s)
print(fromUs.T - 273.15)