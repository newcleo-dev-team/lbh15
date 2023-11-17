*lbe* Module
============
Module implementing the liquid lead-bismuth-eutectic (LBE) class.

A *LBE* instance can be created by providing either the temperature value or the value of one
of the available properties (see :class:`.LBE` for the full list). The instantiation based on the value of
properties other than the temperature passes through the solution, in terms of the temperature value,
of the corresponding correlation implemented in the *lbh15* package.

In addition to the class attributes that are shown in the second part of this section, :class:`.LBE` class dynamically adds the
thermo-physical properties implemented in :py:mod:`lbh15.properties.lbe_properties` module and the
thermo-chemical properties implemented in :py:mod:`lbh15.properties.lbe_thermochemical_properties.diffusivity_in_lbe`,
:py:mod:`lbh15.properties.lbe_thermochemical_properties.lbe_oxygen_limits`,
:py:mod:`lbh15.properties.lbe_thermochemical_properties.lbe_thermochemical` and
:py:mod:`lbh15.properties.lbe_thermochemical_properties.solubility_in_lbe` modules. For instance:

>>> from lbh15 import LBE
>>> liquid_lbe = LBE(T=668.15)
>>> liquid_lbe.k
13.058977206137499

In detail, a :class:`.LBE` object comes with the following default properties:

  a. **Thermo-physical**:

    - :math:`T_{m0}` melting temperature :math:`[K]`:

        :math:`398.0`
    - :math:`Q_{m0}` melting latent heat :math:`\Big[\frac{J}{kg}\Big]`:

        :math:`38.6 \cdot 10^3`
    - :math:`T_{b0}` boiling temperature :math:`[K]`:

        :math:`1927`
    - :math:`Q_{b0}` vaporisation heat :math:`\Big[\frac{J}{kg}\Big]`:

        :math:`856.6 \cdot 10^3`
    - :math:`p_s` saturation vapour pressure :math:`[Pa]`:

        :math:`p_s(T) = \displaystyle1.22 \cdot 10^{10} \cdot \exp{\Big(-22552 / T\Big)}`
    - :math:`\sigma` surface tension :math:`\Big[\frac{N}{m}\Big]`:

        :math:`\sigma(T) = \displaystyle\Big(448.5 - 0.0799 \cdot T\Big) \cdot 10^{-3}`
    - :math:`u_s` speed of sound :math:`\Big[\frac{m}{s}\Big]`:

        :math:`u_s(T) = \displaystyle1855 - 0.212 \cdot T`
    - :math:`\alpha` thermal expansion coefficient :math:`\Big[\frac{1}{K}\Big]`:

        :math:`\alpha(T) = \displaystyle\Big(8558 - T\Big)^{-1}`
    - :math:`c_p` specific heat capacity :math:`\Big[\frac{J}{kg{\cdot}K}\Big]`:

        :math:`c_p(T) = \displaystyle164.8 - 3.94 \cdot 10^{-2} \cdot T + 1.25 \cdot 10^{-5} \cdot T^2 - 4.56 \cdot 10^5 \cdot T^{-2}`
    - :math:`\rho` density :math:`\Big[\frac{kg}{m^3}\Big]`:

        :math:`\rho_0(T) = \displaystyle11065 - 1.293 \cdot T`

        :math:`\rho(T,p) = \displaystyle\rho_0(T) + \Big( \frac{1}{u_s(T)^2} + T \cdot \frac{\alpha(T)^2}{c_p(T)} \Big) \cdot ( p - p_{atm} )`, :math:`\quad` where:
        
        :math:`\quad p_{atm}=101325.00 [Pa]`
    - :math:`\beta_s` isentropic compressibility :math:`\Big[\frac{1}{Pa}\Big]`:

        :math:`\beta_s(T) = \displaystyle\frac{1}{\rho(T,p) \cdot u_s(T)^2}`
    - :math:`h` specific enthalpy (as difference with respect to the melting point enthalpy) :math:`\Big[\frac{J}{kg}\Big]`:

        :math:`h(T) = \displaystyle164.8 \cdot \Big(T - T_{m0}\Big) - 1.97 \cdot 10^{-2} \cdot \Big(T^2 - T_{m0}^2\Big)`

        :math:`\qquad\qquad + 4.167 \cdot 10^{-6} \cdot \Big(T^3 - T_{m0}^3\Big) + 4.56 \cdot 10^5 \cdot \Big(T^{-1} - T_{m0}^{-1}\Big)`
    - :math:`\mu` dynamic viscosity :math:`[Pa \cdot s]`:

        :math:`\mu(T) = \displaystyle4.94 \cdot 10^{-4} \cdot \exp{\Big(754.1 / T\Big)}`
    - :math:`r` electrical resistivity :math:`[\Omega \cdot m]`:

        :math:`r(T) = \displaystyle\Big(90.9 + 0.048 \cdot T\Big) \cdot 10^{-8}`
    - :math:`k` thermal conductivity :math:`\Big[\frac{W}{m \cdot K}\Big]`:

        :math:`k(T) = \displaystyle3.284 + 1.617 \cdot 10^{-2} \cdot T - 2.305 \cdot 10^{-6} \cdot T^2`
    - :math:`Pr` Prandtl number :math:`[-]`:

        :math:`Pr(T) = \displaystyle\frac{c_p(T) \cdot \mu(T)}{k(T)}`

  b. **Thermo-chemical**:

    - :math:`M` molar mass :math:`\Big[\frac{g}{mol}\Big]`:

        :math:`M = \displaystyle0.55 \cdot M_{Bismuth} + 0.45 \cdot M_{Lead}`, :math:`\quad` where:

        :math:`M_{Bismuth}` is the molar mass of Bismuth

        :math:`M_{Lead}` is the molar mass of Lead
    - :math:`H` molar enthalpy :math:`\Big[\frac{J}{mol}\Big]`:

        :math:`H(T) = \displaystyle h(T) \cdot \frac{M}{1000}`
    - :math:`S` molar entropy :math:`\Big[\frac{J}{mol \cdot K}\Big]`:

        :math:`S(T) = \displaystyle \frac{M}{1000} \cdot \int_{T_{m0}}^T \frac{c_p(T)}{T} dT`
    - :math:`G` Gibbs free energy :math:`\Big[\frac{J}{mol}\Big]`:

        :math:`G(T) = \displaystyle H(T) - T \cdot S(T)`
    - :math:`pb\_a` Lead chemical activity :math:`\Big[ - \Big]`:

        :math:`pb\_a(T) = \displaystyle0.42206 - \frac{63.2}{T}`
    - :math:`bi\_a` Bismuth chemical activity :math:`\Big[ - \Big]`:

        :math:`bi\_a(T) = \displaystyle0.53381 - \frac{56.2}{T}`
    - :math:`fe\_sol` Iron solubility :math:`[wt.\%]`:

        :math:`fe\_sol(T) = \displaystyle10^{2.00 - 4399 / T}`
    - :math:`ni\_sol` Nickel solubility :math:`[wt.\%]`:

        :math:`ni\_sol(T) = \displaystyle10^{4.32 - 2933 / T} \quad \Longleftrightarrow \quad T <= 742 K`

        :math:`ni\_sol(T) = \displaystyle10^{1.74 - 1006 / T} \quad \Longleftrightarrow \quad T > 742 K`
    - :math:`cr\_sol` Chromium solubility :math:`[wt.\%]`:

        :math:`cr\_sol(T) = \displaystyle10^{1.12 - 3056 / T}`
    - :math:`o\_sol` Oxygen solubility :math:`[wt.\%]`:

        :math:`o\_sol(T) = \displaystyle10^{2.25 - 4125 / T}`
    - :math:`o\_dif` Oxygen diffusivity :math:`\Big[ \frac{cm^2}{s} \Big]`:

        :math:`o\_dif(T) = \displaystyle2.39 \cdot 10^{-2} \cdot \exp{\left(- 43073 /(RT) \right)}`
    - :math:`fe\_dif` Iron diffusivity :math:`\Big[ \frac{cm^2}{s} \Big]`:

        :math:`fe\_dif(T) = \displaystyle10^{- 2.31 - 2295 / T}`
    - :math:`o\_pp` Oxygen partial pressure divided by Oxygen concentration squared :math:`\Big[ \frac{atm}{wt.\%^2} \Big]`:

        :math:`o\_pp(T) = \displaystyle \left( \frac{M}{M_O} \right)^2 \cdot 10^{ 2 /(2.3 \cdot R) \cdot ( - 127398 / T + 27.938 ) }`, :math:`\quad` where:

        :math:`M_O = 16 \frac{g}{mol} \quad` Oxygen molecular mass
    - :math:`lim\_fe\_sat` Lower limit of Ox concentration with Iron @ saturation :math:`[wt.\%]`:

        :math:`lim\_fe\_sat(T) = \displaystyle pb\_a(T) \cdot o\_sol(T) \cdot \exp{\left( - \frac{57190}{R T} - \frac{21.1}{R} \right)}`
    - :math:`lim\_cr\_sat` Lower limit of Ox concentration with Chromium @ saturation :math:`[wt.\%]`:

        :math:`lim\_cr\_sat(T) = \displaystyle pb\_a(T) \cdot o\_sol(T) \cdot \exp{\left( - \frac{317800}{2 R T} - \frac{27.3}{2 R} \right)}`
    - :math:`lim\_ni\_sat` Lower limit of Ox concentration with Nickel @ saturation :math:`[wt.\%]`:

        :math:`lim\_ni\_sat(T) = \displaystyle pb\_a(T) \cdot o\_sol(T) \cdot \exp{\left( - \frac{36080}{2 R T} - \frac{23.4}{2 R} \right)}`
    - :math:`lim\_si\_sat` Lower limit of Ox concentration with Silicon @ saturation :math:`[wt.\%]`:

        :math:`lim\_si\_sat(T) = \displaystyle pb\_a(T) \cdot o\_sol(T) \cdot \exp{\left( - \frac{471710}{2 R T} - \frac{19.5}{2 R} \right)}`
    - :math:`lim\_al\_sat` Lower limit of Ox concentration with Aluminium @ saturation :math:`[wt.\%]`:

        :math:`lim\_al\_sat(T) = \displaystyle pb\_a(T) \cdot o\_sol(T) \cdot \exp{\left( - \frac{679540}{2 R T} + \frac{10.7}{2R} \right)}`
    - :math:`lim\_cr` Lower limit of Ox concentration times Chromium concentration raised to :math:`2/3` :math:`[wt.\%]`:

        :math:`lim\_cr(T) = \displaystyle lim\_cr\_sat(T) \cdot cr\_sol(T)^{2/3}`
    - :math:`lim\_ni` Lower limit of Ox concentration times Nickel concentration :math:`[wt.\%]`:

        :math:`lim\_ni(T) = \displaystyle lim\_ni\_sat(T) \cdot ni\_sol(T)`
    - :math:`lim\_fe` Lower limit of Ox concentration times Iron concentration raised to :math:`3/4` :math:`[wt.\%]`:

        :math:`lim\_fe(T) = \displaystyle lim\_fe\_sat(T) \cdot fe\_sol(T)^{3/4}`


where :math:`T` is the lbe temperature in :math:`[K]`, :math:`p` is the lbe pressure in :math:`[Pa]` and
:math:`R` is the molar gas constant in :math:`[J/(mol K)]`.

In addition to provide the properties values directly, the :class:`.LBE` object dynamically adds the methods named
:code:`<property_name>_info`, that return full information about the corresponding property. For instance:

>>> from lbh15 import LBE
>>> liquid_lbe = LBE(T=668.15)
>>> liquid_lbe.k_info()
k:
        Value: 13.06 [W/(m*K)]
        Validity range: [398.00, 1200.00] K
        Correlation name: 'sobolev2011'
        Long name: thermal conductivity
        Units: [W/(m*K)]
        Description:
                Liquid lbe thermal conductivity

----

:class:`.LBE` Class Attributes
******************************

.. automodule:: lbh15.lbe
    :members:
    :member-order: bysource
    :inherited-members:
   
