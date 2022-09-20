lbh15.bismuth module
====================
Module with liquid bismuth class.
Bismuth object can be initialized with the temperature
or with one of the available properties (see :class:`.Bismuth` for
the full list). It must be underlined that instantiation from properties
depends on the specific correlation of the properties implemented in
lbh15 package. In addition to the class attributes that are shown
in this section, :class:`.Bismuth` class dynamically adds the properties
implemented in :py:mod:`lbh15.properties.bismuth_properties` module. For instance:

>>> from lbh15 import Bismuth
>>> liquid_bismuth = Bismuth(T=668.15)
>>> liquid_bismuth.rho
9909.857

Therefore the object comes with the following default properties:

    - :math:`T_{m0}` bismuth melting temperature:

        :math:`544.6 [K]`
    - :math:`Q_{m0}` bismuth melting latent heat:

        :math:`53.3\cdot10^3 \Big[\frac{J}{kg}\Big]`
    - :math:`T_{b0}` bismuth boiling temperature:

        :math:`1831 [K]`
    - :math:`Q_{b0}` bismuth vaporisation heat:

        :math:`856.2\cdot10^3 \Big[\frac{J}{kg}\Big]`
    - :math:`p_s` bismuth saturation vapour pressure :math:`[Pa]`:

        :math:`p_s(T) = \displaystyle2.67\cdot10^{10}\cdot
        \exp{\Big(-22858/T\Big)}`
    - :math:`\sigma` bismuth surface tension
      :math:`\Big[\frac{N}{m}\Big]`:

        :math:`\sigma(T) = \displaystyle\Big(420.8
        - 0.081{\cdot}T\Big)\cdot10^{-3}`
    - :math:`\rho` bismuth density \
      :math:`\Big[\frac{kg}{m^3}\Big]`:

        :math:`\rho(T) = \displaystyle10725 - 1.22{\cdot}T`
    - :math:`\alpha` bismuth thermal expansion coefficient
      :math:`\Big[\frac{1}{K}\Big]`:

        :math:`\alpha(T) = \displaystyle\Big(8791 - T\Big)^{-1}`
    - :math:`u_s` speed of sound in bismuth
      :math:`\Big[\frac{m}{s}\Big]`:

        :math:`u_s(T) = \displaystyle1616 + 0.187{\cdot}T
        - 2.2\cdot10^{-4}{\cdot}T`
    - :math:`\beta_s` bismuth isentropic compressibility
      :math:`\Big[\frac{1}{Pa}\Big]`:

        :math:`\beta_s(T) = \displaystyle\frac{1}{\rho(T){\cdot}u_s(T)^2}`
    - :math:`c_p` bismuth specific heat capacity
      :math:`\Big[\frac{J}{kg{\cdot}K}\Big]`:

        :math:`c_p(T) = \displaystyle118.2 - 5.934\cdot10^{-3}{\cdot}T
        + 7.183\cdot10^{6}{\cdot}T^{-2}`
    - :math:`h` bismuth specific enthalpy (as difference with
      respect to the melting point enthalpy)
      :math:`\Big[\frac{J}{kg{\cdot}K}\Big]`:

        :math:`h(T) = \displaystyle
        118.2\cdot\Big(T - T_{m0}\Big)
        + 2.967\cdot10^{-3}\Big(T^2 - T_{m0}^2\Big)
        - 7.183\cdot10^6\Big(T^{-1} - T_{m0}^{-1}\Big)`
    - :math:`\mu` bismuth dynamic viscosity :math:`[Pa{\cdot}s]`:

        :math:`\mu(T) = \displaystyle4.456\cdot10^{-4}\cdot
        \exp{\Big(780/T\Big)}`
    - :math:`r` bismuth electrical resistivity :math:`[\Omega{\cdot}m]`:

        :math:`r(T) = \displaystyle\Big(98.96 + 0.0554{\cdot}T\Big)
        \cdot10^{-8}`
    - :math:`k` bismuth thermal conductivity \
      :math:`\Big[\frac{W}{m{\cdot}K}\Big]`:

        :math:`k(T) = \displaystyle7.34 + 9.5\cdot10^{-3}{\cdot}T`
    - :math:`Pr` Prandtl number :math:`[-]`:

        :math:`Pr = \displaystyle\frac{c_p\cdot\mu}{k}`

where :math:`T` is the bismuth temperature in :math:`[K]`.

Finally, the object dynamically adds useful
methods to retrieve more information on specific thermophysical property
which are named :code:`<property_name>_info`. For instance:

>>> from lbh15 import Bismuth
>>> liquid_bismuth = Bismuth(T=668.15)
>>> liquid_bismuth.rho_info()
rho:
        Value: 9909.8570 [kg/m^3]
        Validity range: [544.60, 1831.00] K
        Long name: density
        Units: [kg/m^3]
        Description:
                Liquid bismuth density

.. automodule:: lbh15.bismuth
    :members:
    :member-order: bysource
    :inherited-members:
