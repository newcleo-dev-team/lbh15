import sys
import inspect
from ._lbh15 import BISMUTH_MELTING_TEMPERATURE
from ._lbh15 import BISMUTH_MELTING_LATENT_HEAT, BISMUTH_BOILING_TEMPERATURE
from ._lbh15 import BISMUTH_VAPORISATION_HEAT, BISMUTH_KEYWORD
from ._lbh15 import BISMUTH_T_AT_CP_MIN, BISMUTH_CP_MIN
from ._lbh15 import LiquidMetalInterface
from .properties.bismuth_properties import PropertyInterface


class Bismuth(LiquidMetalInterface):
    """
    Class to model liquid bismuth properties at a given temperature

    Parameters
    ----------
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
    _correlations_to_use = {}
    _roots_to_use = {'cp': 0}

    def __init__(self, **kwargs):
        self._guess = BISMUTH_MELTING_TEMPERATURE*1.5
        super().__init__(**kwargs)

    def __new__(cls, **kwargs):
        cls._liquid_metal_name = 'bismuth'
        obj = super().__new__(cls)

        return obj

    @staticmethod
    def T_at_cp_min():
        """
        Temperature in [K] corresponding to specific heat minimum

        Returns
        -------
        float
        """
        return BISMUTH_T_AT_CP_MIN

    @staticmethod
    def cp_min():
        """
        Minimum value of cp correlation in [J/(kg*K)]

        Returns
        -------
        float
        """
        return BISMUTH_CP_MIN

    @classmethod
    def _load_properties(cls):
        """
        Loads property objects corresponding to bismuth liquid metal

        Returns
        -------
        list
            list of property objects, i.e. of classes which inherit from
            :class:`_properties.PropertyInterface`
        """
        propertyObjectList = []
        module = 'lbh15.properties.bismuth_properties'
        for name, obj in inspect.getmembers(sys.modules[module]):
            if inspect.isclass(obj) and obj is not PropertyInterface:
                if issubclass(obj, PropertyInterface):
                    propertyObjectList.append(obj())
        return propertyObjectList

    def _set_constants(self):
        """
        Sets the class constants
        """
        self._T_m0 = BISMUTH_MELTING_TEMPERATURE
        self._Q_m0 = BISMUTH_MELTING_LATENT_HEAT
        self._T_b0 = BISMUTH_BOILING_TEMPERATURE
        self._Q_b0 = BISMUTH_VAPORISATION_HEAT
