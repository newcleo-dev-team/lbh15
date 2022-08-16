"""
Module with liquid bismuth class.
Bismuth object can be initialized with the temperature
or with one of the available properties (see :class:`.Bismuth` for \
the full list). In addition to the class attributes that are shown
in this section, :class:`.Bismuth` class dynamically adds the properties
implemented in :py:mod:`lbh15.properties.bismuth_properties` module.

Therefor the object has the following themophysical properties:

    - :math:`T_{m0}` bismuth melting temperature:

        :math:`544.6 [K]`
    - :math:`Q_{m0}` bismuth melting latent heat:

        :math:`53.3\\cdot10^3 \\Big[\\frac{J}{kg}\\Big]`
    - :math:`T_{b0}` bismuth boiling temperature:

        :math:`1831 [K]`
    - :math:`Q_{b0}` bismuth vaporisation heat:

        :math:`856.2\\cdot10^3 \\Big[\\frac{J}{kg}\\Big]`
    - :math:`p_s` bismuth saturation vapour pressure :math:`[Pa]`:

        :math:`p_s(T) = \\displaystyle2.67\\cdot10^{10}\\cdot\
        \\exp{\\Big(-22858/T\\Big)}`
    - :math:`\\sigma` bismuth surface tension \
      :math:`\\Big[\\frac{N}{m}\\Big]`:

        :math:`\\sigma(T) = \\displaystyle\\Big(420.8 \
        - 0.081{\\cdot}T\\Big)\\cdot10^{-3}`
    - :math:`\\rho` bismuth density \
      :math:`\\Big[\\frac{kg}{m^3}\\Big]`:

        :math:`\\rho(T) = \\displaystyle10725 - 1.22{\\cdot}T`
    - :math:`\\alpha` bismuth thermal expansion coefficient \
      :math:`\\Big[\\frac{1}{K}\\Big]`:

        :math:`\\alpha(T) = \\displaystyle\\Big(8791 - T\\Big)^{-1}`
    - :math:`u_s` speed of sound in bismuth \
      :math:`\\Big[\\frac{m}{s}\\Big]`:

        :math:`u_s(T) = \\displaystyle1616 + 0.187{\\cdot}T \
        - 2.2\\cdot10^{-4}{\\cdot}T`
    - :math:`\\beta_s` bismuth isentropic compressibility \
      :math:`\\Big[\\frac{1}{Pa}\\Big]`:

        :math:`\\beta_s(T) = \\displaystyle\\frac{1}{\\rho(T){\\cdot}u_s(T)^2}`
    - :math:`c_p` bismuth specific heat capacity \
      :math:`\\Big[\\frac{J}{kg{\\cdot}K}\\Big]`:

        :math:`c_p(T) = \\displaystyle118.2 - 5.934\\cdot10^{-3}{\\cdot}T \
        + 7.183\\cdot10^{6}{\\cdot}T^{-2}`
    - :math:`h` bismuth specific enthalpy (as difference with \
      respect to the melting point enthalpy) \
      :math:`\\Big[\\frac{J}{kg{\\cdot}K}\\Big]`:

        :math:`h(T) = \\displaystyle\
        118.2\\cdot\\Big(T - T_{m0}\\Big) \
        + 2.967\\cdot10^{-3}\\Big(T^2 - T_{m0}^2\\Big) \
        - 7.183\\cdot10^6\\Big(T^{-1} - T_{m0}^{-1}\\Big)`
    - :math:`\\mu` bismuth dynamic visocity :math:`[Pa{\\cdot}s]`:

        :math:`\\mu(T) = \\displaystyle4.456\\cdot10^{-4}\\cdot\
        \\exp{\\Big(780/T\\Big)}`
    - :math:`r` bismuth electrical resistivity :math:`[\\Omega{\\cdot}m]`:

        :math:`r(T) = \\displaystyle\\Big(98.96 + 0.0554{\\cdot}T\\Big)\
        \\cdot10^{-8}`
    - :math:`k` bismuth thermal conductivity \
      :math:`\\Big[\\frac{W}{m{\\cdot}K}\\Big]`:

        :math:`k(T) = \\displaystyle7.34 + 9.5\\cdot10^{-3}{\\cdot}T`
    - :math:`Pr` Prandtl number :math:`[-]`:

        :math:`Pr = \\displaystyle\\frac{c_p\\cdot\\mu}{k}`

where :math:`T` is the bismuth temperature in :math:`[K]`.

Finally, the object dynamically adds useful
methods to retrieve more information on specific thermophysical property
which are named <property_name>_print_info. For instance:

>>> from lbh15 import Bismuth
>>> liquid_bismuth = Bismuth(T=668.15)
>>> liquid_bismuth.rho_print_info()
rho:
        Value: 9909.8570 [kg/m^3]
        Validity range: [544.60, 1831.00] K
        Long name: density
        Units: [kg/m^3]
        Description:
                Liquid bismuth density

It is possible to retrieve only parts of the information specifying :code:`info='value'`,
:code:`info='validity_range'`, :code:`info='long_name`, :code:`info='units'` or  :code:`info='description'`.
For instance, print the saturation vapour pressure correlation's validity range:

>>> from lbh15 import Bismuth
>>> liquid_bismuth = Bismuth(T=668.15)
>>> liquid_bismuth.p_s_print_info(info='validity_range')
p_s:
        Validity range: [544.60, 1831.00] K
"""
import sys
import inspect
from ._lbh15 import BISMUTH_MELTING_TEMPERATURE
from ._lbh15 import BISMUTH_MELTING_LATENT_HEAT, BISMUTH_BOILING_TEMPERATURE
from ._lbh15 import BISMUTH_VAPORISATION_HEAT, BISMUTH_KEYWORD
from ._lbh15 import BISMUTH_T_AT_CP_MIN, BISMUTH_CP_MIN
from ._lbh15 import LiquidMetalInterface, p_s_initializer
from .properties.bismuth_properties import PropertiesInterface


class Bismuth(LiquidMetalInterface):
    """
    Class to model liquid bismuth properties at a given temperature

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
    >>> liquid_bismuth = Bismuth(T=670.0)
    >>> liquid_bismuth.k  # [W/(m*K)]
    13.705
    """
    def __init__(self, cp_high_range=False, **kwargs):
        if 'p_s' in kwargs.keys():
            self._guess = p_s_initializer(kwargs['p_s'])
        else:
            self._guess = BISMUTH_MELTING_TEMPERATURE*1.5

        super().__init__(cp_high_range, **kwargs)

    def __new__(cls, cp_high_range=False, **kwargs):
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
            :class:`_properties.PropertiesInterface`
        """
        propertyObjectList = []
        module = 'lbh15.properties.bismuth_properties'
        for name, obj in inspect.getmembers(sys.modules[module]):
            if inspect.isclass(obj) and obj is not PropertiesInterface:
                if issubclass(obj, PropertiesInterface):
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
