============
Introduction
============

lbh15 (**L**\ ead **B**\ ismtuh **H**\ andbook 20 **15**) is a Python library that implements the
thermo-physical properties of lead, bismuth and lead-bismuth eutectic (lbe) metal alloy available from
the well known handbook edited by OECD/NEA :cite:`Agency2015`: 
`oecd-nea.org <https://www.oecd-nea.org/jcms/pl_14972/handbook-on-lead-bismuth-eutectic-alloy-and-lead-properties-materials-compatibility-thermal-hydraulics-and-technologies-2015-edition?details=true>`_
. The properties implemented in the package are listed in table :ref:`table_properties`

.. _table_properties:
.. list-table:: lbh15 properties from :cite:`Agency2015`
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

The dimensionless Prandtl number (:math:`Pr`) can be quaried as instance attribute as well.

All properties are given at atmospheric pressure (:math:`101325` :math:`[Pa]`) and the correlations'
validity range is checked at evaluation raising a warning in case it is not satisfied (see :ref:`Examples` for more details).
We also provide an example of instantiation using a target property value, see section :ref:`Initialization from properties` 
for instance. The correlations are reported in the doctring documentation for sake of completeness.

Go to :ref:`Documentation` to see full package documentation.

lbh15 is released under the GNU General Public License 3 (see :any:`License`).


=================
Project Structure
=================
The project is organized in the following folder structure:

.. code:: bash

  <lbh15 parent folder>
    ├── lbh15/
    ├── docs/
    ├── tests/
    ├── LICENSE
    ├── MANIFEST.in
    ├── README.rst

- lbh15: contains all modules, classes and methods implemented in lbh15
- docs: contains materials for the generation of the documentation (Sphinx v5.1.0)
- tests: collection of tests used to verify correct implementation

===========
Dependences
===========

- Python 3.8.10
- scipy 1.8.1

============
Installation
============
To install the package lbh15 simply type the following command:

  .. code-block:: bash

      pip install lbh15

Or download the package at ###LINK###. After downloading the package on disk, 
execute the following command inside the base folder:

  .. code-block:: bash

      pip install .


The documenation can be built both in html and latex. To do that execute the following command in
package docs folder:
 
  .. code-block:: bash

      sphinx-build -b html . <dest_dir>
 
  .. code-block:: bash

      sphinx-build -b latex . <dest_dir>

.. _Examples:

========
Examples
========
This section shows a fex example of basic lbh25 usage.

- Create an instance :class:`.Lead` object with temperature in Celsius
  and print its dynamic viscosity:
  
  >>> from scipy.constants import convert_temperature
  >>> from lbh15 import Lead
  >>> # Initialize Lead object with T=395 Celsius
  >>> liquid_lead = Lead(T=convert_temperature(395.0, 'C', 'K'))
  >>> # Print lead dynamic viscosity in [Pa*s]
  >>> liquid_lead.mu
  0.0022534948395446985

- Request property outside its range of validity. In this example :class:`.Lead` object is initialized
  using a temperature value that is outside surface tension validity range:

  >>> from lbh15 import Lead
  >>> liquid_lead = Lead(T=1400.0)
  >>> liquid_lead.sigma
  <stdin>:1: UserWarning: The surface tension is requested at temperature value of 1400.00 K that is not in validity range [600.60, 1300.00] K
  0.3676999999999999


.. _Initialization from properties:

+++++++++++++++++++++++++++++++++++++++++++++++
Initialization from properties - *experimental*
+++++++++++++++++++++++++++++++++++++++++++++++

The lbh15 package gives the possibility to instantiate a liquid metal properties object just knowing one of its
properties (see :class:`.Lead`, :class:`.Bismuth` and :class:`.LBE` documentation for the full list). 
This is accomplished by finding the root of the function used to calculate the target property value.
This functionality is marked as *experimental* since it depends on the specific mathematical formulation of 
property correlations that are implemented in lbh15. The authors cannot guarantee its correct behaviour if 
such implementations are changed by the user.

- Initialize :class:`.LBE`, i.e., lead-bismuth-eutectic object knowing its density
  and retrieve the corresponding temperature in Kelvin:

  >>> from lbh15 import LBE
  >>> # Initialize LBE with rho=9800 [kg/m^3]
  >>> liquid_lbe = LBE(rho=9800)
  >>> # Print lbe temperature in [K]
  >>> liquid_lbe.T
  978.3449342614078

- Use other liquid metal objects to compare properties at a given temperature. In this 
  example :class:`.Lead` object is initialized knowing the conductivity value :math:`k`, then its temperature in Kelvin
  is used to initialize a :class:`.Bismuth` object. Finally, the conductivity of the bismuth object is printed for comparison:

  >>> from lbh15 import Lead
  >>> from lbh15 import Bismuth
  >>> # Inititialize Lead with k=17.37 [W/(m*K)]
  >>> liquid_lead = Lead(k=17.37)
  >>> # Initialize Bismuth with Lead temperature in K
  >>> liquid_bismuth = Bismuth(liquid_lead.T)
  >>> # Print bismuth conductivity
  >>> liquid_bismuth.k
  14.395909090909093

- Initialization from specific heat capacity needs some attention because the corresponding function of temperature is not injective, 
  hence for some values of :math:`c_p` two values of temperature are mapped. This is an undesired
  behaviour. To overcome such difficulty the package provides the possibility to the user to choose if the high or
  low range of cp values shall be considered, i.e., the one at the left or at the right of the function minimum. The following example
  shows its usage with :class:`.Lead` (the same is valid for :class:`.Bismuth` and :class:`.LBE`):

  >>> from lbh15 import Lead
  >>> # Visualize temperature in [K] corresponding to cp min
  >>> Lead.T_at_cp_min()
  1342.753
  >>> # Visualize minimum value of cp in [J/(kg*K)]
  >>> Lead.cp_min()
  136.348649
  >>> # Initialize two objects with cp, one for the low range and one for the high range
  >>> lead_cp_1 = Lead(cp=136.6, cp_high_range=False)
  >>> lead_cp_2 = Lead(cp=136.6, cp_high_range=True)
  >>> # Print their temperatures in [K]
  >>> lead_cp_1.T, lead_cp_1.T
  (1437.4148683655994, 1699.1573335323235)


.. _Documentation:

=============
Documentation
=============
.. only:: html

  You can navigate the full documentation of package:

.. toctree::
   :maxdepth: 3

   documentation.rst


==============
Aknowledgments
==============
The authors are very thankful to `Juan José Gómez Romera <jjgomera@gmail.com>`_ who mantains `iapws <https://iapws.readthedocs.io/en/latest/>`_
Python package, since they took inspiration from his work to develop the lbh15 package.
