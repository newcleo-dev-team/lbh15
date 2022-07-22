======
lbeh15
======

lbeh15 is a python library that models properties of liquid metals: lead, bismuth and lead-bismuth eutectic (lbe).
Properties are taken from "Handbook on Lead-bismuth Eutectic Alloy and Lead Properties, Materials Compatibility, Thermal-hydraulics and Technologies"
(see :cite:p:`Agency2015`). The following properties are provided: 

.. list-table:: lbeh15 Properties
   :widths: 50 25 25
   :header-rows: 1

   * - Property
     - Symbol
     - Units
   * - Melting temperature
     - :math:`T_{m0}`
     - :math:`[K]`
   * - Melting latent heat
     - :math:`Q_{m0}`
     - :math:`[J/kg]`
   * - Boiling temperature
     - :math:`T_{b0}`
     - :math:`[K]`
   * - Vaporisation heat
     - :math:`Q_{b0}`
     - :math:`[J/kg]`
   * - Saturation vapour pressure
     - :math:`p_s`
     - :math:`[Pa]`
   * - Surface tension
     - :math:`\sigma`
     - :math:`[N/m]`
   * - Density
     - :math:`\rho`
     - :math:`[kg/m^3]`
   * - Thermal expansion coefficient
     - :math:`\alpha`
     - :math:`[kg/m^3]`
   * - Speed of sound
     - :math:`u_s`
     - :math:`[m/s]`
   * - Isentropic compressibility
     - :math:`\beta_s`
     - :math:`[1/Pa]`
   * - Specific heat capacity
     - :math:`c_p`
     - :math:`[J/(kg{\cdot}K)]`
   * - Specific enthalpy
     - :math:`h`
     - :math:`[J/kg]`
   * - Dynamic viscosity
     - :math:`\mu`
     - :math:`[Pa{\cdot}s]`
   * - Electrical resistivity
     - :math:`r`
     - :math:`[{\Omega}{\cdot}m]`
   * - Thermal conductivity
     - :math:`\lambda`
     - :math:`[W/(m{\cdot}K)]`

All properties are computed at atmospheric pressure ( :math:`101325 [Pa]` ). Finally, 
it is possible to initialize an object knowing one of its properties (see :ref:`Initialization from properties`
for more details)

Project Structure
*****************
The project is organized in the following folder structure:

.. code:: bash

  <lbeh15 parent folder>
    ├── lbeh15
    ├── docs

- lbeh15 folder: this folder collects all modules, classes and methods implemented in lbeh15
- docs: collection of material for the generation of the documentation


Examples
********
In this section some examples of lbeh15 usage are shown.

- Initialize :class:`lead.Lead` object with temperature in Celsius
  and print its dynamic viscosity:

  >>> import lbeh15.lead as lead
  >>> # Initialize Lead object with T=395 [degC]
  >>> lead_properties = lead.Lead(395.0, 'degC')
  >>> # Print lead dynamic viscosity in [Pa*s]
  >>> lead_properties.mi
  0.0022534948395446985

- Initialize :class:`lbe.LBERho`, i.e., lead-bismuth-eutectic object knowing its density
  and retrieve the corresponding temperature in Kelvin:

  >>> import lbeh15.lbe as lbe
  >>> # Initialize LBERho with rho=9800 [kg/m^3]
  >>> lbe_properties = lbe.LBERho(9800)
  >>> # Print lbe temperature in [K]
  >>> lbe_properties.T
  978.3449342614078

- Use other liquid metals object to compare properties at a given temperature. In this 
  example :class:`lead.LeadConductivity` object is initialized from its conductivity, then its temperature in Kelvin
  is used to initialize a :class:`bismuth.Bismuth` object, then its conductivity is printed as comparison:

  >>> import lbeh15.lead as lead
  >>> import lbeh15.bismuth as bismuth
  >>> # Inititialize LeadConductivity with conductivity=17.37 [W/(m*K)]
  >>> lead_properties = lead.LeadConductivity(17.37)
  >>> # Initialize Bismuth with LeadConductivity temperature in K
  >>> bismuth_properties = bismuth.Bismuth(lead_properties.T, 'K')
  >>> # Print bismuth conductivity
  >>> bismuth_properties.conductivity
  14.395909090909093


.. _Initialization from properties:

Initialization from properties
******************************

lbeh15 package gives the possibility to initialize a liquid metal properties object just knowing one of its
properties. This is accomplished by finding the root of the function used to calculate the target property value.
It follows that two main points must be underlined: 

- It is not possible to initialize objects from :math:`T_{m0}`, :math:`Q_{m0}`, :math:`T_{b0}` and :math:`Q_{b0}`
- Initialization from specific heat capacity is not trivial: specific heat capacity function is not injective, 
  this means that for some values of :math:`c_p` two values of temperature could be returned. This is an undesired
  behaviour. To overcome such difficulty the package provides the possibility to the user to choose if the first or
  second root shall be considered, i.e., the one at the left or at the right of the function minimum. An example follows:

  >>> import lbeh15.lead as lead
  >>> # Visualize temperature in [K] corresponding to cp min
  >>> lead.LeadCp.T_at_cp_min()
  1682.522
  >>> # Initialize two objects with low cp, one for the first and one for the second root
  >>> lead_cp_1 = lead.LeadCp(137.35, second_root=False)
  >>> lead_cp_2 = lead.LeadCp(137.35, second_root=True)
  >>> # Print their temperatures in [K]
  >>> lead_cp_1.T, lead_cp_2.T
  (1598.101345921492, 1768.3157244316133)

  This is true for all the three liquid metals inside the package. 
