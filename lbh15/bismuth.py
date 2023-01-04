"""Module with the definition of bismuth liquid metal object class,
i.e., Bismuth"""
from ._constants import BISMUTH_MELTING_TEMPERATURE
from ._constants import BISMUTH_MELTING_LATENT_HEAT
from ._constants import BISMUTH_BOILING_TEMPERATURE
from ._constants import BISMUTH_VAPORISATION_HEAT, P_ATM
from ._lbh15 import LiquidMetalInterface


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
    _default_corr_to_use = {}
    _correlations_to_use = {}
    _roots_to_use = {'cp': 0}
    _properties_module = 'lbh15.properties.bismuth_properties'

    def __init__(self, p=P_ATM, **kwargs):
        self._guess = BISMUTH_MELTING_TEMPERATURE*1.5
        super().__init__(p=p, **kwargs)

    def _set_constants(self):
        """
        Sets the class constants
        """
        self._T_m0 = BISMUTH_MELTING_TEMPERATURE
        self._Q_m0 = BISMUTH_MELTING_LATENT_HEAT
        self._T_b0 = BISMUTH_BOILING_TEMPERATURE
        self._Q_b0 = BISMUTH_VAPORISATION_HEAT
