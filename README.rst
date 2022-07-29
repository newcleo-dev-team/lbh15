============
Introduction
============

lbeh15 is a python library that models properties of liquid metals: lead, bismuth and lead-bismuth eutectic (lbe).
Properties are taken from "Handbook on Lead-bismuth Eutectic Alloy and Lead Properties, Materials Compatibility, Thermal-hydraulics and Technologies"
(see :cite:p:`Agency2015`). The following properties are provided: 

.. list-table:: lbeh15 properties from (:cite:p:`Agency2015`)
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
     - :math:`k`
     - :math:`[W/(m{\cdot}K)]`

Additional properties are provided as well:

.. list-table:: lbeh15 additional properties
   :widths: 50 25 25
   :header-rows: 1

   * - Property
     - Symbol
     - Units
   * - Prandtl number
     - :math:`Pr`
     - :math:`[-]`

All properties are computed at atmospheric pressure ( :math:`101325 [Pa]` ) and for each of 
them the validty range of the correlation is provided as well. lbeh15 package warns
the user if it asks for a property that is computed with a temperature outside correlation validity range
see (see :ref:`Examples` for more details).Finally, it is possible to initialize an object knowing one of 
its properties (see :ref:`Initialization from properties` for more details).

Go to :ref:`Documentation` to see full package documentation.

lbeh15 is released under the GNU General Public License 3.

=================
Project Structure
=================
The project is organized in the following folder structure:

.. code:: bash

  <lbeh15 parent folder>
    ├── lbeh15
    ├── docs
    ├── tests

- lbeh15 folder: this folder collects all modules, classes and methods implemented in lbeh15
- docs: collection of material for the generation of the documentation
- tests: collection of scripts used to verify package correct implementation

===========
Dependences
===========

- python 3.x
- numpy-scipy: library with mathematic and scientific tools

============
Installation
============
  .. code-block:: bash

      pip install lbeh15

.. _Examples:

========
Examples
========
In this section some examples of lbeh15 usage are shown.

- Initialize :class:`lbeh15.lead.Lead` object with temperature in Celsius
  and print its dynamic viscosity:
  
  >>> from scipy.constants import convert_temperature
  >>> from lbeh15.lead import Lead
  >>> # Initialize Lead object with T=395 Celsius
  >>> liquid_lead = Lead(T=convert_temperature(395.0, 'C', 'K'))
  >>> # Print lead dynamic viscosity in [Pa*s]
  >>> liquid_lead.mu
  0.0022534948395446985

- Initialize :class:`lbeh15.lbe.LBE`, i.e., lead-bismuth-eutectic object knowing its density
  and retrieve the corresponding temperature in Kelvin:

  >>> from lbeh15.lbe import LBE
  >>> # Initialize LBE with rho=9800 [kg/m^3]
  >>> liquid_lbe = LBE(rho=9800)
  >>> # Print lbe temperature in [K]
  >>> liquid_lbe.T
  978.3449342614078

- Use other liquid metals object to compare properties at a given temperature. In this 
  example :class:`lbeh15.lead.Lead` object is initialized knowing conductivity value k, then its temperature in Kelvin
  is used to initialize a :class:`lbeh15.bismuth.Bismuth` object, finally its conductivity is printed as comparison:

  >>> from lbeh15.lead import Lead
  >>> from lbeh15.bismuth import Bismuth
  >>> # Inititialize Lead with k=17.37 [W/(m*K)]
  >>> liquid_lead = Lead(k=17.37)
  >>> # Initialize Bismuth with Lead temperature in K
  >>> liquid_bismuth = Bismuth(liquid_lead.T)
  >>> # Print bismuth conductivity
  >>> liquid_bismuth.k
  14.395909090909093

- Use property outside its range of validity. In this example :class:`lbeh15.lead.Lead` object is initialized
  using a temperature value that is outside surface tension validity range:

  >>> from lbeh15.lead import Lead
  >>> liquid_lead = Lead(1400.0)
  >>> liquid_lead.sigma
  <stdin>:1: UserWarning: Temperature 1400.00 is outside sigma range [600.60, 1300.00] K
  0.3676999999999999


.. _Initialization from properties:

==============================
Initialization from properties
==============================

lbeh15 package gives the possibility to initialize a liquid metal properties object just knowing one of its
properties. This is accomplished by finding the root of the function used to calculate the target property value.
It follows that two main points must be underlined:

- Initialization from specific heat capacity is not trivial: specific heat capacity function is not injective, 
  this means that for some values of :math:`c_p` two values of temperature could be returned. This is an undesired
  behaviour. To overcome such difficulty the package provides the possibility to the user to choose if the high or
  low range of cp values shall be considered, i.e., the one at the left or at the right of the function minimum. The following example
  shows its usage with :class:`lbeh15.bismuth.Bismuth` (the same is valid for :class:`lbeh15.lead.Lead` and :class:`lbeh15.lbe.LBE`):

  >>> from lbeh15.bismuth import Bismuth
  >>> # Visualize temperature in [K] corresponding to cp min
  >>> Bismuth.T_at_cp_min()
  1342.753
  >>> # Initialize two objects with low cp, one for the first and one for the second root
  >>> bismuth_cp_1 = Bismuth(cp=137.35, cp_high_range=False)
  >>> bismuth_cp_2 = Bismuth(cp=137.35, cp_high_range=True)
  >>> # Print their temperatures in [K]
  >>> bismuth_cp_1.T, bismuth_cp_2.T
  (1041.8294863232934 1771.2122382213047)


.. _Documentation:

=============
Documentation
=============

You can navigate the full documentation of package:

.. toctree::
   :maxdepth: 3

   documentation.rst
