"""Module with the definition of lead liquid metal object class,
i.e., Lead"""
import copy
from ._constants import LEAD_MELTING_TEMPERATURE
from ._constants import LEAD_MELTING_LATENT_HEAT, LEAD_BOILING_TEMPERATURE
from ._constants import SOBOLEV_KEYWORD, LEAD_VAPORISATION_HEAT, P_ATM
from ._lbh15 import LiquidMetalInterface


class Lead(LiquidMetalInterface):
    """
    Class to model liquid lead properties at a given temperature

    Parameters
    ----------
    p : float, optional
        Pressure in [Pa], by default atmospheric pressure, i.e.,
        101325.0 Pa
    \\**kwargs : dict
        Dictionary that specifies the quantity from which the object shall
        be initialized. The default available ones are:

        - **T** (float) : temperature [K]
        - **p_s** (float) : saturation vapour pressure [Pa]
        - **sigma** (float) : surface tension [N/m]
        - **rho** (float) : density [Kg/m^3]
        - **alpha** (float) : thermal expansion coefficient [1/K]
        - **u_s** (float) : speed of sound [m/s]
        - **beta_s** (float) : isentropic compressibility [1/Pa]
        - **cp** (float) : specific heat capacity [J/(kg*K)]
        - **h** (float) : specific enthalpy \
        (in respect to melting point) [J/kg]
        - **mu** (float) : dynamic viscosity [Pa*s]
        - **r** (float) : electrical resistivity [Ohm*m]
        - **k** (float) : thermal conductivity [W/(m*K)]

    Examples
    --------
    Compare :class:`.lead.Lead` specific heat values at T=800 K
    with with using 'sobolev2011' and 'gurvich1991':

    >>> liquid_lead_1 = Lead(T=800)  # 'sobolev2011'
    >>> liquid_lead_1.cp
    144.31634999999997
    >>> Lead.set_correlation_to_use('cp', 'gurvich1991')
    >>> liquid_lead_2 = Lead(T=800)
    >>> liquid_lead_2.cp
    144.66006199999998
    """
    _default_corr_to_use = {'cp': SOBOLEV_KEYWORD}
    _correlations_to_use = copy.deepcopy(_default_corr_to_use)
    _roots_to_use = {'cp': 0}
    _properties_module = 'lbh15.properties.lead_properties'

    def __init__(self, p=P_ATM, **kwargs):
        self._guess = LEAD_MELTING_TEMPERATURE*1.7
        super().__init__(p=p, **kwargs)

    def _set_constants(self):
        """
        Sets the class constants
        """
        self._T_m0 = LEAD_MELTING_TEMPERATURE
        self._Q_m0 = LEAD_MELTING_LATENT_HEAT
        self._T_b0 = LEAD_BOILING_TEMPERATURE
        self._Q_b0 = LEAD_VAPORISATION_HEAT
