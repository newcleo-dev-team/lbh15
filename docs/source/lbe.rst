.. _lbe-module:

*lbe* Module
============
Module implementing the liquid lead-bismuth-eutectic (lbe) class.

A :class:`.LBE` instance can be created by providing either the temperature value or the value of one
of the available properties. The instantiation based on the value of
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

    - ``T_m0`` melting temperature :math:`\left[K\right]`:

        :math:`398.0`
    - ``Q_m0`` melting latent heat :math:`\left[\frac{J}{kg}\right]`:

        :math:`38.6 \cdot 10^3`
    - ``T_b0`` boiling temperature :math:`\left[K\right]`:

        :math:`1927`
    - ``Q_b0`` vaporization heat :math:`\left[\frac{J}{kg}\right]`:

        :math:`856.6 \cdot 10^3`
    - ``p_s`` saturation vapor pressure :math:`\left[Pa\right]`:

        :math:`p_s\left(T\right) = \displaystyle1.22 \cdot 10^{10} \cdot \exp{\left(-22552 / T\right)}`
    - ``sigma`` surface tension :math:`\left[\frac{N}{m}\right]`:

        :math:`\sigma\left(T\right) = \displaystyle\left(448.5 - 0.0799 \cdot T\right) \cdot 10^{-3}`
    - ``u_s`` speed of sound :math:`\left[\frac{m}{s}\right]`:

        :math:`u_s\left(T\right) = \displaystyle1855 - 0.212 \cdot T`
    - ``alpha`` thermal expansion coefficient :math:`\left[\frac{1}{K}\right]`:

        :math:`\alpha\left(T\right) = \displaystyle\left(8558 - T\right)^{-1}`
    - ``cp`` specific heat capacity :math:`\left[\frac{J}{kg{\cdot}K}\right]`:

        :math:`c_p\left(T\right) = \displaystyle164.8 - 3.94 \cdot 10^{-2} \cdot T + 1.25 \cdot 10^{-5} \cdot T^2 - 4.56 \cdot 10^5 \cdot T^{-2}`
    - ``rho`` density :math:`\left[\frac{kg}{m^3}\right]`:

        :math:`\rho_0\left(T\right) = \displaystyle11065 - 1.293 \cdot T`

        :math:`\rho\left(T,p\right) = \displaystyle\rho_0\left(T\right) + \left( \frac{1}{u_s\left(T\right)^2} + T \cdot \frac{\alpha\left(T\right)^2}{c_p\left(T\right)} \right) \cdot \left( p - p_{atm} \right)`, :math:`\quad` where:
        
        :math:`\quad p_{atm}=101325.00 \left[Pa\right]`
    - ``beta_s`` isentropic compressibility :math:`\left[\frac{1}{Pa}\right]`:

        :math:`\beta_s\left(T\right) = \displaystyle\frac{1}{\rho\left(T,p\right) \cdot u_s\left(T\right)^2}`
    - ``h`` specific enthalpy (as difference with respect to the melting point enthalpy) :math:`\left[\frac{J}{kg}\right]`:

        :math:`h\left(T\right) = \displaystyle164.8 \cdot \left(T - T_{m0}\right) - 1.97 \cdot 10^{-2} \cdot \left(T^2 - T_{m0}^2\right)`

        :math:`\qquad\qquad + 4.167 \cdot 10^{-6} \cdot \left(T^3 - T_{m0}^3\right) + 4.56 \cdot 10^5 \cdot \left(T^{-1} - T_{m0}^{-1}\right)`
    - ``mu`` dynamic viscosity :math:`\left[Pa \cdot s\right]`:

        :math:`\mu\left(T\right) = \displaystyle4.94 \cdot 10^{-4} \cdot \exp{\left(754.1 / T\right)}`
    - ``r`` electrical resistivity :math:`\left[\Omega \cdot m\right]`:

        :math:`r\left(T\right) = \displaystyle\left(90.9 + 0.048 \cdot T\right) \cdot 10^{-8}`
    - ``k`` thermal conductivity :math:`\left[\frac{W}{m \cdot K}\right]`:

        :math:`k\left(T\right) = \displaystyle3.284 + 1.617 \cdot 10^{-2} \cdot T - 2.305 \cdot 10^{-6} \cdot T^2`
    - ``Pr`` Prandtl number :math:`\left[-\right]`:

        :math:`Pr\left(T\right) = \displaystyle\frac{c_p\left(T\right) \cdot \mu\left(T\right)}{k\left(T\right)}`

  b. **Thermo-chemical**:

    - ``M`` molar mass :math:`\left[\frac{g}{mol}\right]`:

        :math:`M = \displaystyle0.55 \cdot M_{Bismuth} + 0.45 \cdot M_{Lead}`, :math:`\quad` where:

        :math:`M_{Bismuth}` is the molar mass of bismuth

        :math:`M_{Lead}` is the molar mass of Lead
    - ``H`` molar enthalpy :math:`\left[\frac{J}{mol}\right]`:

        :math:`H\left(T\right) = \displaystyle h\left(T\right) \cdot \frac{M}{1000}`
    - ``S`` molar entropy :math:`\left[\frac{J}{mol \cdot K}\right]`:

        :math:`S\left(T\right) = \displaystyle \frac{M}{1000} \cdot \int_{T_{m0}}^T \frac{c_p\left(T\right)}{T} dT`
    - ``G`` Gibbs free energy :math:`\left[\frac{J}{mol}\right]`:

        :math:`G\left(T\right) = \displaystyle H\left(T\right) - T \cdot S\left(T\right)`
    - ``pb_a`` lead chemical activity :math:`\left[ - \right]`:

        :math:`pb\_a\left(T\right) = \displaystyle0.42206 - \frac{63.2}{T}`
    - ``bi_a`` bismuth chemical activity :math:`\left[ - \right]`:

        :math:`bi\_a\left(T\right) = \displaystyle0.53381 - \frac{56.2}{T}`
    - ``fe_sol`` iron solubility :math:`\left[wt.\%\right]`:

        :math:`fe\_sol\left(T\right) = \displaystyle10^{2.00 - 4399 / T}`
    - ``ni_sol`` nickel solubility :math:`\left[wt.\%\right]`:

        :math:`ni\_sol\left(T\right) = \displaystyle10^{4.32 - 2933 / T} \quad \Longleftrightarrow \quad T <= 742 K`

        :math:`ni\_sol\left(T\right) = \displaystyle10^{1.74 - 1006 / T} \quad \Longleftrightarrow \quad T > 742 K`
    - ``cr_sol`` chromium solubility :math:`\left[wt.\%\right]`:

        :math:`cr\_sol\left(T\right) = \displaystyle10^{1.12 - 3056 / T}`
    - ``o_sol`` oxygen solubility :math:`\left[wt.\%\right]`:

        :math:`o\_sol\left(T\right) = \displaystyle10^{2.25 - 4125 / T}`
    - ``o_dif`` oxygen diffusivity :math:`\left[ \frac{cm^2}{s} \right]`:

        :math:`o\_dif\left(T\right) = \displaystyle2.39 \cdot 10^{-2} \cdot \exp{\left(- 43073 /(RT) \right)}`
    - ``fe_dif`` iron diffusivity :math:`\left[ \frac{cm^2}{s} \right]`:

        :math:`fe\_dif\left(T\right) = \displaystyle10^{- 2.31 - 2295 / T}`
    - ``o_pp`` oxygen partial pressure divided by oxygen concentration squared :math:`\left[ \frac{atm}{wt.\%^2} \right]`:

        :math:`o\_pp\left(T\right) = \displaystyle \left( \frac{M}{M_O} \right)^2 \cdot 10^{ 2 /\left(2.3 \cdot R\right) \cdot \left( - 127398 / T + 27.938 \right) }`, :math:`\quad` where:

        :math:`M_O = 16 \frac{g}{mol} \quad` oxygen molecular mass
    - ``lim_fe_sat`` lower limit of ox concentration with iron @ saturation :math:`\left[wt.\%\right]`:

        :math:`lim\_fe\_sat\left(T\right) = \displaystyle pb\_a\left(T\right) \cdot o\_sol\left(T\right) \cdot \exp{\left( - \frac{57190}{R T} - \frac{21.1}{R} \right)}`
    - ``lim_cr_sat`` lower limit of ox concentration with chromium @ saturation :math:`\left[wt.\%\right]`:

        :math:`lim\_cr\_sat\left(T\right) = \displaystyle pb\_a\left(T\right) \cdot o\_sol\left(T\right) \cdot \exp{\left( - \frac{317800}{2 R T} - \frac{27.3}{2 R} \right)}`
    - ``lim_ni_sat`` lower limit of ox concentration with nickel @ saturation :math:`\left[wt.\%\right]`:

        :math:`lim\_ni\_sat\left(T\right) = \displaystyle pb\_a\left(T\right) \cdot o\_sol\left(T\right) \cdot \exp{\left( - \frac{36080}{2 R T} - \frac{23.4}{2 R} \right)}`
    - ``lim_si_sat`` lower limit of ox concentration with silicon @ saturation :math:`\left[wt.\%\right]`:

        :math:`lim\_si\_sat\left(T\right) = \displaystyle pb\_a\left(T\right) \cdot o\_sol\left(T\right) \cdot \exp{\left( - \frac{471710}{2 R T} - \frac{19.5}{2 R} \right)}`
    - ``lim_al_sat`` lower limit of ox concentration with aluminium @ saturation :math:`\left[wt.\%\right]`:

        :math:`lim\_al\_sat\left(T\right) = \displaystyle pb\_a\left(T\right) \cdot o\_sol\left(T\right) \cdot \exp{\left( - \frac{679540}{2 R T} + \frac{10.7}{2R} \right)}`
    - ``lim_cr`` lower limit of ox concentration times chromium concentration raised to :math:`2/3` :math:`\left[wt.\%\right]`:

        :math:`lim\_cr\left(T\right) = \displaystyle lim\_cr\_sat\left(T\right) \cdot cr\_sol\left(T\right)^{2/3}`
    - ``lim_ni`` lower limit of ox concentration times nickel concentration :math:`\left[wt.\%\right]`:

        :math:`lim\_ni\left(T\right) = \displaystyle lim\_ni\_sat\left(T\right) \cdot ni\_sol\left(T\right)`
    - ``lim_fe`` lower limit of ox concentration times iron concentration raised to :math:`3/4` :math:`\left[wt.\%\right]`:

        :math:`lim\_fe\left(T\right) = \displaystyle lim\_fe\_sat\left(T\right) \cdot fe\_sol\left(T\right)^{3/4}`


where :math:`T` is the lbe temperature in :math:`\left[K\right]`, :math:`p` is the lbe pressure in :math:`\left[Pa\right]` and
:math:`R` is the molar gas constant in :math:`\left[J/(mol K)\right]`.

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
   
