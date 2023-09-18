============
Introduction
============

lbh15 (**L**\ ead **B**\ ismuth **H**\ andbook 20\ **15**) is a Python package that implements the
thermo-physical and thermo-chemical properties of lead, bismuth and lead-bismuth eutectic (lbe) metal alloy available from
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

The properties implemented in the updated package are listed in table :numref:`tablethermochemicalprop`.

.. list-table:: lbh15 thermochemical properties from the handbook edited by OECD/NEA  
   :widths: 50 25 25 25 25 25
   :name: tablethermochemicalprop
   :header-rows: 1

   * - Property
     - Symbol
     - Units
     - Lead
     - LBE
     - Bismuth
   * - Molar-specific enthalpy
     - :math:`H`
     - :math:`[J/mol]`
     - ✔
     - ✔
     - ✔
   * - Molar-specific entropy
     - :math:`S`
     - :math:`[J/(mol.K)]`
     - ✔
     - ✔
     - ✔
   * - Gibbs free energy
     - :math:`G`
     - :math:`[J/mol]`
     - ✔
     - ✔
     - ✔
   * - Lead chemical activity in LBE
     - :math:`\alpha_{Pb}`
     - :math:`[-]`
     - :math:`-`
     - ✔
     - :math:`-`
   * - Bismuth chemical activity in LBE
     - :math:`\alpha_{Bi}`
     - :math:`[-]`
     - :math:`-`
     - ✔
     - :math:`-`
   * - Iron solubility
     - :math:`S_{Fe}`
     - :math:`[wt.\%]`
     - ✔
     - ✔
     - ✔
   * - Nickel solubility
     - :math:`S_{Ni}`
     - :math:`[wt.\%]`
     - ✔
     - ✔
     - ✔
   * - Chromium solubility
     - :math:`S_{Cr}`
     - :math:`[wt.\%]`
     - ✔
     - ✔
     - ✔
   * - Silicon solubility in liquid lead
     - :math:`S_{Si}`
     - :math:`[wt.\%]`
     - ✔
     - :math:`-`
     - :math:`-`
   * - Oxygen solubility
     - :math:`S_{O}`
     - :math:`[wt.\%]`
     - ✔
     - ✔
     - ✔
   * - Oxygen partial pressure divided by the oxygen concentration squared
     - :math:`P_{O_2}`
     - :math:`[atm/wt.\%^2]`
     - ✔
     - ✔
     - ✔
   * - Oxygen diffusivity
     - :math:`D_{Fe}`
     - :math:`[cm^2/s]`
     - ✔
     - ✔
     - ✔
   * - Iron diffusivity in lead and LBE
     - :math:`D_{Fe}`
     - :math:`[cm^2/s]`
     - ✔
     - ✔
     - :math:`-`
   * - Cobalt diffusivity in lead
     - :math:`D_{Co}`
     - :math:`[cm^2/s]`
     - ✔
     - :math:`-`
     - :math:`-`
   * - Selenium diffusivity in lead
     - :math:`D_{Se}`
     - :math:`[cm^2/s]`
     - ✔
     - :math:`-`
     - :math:`-`
   * - Indium diffusivity in lead
     - :math:`D_{In}`
     - :math:`[cm^2/s]`
     - ✔
     - :math:`-`
     - :math:`-`
   * - Tellurium diffusivity in lead
     - :math:`D_{Tl}`
     - :math:`[cm^2/s]`
     - ✔
     - :math:`-`
     - :math:`-`
   * - Lower limit of oxygen concentration for operational control with
   
       iron, the structural material, at its saturation concentration
       
       in the liquid metal, lead or LBE.
     - :math:`C_{O_2, Fe(sat)}`
     - :math:`[wt.\%]`
     - ✔
     - ✔
     - :math:`-`
   * - Lower limit of oxygen concentration for operational control with
   
       nickel, the structural material, at its saturation concentration
       
       in the liquid metal, lead or LBE.
     - :math:`C_{O_2, Ni(sat)}`
     - :math:`[wt.\%]`
     - ✔
     - ✔
     - :math:`-`
   * - Lower limit of oxygen concentration for operational control with
   
       chromium, the structural material, at its saturation concentration
       
       in the liquid metal, lead or LBE.
     - :math:`C_{O_2, Cr(sat)}`
     - :math:`[wt.\%]`
     - ✔
     - ✔
     - :math:`-`
   * - Lower limit of oxygen concentration for operational control with
   
       silicon (the structural material) at its saturation concentration
       
       in the liquid metal, lead or LBE.
     - :math:`C_{O_2, Si(sat)}`
     - :math:`[wt.\%]`
     - ✔
     - ✔
     - :math:`-`
   * - Lower limit of oxygen concentration for operational control with
   
       aluminium, the structural material, at its saturation concentration
       
       in the liquid metal, lead or LBE.
     - :math:`C_{O_2, Al(sat)}`
     - :math:`[wt.\%]`
     - ✔
     - ✔
     - :math:`-`
   * - Lower limit of oxygen concentration for operational control

       times the iron (the structural material) concentration
       
       in the liquid metal, lead or LBE, raised to 3/4. 
     - :math:`C_{O_2}.C_{Fe}^{3/4}`
     - :math:`[wt.\%]`
     - ✔
     - ✔
     - :math:`-`
   * - Lower limit of oxygen concentration for operational control

       times the nickel (the structural material) concentration
       
       in the liquid metal, lead or LBE. 
     - :math:`C_{O_2}.C_{Ni}`
     - :math:`[wt.\%]`
     - ✔
     - ✔
     - :math:`-`
   * - Lower limit of oxygen concentration for operational control

       times the chromium (the structural material) concentration
       
       in the liquid metal, lead or LBE, raised to 2/3. 
     - :math:`C_{O_2}.C_{Cr}^{2/3}`
     - :math:`[wt.\%]`
     - ✔
     - ✔
     - :math:`-`
   * - Lower limit of oxygen concentration for operational control

       times the silicon (the structural material) concentration
       
       in the liquid metal, lead, raised to 1/2. 
     - :math:`C_{O_2}.C_{Si}^{1/2}`
     - :math:`[wt.\%]`
     - ✔
     - :math:`-`
     - :math:`-`

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

The html documentation is available on GitHub Pages at `newcleo-dev-team.github.io/lbh15 <https://newcleo-dev-team.github.io/lbh15/index.html>`_.

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

- Create an instance of :class:`.Lead` at a given temperature, than change it. Compare the oxygen
  diffusivity value at the two temperatures:

  >>> from lbh15 import Lead
  >>> liquid_lead = Lead(T=700)
  >>> liquid_lead.o_dif
  4.11000872874867e-06
  >>> liquid_lead.T = 850
  >>> liquid_lead.o_dif
  6.708316471487037e-06

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
  'Lead(T=1000.00, cr_sol=9.38e-04, fe_sol=7.67e-04, ni_sol=0.92, o_sol=0.02, si_sol=5.08e-04, co_dif=3.20e-05, in_dif=5.90e-05, fe_dif=2.48e-05, o_dif=9.45e-06, se_dif=7.16e-05, te_dif=4.59e-05, G=-3.34e+03, H=11946.50, S=15.28, o_pp=1.06e-09, h=57656.86, lim_cr=1.43e-13, lim_fe=5.77e-09, lim_ni=3.97e-04, lim_al_sat=5.24e-20, lim_cr_sat=1.49e-11, lim_fe_sat=1.25e-06, lim_ni_sat=4.30e-04, lim_si_sat=2.28e-15, lim_zr_sat=16775.84, lim_si=5.14e-17, alpha=1.26e-04, beta_s=3.38e-11, cp=140.89, k=20.20, mu=1.33e-03, p_s=1.41, r=1.14e-06, rho=10161.50, sigma=0.41, u_s=1707.00)'



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
  reference handbook :cite:`Agency2015`):
  
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
  {'cr_sol': ['alden1958', 'gosse2014', 'venkatraman1988'], 'fe_sol': 'gosse2014', 'ni_sol': 'gosse2014', 'o_sol': 'lbh15', 'si_sol': 'lbh15', 'co_dif': 'lbh15', 'in_dif': 'lbh15', 'fe_dif': 'lbh15', 'o_dif': ['arcella1968', 'charle1976', 'ganesan2006b', 'gromov1996', 'homna1971', 'otsuka1975', 'swzarc1972'], 'se_dif': 'lbh15', 'te_dif': 'lbh15', 'G': 'lbh15', 'H': 'lbh15', 'S': 'lbh15', 'o_pp': ['alcock1964', 'charle1976', 'fisher1966', 'ganesan2006', 'isecke1977', 'otsuka1979', 'otsuka1981', 'szwarc1972', 'taskinen1979'], 'h': 'sobolev2011', 'lim_cr': ['alden1958', 'gosse2014', 'venkatraman1988'], 'lim_fe': 'lbh15', 'lim_ni': 'lbh15', 'lim_al_sat': 'lbh15', 'lim_cr_sat': 'lbh15', 'lim_fe_sat': 'lbh15', 'lim_ni_sat': 'lbh15', 'lim_si_sat': 'lbh15', 'lim_zr_sat': 'lbh15', 'lim_si': 'lbh15', 'alpha': 'lbh15', 'beta_s': 'lbh15', 'cp': ['gurvich1991', 'sobolev2011'], 'k': 'lbh15', 'mu': 'lbh15', 'p_s': 'sobolev2011', 'r': 'lbh15', 'rho': 'sobolev2008a', 'sigma': 'jauch1986', 'u_s': 'sobolev2011'}

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

.. _Learn more:

==========
Learn more
==========

This section contains in a first part some informations about the correlations linked to the oxygen control
in lead and LBE systems. More precisely, we develop how to obtain the relations provided in the lbh15.
The second part contains an example of application of the complete package, simulating an heat variation and 
some of its consequences in a liquid lead system.

.. include:: learn_more.rst
 
.. _API Guide:

=========
API Guide
=========
.. only:: html

  This section provides the guide for the application programming interface.

.. toctree::
   :maxdepth: 2

   documentation.rst
