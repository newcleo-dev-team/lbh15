"""
Module with liquid lead class.
Lead object can be initialized with the temperature
or with one of the available properties (see :class:`.Lead` for \
the full list). It must be underlined that instantiation from properties
depends on the specific correlation of the properties implemented in
lbh15 package. In addition to the class attributes that are shown
in this section, :class:`.Lead` class dynamically adds the properties
implemented in :py:mod:`lbh15.properties.lead_properties` module.

Therefore the object has the following themophysical properties:

    - :math:`T_{m0}` lead melting temperature:

        :math:`600.6 [K]`
    - :math:`Q_{m0}` lead melting latent heat:

        :math:`23.07\\cdot10^3 \\Big[\\frac{J}{kg}\\Big]`
    - :math:`T_{b0}` lead boiling temperature:

        :math:`2021 [K]`
    - :math:`Q_{b0}` lead vaporisation heat:

        :math:`858.6\\cdot10^3 \\Big[\\frac{J}{kg}\\Big]`
    - :math:`p_s` lead saturation vapour pressure :math:`[Pa]`:

        :math:`p_s(T) = \\displaystyle5.79\\cdot10^9\\cdot\
        \\exp{\\Big(-22131/T\\Big)}`
    - :math:`\\sigma` lead surface tension \
      :math:`\\Big[\\frac{N}{m}\\Big]`:

        :math:`\\sigma(T) = \\displaystyle\\Big(525.9 \
        - 0.113{\\cdot}T\\Big)\\cdot10^{-3}`
    - :math:`\\rho` lead density \
      :math:`\\Big[\\frac{kg}{m^3}\\Big]`:

        :math:`\\rho(T) = \\displaystyle11441 - 1.2795{\\cdot}T`
    - :math:`\\alpha` lead thermal expansion coefficient \
      :math:`\\Big[\\frac{1}{K}\\Big]`:

        :math:`\\alpha(T) = \\displaystyle\\Big(8942 - T\\Big)^{-1}`
    - :math:`u_s` speed of sound in lead \
      :math:`\\Big[\\frac{m}{s}\\Big]`:

        :math:`u_s(T) = \\displaystyle1953 - 0.246{\\cdot}T`
    - :math:`\\beta_s` lead isentropic compressibility \
      :math:`\\Big[\\frac{1}{Pa}\\Big]`:

        :math:`\\beta_s(T) = \\displaystyle\\frac{1}{\\rho(T){\\cdot}u_s(T)^2}`
    - :math:`c_p` lead specific heat capacity :math:`\\Big[\
      \\frac{J}{kg{\\cdot}K}\\Big]`, two correlations are available,\
      'sobolev2011' and 'gurvich1991'. The first one is the\
      default one used by :class:`.Lead` and its inherited classes:

        :math:`c_p(T) = \\displaystyle176.2 - 4.923\\cdot10^{-2}{\\cdot}T \
        + 1.544\\cdot10^{-5}{\\cdot}T^2 - 1.524\\cdot10^{6}{\\cdot}T^{-2}`

        :math:`c_p(T) = \\displaystyle175.1 - 4.961\\cdot10^{-2}{\\cdot}T \
        + 1.985\\cdot10^{-5}{\\cdot}T^2 - 2.099\\cdot10^{-9}{\\cdot}T^3 \
        - 1.524\\cdot10^{6}{\\cdot}T^{-2}`
    - :math:`h` lead specific enthalpy (as difference with \
      respect to the melting point enthalpy) \
      :math:`\\Big[\\frac{J}{kg{\\cdot}K}\\Big]`:

        :math:`h(T) = \\displaystyle\
        176.2\\cdot\\Big(T - T_{m0}\\Big) \
        - 2.4615\\cdot10^{-2}\\Big(T^2 - T_{m0}^2\\Big) \
        + 5.147\\cdot10^{-6}\\Big(T^3 - T_{m0}^3\\Big)`

        :math:`\\qquad\\qquad+ 1.524\\cdot10^6\\Big(T^{-1} - T_{m0}^{-1}\\Big)`
    - :math:`\\mu` lead dynamic visocity :math:`[Pa{\\cdot}s]`:

        :math:`\\mu(T) = \\displaystyle4.55\\cdot10^{-4}\\cdot\
        \\exp{\\Big(1069/T\\Big)}`
    - :math:`r` lead electrical resistivity :math:`[\\Omega{\\cdot}m]`:

        :math:`r(T) = \\displaystyle\\Big(67.0 + 0.0471{\\cdot}T\\Big)\
        \\cdot10^{-8}`
    - :math:`k` lead thermal conductivity \
      :math:`\\Big[\\frac{W}{m{\\cdot}K}\\Big]`:

        :math:`k(T) = \\displaystyle9.2 + 0.011{\\cdot}T`
    - :math:`Pr` Prandtl number :math:`[-]`:

        :math:`Pr = \\displaystyle\\frac{c_p\\cdot\\mu}{k}`

where :math:`T` is the lead temperature in :math:`[K]`.

The two :math:`c_p(T)` correlations are shown below,
together with the relative error.

.. figure:: figures/cp_correlations.png
   :width: 700

Finally, the object dynamically adds useful
methods to retrieve more information on specific thermophysical property
which are named <property_name>_print_info. For instance:

>>> from lbh15 import Lead
>>> liquid_lead = Lead(T=668.15)
>>> liquid_lead.mu_print_info()
mu:
        Value: 0.0023 [Pa*s]
        Validity range: [600.60, 1473.00] K
        Long name: dynamic viscosity
        Units: [Pa*s]
        Description:
                Liquid lead dynamic viscosity

It is possible to retrieve only parts of the information
specifying :code:`info='value'`, :code:`info='validity_range'`,
:code:`info='long_name`, :code:`info='units'` or  :code:`info='description'`.
For instance, print the specific enthalpy description:

>>> from lbh15 import Lead
>>> liquid_lead = Lead(T=668.15)
>>> liquid_lead.h_print_info(info='description')
h:
        Description:
                Liquid lead specific enthalpy \
                (as difference with respect to the melting point enthalpy)
"""
import sys
import inspect
import pathlib
import pkgutil
from ._lbh15 import LEAD_MELTING_TEMPERATURE
from ._lbh15 import LEAD_MELTING_LATENT_HEAT, LEAD_BOILING_TEMPERATURE
from ._lbh15 import SOBOLEV_KEYWORD, GURVICH_KEYWORD
from ._lbh15 import LEAD_VAPORISATION_HEAT, LEAD_KEYWORD
from ._lbh15 import LEAD_T_AT_CP_MIN_SOBOLEV, LEAD_T_AT_CP_MIN_GURVICH
from ._lbh15 import LEAD_CP_MIN_SOBOLEV, LEAD_CP_MIN_GURVICH
from ._lbh15 import LiquidMetalInterface, p_s_initializer
from .properties.lead_properties import PropertyInterface


class Lead(LiquidMetalInterface):
    """
    Class to model liquid lead properties at a given temperature

    Parameters
    ----------
    cp_correlation_to_use : str
        Name of cp correlation, can be 'sobolev2011' or 'gurvich1991'
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
    Compare :class:`.lead.Lead` specific heat values at T=800 K
    with with cp_correlation_to_use equal to 'sobolev2011' and 'gurvich1991':

    >>> liquid_lead_1 = Lead(T=800)  # cp_correlation_to_use='sobolev2011'
    >>> liquid_lead_2 = Lead(T=800, cp_correlation_to_use='gurvich1991')
    >>> liquid_lead_1.cp, liquid_lead_2.cp
    (144.31634999999997, 144.66006199999998)
    """
    _correlations_to_use = {'cp': SOBOLEV_KEYWORD}

    def __init__(self, cp_high_range=False, **kwargs):
        self._guess = LEAD_MELTING_TEMPERATURE*1.7
        super().__init__(cp_high_range=cp_high_range, **kwargs)

    def __new__(cls, cp_high_range=False, **kwargs):
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
            raise ValueError("cp correlation can be one among: {:s}, "
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
            raise ValueError("cp correlation can be one among: {:s}, "
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
