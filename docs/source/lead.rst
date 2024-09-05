.. _lead-module:

*lead* Module
=============
Module implementing the liquid lead class.

A :class:`.Lead` instance can be created by providing either the temperature value or the value of one
of the available properties. The instantiation based on the value of
properties other than the temperature passes through the solution, in terms of the temperature value,
of the corresponding correlation implemented in the *lbh15* package.

In addition to the class attributes that are shown in the second part of this section, :class:`.Lead` class dynamically adds the
thermo-physical properties implemented in :py:mod:`lbh15.properties.lead_properties` module and the
thermo-chemical properties implemented in :py:mod:`lbh15.properties.lead_thermochemical_properties.diffusivity_in_lead`,
:py:mod:`lbh15.properties.lead_thermochemical_properties.lead_oxygen_limits`,
:py:mod:`lbh15.properties.lead_thermochemical_properties.lead_thermochemical`,
:py:mod:`lbh15.properties.lead_thermochemical_properties.solubility_in_lead` and
:py:mod:`lbh15.properties.lead_thermochemical_properties.lead_contamination` modules. For instance:

>>> from lbh15 import Lead
>>> liquid_lead = Lead(T=668.15)
>>> liquid_lead.mu
0.0022534948395446985

In detail, a :class:`.Lead` object comes with the following default properties:

  a. **Thermo-physical**:

    - ``T_m0`` melting temperature :math:`\left[K\right]`:

        :math:`600.6`
    - ``Q_m0`` melting latent heat :math:`\left[\frac{J}{kg}\right]`:

        :math:`23.07 \cdot 10^3`
    - ``T_b0`` boiling temperature :math:`\left[K\right]`:

        :math:`2021`
    - ``Q_b0`` vaporization heat :math:`\left[\frac{J}{kg}\right]`:

        :math:`858.6 \cdot 10^3`
    - ``p_s`` saturation vapor pressure :math:`\left[Pa\right]`:

        :math:`p_s\left(T\right) = \displaystyle 5.76\cdot10^9\cdot\exp{\left(-22131/T\right)}`
    - ``sigma`` surface tension :math:`\left[\frac{N}{m}\right]`:

        :math:`\sigma\left(T\right) = \displaystyle\left(525.9 - 0.113{\cdot}T\right)\cdot10^{-3}`
    - ``u_s`` speed of sound :math:`\left[\frac{m}{s}\right]`:

        :math:`u_s\left(T\right) = \displaystyle 1953 - 0.246{\cdot}T`
    - ``alpha`` thermal expansion coefficient :math:`\left[\frac{1}{K}\right]`:

        :math:`\alpha\left(T\right) = \displaystyle \left(8942 - T\right)^{-1}`
    - ``cp`` specific heat capacity :math:`\left[\frac{J}{kg{\cdot}K}\right]`:

        :math:`c_p\left(T\right) = \displaystyle176.2 - 4.923\cdot10^{-2}{\cdot}T + 1.544\cdot10^{-5}{\cdot}T^2 - 1.524\cdot10^{6}{\cdot}T^{-2}`
    - ``rho`` density :math:`\left[\frac{kg}{m^3}\right]`:

        :math:`\rho_0\left(T\right) = \displaystyle11441 - 1.2795{\cdot}T`

        :math:`\rho\left(T,p\right) = \displaystyle\rho_0\left(T\right) + \left( \frac{1}{u_s\left(T\right)^2} + T \cdot \frac{\alpha\left(T\right)^2}{c_p\left(T\right)} \right) \cdot \left( p - p_{atm} \right)`, :math:`\quad` where:
        
        :math:`\quad p_{atm}=101325.00 \left[Pa\right]`
    - ``beta_s`` isentropic compressibility :math:`\left[\frac{1}{Pa}\right]`:

        :math:`\beta_s\left(T\right) = \displaystyle\frac{1}{\rho\left(T,p\right) \cdot u_s\left(T\right)^2}`
    - ``h`` specific enthalpy (as difference with respect to the melting point enthalpy) :math:`\left[\frac{J}{kg}\right]`:

        :math:`h\left(T\right) = \displaystyle176.2 \cdot \left(T - T_{m0}\right) - 2.4615 \cdot 10^{-2} \cdot \left(T^2 - T_{m0}^2\right)`

        :math:`\qquad\qquad+ 5.147 \cdot 10^{-6} \cdot \left(T^3 - T_{m0}^3\right) + 1.524 \cdot 10^6 \cdot \left(T^{-1} - T_{m0}^{-1}\right)`
    - ``mu`` dynamic viscosity :math:`\left[Pa{\cdot}s\right]`:

        :math:`\mu\left(T\right) = \displaystyle4.55 \cdot 10^{-4} \cdot \exp{\left( 1069 / T \right)}`
    - ``r`` electrical resistivity :math:`\left[\Omega{\cdot}m\right]`:

        :math:`r\left(T\right) = \displaystyle\left( 67.0 + 0.0471 \cdot T \right) \cdot 10^{-8}`
    - ``k`` thermal conductivity :math:`\left[\frac{W}{m \cdot K}\right]`:

        :math:`k\left(T\right) = \displaystyle9.2 + 0.011 \cdot T`
    - ``Pr`` Prandtl number :math:`\left[-\right]`:

        :math:`Pr\left(T\right) = \displaystyle\frac{c_p\left(T\right) \cdot \mu\left(T\right)}{k\left(T\right)}`

  b. **Thermo-chemical**:

    - ``M`` molar mass :math:`\left[\frac{g}{mol}\right]`:

        :math:`207.20`
    - ``H`` molar enthalpy :math:`\left[\frac{J}{mol}\right]`:

        :math:`H\left(T\right) = \displaystyle h\left(T\right) \cdot \frac{M}{1000}`
    - ``S`` molar entropy :math:`\left[\frac{J}{mol \cdot K}\right]`:

        :math:`S\left(T\right) = \displaystyle \frac{M}{1000} \cdot \int_{T_{m0}}^T \frac{c_p\left(T\right)}{T} dT`
    - ``G`` Gibbs free energy :math:`\left[\frac{J}{mol}\right]`:

        :math:`G\left(T\right) = \displaystyle H\left(T\right) - T \cdot S\left(T\right)`
    - ``fe_sol`` iron solubility :math:`\left[wt.\%\right]`:

        :math:`fe\_sol\left(T\right) = \displaystyle10^{2.11 - 5225 / T}`
    - ``ni_sol`` nickel solubility :math:`\left[wt.\%\right]`:

        :math:`ni\_sol\left(T\right) = \displaystyle10^{1.36 - 1395 / T}`
    - ``cr_sol`` chromium solubility :math:`\left[wt.\%\right]`:

        :math:`cr\_sol\left(T\right) = \displaystyle10^{3.62 - 6648 / T}`
    - ``si_sol`` silicon solubility :math:`\left[wt.\%\right]`:

        :math:`si\_sol\left(T\right) = \displaystyle10^{3.886 - 7180 / T}`
    - ``o_sol`` oxygen solubility :math:`\left[wt.\%\right]`:

        :math:`o\_sol\left(T\right) = \displaystyle10^{3.23 - 5043 / T}`
    - ``o_dif`` oxygen diffusivity :math:`\left[ \frac{cm^2}{s} \right]`:

        :math:`o\_dif\left(T\right) = \displaystyle6.6 \cdot 10^{-5} \cdot \exp{\left(- 16158 /\left(RT\right) \right)}`
    - ``fe_dif`` iron diffusivity :math:`\left[ \frac{cm^2}{s} \right]`:

        :math:`fe\_dif\left(T\right) = \displaystyle10^{- 2.31 - 2295 / T}`
    - ``co_dif`` cobalt diffusivity :math:`\left[ \frac{cm^2}{s} \right]`:

        :math:`co\_dif\left(T\right) = \displaystyle4.6 \cdot 10^{-4} \cdot \exp{\left(- 22154 /\left(RT\right) \right)}`
    - ``se_dif`` selenium diffusivity :math:`\left[ \frac{cm^2}{s} \right]`:

        :math:`co\_dif\left(T\right) = \displaystyle3.4 \cdot 10^{-4} \cdot \exp{\left(- 12958 /\left(RT\right) \right)}`
    - ``in_dif`` indium diffusivity :math:`\left[ \frac{cm^2}{s} \right]`:

        :math:`in\_dif\left(T\right) = \displaystyle3.1 \cdot 10^{-4} \cdot \exp{\left(- 13794 /\left(RT\right) \right)}`
    - ``te_dif`` tellurium diffusivity :math:`\left[ \frac{cm^2}{s} \right]`:

        :math:`te\_dif\left(T\right) = \displaystyle3.1 \cdot 10^{-4} \cdot \exp{\left(- 15884 /\left(RT\right) \right)}`
    - ``o_pp`` oxygen partial pressure divided by oxygen concentration squared :math:`\left[ \frac{atm}{wt.\%^2} \right]`:

        :math:`o\_pp\left(T\right) = \displaystyle \left( \frac{M}{M_O} \right)^2 \cdot 10^{ 2 /\left(2.3 \cdot R\right) \cdot \left( - 119411 / T + 12.222 \right) }`, :math:`\quad` where:

        :math:`M_O = 16 \frac{g}{mol} \quad` oxygen molecular mass
    - ``lim_fe_sat`` lower limit of oxygen concentration with iron @ saturation :math:`\left[wt.\%\right]`:

        :math:`lim\_fe\_sat\left(T\right) = \displaystyle o\_sol\left(T\right) \cdot \exp{\left( - \frac{57190}{R T} - \frac{21.1}{R} \right)}`
    - ``lim_cr_sat`` lower limit of oxygen concentration with chromium @ saturation :math:`\left[wt.\%\right]`:

        :math:`lim\_cr\_sat\left(T\right) = \displaystyle o\_sol\left(T\right) \cdot \exp{\left( - \frac{317800}{2 R T} - \frac{27.3}{2R} \right)}`
    - ``lim_ni_sat`` lower limit of oxygen concentration with nickel @ saturation :math:`\left[wt.\%\right]`:

        :math:`lim\_ni\_sat\left(T\right) = \displaystyle o\_sol\left(T\right) \cdot \exp{\left( - \frac{36080}{2 R T} - \frac{23.4}{2R} \right)}`
    - ``lim_si_sat`` lower limit of oxygen concentration with silicon @ saturation :math:`\left[wt.\%\right]`:

        :math:`lim\_si\_sat\left(T\right) = \displaystyle o\_sol\left(T\right) \cdot \exp{\left( - \frac{471710}{2 R T} - \frac{19.5}{2R} \right)}`
    - ``lim_al_sat`` lower limit of oxygen concentration with aluminium @ saturation :math:`\left[wt.\%\right]`:

        :math:`lim\_al\_sat\left(T\right) = \displaystyle o\_sol\left(T\right) \cdot \exp{\left( - \frac{679540}{2 R T} + \frac{10.7}{2R} \right)}`
    - ``lim_cr`` lower limit of oxygen concentration times chromium concentration raised to :math:`2/3` :math:`\left[wt.\%\right]`:

        :math:`lim\_cr\left(T\right) = \displaystyle lim\_cr\_sat\left(T\right) \cdot cr\_sol\left(T\right)^{2/3}`
    - ``lim_ni`` lower limit of oxygen concentration times nickel concentration :math:`\left[wt.\%\right]`:

        :math:`lim\_ni\left(T\right) = \displaystyle lim\_ni\_sat\left(T\right) \cdot ni\_sol\left(T\right)`
    - ``lim_fe`` lower limit of oxygen concentration times iron concentration raised to :math:`3/4` :math:`\left[wt.\%\right]`:

        :math:`lim\_fe\left(T\right) = \displaystyle lim\_fe\_sat\left(T\right) \cdot fe\_sol\left(T\right)^{3/4}`
    - ``lim_si`` lower limit of oxygen concentration times silicon concentration raised to :math:`1/2` :math:`\left[wt.\%\right]`:

        :math:`lim\_si\left(T\right) = \displaystyle lim\_si\_sat\left(T\right) \cdot si\_sol\left(T\right)^{1/2}`
    - ``P_PbPo`` vapour pressure of Po :math:`[Pa]`:

        :math:`P_{PbPo} = 10^{-\frac{7270\pm80}{T} + 9.06\pm0.07}`
    - ``K_PbPo`` Henry constant of Po :math:`[Pa]`:

        :math:`K_{PbPo} = 10^{-\frac{8348}{T} + 10.5357}`
    - ``gamma_PbPo`` Activity coefficient of Po:

        :math:`\gamma_{Po(LBE)} = 10^{-\frac{1830}{T}-0.40}`
    - ``P_PbI2_a`` vapour pressure of I :math:`[Pa]`:

        :math:`P_{PbI_{2}} = 10^{-\frac{8691 \pm 84}{T} + 13.814 \pm 0.140}`
    - ``P_PbI2_b`` vapour pressure of I :math:`[Pa]`:

        :math:`P_{PbI_{2}} = 10^{-\frac{9087}{T} + 31.897 - 6.16\log{T}}`
    - ``K_PbCs`` Henry constant of Cs :math:`[Pa]`:

        :math:`K_{H(Cs,Pb)} = 10^{-\frac{4980}{T} - 9.323\log{T} + 0.004473T - 8.684.10^{-7}T^{2} + 33.07}`
    - ``P_PbCs`` vapour pressure of Cs :math:`[Pa]`:

        :math:`P_{PbCs} = 10^{-1.5}10^{-\frac{4979.5799}{T} - 9.3234247\log{T} + 0.0044733132T - 8.684092*10^{-7}T^{2} + 34.573234}`

  c. **Impurities**:

    - ``P_PbPo`` polonium compound vapour pressure :math:`\left[Pa\right]`:

        :math:`P_{PbPo}\left(T\right) = 10^{- \frac{7270}{T} + 9.06}`
    - ``gamma_PbPo`` polonium compound activity coefficient :math:`\left[-\right]`:

        :math:`\gamma_{PbPo}\left(T\right) = 1`
    - ``K_PbPo`` polonium compound Henry constant :math:`\left[Pa\right]`:

        :math:`K_{PbPo}\left(T\right) = 10^{- \frac{7270}{T} + 9.06}`
    - ``P_PbI2`` iodine compound vapour pressure :math:`\left[Pa\right]`:

        :math:`P_{PbI2}\left(T\right) = 10^{- \frac{9087}{T} - 6.16 \cdot \log\left(T\right) + 31.897}`
    - ``gamma_PbI2`` iodine compound activity coefficient :math:`\left[-\right]`:

        :math:`\gamma_{PbI2}\left(T\right) = 1`
    - ``K_PbI2`` iodine compound Henry constant :math:`\left[Pa\right]`:

        :math:`K_{PbI2}\left(T\right) = 10^{- \frac{9087}{T} - 6.16 \cdot \log\left(T\right) + 31.897}`
    - ``K_PbCs`` caesium intermetallic compounds Henry constant :math:`\left[Pa\right]`:

        :math:`K_{PbCs}\left(T\right) = 10^{- \frac{4980}{T} - 9.323 \cdot \log\left(T\right) + 0.004473 \cdot T - 8.684 \cdot 10^{-7} \cdot T^2 + 33.07}`
    - ``gamma_PbCs`` caesium intermetallic compounds activity coefficient :math:`\left[-\right]`:

        :math:`\gamma_{PbCs}\left(T\right) = 10^{-1.5}`
    - ``P_PbCs`` caesium intermetallic compounds vapour pressure :math:`\left[Pa\right]`:

        :math:`P_{PbCs}\left(T\right) = 10^{1.5} \cdot 10^{- \frac{4980}{T} - 9.323 \cdot \log\left(T\right) + 0.004473 \cdot T - 8.684 \cdot 10^{-7} \cdot T^2 + 33.07}`


where :math:`T` is the lead temperature in :math:`\left[K\right]`, :math:`p` is the lead pressure in :math:`\left[Pa\right]` and
:math:`R` is the molar gas constant in :math:`\left[J/(mol K)\right]`.

In addition, to provide the property values directly, the :class:`.Lead` object dynamically adds the methods named
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

:class:`.Lead` Class Attributes
*******************************

.. automodule:: lbh15.lead
    :members:
    :member-order: bysource
    :inherited-members:
   
