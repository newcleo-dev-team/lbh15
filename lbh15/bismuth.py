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
from ._decorators import typecheck_for_method
from .properties.interface import PropertyInterface


class Bismuth(LiquidMetalInterface):
    """
    Class to model liquid bismuth properties at a given temperature

    Parameters
    ----------
    p : float, optional
        Pressure in [Pa], by default atmospheric pressure, i.e.,
        101325.0 Pa
    \\**kwargs : dict
        Dictionary that specifies the quantity from which the object shall
        be initialized. The available default ones are:

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

    @typecheck_for_method
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
