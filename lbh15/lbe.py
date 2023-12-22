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
from .properties.interface import PropertyInterface


class LBE(LiquidMetalInterface):
    """
    Class to model liquid lbe properties either at a given temperature or
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
        - **pb_a** (float) : Lead chemical activity :math:`[-]`
        - **bi_a** (float) : Bismuth chemical activity :math:`[-]`
        - **fe_sol** (float) : Iron solubility :math:`[wt.\\%]`
        - **ni_sol** (float) : Nickel solubility :math:`[wt.\\%]`
        - **cr_sol** (float) : Chromium solubility :math:`[wt.\\%]`
        - **o_sol** (float) : Oxygen solubility :math:`[wt.\\%]`
        - **o_dif** (float) : Oxygen diffusivity :math:`[cm^2 / s]`
        - **fe_dif** (float) : Iron diffusivity :math:`[cm^2 / s]`
        - **o_pp** (float) : Oxygen partial pressure divided by Oxygen \
            concentration squared :math:`[atm / wt.\\%^2]`
        - **lim_fe_sat** (float) : Lower limit of Oxygen concentration with \
            Iron at saturation :math:`[wt.\\%]`
        - **lim_cr_sat** (float) : Lower limit of Oxygen concentration with \
            Chromium at saturation :math:`[wt.\\%]`
        - **lim_ni_sat** (float) : Lower limit of Oxygen concentration with \
            Nickel at saturation :math:`[wt.\\%]`
        - **lim_si_sat** (float) : Lower limit of Oxygen concentration with \
            Silicon at saturation :math:`[wt.\\%]`
        - **lim_al_sat** (float) : Lower limit of Oxygen concentration with \
            Aluminium at saturation :math:`[wt.\\%]`
        - **lim_cr** (float) : Lower limit of Oxygen concentration times \
            Chromium concentration raised to :math:`2/3` :math:`[wt.\\%]`
        - **lim_ni** (float) : Lower limit of Oxygen concentration times \
            Nickel concentration :math:`[wt.\\%]`
        - **lim_fe** (float) : Lower limit of Oxygen concentration times \
            Iron concentration raised to :math:`3/4` :math:`[wt.\\%]`

    Example
    -------
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
    _available_properties_dict: Dict[str, PropertyInterface] = {}
    _available_correlations_dict: Dict[str, List[str]] = {}
    _properties_modules_list: List[str] = \
        ['lbh15.properties.lbe_thermochemical_properties.solubility_in_lbe',
         'lbh15.properties.lbe_thermochemical_properties.diffusivity_in_lbe',
         'lbh15.properties.lbe_thermochemical_properties.lbe_thermochemical',
         'lbh15.properties.lbe_thermochemical_properties.lbe_oxygen_limits',
         'lbh15.properties.lbe_properties']

    def __init__(self, p: float = atm, **kwargs):
        self._guess = LBE_BOILING_TEMPERATURE / 2.0
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
