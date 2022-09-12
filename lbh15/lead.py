import sys
import inspect
from ._lbh15 import LEAD_MELTING_TEMPERATURE
from ._lbh15 import LEAD_MELTING_LATENT_HEAT, LEAD_BOILING_TEMPERATURE
from ._lbh15 import SOBOLEV_KEYWORD, GURVICH_KEYWORD
from ._lbh15 import LEAD_VAPORISATION_HEAT, LEAD_KEYWORD
from ._lbh15 import LEAD_T_AT_CP_MIN_SOBOLEV, LEAD_T_AT_CP_MIN_GURVICH
from ._lbh15 import LEAD_CP_MIN_SOBOLEV, LEAD_CP_MIN_GURVICH
from ._lbh15 import LiquidMetalInterface
from .properties.lead_properties import PropertyInterface


class Lead(LiquidMetalInterface):
    """
    Class to model liquid lead properties at a given temperature

    Parameters
    ----------
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
    _correlations_to_use = {'cp': SOBOLEV_KEYWORD}
    _roots_to_use = {'cp': 0}

    def __init__(self, **kwargs):
        self._guess = LEAD_MELTING_TEMPERATURE*1.7
        super().__init__(**kwargs)

    def __new__(cls, **kwargs):
        cls._liquid_metal_name = 'lead'
        obj = super().__new__(cls)

        return obj

    @staticmethod
    def T_at_cp_min(cp_correlation_to_use=SOBOLEV_KEYWORD):
        """
        Temperature in [K] corresponding to specific heat minimum

        Parameters
        ----------
        cp_correlation_to_use : str
            Name of cp correlation, can be 'sobolev2011' or 'gurvich1991'

        Returns
        -------
        float
        """
        if cp_correlation_to_use == SOBOLEV_KEYWORD:
            rvalue = LEAD_T_AT_CP_MIN_SOBOLEV
        elif cp_correlation_to_use == GURVICH_KEYWORD:
            rvalue = LEAD_T_AT_CP_MIN_GURVICH
        else:
            raise ValueError("cp correlation can be one between: {:s}, "
                             "{:s}. {:s} was provided"
                             .format(SOBOLEV_KEYWORD, GURVICH_KEYWORD,
                                     cp_correlation_to_use))

        return rvalue

    @staticmethod
    def cp_min(cp_correlation_to_use=SOBOLEV_KEYWORD):
        """
        Minimum value of cp correlation in [J/(kg*K)]

        Parameters
        ----------
        cp_correlation_to_use : str
            Name of cp correlation, can be 'sobolev2011' or 'gurvich1991'

        Returns
        -------
        float
        """
        if cp_correlation_to_use == SOBOLEV_KEYWORD:
            rvalue = LEAD_CP_MIN_SOBOLEV
        elif cp_correlation_to_use == GURVICH_KEYWORD:
            rvalue = LEAD_CP_MIN_GURVICH
        else:
            raise ValueError("cp correlation can be one between: {:s}, "
                             "{:s}. {:s} was provided"
                             .format(SOBOLEV_KEYWORD, GURVICH_KEYWORD,
                                     cp_correlation_to_use))

        return rvalue

    @classmethod
    def _load_properties(cls):
        """
        Loads property objects corresponding to lead liquid metal

        Returns
        -------
        list
            list of property objects, i.e. of classes which inherit from
            :class:`_properties.PropertyInterface`
        """
        propertyObjectList = []
        module = 'lbh15.properties.lead_properties'
        for name, obj in inspect.getmembers(sys.modules[module]):
            if inspect.isclass(obj) and obj is not PropertyInterface:
                if issubclass(obj, PropertyInterface):
                    propertyObjectList.append(obj())
        return propertyObjectList

    def _set_constants(self):
        """
        Sets the class constants
        """
        self._T_m0 = LEAD_MELTING_TEMPERATURE
        self._Q_m0 = LEAD_MELTING_LATENT_HEAT
        self._T_b0 = LEAD_BOILING_TEMPERATURE
        self._Q_b0 = LEAD_VAPORISATION_HEAT
