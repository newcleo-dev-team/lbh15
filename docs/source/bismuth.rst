.. _bismuth-module:

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

    - :math:`T_{m0}` melting temperature :math:`\left[K\right]`:

        :math:`544.6`
    - :math:`Q_{m0}` melting latent heat :math:`\left[\frac{J}{kg}\right]`:

        :math:`53.3 \cdot 10^3`
    - :math:`T_{b0}` boiling temperature :math:`\left[K\right]`:

        :math:`1831`
    - :math:`Q_{b0}` vaporisation heat :math:`\left[\frac{J}{kg}\right]`:

        :math:`856.2 \cdot 10^3`
    - :math:`p_s` saturation vapour pressure :math:`\left[Pa\right]`:

        :math:`p_s\left(T\right) = \displaystyle2.67 \cdot 10^{10} \cdot \exp{\left(-22858/T\right)}`
    - :math:`\sigma` surface tension :math:`\left[\frac{N}{m}\right]`:

        :math:`\sigma\left(T\right) = \displaystyle\left(420.8 - 0.081 \cdot T \right) \cdot 10^{-3}`
    - :math:`u_s` speed of sound :math:`\left[\frac{m}{s}\right]`:

        :math:`u_s\left(T\right) = \displaystyle1616 + 0.187 \cdot T - 2.2 \cdot 10^{-4} \cdot T^2`
    - :math:`\alpha` thermal expansion coefficient :math:`\left[\frac{1}{K}\right]`:

        :math:`\alpha\left(T\right) = \displaystyle\left(8791 - T\right)^{-1}`
    - :math:`c_p` specific heat capacity :math:`\left[\frac{J}{kg{\cdot}K}\right]`:

        :math:`c_p\left(T\right) = \displaystyle118.2 + 5.934 \cdot 10^{-3} \cdot T + 7.183 \cdot 10^6 \cdot T^{-2}`
    - :math:`\rho` density :math:`\left[\frac{kg}{m^3}\right]`:

        :math:`\rho_0\left(T\right) = \displaystyle10725 - 1.22{\cdot}T`

        :math:`\rho\left(T,p\right) = \displaystyle\rho_0\left(T\right) + \left( \frac{1}{u_s\left(T\right)^2} + T \cdot \frac{\alpha\left(T\right)^2}{c_p\left(T\right)} \right) \cdot \left( p - p_{atm} \right)`, :math:`\quad` where:
        
        :math:`\quad p_{atm}=101325.00 \left[Pa\right]`
    - :math:`\beta_s` isentropic compressibility :math:`\left[\frac{1}{Pa}\right]`:

        :math:`\beta_s\left(T\right) = \displaystyle\frac{1}{\rho\left(T,p\right) \cdot u_s\left(T\right)^2}`
    - :math:`h` specific enthalpy (as difference with respect to the melting point enthalpy) :math:`\left[\frac{J}{kg}\right]`:

        :math:`h\left(T\right) = \displaystyle118.2 \cdot \left(T - T_{m0}\right) + 2.967 \cdot 10^{-3} \cdot \left(T^2 - T_{m0}^2\right)`

        :math:`\qquad\qquad - 7.183 \cdot 10^6 \cdot \left(T^{-1} - T_{m0}^{-1}\right)`
    - :math:`\mu` dynamic viscosity :math:`\left[Pa{\cdot}s\right]`:

        :math:`\mu\left(T\right) = \displaystyle4.456 \cdot 10^{-4} \cdot \exp{\left(780 / T\right)}`
    - :math:`r` electrical resistivity :math:`\left[\Omega{\cdot}m\right]`:

        :math:`r\left(T\right) = \displaystyle\left(98.96 + 0.0554 \cdot T \right) \cdot 10^{-8}`
    - :math:`k` thermal conductivity :math:`\left[\frac{W}{m \cdot K}\right]`:

        :math:`k\left(T\right) = \displaystyle7.34 + 9.5 \cdot 10^{-3} \cdot T`
    - :math:`Pr` Prandtl number :math:`\left[-\right]`:

        :math:`Pr\left(T\right) = \displaystyle\frac{c_p\left(T\right) \cdot \mu\left(T\right)}{k\left(T\right)}`

  b. **Thermo-chemical**:

    - :math:`M` molar mass :math:`\left[\frac{g}{mol}\right]`:

        :math:`208.98`
    - :math:`H` molar enthalpy :math:`\left[\frac{J}{mol}\right]`:

        :math:`H\left(T\right) = \displaystyle h\left(T\right) \cdot \frac{M}{1000}`
    - :math:`S` molar entropy :math:`\left[\frac{J}{mol \cdot K}\right]`:

        :math:`S\left(T\right) = \displaystyle \frac{M}{1000} \cdot \int_{T_{m0}}^T \frac{c_p\left(T\right)}{T} dT`
    - :math:`G` Gibbs free energy :math:`\left[\frac{J}{mol}\right]`:

        :math:`G\left(T\right) = \displaystyle H\left(T\right) - T \cdot S\left(T\right)`
    - :math:`fe\_sol` Iron solubility :math:`\left[wt.\%\right]`:

        :math:`fe\_sol\left(T\right) = \displaystyle10^{2.20 - 3930 / T}`
    - :math:`ni\_sol` Nickel solubility :math:`\left[wt.\%\right]`:

        :math:`ni\_sol\left(T\right) = \displaystyle10^{3.81 - 2429 / T} \quad \Longleftrightarrow \quad 543 K <= T < 738 K`

        :math:`ni\_sol\left(T\right) = \displaystyle10^{2.05 - 1131 / T} \quad \Longleftrightarrow \quad 738 K <= T < 918 K`
  
        :math:`ni\_sol\left(T\right) = \displaystyle10^{1.35 - 484 / T} \quad \Longleftrightarrow \quad 918 K <= T < 1173 K`
    - :math:`cr\_sol` Chromium solubility :math:`\left[wt.\%\right]`:

        :math:`cr\_sol\left(T\right) = \displaystyle10^{2.34 - 3610 / T}`
    - :math:`o\_sol` Oxygen solubility :math:`\left[wt.\%\right]`:

        :math:`o\_sol\left(T\right) = \displaystyle10^{2.30 - 4066 / T} \quad \Longleftrightarrow \quad T <= 1002 K`

        :math:`o\_sol\left(T\right) = \displaystyle10^{3.04 - 4810 / T} \quad \Longleftrightarrow \quad T > 1002 K`
    - :math:`o\_dif` Oxygen diffusivity :math:`\left[ \frac{cm^2}{s} \right]`:

        :math:`o\_dif\left(T\right) = \displaystyle1.07 \cdot 10^{-2} \cdot \exp{\left(- 49229 /\left(RT\right) \right)}`
    - :math:`o\_pp` Oxygen partial pressure divided by Oxygen concentration squared :math:`\left[ \frac{atm}{wt.\%^2} \right]`:

        :math:`o\_pp\left(T\right) = \displaystyle \left( \frac{M}{M_O} \right)^2 \cdot 10^{ 2 /\left(2.3 \cdot R\right) \cdot \left( - 101098 / T + 15.66 \right) }`, :math:`\quad` where:

        :math:`M_O = 16 \frac{g}{mol} \quad` Oxygen molecular mass

where :math:`T` is the bismuth temperature in :math:`\left[K\right]`, :math:`p` is the bismuth pressure in :math:`\left[Pa\right]` and
:math:`R` is the molar gas constant in :math:`\left[J/(mol K)\right]`.

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
