*bismuth* Module
====================
Module implementing the liquid bismuth class.

A *bismuth* instance can be created by providing either the temperature value or the value of one
of the available properties (see :class:`.Bismuth` for the full list). The instantiation based on the value of
properties other than the temperature passes through the solution, in terms of the temperature value,
of the corresponding correlation implemented in the *lbh15* package.

In addition to the class attributes that are shown in the second part of this section, :class:`.Bismuth` class dynamically adds the
thermo-physical properties implemented in :py:mod:`lbh15.properties.bismuth_properties` module and the
thermo-chemical properties implemented in :py:mod:`lbh15.properties.bismuth_thermochemical_properties.diffusivity_in_bismuth`,
:py:mod:`lbh15.properties.bismuth_thermochemical_properties.bismuth_thermochemical` and
:py:mod:`lbh15.properties.bismuth_thermochemical_properties.solubility_in_bismuth` modules. For instance:

>>> from lbh15 import Bismuth
>>> liquid_bismuth = Bismuth(T=668.15)
>>> liquid_bismuth.rho
9909.857

In detail, a :class:`.Bismuth` object comes with the following default properties:

  a. **Thermo-physical**:

    - :math:`T_{m0}` melting temperature :math:`[K]`:

        :math:`544.6`
    - :math:`Q_{m0}` melting latent heat :math:`\Big[\frac{J}{kg}\Big]`:

        :math:`53.3 \cdot 10^3`
    - :math:`T_{b0}` boiling temperature :math:`[K]`:

        :math:`1831`
    - :math:`Q_{b0}` vaporisation heat :math:`\Big[\frac{J}{kg}\Big]`:

        :math:`856.2 \cdot 10^3`
    - :math:`p_s` saturation vapour pressure :math:`[Pa]`:

        :math:`p_s(T) = \displaystyle2.67 \cdot 10^{10} \cdot \exp{\Big(-22858/T\Big)}`
    - :math:`\sigma` surface tension :math:`\Big[\frac{N}{m}\Big]`:

        :math:`\sigma(T) = \displaystyle\Big(420.8 - 0.081 \cdot T \Big) \cdot 10^{-3}`
    - :math:`u_s` speed of sound :math:`\Big[\frac{m}{s}\Big]`:

        :math:`u_s(T) = \displaystyle1616 + 0.187 \cdot T - 2.2 \cdot 10^{-4} \cdot T^2`
    - :math:`\alpha` thermal expansion coefficient :math:`\Big[\frac{1}{K}\Big]`:

        :math:`\alpha(T) = \displaystyle\Big(8791 - T\Big)^{-1}`
    - :math:`c_p` specific heat capacity :math:`\Big[\frac{J}{kg{\cdot}K}\Big]`:

        :math:`c_p(T) = \displaystyle118.2 + 5.934 \cdot 10^{-3} \cdot T + 7.183 \cdot 10^6 \cdot T^{-2}`
    - :math:`\rho` density :math:`\Big[\frac{kg}{m^3}\Big]`:

        :math:`\rho_0(T) = \displaystyle10725 - 1.22{\cdot}T`

        :math:`\rho(T,p) = \displaystyle\rho_0(T) + \Big( \frac{1}{u_s(T)^2} + T \cdot \frac{\alpha(T)^2}{c_p(T)} \Big) \cdot ( p - p_{atm} )`, :math:`\quad` where:
        
        :math:`\quad p_{atm}=101325.00 [Pa]`
    - :math:`\beta_s` isentropic compressibility :math:`\Big[\frac{1}{Pa}\Big]`:

        :math:`\beta_s(T) = \displaystyle\frac{1}{\rho(T,p) \cdot u_s(T)^2}`
    - :math:`h` specific enthalpy (as difference with respect to the melting point enthalpy) :math:`\Big[\frac{J}{kg}\Big]`:

        :math:`h(T) = \displaystyle118.2 \cdot \Big(T - T_{m0}\Big) + 2.967 \cdot 10^{-3} \cdot \Big(T^2 - T_{m0}^2\Big)`
        :math:`\qquad\qquad - 7.183 \cdot 10^6 \cdot \Big(T^{-1} - T_{m0}^{-1}\Big)`
    - :math:`\mu` dynamic viscosity :math:`[Pa{\cdot}s]`:

        :math:`\mu(T) = \displaystyle4.456 \cdot 10^{-4} \cdot \exp{\Big(780 / T\Big)}`
    - :math:`r` electrical resistivity :math:`[\Omega{\cdot}m]`:

        :math:`r(T) = \displaystyle\Big(98.96 + 0.0554 \cdot T \Big) \cdot 10^{-8}`
    - :math:`k` thermal conductivity :math:`\Big[\frac{W}{m \cdot K}\Big]`:

        :math:`k(T) = \displaystyle7.34 + 9.5 \cdot 10^{-3} \cdot T`
    - :math:`Pr` Prandtl number :math:`[-]`:

        :math:`Pr(T) = \displaystyle\frac{c_p(T) \cdot \mu(T)}{k(T)}`

  b. **Thermo-chemical**:

    - :math:`M` molar mass :math:`\Big[\frac{g}{mol}\Big]`:

        :math:`208.98`
    - :math:`H` molar enthalpy :math:`\Big[\frac{J}{mol}\Big]`:

        :math:`H(T) = \displaystyle h(T) \cdot \frac{M}{1000}`
    - :math:`S` molar entropy :math:`\Big[\frac{J}{mol \cdot K}\Big]`:

        :math:`S(T) = \displaystyle \frac{M}{1000} \cdot \int_{T_{m0}}^T \frac{c_p(T)}{T} dT`
    - :math:`G` Gibbs free energy :math:`\Big[\frac{J}{mol}\Big]`:

        :math:`G(T) = \displaystyle H(T) - T \cdot S(T)`
    - :math:`fe\_sol` Iron solubility :math:`[wt.\%]`:

        :math:`fe\_sol(T) = \displaystyle10^{2.20 - 3930 / T}`
    - :math:`ni\_sol` Nickel solubility :math:`[wt.\%]`:

        :math:`ni\_sol(T) = \displaystyle10^{3.81 - 2429 / T} \quad \Longleftrightarrow \quad 543 K <= T < 738 K`

        :math:`ni\_sol(T) = \displaystyle10^{2.05 - 1131 / T} \quad \Longleftrightarrow \quad 738 K <= T < 918 K`
  
        :math:`ni\_sol(T) = \displaystyle10^{1.35 - 484 / T} \quad \Longleftrightarrow \quad 918 K <= T < 1173 K`
    - :math:`cr\_sol` Chromium solubility :math:`[wt.\%]`:

        :math:`cr\_sol(T) = \displaystyle10^{2.34 - 3610 / T}`
    - :math:`o\_sol` Oxygen solubility :math:`[wt.\%]`:

        :math:`o\_sol(T) = \displaystyle10^{2.30 - 4066 / T} \quad \Longleftrightarrow \quad T <= 1002 K`

        :math:`o\_sol(T) = \displaystyle10^{3.04 - 4810 / T} \quad \Longleftrightarrow \quad T > 1002 K`
    - :math:`o\_dif` Oxygen diffusivity :math:`\Big[ \frac{cm^2}{s} \Big]`:

        :math:`o\_dif(T) = \displaystyle1.07 \cdot 10^{-2} \cdot \exp{ - 49229 /(RT) }`
    - :math:`o\_pp` Oxygen partial pressure divided by Oxygen concentration squared :math:`\Big[ \frac{atm}{wt.\%^2} \Big]`:

        :math:`o\_pp(T) = \displaystyle \left( \frac{M}{M_O} \right)^2 \cdot 10^{ 2 /(2.3 \cdot R) \cdot ( - 101098 / T + 15.66 ) }`, :math:`\quad` where:

        :math:`M_O = 16 \frac{g}{mol} \quad` Oxygen molecular mass

where :math:`T` is the bismuth temperature in :math:`[K]`, :math:`p` is the bismuth pressure in :math:`[Pa]` and
:math:`R` is the molar gas constant in :math:`[J/(mol K)]`.

In addition to provide the properties values directly, the :class:`.Bismuth` object dynamically adds the methods named
:code:`<property_name>_info`, that return full information about the corresponding property. For instance:

>>> from lbh15 import Bismuth
>>> liquid_bismuth = Bismuth(T=668.15)
>>> liquid_bismuth.rho_info()
rho:
        Value: 9909.86 [kg/m^3]
        Validity range: [544.60, 1831.00] K
        Correlation name: 'imbeni1998'
        Long name: density
        Units: [kg/m^3]
        Description:
                Liquid bismuth density

----

:class:`.Bismuth` Class Attributes
**********************************

.. automodule:: lbh15.bismuth
    :members:
    :member-order: bysource
    :inherited-members:
