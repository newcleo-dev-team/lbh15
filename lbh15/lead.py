"""Module with the definition of lead liquid metal object class,
i.e., Lead"""
import copy
from typing import Dict
from typing import List
from scipy.constants import atm
from ._commons import LEAD_MELTING_TEMPERATURE
from ._commons import LEAD_MELTING_LATENT_HEAT
from ._commons import LEAD_BOILING_TEMPERATURE
from ._commons import SOBOLEV_KEYWORD
from ._commons import LEAD_VAPORISATION_HEAT
from ._commons import LEAD_MOLAR_MASS
from ._lbh15 import LiquidMetalInterface
from ._decorators import typecheck_for_method


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
    _default_corr_to_use: Dict[str, str] = \
        {'cp': SOBOLEV_KEYWORD, 'cr_sol': "gosse2014",
         'o_pp': "alcock1964", 'o_dif': "gromov1996",
         'lim_cr': "gosse2014"}
    _correlations_to_use: Dict[str, str] = copy.deepcopy(_default_corr_to_use)
    _roots_to_use: Dict[str, int] = {'cp': 0}
    _properties_modules_dict: Dict[str, List[str]] = \
        {'Lead': ['lbh15.properties.lead_thermochemical_properties.solubility_in_lead',
                  'lbh15.properties.lead_thermochemical_properties.diffusivity_in_lead',
                  'lbh15.properties.lead_thermochemical_properties.lead_thermochemical',
                  'lbh15.properties.lead_thermochemical_properties.lead_oxygen_limits',
                  'lbh15.properties.lead_properties']}

    @typecheck_for_method
    def __init__(self, p: float = atm, **kwargs):
        self._guess = LEAD_MELTING_TEMPERATURE * 1.7
        super().__init__(p=p, **kwargs)

    def _set_constants(self) -> None:
        """
        Sets the class constants
        """
        self._T_m0 = LEAD_MELTING_TEMPERATURE
        self._Q_m0 = LEAD_MELTING_LATENT_HEAT
        self._T_b0 = LEAD_BOILING_TEMPERATURE
        self._Q_b0 = LEAD_VAPORISATION_HEAT
        self._M = LEAD_MOLAR_MASS
