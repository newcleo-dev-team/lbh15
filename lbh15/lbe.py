"""
Module with liquid lead-bismuth-eutectic (LBE) class.
LBE object can be initialized with the temperature
or with one of the available properties (see :class:`.LBE` for \
the full list). It must be underlined that instantiation from properties
depends on the specific correlation of the properties implemented in
lbh15 package. In addition to the class attributes that are shown
in this section, :class:`.LBE` class dynamically adds the properties
implemented in :py:mod:`lbh15.properties.lbe_properties` module.

Therefore the object has the following themophysical properties:

    - :math:`T_{m0}` lbe melting temperature:

        :math:`398.0 [K]`
    - :math:`Q_{m0}` lbe melting latent heat:

        :math:`38.6\\cdot10^3 \\Big[\\frac{J}{kg}\\Big]`
    - :math:`T_{b0}` lbe boiling temperature:

        :math:`1927 [K]`
    - :math:`Q_{b0}` lbe vaporisation heat:

        :math:`856.6\\cdot10^3 \\Big[\\frac{J}{kg}\\Big]`
    - :math:`p_s` lbe saturation vapour pressure :math:`[Pa]`:

        :math:`p_s(T) = \\displaystyle1.22\\cdot10^{10}\\cdot\
        \\exp{\\Big(-22852/T\\Big)}`
    - :math:`\\sigma` lbe surface tension \
      :math:`\\Big[\\frac{N}{m}\\Big]`:

        :math:`\\sigma(T) = \\displaystyle\\Big(448.5 \
        - 0.0799{\\cdot}T\\Big)\\cdot10^{-3}`
    - :math:`\\rho` lbe density \
      :math:`\\Big[\\frac{kg}{m^3}\\Big]`:

        :math:`\\rho(T) = \\displaystyle11065 - 1.293{\\cdot}T`
    - :math:`\\alpha` lbe thermal expansion coefficient \
      :math:`\\Big[\\frac{1}{K}\\Big]`:

        :math:`\\alpha(T) = \\displaystyle\\Big(8558 - T\\Big)^{-1}`
    - :math:`u_s` speed of sound in lbe \
      :math:`\\Big[\\frac{m}{s}\\Big]`:

        :math:`u_s(T) = \\displaystyle1855 - 0.212{\\cdot}T`
    - :math:`\\beta_s` lbe isentropic compressibility \
      :math:`\\Big[\\frac{1}{Pa}\\Big]`:

        :math:`\\beta_s(T) = \\displaystyle\\frac{1}{\\rho(T){\\cdot}u_s(T)^2}`
    - :math:`c_p` lbe specific heat capacity \
      :math:`\\Big[\\frac{J}{kg{\\cdot}K}\\Big]`:

        :math:`c_p(T) = \\displaystyle164.8 - 3.94\\cdot10^{-2}{\\cdot}T \
        + 1.25\\cdot10^{-5}{\\cdot}T^2 - 4.56\\cdot10^{5}{\\cdot}T^{-2}`
    - :math:`h` lbe specific enthalpy (as difference with \
      respect to the melting point enthalpy) \
      :math:`\\Big[\\frac{J}{kg{\\cdot}K}\\Big]`:

        :math:`h(T) = \\displaystyle\
        164.8\\cdot\\Big(T - T_{m0}\\Big) \
        - 1.97\\cdot10^{-2}\\Big(T^2 - T_{m0}^2\\Big) \
        + 4.167\\cdot10^{-6}\\Big(T^3 - T_{m0}^3\\Big)`

        :math:`\\qquad\\qquad- 4.56\\cdot10^5\\Big(T^{-1} - T_{m0}^{-1}\\Big)`
    - :math:`\\mu` lbe dynamic visocity :math:`[Pa{\\cdot}s]`:

        :math:`\\mu(T) = \\displaystyle4.94\\cdot10^{-4}\\cdot\
        \\exp{\\Big(754.1/T\\Bigg)}`
    - :math:`r` lbe electrical resistivity :math:`[\\Omega{\\cdot}m]`:

        :math:`r(T) = \\displaystyle\\Big(90.9 + 0.048{\\cdot}T\\Big)\
        \\cdot10^{-8}`
    - :math:`k` lbe thermal conductivity \
      :math:`\\Big[\\frac{W}{m{\\cdot}K}\\Big]`:

        :math:`k(T) = \\displaystyle3.284 + 1.617\\cdot10^{-2}{\\cdot}T \
        - 2.305\\cdot10^{-6}{\\cdot}T^2`
    - :math:`Pr` Prandtl number :math:`[-]`:

        :math:`Pr = \\displaystyle\\frac{c_p\\cdot\\mu}{k}`

where :math:`T` is the lbe temperature in :math:`[K]`.

Finally, the object dynamically adds useful
methods to retrieve more information on specific thermophysical property
which are named <property_name>_print_info. For instance:

>>> from lbh15 import LBE
>>> liquid_lbe = LBE(T=668.15)
>>> liquid_lbe.k_print_info()
k:
        Value: 13.0590 [W/(m*K)]
        Validity range: [398.00, 1100.00] K
        Long name: thermal conductivity
        Units: [W/(m*K)]
        Description:
                Liquid lbe thermal conductivity

It is possible to retrieve only parts of the information
specifying :code:`info='value'`, :code:`info='validity_range'`,
:code:`info='long_name`, :code:`info='units'` or  :code:`info='description'`.
For instance, print the electrical conductivity units:

>>> from lbh15 import LBE
>>> liquid_lbe = LBE(T=668.15)
>>> liquid_lbe.r_print_info(info='units')
r:
        Units: [Ohm*m]
"""
import sys
import inspect
from ._lbh15 import LBE_MELTING_TEMPERATURE
from ._lbh15 import LBE_MELTING_LATENT_HEAT, LBE_BOILING_TEMPERATURE
from ._lbh15 import LBE_VAPORISATION_HEAT, LBE_KEYWORD
from ._lbh15 import LBE_T_AT_CP_MIN, LBE_CP_MIN
from ._lbh15 import LiquidMetalInterface, p_s_initializer
from .properties.lbe_properties import PropertyInterface


class LBE(LiquidMetalInterface):
    """
    Class to model liquid lead-bismuth eutectic properties
    at a given temperature

    Parameters
    ----------
    cp_high_range : bool
        True to initialize the object with temperature larger than
        the one corresponding to cp minumum (if present), False otherwise.
        It is used if \\**kwargs contains 'cp', i.e., if initialization from
        specific heat is required
    \\**kwargs : dict
        Dictionary that specifies the quantity from which the object shall
        be initialized. The available ones are:

        - **T** (float) : temperature [K]
        - **p_s** (float) : saturation vapour pressure [Pa]
        - **sigma** (float) : surface tension [N/m]
        - **rho** (float) : density [Kg/m^3]
        - **alpha** (float) : thermal expansion coefficient [1/K]
        - **u_s** (float) : speed of sound [m/s]
        - **beta_s** (float) : isentropic compressibility [1/Pa]
        - **cp** (float) : specific heat capacity [J/(kg*K)]
        - **h** (float) : specific hentalpy \
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
    _correlations_to_use = {}

    def __init__(self, cp_high_range=False, **kwargs):
        self._guess = LBE_MELTING_TEMPERATURE*2.0
        super().__init__(cp_high_range, **kwargs)

    def __new__(cls, cp_high_range=False, **kwargs):
        cls._liquid_metal_name = 'lbe'
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
        return LBE_T_AT_CP_MIN

    @staticmethod
    def cp_min():
        """
        Minimum value of cp correlation in [J/(kg*K)]

        Returns
        -------
        float
        """
        return LBE_CP_MIN

    @classmethod
    def _load_properties(cls):
        """
        Loads property objects corresponding to lbe liquid metal

        Returns
        -------
        list
            list of property objects, i.e. of classes which inherit from
            :class:`_properties.PropertyInterface`
        """
        propertyObjectList = []
        module = 'lbh15.properties.lbe_properties'
        for name, obj in inspect.getmembers(sys.modules[module]):
            if inspect.isclass(obj) and obj is not PropertyInterface:
                if issubclass(obj, PropertyInterface):
                    propertyObjectList.append(obj())
        return propertyObjectList

    def _set_constants(self):
        """
        Sets the class constants
        """
        self._T_m0 = LBE_MELTING_TEMPERATURE
        self._Q_m0 = LBE_MELTING_LATENT_HEAT
        self._T_b0 = LBE_BOILING_TEMPERATURE
        self._Q_b0 = LBE_VAPORISATION_HEAT
