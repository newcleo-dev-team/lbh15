============
Introduction
============

lbh15 (**L**\ ead **B**\ ismuth **H**\ andbook 20\ **15**) is a Python package that implements the
thermo-physical properties of lead, bismuth and lead-bismuth eutectic (lbe) metal alloy available from
the well known handbook edited by OECD/NEA :cite:`Agency2015`: 
`oecd-nea.org <https://www.oecd-nea.org/jcms/pl_14972/handbook-on-lead-bismuth-eutectic-alloy-and-lead-properties-materials-compatibility-thermal-hydraulics-and-technologies-2015-edition?details=true>`_
. The properties implemented in the package are listed in table :numref:`tableprop`

.. list-table:: lbh15 properties from :cite:`Agency2015`
   :widths: 50 25 25
   :name: tableprop
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
     - :math:`[1/K]`
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

The dimensionless Prandtl number (:math:`Pr`) can be queried as instance attribute as well.

All properties are given at atmospheric pressure (:math:`101325` :math:`[Pa]`) and the correlations'
validity range is checked at evaluation raising a warning in case it is not satisfied (see :ref:`Basic usage` for more details).
We also provide some examples of instantiation using a target property value, see section :ref:`Initialization from properties` 
for instance. The correlations are reported in the doctring documentation for sake of completeness.
The implementation strategy is fully object oriented, that guarantees both an easy package maintainability
and customization (see :ref:`Advanced usage`).

Go to :ref:`Documentation` to see full package documentation.

lbh15 is released under the GNU Lesser General Public License 3 (see :any:`License`).


=================
Project Structure
=================
The project is organized in the following folder structure:

.. code:: text

  <lbh15 parent folder>
    ├── docs/
    ├── lbh15/
    ├── tests/
    ├── LICENSE
    ├── MANIFEST.in
    ├── README.rst
    └── setup.py
    

- lbh15: contains all modules, classes and methods implemented in lbh15
- docs: contains materials for the generation of the documentation (Sphinx v5.1.0)
- tests: collection of tests used to verify correct implementation

===========
Dependencies
===========

- Python 3.8.10
- scipy 1.8.1

============
Installation
============
To install the package lbh15 simply type the following command:

  .. code-block:: bash

      pip install lbh15

Or cloning the package at http://172.16.10.46/gitlab-instance-c126a35e/lbh15.git. 
After cloning the package, execute the following command inside the base folder:

  .. code-block:: bash

      pip install .


The documentation can be built both in html and latex. To do that execute the following command in
package docs folder:
 
  .. code-block:: bash

      make html
 
  .. code-block:: bash

      make latex
      cd _build/latex
      latexmk -pdf -f

.. _Examples:

========
Examples
========

Some examples of lbh15 usage and possible package customization.
More examples can be found in :class:`.Lead`, :class:`.Bismuth` and :class:`.LBE`

.. _Basic usage:

+++++++++++
Basic usage
+++++++++++

This section shows a few example of basic lbh15 usage.

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


- Get synthetic information liquid metal using :code:`__repr__` (:code:`__str__` is implemented as well):

  >>> from lbh15 import Lead
  >>> liquid_lead = Lead(T=1000)
  >>> repr(liquid_lead)
  'Lead(T=1000.00, alpha=1.26e-04, beta_s=3.38e-11, cp=140.89, h=57656.86, k=20.20, mu=1.33e-03, p_s=1.41, r=1.14e-06, rho=10161.50, sigma=0.41, u_s=1707.00)'



.. _Initialization from properties:

+++++++++++++++++++++++++++++++++++++++++++++++
Initialization from properties - *experimental*
+++++++++++++++++++++++++++++++++++++++++++++++

The lbh15 package gives the possibility to instantiate a liquid metal properties object just knowing one of its
properties (see :class:`.Lead`, :class:`.Bismuth` and :class:`.LBE` documentation for the full list). 
This is accomplished by finding the root of the function used to calculate the target property value.
This functionality is marked as *experimental* since it depends on the specific mathematical formulation of 
property correlations that are implemented in lbh15. The authors cannot guarantee its correct behaviour if 
such implementations are changed by the user, or if new properties with non injective correlations are implemented
(see :ref:`Advanced usage` section). 

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
  behaviour. To overcome such difficulty the package provides the possibility for the user to choose which temperature root
  shall be considered, by providing the index of the function inversion solution array. The default root index is 0, i.e, the lowest temperature.
  The following example shows its usage with :class:`.Lead` (the same is valid for :class:`.Bismuth` and :class:`.LBE`):

  >>> from lbh15 import Lead
  >>> # Visualize temperature in [K] corresponding to cp min
  >>> Lead.T_at_cp_min() # sobolev2011 correlation
  1568.665
  >>> # Visualize minimum value of cp in [J/(kg*K)]
  >>> Lead.cp_min() # sobolev2011 correlation
  136.348649
  >>> # Initialize first object with default index
  >>> lead_cp_1 = Lead(cp=136.6)
  >>> # Change default cp index for selecting second root, root_index=1
  >>> Lead.set_root_to_use('cp', root_index=1)
  >>> # Initialize second object
  >>> lead_cp_2 = Lead(cp=136.6)
  >>> # Print their temperatures in [K]
  >>> lead_cp_1.T, lead_cp_2.T
  (1437.4148683663843, 1699.1573335323235)


.. _Advanced usage:

++++++++++++++
Advanced usage
++++++++++++++

In this section the capability of the package to be easily customised is shown.

- The following example shows how to define a custom correlation for liquid lead density and use it instead 
  of the package default one. First inspect available correlations (if only one correlation is available in :cite:`Agency2015`, 
  :code:`lbh15` is used as correlation name):
  
  >>> from lbh15 import Lead
  >>> Lead.correlations_available()
  {'alpha': 'lbh15', 'beta_s': 'lbh15', 'cp': ['gurvich1991', 'sobolev2011'], 'h': 'lbh15', 'k': 'lbh15', 'mu': 'lbh15', 'p_s': 'lbh15', 'r': 'lbh15', 'rho': 'lbh15', 'sigma': 'lbh15', 'u_s': 'lbh15'}
  
  The new property must be implemented in :py:mod:`lbh15.properties.lead_properties`:

  .. code-block:: python

    class rho_custom_corr(PropertyInterface):
        def __init__(self):
            super().__init__()
            self._range = [T_m0, T_b0]
            self._units = "[kg/m^3]"
            self._name = "rho"
            self._long_name = "custom density"
            self._description = "Liquid lead " + self._long_name
            self._correlation_name = "custom2022"
            self._is_injective = True

        def correlation(self, T):
            return 11400 - 1.2*T

  After having re-installed the package, check that the new correlation is correctly available:

  >>> from lbh15 import Lead
  >>> Lead.correlations_available()
  {'alpha': 'lbh15', 'beta_s': 'lbh15', 'cp': ['gurvich1991', 'sobolev2011'], 'h': 'lbh15', 'k': 'lbh15', 'mu': 'lbh15', 'p_s': 'lbh15', 'r': 'lbh15', 'rho': ['lbh15', 'custom2022'], 'sigma': 'lbh15', 'u_s': 'lbh15'}

  It is possible to notice that :code:`rho` has two correlations: default :code:`lbh15` and the new :code:`custom2022`.
  Since two options are available, it is mandatory to specify which one shall be used, otherwise the second one 
  will be used. Here it is how to use it:

  >>> # Use default one
  >>> Lead.set_correlation_to_use('rho', 'lbh15')
  >>> # Get an instance of Lead object at T=1000 K
  >>> liquid_lead_1 = Lead(T=1000)
  >>> # Print info about rho
  >>> liquid_lead_1.rho_info()
  rho:
        Value: 10161.50 [kg/m^3]
        Validity range: [600.60, 2021.00] K
        Correlation name: 'lbh15'
        Long name: density
        Units: [kg/m^3]
        Description:
                Liquid lead density
  >>> # Use the custom implementation of density
  >>> Lead.set_correlation_to_use('rho', 'custom2022')
  >>> # Get another instance of Lead object with new rho
  >>> liquid_lead_2 = Lead(T=1000)
  >>> # Print info about rho
  >>> liquid_lead_2.rho_info()
  rho:
        Value: 10200.00 [kg/m^3]
        Validity range: [600.60, 2021.00] K
        Correlation name: 'custom2022'
        Long name: custom density
        Units: [kg/m^3]
        Description:
                Liquid lead custom density


- lbh15 gives also the possibility to add brand new properties to liquid metal objects. The user
  must implement it in :py:mod:`lbh15.properties.lead_properties`. For instance, let's implement a property
  that is just the double of the temperature:

  .. code-block:: python

    class T_double(PropertyInterface):
      def __init__(self):
          super().__init__()
          self._range = [T_m0, T_b0]
          self._units = "[K]"
          self._name = "T_double"
          self._long_name = "double of the temperature"
          self._description = "Liquid lead " + self._long_name
          self._correlation_name = "double2022"
          self._is_injective = True

      def correlation(self, T):
          return 2*T

  After having re-installed the package the new property will be available with its name as 
  :class:`.Lead` attribute together with its info:

  >>> from lbh15 import Lead
  >>> # Initialization of lead object at T=750 K
  >>> liquid_lead = Lead(T=750)
  >>> # Get T_double
  >>> liquid_lead.T_double
  1500
  >>> # Get its info
  >>> liquid_lead.T_double_info()
  T_double:
          Value: 1500.00 [K]
          Validity range: [600.60, 2021.00] K
          Correlation name: 'double2022'
          Long name: double of the temperature
          Units: [K]
          Description:
                  Liquid lead double of the temperature

Each new property implemented by the user is also available for initialization. It is
worth to underline once again that package authors cannot guarantee correct execution of
such functionality for new implemented properties.

Another important remark is given about the usage of :code:`set_correlation_to_use` and :code:`set_root_to_use`:
those methods impact on class behaviour not only on instance one, therefore it is suggested to use them only if
completely aware of the implications.

.. _Documentation:

=============
Documentation
=============
.. only:: html

  You can navigate the full documentation of package:

.. toctree::
   :maxdepth: 3

   documentation.rst


===============
Acknowledgments
===============
The authors are very thankful to `Juan José Gómez Romera <jjgomera@gmail.com>`_ who maintains `iapws <https://iapws.readthedocs.io/en/latest/>`_
Python package, since they took inspiration from his work to develop the lbh15 package.
