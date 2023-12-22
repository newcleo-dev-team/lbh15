"""Module with the definition of bismuth liquid metal object class,
i.e., Bismuth"""
import copy
from typing import Dict
from typing import List
from scipy.constants import atm
from ._commons import BISMUTH_MELTING_TEMPERATURE
from ._commons import BISMUTH_MELTING_LATENT_HEAT
from ._commons import BISMUTH_BOILING_TEMPERATURE
from ._commons import BISMUTH_VAPORISATION_HEAT
from ._commons import BISMUTH_MOLAR_MASS
from ._lbh15 import LiquidMetalInterface
from .properties.interface import PropertyInterface


class Bismuth(LiquidMetalInterface):
    """
    Class to model liquid bismuth properties either at a given temperature or
    at a given value of a specific property to choose among a list of
    available properties.

    Parameters
    ----------
    p : float, optional
        Pressure in [Pa], by default the atmospheric pressure value, i.e.,
        101325.0 Pa
    \\**kwargs : dict
        One-item dictionary that specifies the quantity which the object shall
        be initialized from. The available ones by default are:

        - **T** (float) : temperature :math:`[K]`
        - **p_s** (float) : saturation vapour pressure :math:`[Pa]`
        - **sigma** (float) : surface tension :math:`[N/m]`
        - **rho** (float) : density :math:`[kg/m^3]`
        - **alpha** (float) : thermal expansion coefficient :math:`[1/K]`
        - **u_s** (float) : speed of sound :math:`[m/s]`
        - **beta_s** (float) : isentropic compressibility :math:`[1/Pa]`
        - **cp** (float) : specific heat capacity :math:`[J/(kg \\cdot K)]`
        - **h** (float) : specific enthalpy \
            (with respect to melting point) :math:`[J/kg]`
        - **mu** (float) : dynamic viscosity :math:`[Pa \\cdot s]`
        - **r** (float) : electrical resistivity :math:`[Ohm \\cdot m]`
        - **k** (float) : thermal conductivity :math:`[W/(m \\cdot K)]`
        - **H** (float) : molar enthalpy :math:`[J/mol]`
        - **S** (float) : molar entropy :math:`[J/(mol \\cdot K)]`
        - **G** (float) : Gibbs free energy :math:`[J/mol]`
        - **fe_sol** (float) : Iron solubility :math:`[wt.\\%]`
        - **ni_sol** (float) : Nickel solubility :math:`[wt.\\%]`
        - **cr_sol** (float) : Chromium solubility :math:`[wt.\\%]`
        - **o_sol** (float) : Oxygen solubility :math:`[wt.\\%]`
        - **o_dif** (float) : Oxygen diffusivity :math:`[cm^2 / s]`
        - **o_pp** (float) : Oxygen partial pressure divided by Oxygen \
            concentration squared :math:`[atm / wt.\\%^2]`

    Example
    -------
    >>> liquid_bismuth = Bismuth(T=670.0)
    >>> liquid_bismuth.k  # [W/(m*K)]
    13.705
    """
    _default_corr_to_use: Dict[str, str] = \
        {'fe_sol': "gosse2014", 'ni_sol': "gosse2014",
         'cr_sol': "gosse2014", 'o_dif': "fitzner1980",
         'o_pp': "isecke1979"}
    _correlations_to_use: Dict[str, str] = copy.deepcopy(_default_corr_to_use)
    _roots_to_use: Dict[str, int] = {'cp': 0}
    _custom_properties_path: Dict[str, List[str]] = {}
    _available_properties_dict: Dict[str, PropertyInterface] = {}
    _available_correlations_dict: Dict[str, List[str]] = {}
    _properties_modules_list: List[str] = \
        ['lbh15.properties.bismuth_thermochemical_properties\
.solubility_in_bismuth',
         'lbh15.properties.bismuth_thermochemical_properties\
.diffusivity_in_bismuth',
         'lbh15.properties.bismuth_thermochemical_properties\
.bismuth_thermochemical',
         'lbh15.properties.bismuth_properties']

    def __init__(self, p: float = atm, **kwargs):
        self._guess = BISMUTH_BOILING_TEMPERATURE / 2.0
        super().__init__(p=p, **kwargs)

    def _set_constants(self) -> None:
        """
        Sets the class constants
        """
        self._T_m0 = BISMUTH_MELTING_TEMPERATURE
        self._Q_m0 = BISMUTH_MELTING_LATENT_HEAT
        self._T_b0 = BISMUTH_BOILING_TEMPERATURE
        self._Q_b0 = BISMUTH_VAPORISATION_HEAT
        self._M = BISMUTH_MOLAR_MASS
