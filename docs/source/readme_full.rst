============
Introduction
============

lbh15 (**L**\ ead **B**\ ismuth **H**\ andbook 20\ **15**) is a Python package that implements the
thermo-physical properties of lead, bismuth and lead-bismuth eutectic (lbe) metal alloy available from
the handbook edited by OECD/NEA :cite:`Agency2015`: 
`oecd-nea.org <https://www.oecd-nea.org/jcms/pl_14972/handbook-on-lead-bismuth-eutectic-alloy-and-lead-properties-materials-compatibility-thermal-hydraulics-and-technologies-2015-edition?details=true>`_
. The properties implemented in the package are listed in table :numref:`tableprop`.

.. list-table:: lbh15 properties from the handbook edited by OECD/NEA  
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
   * - Mass-specific heat capacity
     - :math:`c_p`
     - :math:`[J/(kg{\cdot}K)]`
   * - Mass-specific enthalpy
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

All properties are given at atmospheric pressure (:math:`101325` :math:`[Pa]`) by default and the correlations'
validity range is checked at evaluation, raising a warning in case it is not satisfied (see :ref:`Basic usage` for more details).
The pressure at which evaluate the properties can be specified at object's initialization.
We also provide some examples of instantiation using a target property value, see section :ref:`Initialization from properties` 
for instance. The correlations are also reported in the docstring documentation for sake of completeness.
The implementation is fully object-oriented to guarantee easy maintainability and customization of the package (see :ref:`Advanced usage`).

Go to :ref:`API Guide` to see the full code documentation.

lbh15 is released under the GNU Lesser General Public License 3 (see :any:`License`).


=================
Project Structure
=================
The project is organized according to the following folder structure:

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
- docs: contains materials for the generation of the documentation by Sphinx
- tests: collection of tests used to verify the correct implementation

============
Dependencies
============

- Python >=3.8.10
- Sphinx >=5.1.0
- SciPy >=1.8.1
- NumPy >=1.22.3

============
Installation
============
To install the package lbh15, type please the following command:

  .. code-block:: bash

      pip install lbh15

Or use https://github.com/newcleo-dev-team/lbh15.git to clone the package.
After cloning the package, execute the following command inside the base folder:

  .. code-block:: bash

      pip install .


The Sphinx documentation can be built in html and latex by executing
the following command in the folder ``docs/``:
 
  .. code-block:: bash

      make html
 
  .. code-block:: bash

      make latexpdf

.. _Examples:

========
Examples
========

This section contains some examples of basic usage and possible customization
of the package lbh15. More examples are available in
:class:`.Lead`, :class:`.Bismuth` and :class:`.LBE`.

.. _Basic usage:

+++++++++++
Basic usage
+++++++++++

This section shows a few examples of basic usage of lbh15.

- Create an instance :class:`.Lead` object with temperature in Celsius
  and print its dynamic viscosity:
  
  >>> from scipy.constants import convert_temperature
  >>> from lbh15 import Lead
  >>> # Initialize Lead object with T=395 Celsius
  >>> liquid_lead = Lead(T=convert_temperature(395.0, 'C', 'K'))
  >>> # Print lead dynamic viscosity in [Pa*s]
  >>> liquid_lead.mu
  0.0022534948395446985

- Create two instances of :class:`.Lead`, one at atmospheric pressure and one at twenty times the 
  atmospheric pressure. Then compare their density:

  >>> from lbh15 import Lead
  >>> from scipy.constants import atm
  >>> # Initialize first object, default pressure is atm
  >>> liquid_lead = Lead(T=800)
  >>> # Initialize the second object specifying the pressure
  >>> liquid_lead_2 = Lead(T=800, p=20*atm)
  >>> # Compare their density
  >>> liquid_lead.rho, liquid_lead_2.rho
  (10417.4, 10418.185181757714)

- Create an instance of :class:`.Lead` at a given temperature, than change it. Compare the conductivity
  value at the two temperatures:

  >>> from lbh15 import Lead
  >>> liquid_lead = Lead(T=750)
  >>> liquid_lead.k
  17.45
  >>> liquid_lead.T = 1200
  >>> liquid_lead.k
  22.4

- Request property outside its range of validity. In this example :class:`.Lead` object is initialized
  using a temperature value that is outside the range of physical validity of the surface tension
  correlation:

  >>> from lbh15 import Lead
  >>> liquid_lead = Lead(T=1400.0)
  >>> liquid_lead.sigma
  <stdin>:1: UserWarning: The surface tension is requested at temperature value of 1400.00 K that is not in validity range [600.60, 1300.00] K
  0.3676999999999999


- Get short information of the liquid metal using :code:`__repr__` (:code:`__str__` is also implemented offering a more detailed print):

  >>> from lbh15 import Lead
  >>> liquid_lead = Lead(T=1000)
  >>> repr(liquid_lead)
  'Lead(T=1000.00, alpha=1.26e-04, beta_s=3.38e-11, cp=140.89, h=57656.86, k=20.20, mu=1.33e-03, p_s=1.41, r=1.14e-06, rho=10161.50, sigma=0.41, u_s=1707.00)'



.. _Initialization from properties:

+++++++++++++++++++++++++++++++++++++++++++++++
Initialization from properties (*experimental*)
+++++++++++++++++++++++++++++++++++++++++++++++

The lbh15 package gives the possibility to instantiate an object with liquid metal properties by simply knowing the value of one of its
properties (see :class:`.Lead`, :class:`.Bismuth` and :class:`.LBE` documentation for the full list). 
This is accomplished by finding the root of the function matching the target property value. Such function, which constitutes a physical correlation, must be injective in the range considered for the root. Note that this is a necessary but not jointly sufficient condition to find a single root for the function. Since the existence of a (single) root cannot be guaranteed for every correlation, this functionality is marked as *experimental*: we invite then the user to double-check the result (see :ref:`Advanced usage` section). 

- Initialize :class:`.LBE`, i.e., lead-bismuth-eutectic object knowing its density
  and retrieve the corresponding temperature in Kelvin:

  >>> from lbh15 import LBE
  >>> # Initialize LBE with rho=9800 [kg/m^3]
  >>> liquid_lbe = LBE(rho=9800)
  >>> # Print lbe temperature in [K]
  >>> liquid_lbe.T
  978.3449342614078

- Use other liquid metal objects to compare properties at a given temperature. In this 
  example :class:`.Lead` object is initialized using a value of the thermal conductivity :math:`k`; then, a :class:`.Bismuth` object is initialized using its temperature in Kelvin. Finally, the conductivity of the bismuth object is printed for comparison:

  >>> from lbh15 import Lead
  >>> from lbh15 import Bismuth
  >>> # Inititialize Lead with k=17.37 [W/(m*K)]
  >>> liquid_lead = Lead(k=17.37)
  >>> # Initialize Bismuth with Lead temperature in K
  >>> liquid_bismuth = Bismuth(liquid_lead.T)
  >>> # Print bismuth conductivity
  >>> liquid_bismuth.k
  14.395909090909093

- Initialization from mass-specific heat capacity :math:`c_p` needs some attention because the corresponding function of temperature is not injective.
  Hence, two temperature values may be possible for the same value of :math:`c_p`. This occurrence must be handled carefully.
  Currently, the package allows the user to look for the root in the two distinct ranges where the function is monotone.
  The default range index is 0, which corresponds to the lowest temperature range.
  Here is an example with :class:`.Lead` (the same holds for :class:`.Bismuth` and :class:`.LBE`):

  >>> from lbh15 import Lead
  >>> from lbh15 import lead_properties
  >>> # Get an instance of cp property, sobolev2011 correlation
  >>> cp = lead_properties.cp_sobolev2011()
  >>> # Compute correlation bounds (min, max, T_at_min, T_at_max)
  >>> cp.compute_bounds()
  >>> # Visualize temperature in [K] corresponding to cp min
  >>> cp.T_at_min
  1568.664780487
  >>> # Visualize minimum value of cp in [J/(kg*K)]
  >>> cp.min
  136.34864915749822
  >>> # Initialize first object with default index
  >>> lead_cp_1 = Lead(cp=136.6)
  >>> # Change default cp index for selecting second root, root_index=1
  >>> Lead.set_root_to_use('cp', root_index=1)
  >>> # Initialize second object
  >>> lead_cp_2 = Lead(cp=136.6)
  >>> # Print their temperatures in [K]
  >>> lead_cp_1.T, lead_cp_2.T
  (1437.4148683663843, 1699.1573335324128)


.. _Advanced usage:

++++++++++++++
Advanced usage
++++++++++++++

Advanced usage comprises the possibility of adding new properties and physical correlations as follows.

- This example shows how to define a custom correlation for the liquid lead density that 
  does not depend on pressure and use it instead of the default one (the same holds :class:`.Bismuth` and :class:`.LBE`).
  The names of the available correlations can be queried by a simple function call
  (the generic name :code:`lbh15` is used in case the correlation's name is not specified in the
  reference handbook :cite: `Agency2015`):
  
  >>> from lbh15 import Lead
  >>> Lead.correlations_available()
  {'alpha': 'lbh15', 'beta_s': 'lbh15', 'cp': ['gurvich1991', 'sobolev2011'], 'h': 'sobolev2011', 'k': 'lbh15', 'mu': 'lbh15', 'p_s': 'sobolev2011', 'r': 'lbh15', 'rho': 'sobolev2008a', 'sigma': 'jauch1986', 'u_s': 'sobolev2011'}
  
  Implement the new property in :code:`<execution_dir>/custom_property/custom_density.py` as:

  .. code-block:: python

    from scipy.constants import atm
    from lbh15.properties.interface import PropertyInterface
    from lbh15.properties.interface import range_warning

    class rho_custom_corr(PropertyInterface):
      @range_warning
      def correlation(self, T, p=atm, verbose=False):
          "Implement here the user-defined correlation."
          return 11400 - 1.2*T

      @property
      def range(self):
          return [700.0, 1900.0]

      @property
      def units(self):
          return "[kg/m^3]"

      @property
      def name(self):
          return "rho"

      @property
      def long_name(self):
          return "custom density"

      @property
      def description(self):
          return "Liquid lead " + self.long_name

      @property
      def correlation_name(self):
          return "custom2022"

  .. note:: It is mandatory to override the method ``correlation`` and the properties ``range``, ``units``, ``long_name`` and ``description``.

  .. note:: It is strongly recommended to use decorator ``@range_warning`` so that correlation range is checked when property is queried as liquid metal property and wanrings is preinted as in :ref:`Basic usage`

  Provided that the execution is performed in :code:`<execution_dir>`, one can check the correct implementation as follows:

  >>> from lbh15 import Lead
  >>> import os
  >>> Lead.set_custom_properties_path(os.getcwd() + 'custom_property/custom_density.py')
  >>> Lead.correlations_available()
  {'alpha': 'lbh15', 'beta_s': 'lbh15', 'cp': ['gurvich1991', 'sobolev2011'], 'h': 'sobolev2011', 'k': 'lbh15', 'mu': 'lbh15', 'p_s': 'sobolev2011', 'r': 'lbh15', 'rho': ['sobolev2008a','custom2022'], 'sigma': 'jauch1986', 'u_s': 'sobolev2011'}

  It is possible to see that now there are two correlations possible for the density :code:`rho`: :code:`sobolev2008a` and :code:`custom2022`.
  If the density correlation is not specified for a new object instantiation, the last one in the list will be selected as default:

  >>> # Use default one
  >>> Lead.set_correlation_to_use('rho', 'sobolev2008a')
  >>> # Get an instance of Lead object at T=1000 K
  >>> liquid_lead_1 = Lead(T=1000)
  >>> # Print info about rho
  >>> liquid_lead_1.rho_info()
  rho:
        Value: 10161.50 [kg/m^3]
        Validity range: [600.60, 2021.00] K
        Correlation name: 'sobolev2008a'
        Long name: density
        Units: [kg/m^3]
        Description:
                Liquid lead density
  >>> # Use the custom implementation of density
  >>> Lead.set_correlation_to_use('rho', 'custom2022')
  >>> # Get another instance of Lead object with new rho
  >>> liquid_lead_2 = Lead(T=1000)
  >>> # Compare the density of the two objects
  >>> liquid_lead_1.rho, liquid_lead_2.rho
  (10161.5 10200.0)
  >>> # Print full info about density of second instance
  >>> liquid_lead_2.rho_info()
  rho:
        Value: 10200.00 [kg/m^3]
        Validity range: [700.00, 1900.00] K
        Correlation name: 'custom2022'
        Long name: custom density
        Units: [kg/m^3]
        Description:
                Liquid lead custom density

  It is also possible to change the correlation used by a liquid metal object instance calling the method :code:`change_correlation_to_use`.

- lbh15 gives also the possibility to add new properties to the liquid metal objects. For 
  instance, let's implement a property that is simply the double of the temperature in :code:`<execution_dir>/custom_property/double_T.py`:

  .. code-block:: python

    from scipy.constants import atm
    from lbh15.properties.interface import PropertyInterface
    from lbh15.properties.interface import range_warning

    class T_double(PropertyInterface):
      @range_warning
      def correlation(self, T, p=atm, verbose=False):
          "Return the temperature value multiplied by 2."
          return 2*T

      @property
      def range(self):
          return [700.0, 1900.0]

      @property
      def units(self):
          return "[K]"

      @property
      def name(self):
          return "T_double"

      @property
      def long_name(self):
          return "double of the temperature"

      @property
      def description(self):
          return "Liquid lead " + self.long_name

      @property
      def correlation_name(self):
          return "double2022"

  The new custom property can be set as :class:`.Lead` attribute by using the filepath to its module:

  >>> from lbh15 import Lead
  >>> import os
  >>> Lead.set_custom_properties_path(os.getcwd() + 'custom_property/double_T.py')
  >>> # Initialization of lead object at T=750 K
  >>> liquid_lead = Lead(T=750)
  >>> # Get T_double
  >>> liquid_lead.T_double
  1500
  >>> # Get its info
  >>> liquid_lead.T_double_info()
  T_double:
          Value: 1500.00 [K]
          Validity range: [700.00, 1900.00] K
          Correlation name: 'double2022'
          Long name: double of the temperature
          Units: [K]
          Description:
                  Liquid lead double of the temperature

  Each new property implemented by the user is also available at initialization.

.. note:: The filepaths used here must be absolute.

.. _API Guide:

=========
API Guide
=========
.. only:: html

  This section provides the guide for the application programming interface.

.. toctree::
   :maxdepth: 2

   documentation.rst
