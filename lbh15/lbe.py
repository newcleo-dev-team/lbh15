"""Module with the definition of lead-bismuth eutectic
liquid metal object class, i.e., LBE"""
import copy
from typing import Dict
from typing import List
from scipy.constants import atm
from ._commons import LBE_MELTING_TEMPERATURE
from ._commons import LBE_MELTING_LATENT_HEAT
from ._commons import LBE_BOILING_TEMPERATURE
from ._commons import LBE_VAPORISATION_HEAT
from ._commons import LBE_MOLAR_MASS
from ._lbh15 import LiquidMetalInterface
from ._decorators import typecheck_for_method


class LBE(LiquidMetalInterface):
    """
    Class to model liquid lead-bismuth eutectic properties
    at a given temperature

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
    >>> liquid_lbe = LBE(T=600.0)
    >>> liquid_lbe.mu  # [Pa*s]
    0.001736052003181349
    """
    _default_corr_to_use: Dict[str, str] = \
        {'fe_sol': "gosse2014", 'ni_sol': "gosse2014",
         'cr_sol': 'gosse2014', 'o_dif': "gromov1996",
         'lim_cr': "gosse2014", 'lim_ni': "gosse2014",
         'lim_fe': "gosse2014"}
    _correlations_to_use: Dict[str, str] = copy.deepcopy(_default_corr_to_use)
    _roots_to_use: Dict[str, int] = {'cp': 0}
    _custom_properties_path: Dict[str, List[str]] = {}
    _properties_modules_list: List[str] = \
        ['lbh15.properties.lbe_thermochemical_properties.solubility_in_lbe',
         'lbh15.properties.lbe_thermochemical_properties.diffusivity_in_lbe',
         'lbh15.properties.lbe_thermochemical_properties.lbe_thermochemical',
         'lbh15.properties.lbe_thermochemical_properties.lbe_oxygen_limits',
         'lbh15.properties.lbe_properties']

    @typecheck_for_method
    def __init__(self, p: float = atm, **kwargs):
        self._guess = LBE_MELTING_TEMPERATURE * 2.0
        super().__init__(p=p, **kwargs)

    def _set_constants(self) -> None:
        """
        Sets the class constants
        """
        self._T_m0 = LBE_MELTING_TEMPERATURE
        self._Q_m0 = LBE_MELTING_LATENT_HEAT
        self._T_b0 = LBE_BOILING_TEMPERATURE
        self._Q_b0 = LBE_VAPORISATION_HEAT
        self._M = LBE_MOLAR_MASS
