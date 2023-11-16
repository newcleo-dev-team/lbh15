*lead* Module
=============
Module implementing the liquid lead class.

A *lead* instance can be created by providing either the temperature value or the value of one
of the available properties (see :class:`.Lead` for the full list). The instantiation based on the value of
properties other than the temperature passes through the solution, in terms of the temperature value,
of the corresponding correlation implemented in the *lbh15* package.

In addition to the class attributes that are shown in the second part of this section, :class:`.Lead` class dynamically adds the
thermo-physical properties implemented in :py:mod:`lbh15.properties.lead_properties` module and the
thermo-chemical properties implemented in :py:mod:`lbh15.properties.lead_thermochemical_properties.diffusivity_in_lead`,
:py:mod:`lbh15.properties.lead_thermochemical_properties.lead_oxygen_limits`,
:py:mod:`lbh15.properties.lead_thermochemical_properties.lead_thermochemical` and
:py:mod:`lbh15.properties.lead_thermochemical_properties.solubility_in_lead` modules. For instance:

>>> from lbh15 import Lead
>>> liquid_lead = Lead(T=668.15)
>>> liquid_lead.mu
0.0022534948395446985

In detail, a :class:`.Lead` object comes with the following default properties:

  a. **Thermo-physical**:

    - :math:`T_{m0}` melting temperature :math:`[K]`:

        :math:`600.6`
    - :math:`Q_{m0}` melting latent heat :math:`\Big[\frac{J}{kg}\Big]`:

        :math:`23.07\cdot10^3`
    - :math:`T_{b0}` boiling temperature :math:`[K]`:

        :math:`2021`
    - :math:`Q_{b0}` vaporisation heat :math:`\Big[\frac{J}{kg}\Big]`:

        :math:`858.6\cdot10^3`
    - :math:`p_s` saturation vapour pressure :math:`[Pa]`:

        :math:`p_s(T) = \displaystyle5.76\cdot10^9\cdot\exp{\Big(-22131/T\Big)}`
    - :math:`\sigma` surface tension :math:`\Big[\frac{N}{m}\Big]`:

        :math:`\sigma(T) = \displaystyle\Big(525.9 - 0.113{\cdot}T\Big)\cdot10^{-3}`
    - :math:`u_s` speed of sound :math:`\Big[\frac{m}{s}\Big]`:

        :math:`u_s(T) = \displaystyle1953 - 0.246{\cdot}T`
    - :math:`\alpha` thermal expansion coefficient :math:`\Big[\frac{1}{K}\Big]`:

        :math:`\alpha(T) = \displaystyle\Big(8942 - T\Big)^{-1}`
    - :math:`c_p` specific heat capacity :math:`\Big[\frac{J}{kg{\cdot}K}\Big]`:

        :math:`c_p(T) = \displaystyle176.2 - 4.923\cdot10^{-2}{\cdot}T + 1.544\cdot10^{-5}{\cdot}T^2 - 1.524\cdot10^{6}{\cdot}T^{-2}`
    - :math:`\rho` density :math:`\Big[\frac{kg}{m^3}\Big]`:

        :math:`\rho_0(T) = \displaystyle11441 - 1.2795{\cdot}T`

        :math:`\rho(T,p) = \displaystyle\rho_0(T) + \Big( \frac{1}{u_s(T)^2} + T \cdot \frac{\alpha(T)^2}{c_p(T)} \Big) \cdot ( p - p_{atm} )`, :math:`\quad p_{atm}=101325.00 [Pa]`
    - :math:`\beta_s` isentropic compressibility :math:`\Big[\frac{1}{Pa}\Big]`:

        :math:`\beta_s(T) = \displaystyle\frac{1}{\rho(T,p) \cdot u_s(T)^2}`
    - :math:`h` specific enthalpy (as difference with respect to the melting point enthalpy) :math:`\Big[\frac{J}{kg}\Big]`:

        :math:`h(T) = \displaystyle176.2 \cdot \Big(T - T_{m0}\Big) - 2.4615 \cdot 10^{-2} \cdot \Big(T^2 - T_{m0}^2\Big)`
        :math:`\qquad\qquad+ 5.147 \cdot 10^{-6} \cdot \Big(T^3 - T_{m0}^3\Big) + 1.524 \cdot 10^6\Big(T^{-1} - T_{m0}^{-1}\Big)`
    - :math:`\mu` dynamic viscosity :math:`[Pa{\cdot}s]`:

        :math:`\mu(T) = \displaystyle4.55 \cdot 10^{-4} \cdot \exp{\Big( 1069 / T \Big)}`
    - :math:`r` electrical resistivity :math:`[\Omega{\cdot}m]`:

        :math:`r(T) = \displaystyle\Big( 67.0 + 0.0471 \cdot T \Big) \cdot 10^{-8}`
    - :math:`k` thermal conductivity :math:`\Big[\frac{W}{m \cdot K}\Big]`:

        :math:`k(T) = \displaystyle9.2 + 0.011 \cdot T`
    - :math:`Pr` Prandtl number :math:`[-]`:

        :math:`Pr(T) = \displaystyle\frac{c_p(T) \cdot \mu(T)}{k(T)}`

  b. **Thermo-chemical**:

    - :math:`M` molar mass :math:`\Big[\frac{g}{mol}\Big]`:

        :math:`207.20`
    - :math:`H` molar enthalpy :math:`\Big[\frac{J}{mol}\Big]`:

        :math:`H(T) = \displaystyle h(T) \cdot \frac{M}{1000}`

    - :math:`S` molar entropy :math:`\Big[\frac{J}{mol \cdot K}\Big]`:

        :math:`S(T) = \displaystyle \frac{M}{1000} \cdot \int_{T_{m0}}^T \frac{c_p(T)}{T} dT`

    - :math:`G` Gibbs free energy :math:`\Big[\frac{J}{mol}\Big]`:

        :math:`G(T) = \displaystyle H(T) - T \cdot S(T)`
    - :math:`fe\_sol` Iron solubility :math:`[wt.\%]`:

        :math:`fe\_sol(T) = \displaystyle10^{2.11 - 5225 / T}`
    - :math:`ni\_sol` Nickel solubility :math:`[wt.\%]`:

        :math:`ni\_sol(T) = \displaystyle10^{1.36 - 1395 / T}`
    - :math:`cr\_sol` Chromium solubility :math:`[wt.\%]`:

        :math:`cr\_sol(T) = \displaystyle10^{3.62 - 6648 / T}`
    - :math:`si\_sol` Silicon solubility :math:`[wt.\%]`:

        :math:`si\_sol(T) = \displaystyle10^{3.886 - 7180 / T}`
    - :math:`o\_sol` Oxygen solubility :math:`[wt.\%]`:

        :math:`o\_sol(T) = \displaystyle10^{3.23 - 5043 / T}`
    - :math:`o\_dif` Oxygen diffusivity :math:`\Big[ \frac{cm^2}{s} \Big]`:

        :math:`o\_dif(T) = \displaystyle6.6 \cdot 10^{-5} \cdot e^{ - 16158 /(RT) }`
    - :math:`fe\_dif` Iron diffusivity :math:`\Big[ \frac{cm^2}{s} \Big]`:

        :math:`fe\_dif(T) = \displaystyle10^{- 2.31 - 2295 / T}`
    - :math:`co\_dif` Cobalt diffusivity :math:`\Big[ \frac{cm^2}{s} \Big]`:

        :math:`co\_dif(T) = \displaystyle4.6 \cdot 10^{-4} \cdot e^{ - 22154 /(RT) }`
    - :math:`se\_dif` Selenium diffusivity :math:`\Big[ \frac{cm^2}{s} \Big]`:

        :math:`co\_dif(T) = \displaystyle3.4 \cdot 10^{-4} \cdot e^{ - 12958 /(RT) }`
    - :math:`in\_dif` Indium diffusivity :math:`\Big[ \frac{cm^2}{s} \Big]`:

        :math:`in\_dif(T) = \displaystyle3.1 \cdot 10^{-4} \cdot e^{ - 13794 /(RT) }`
    - :math:`te\_dif` Tellurium diffusivity :math:`\Big[ \frac{cm^2}{s} \Big]`:

        :math:`te\_dif(T) = \displaystyle3.1 \cdot 10^{-4} \cdot e^{ - 15884 /(RT) }`
    - :math:`o\_pp` Oxygen partial pressure divided by Oxygen concentration squared :math:`\Big[ \frac{atm}{wt.\%^2} \Big]`:

        :math:`o\_pp(T) = \displaystyle \left( \frac{M}{M_O} \right)^2 \cdot 10^{ 2 /(2.3 \cdot R) \cdot ( - 119411 / T + 12.222 ) }`, :math:`\quad` where:

        :math:`M_O = 16 \frac{g}{mol} \quad` Oxygen molecular mass
    - :math:`lim\_fe\_sat` Lower limit of Ox concentration with Iron @ saturation :math:`[wt.\%]`:

        :math:`lim\_fe\_sat(T) = \displaystyle o\_sol(T) \cdot \exp{\left( - \frac{57190}{R T} - \frac{21.1}{R} \right)}`
    - :math:`lim\_cr\_sat` Lower limit of Ox concentration with Chromium @ saturation :math:`[wt.\%]`:

        :math:`lim\_cr\_sat(T) = \displaystyle o\_sol(T) \cdot \exp{\left( - \frac{317800}{2 R T} - \frac{27.3}{2R} \right)}`
    - :math:`lim\_ni\_sat` Lower limit of Ox concentration with Nickel @ saturation :math:`[wt.\%]`:

        :math:`lim\_ni\_sat(T) = \displaystyle o\_sol(T) \cdot \exp{\left( - \frac{36080}{2 R T} - \frac{23.4}{2R} \right)}`
    - :math:`lim\_si\_sat` Lower limit of Ox concentration with Silicon @ saturation :math:`[wt.\%]`:

        :math:`lim\_si\_sat(T) = \displaystyle o\_sol(T) \cdot \exp{\left( - \frac{471710}{2 R T} - \frac{19.5}{2R} \right)}`
    - :math:`lim\_al\_sat` Lower limit of Ox concentration with Aluminium @ saturation :math:`[wt.\%]`:

        :math:`lim\_al\_sat(T) = \displaystyle o\_sol(T) \cdot \exp{\left( - \frac{679540}{2 R T} + \frac{10.7}{2R} \right)}`
    - :math:`lim\_cr` Lower limit of Ox concentration times Chromium concentration raised to :math:`2/3` :math:`[wt.\%]`:

        :math:`lim\_cr(T) = \displaystyle lim\_cr\_sat(T) \cdot cr\_sol^{2/3}`
    - :math:`lim\_ni` Lower limit of Ox concentration times Nickel concentration :math:`[wt.\%]`:

        :math:`lim\_ni(T) = \displaystyle lim\_ni\_sat(T) \cdot ni\_sol`
    - :math:`lim\_fe` Lower limit of Ox concentration times Iron concentration raised to :math:`3/4` :math:`[wt.\%]`:

        :math:`lim\_fe(T) = \displaystyle lim\_fe\_sat(T) \cdot fe\_sol^{3/4}`
    - :math:`lim\_si` Lower limit of Ox concentration times Silicon concentration raised to :math:`1/2` :math:`[wt.\%]`:

        :math:`lim\_si(T) = \displaystyle lim\_si\_sat(T) \cdot si\_sol^{1/2}`

where :math:`T` is the lead temperature in :math:`[K]`, :math:`p` is the lead pressure in :math:`[Pa]` and
:math:`R` is the molar gas constant in :math:`[J/(mol K)]`.

In addition to provide the properties values directly, the :class:`.Lead` object dynamically adds the methods named
:code:`<property_name>_info`, that return full information about the corresponding property. For instance:

>>> from lbh15 import Lead
>>> liquid_lead = Lead(T=668.15)
>>> liquid_lead.mu_info()
mu:
        Value: 2.25e-03 [Pa*s]
        Validity range: [600.60, 1473.00] K
        Correlation name: 'lbh15'
        Long name: dynamic viscosity
        Units: [Pa*s]
        Description:
                Liquid lead dynamic viscosity

----

.. _ Lead class attributes:

:class:`.Lead` Class Attributes
===============================

.. automodule:: lbh15.lead
    :members:
    :member-order: bysource
    :inherited-members:
   
