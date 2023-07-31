"""Module with the definition of common objects for lbh15 package"""
# KEYWORDS
GURVICH_KEYWORD = 'gurvich1991'
SOBOLEV_KEYWORD = 'sobolev2011'

# LEAD CONSTANTS
LEAD_MELTING_TEMPERATURE = 600.6  # [K]
LEAD_MELTING_LATENT_HEAT = 23.07e3  # [J/kg]
LEAD_BOILING_TEMPERATURE = 2021  # [K]
LEAD_VAPORISATION_HEAT = 858.6e3  # [J/kg]
LEAD_MOLAR_MASS = 207.20  # [g/mol]

# BISMUTH CONSTANTS
BISMUTH_MELTING_TEMPERATURE = 544.6  # [K]
BISMUTH_MELTING_LATENT_HEAT = 53.3e3  # [J/kg]
BISMUTH_BOILING_TEMPERATURE = 1831  # [K]
BISMUTH_VAPORISATION_HEAT = 856.2e3  # [J/kg]
BISMUTH_MOLAR_MASS = 208.98  # [g/mol]

# LEAD-BISMUTH-EUTECTIC CONSTANTS
LBE_MELTING_TEMPERATURE = 398.0  # [K]
LBE_MELTING_LATENT_HEAT = 38.6e3  # [J/kg]
LBE_BOILING_TEMPERATURE = 1927  # [K]
LBE_VAPORISATION_HEAT = 856.6e3  # [J/kg]
LBE_MOLAR_MASS = 0.55*BISMUTH_MOLAR_MASS + 0.45*LEAD_MOLAR_MASS  # [g/mol]

# OXYGEN CONSTANT
OXYGEN_MOLAR_MASS = 16  # [g/mol]