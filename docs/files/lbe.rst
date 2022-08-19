lbh15.lbe module
=================
Module with liquid lead-bismuth-eutectic (LBE) class.
LBE object can be initialized with the temperature
or with one of the available properties (see :class:`.LBE` for
the full list). It must be underlined that instantiation from properties
depends on the specific correlation of the properties implemented in
lbh15 package. In addition to the class attributes that are shown
in this section, :class:`.LBE` class dynamically adds the properties
implemented in :py:mod:`lbh15.properties.lbe_properties` module. For instance:

>>> from lbh15 import LBE
>>> liquid_lbe = LBE(T=668.15)
>>> liquid_lbe.k
13.058977206137499

Therefore the object comes with the following default properties:

    - :math:`T_{m0}` lbe melting temperature:

        :math:`398.0 [K]`
    - :math:`Q_{m0}` lbe melting latent heat:

        :math:`38.6\cdot10^3 \Big[\frac{J}{kg}\Big]`
    - :math:`T_{b0}` lbe boiling temperature:

        :math:`1927 [K]`
    - :math:`Q_{b0}` lbe vaporisation heat:

        :math:`856.6\cdot10^3 \Big[\frac{J}{kg}\Big]`
    - :math:`p_s` lbe saturation vapour pressure :math:`[Pa]`:

        :math:`p_s(T) = \displaystyle1.22\cdot10^{10}\cdot
        \exp{\Big(-22852/T\Big)}`
    - :math:`\sigma` lbe surface tension
      :math:`\Big[\frac{N}{m}\Big]`:

        :math:`\sigma(T) = \displaystyle\Big(448.5
        - 0.0799{\cdot}T\Big)\cdot10^{-3}`
    - :math:`\rho` lbe density
      :math:`\Big[\frac{kg}{m^3}\Big]`:

        :math:`\rho(T) = \displaystyle11065 - 1.293{\cdot}T`
    - :math:`\alpha` lbe thermal expansion coefficient
      :math:`\Big[\frac{1}{K}\Big]`:

        :math:`\alpha(T) = \displaystyle\Big(8558 - T\Big)^{-1}`
    - :math:`u_s` speed of sound in lbe
      :math:`\Big[\frac{m}{s}\Big]`:

        :math:`u_s(T) = \displaystyle1855 - 0.212{\cdot}T`
    - :math:`\beta_s` lbe isentropic compressibility
      :math:`\Big[\frac{1}{Pa}\Big]`:

        :math:`\beta_s(T) = \displaystyle\frac{1}{\rho(T){\cdot}u_s(T)^2}`
    - :math:`c_p` lbe specific heat capacity
      :math:`\Big[\frac{J}{kg{\cdot}K}\Big]`:

        :math:`c_p(T) = \displaystyle164.8 - 3.94\cdot10^{-2}{\cdot}T
        + 1.25\cdot10^{-5}{\cdot}T^2 - 4.56\cdot10^{5}{\cdot}T^{-2}`
    - :math:`h` lbe specific enthalpy (as difference with
      respect to the melting point enthalpy)
      :math:`\Big[\frac{J}{kg{\cdot}K}\Big]`:

        :math:`h(T) = \displaystyle
        164.8\cdot\Big(T - T_{m0}\Big)
        - 1.97\cdot10^{-2}\Big(T^2 - T_{m0}^2\Big)
        + 4.167\cdot10^{-6}\Big(T^3 - T_{m0}^3\Big)`

        :math:`\qquad\qquad- 4.56\cdot10^5\Big(T^{-1} - T_{m0}^{-1}\Big)`
    - :math:`\mu` lbe dynamic visocity :math:`[Pa{\cdot}s]`:

        :math:`\mu(T) = \displaystyle4.94\cdot10^{-4}\cdot
        \exp{\Big(754.1/T\Bigg)}`
    - :math:`r` lbe electrical resistivity :math:`[\Omega{\cdot}m]`:

        :math:`r(T) = \displaystyle\Big(90.9 + 0.048{\cdot}T\Big)
        \cdot10^{-8}`
    - :math:`k` lbe thermal conductivity
      :math:`\Big[\frac{W}{m{\cdot}K}\Big]`:

        :math:`k(T) = \displaystyle3.284 + 1.617\cdot10^{-2}{\cdot}T
        - 2.305\cdot10^{-6}{\cdot}T^2`
    - :math:`Pr` Prandtl number :math:`[-]`:

        :math:`Pr = \displaystyle\frac{c_p\cdot\mu}{k}`

where :math:`T` is the lbe temperature in :math:`[K]`.

Finally, the object dynamically adds useful
methods to retrieve more information on specific thermophysical property
which are named :code:`<property_name>_info`. For instance:

>>> from lbh15 import LBE
>>> liquid_lbe = LBE(T=668.15)
>>> liquid_lbe.k_info()
k:
        Value: 13.0590 [W/(m*K)]
        Validity range: [398.00, 1100.00] K
        Long name: thermal conductivity
        Units: [W/(m*K)]
        Description:
                Liquid lbe thermal conductivity

.. automodule:: lbh15.lbe
    :members:
    :member-order: bysource
    :inherited-members:
   
