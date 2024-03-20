.. raw:: latex

   \setcounter{secnumdepth}{3}

============
Introduction
============

*lbh15* (**L**\ ead **B**\ ismuth **H**\ andbook 20\ **15**) is a Python package that implements the
thermo-physical and the thermo-chemical properties of lead, bismuth and lead-bismuth eutectic (lbe) metal alloy available from
the handbook edited by OECD/NEA :cite:`Agency2015`:
https://www.oecd-nea.org/jcms/pl_14972/handbook-on-lead-bismuth-eutectic-alloy-and-lead-properties-materials-compatibility-thermal-hydraulics-and-technologies-2015-edition.

*lbh15* offers a standard implementation for use of these properties in scientific applications.
In particular, this package is used for numerical simulation and experimental activities supporting the
development of nuclear reactors that employ heavy liquid metals as primary coolant.

The thermo-physical properties implemented in the package are listed in :numref:`tableprop`.

.. list-table:: *lbh15* thermo-physical properties from the handbook edited by OECD/NEA.
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

The thermo-chemical properties implemented since version 1.2.0 are listed in :numref:`tablechemdata` (basic properties), :numref:`tablechemsoldiff`
(solubilities, diffusivities and Oxygen partial pressure), :numref:`tablechemlowlimssat` (lower limits of Oxygen concentration for oxide layers generation
when the corresponding metal is considered at its saturation concentration) and :numref:`tablechemlowlims` (lower limits of Oxygen concentration for
oxide layers generation multiplied by the corresponding metal concentration raised to a specific coefficient).

.. list-table:: *lbh15* thermo-chemical properties from the handbook edited by OECD/NEA: basic data.
   :widths: 50 25 25 25 25 25
   :name: tablechemdata
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
     - :math:`[J/(mol \cdot K)]`
     - ✔
     - ✔
     - ✔
   * - Gibbs free energy
     - :math:`G`
     - :math:`[J/mol]`
     - ✔
     - ✔
     - ✔

.. list-table:: *lbh15* thermo-chemical properties from the handbook edited by OECD/NEA: solubilities, diffusivities and Oxygen partial pressure.
   :widths: 50 25 25 25 25 25
   :name: tablechemsoldiff
   :header-rows: 1

   * - Property
     - Symbol
     - Units
     - Lead
     - LBE
     - Bismuth
   * - Iron solubility
     - :math:`S_{\ce{Fe}}`
     - :math:`[wt.\%]`
     - ✔
     - ✔
     - ✔
   * - Nickel solubility
     - :math:`S_{\ce{Ni}}`
     - :math:`[wt.\%]`
     - ✔
     - ✔
     - ✔
   * - Chromium solubility
     - :math:`S_{\ce{Cr}}`
     - :math:`[wt.\%]`
     - ✔
     - ✔
     - ✔
   * - Silicon solubility
     - :math:`S_{\ce{Si}}`
     - :math:`[wt.\%]`
     - ✔
     - :math:`-`
     - :math:`-`
   * - Oxygen solubility
     - :math:`S_{\ce{O}}`
     - :math:`[wt.\%]`
     - ✔
     - ✔
     - ✔
   * - Oxygen diffusivity
     - :math:`D_{\ce{O}}`
     - :math:`[cm^2/s]`
     - ✔
     - ✔
     - ✔
   * - Iron diffusivity
     - :math:`D_{\ce{Fe}}`
     - :math:`[cm^2/s]`
     - ✔
     - ✔
     - :math:`-`
   * - Cobalt diffusivity
     - :math:`D_{\ce{Co}}`
     - :math:`[cm^2/s]`
     - ✔
     - :math:`-`
     - :math:`-`
   * - Selenium diffusivity
     - :math:`D_{\ce{Se}}`
     - :math:`[cm^2/s]`
     - ✔
     - :math:`-`
     - :math:`-`
   * - Indium diffusivity
     - :math:`D_{\ce{In}}`
     - :math:`[cm^2/s]`
     - ✔
     - :math:`-`
     - :math:`-`
   * - Tellurium diffusivity
     - :math:`D_{\ce{Tl}}`
     - :math:`[cm^2/s]`
     - ✔
     - :math:`-`
     - :math:`-`
   * - Oxygen partial pressure

       divided by the Oxygen
       
       concentration squared
     - :math:`P_{\ce{O2}}`
     - :math:`[atm/wt.\%^2]`
     - ✔
     - ✔
     - ✔

.. list-table:: *lbh15* thermo-chemical properties from the handbook edited by OECD/NEA: lower limits of Oxygen concentration for oxide layers generation when the corresponding metal is considered at its saturation concentration.
   :widths: 50 25 25 25 25 25
   :name: tablechemlowlimssat
   :header-rows: 1

   * - Property
     - Symbol
     - Units
     - Lead
     - LBE
     - Bismuth
   * - :math:`\ce{Fe3O4}`-related lower limit

       of :math:`\ce{O2}` concentration in case
       
       of :math:`\ce{Fe}`-saturated metal
     - :math:`C_{\ce{O2}, \ce{Fe}(sat)}`
     - :math:`[wt.\%]`
     - ✔
     - ✔
     - :math:`-`
   * - :math:`\ce{NiO}`-related lower limit

       of :math:`\ce{O2}` concentration in case
       
       of :math:`\ce{Ni}`-saturated metal
     - :math:`C_{\ce{O2}, \ce{Ni}(sat)}`
     - :math:`[wt.\%]`
     - ✔
     - ✔
     - :math:`-`
   * - :math:`\ce{Cr2O3}`-related lower limit

       of :math:`\ce{O2}` concentration in case
       
       of :math:`\ce{Cr}`-saturated metal
     - :math:`C_{\ce{O2}, \ce{Cr}(sat)}`
     - :math:`[wt.\%]`
     - ✔
     - ✔
     - :math:`-`
   * - :math:`\ce{SiO2}`-related lower limit

       of :math:`\ce{O2}` concentration in case
       
       of :math:`\ce{Si}`-saturated metal
     - :math:`C_{\ce{O2}, \ce{Si}(sat)}`
     - :math:`[wt.\%]`
     - ✔
     - ✔
     - :math:`-`
   * - :math:`\ce{Al2O3}`-related lower limit

       of :math:`\ce{O2}` concentration in case
       
       of :math:`\ce{Al}`-saturated metal
     - :math:`C_{\ce{O2}, \ce{Al}(sat)}`
     - :math:`[wt.\%]`
     - ✔
     - ✔
     - :math:`-`

.. list-table:: *lbh15* thermo-chemical properties from the handbook edited by OECD/NEA: lower limits of Oxygen concentration for oxide layers generation multiplied by the corresponding metal concentration raised to a specific coefficient.
   :widths: 50 25 25 25 25 25
   :name: tablechemlowlims
   :header-rows: 1

   * - Property
     - Symbol
     - Units
     - Lead
     - LBE
     - Bismuth
   * - Lead chemical activity in LBE
     - :math:`\alpha_{\ce{Pb}}`
     - :math:`[-]`
     - :math:`-`
     - ✔
     - :math:`-`
   * - Bismuth chemical activity in LBE
     - :math:`\alpha_{\ce{Bi}}`
     - :math:`[-]`
     - :math:`-`
     - ✔
     - :math:`-`
   * - :math:`\ce{Fe3O4}`-related lower limit

       of :math:`\ce{O2}` concentration times
       
       :math:`\ce{Fe}` concentration raised to 3/4
     - :math:`C_{\ce{O2}} \cdot C_{\ce{Fe}}^{3/4}`
     - :math:`[wt.\%]`
     - ✔
     - ✔
     - :math:`-`
   * - :math:`\ce{NiO}`-related lower limit

       of :math:`\ce{O2}` concentration times
       
       :math:`\ce{Ni}` concentration
     - :math:`C_{\ce{O2}} \cdot C_{\ce{Ni}}`
     - :math:`[wt.\%]`
     - ✔
     - ✔
     - :math:`-`
   * - :math:`\ce{Cr2O3}`-related lower limit

       of :math:`\ce{O2}` concentration times
       
       :math:`\ce{Cr}` concentration raised to 2/3
     - :math:`C_{\ce{O2}} \cdot C_{\ce{Cr}}^{2/3}`
     - :math:`[wt.\%]`
     - ✔
     - ✔
     - :math:`-`
   * - :math:`\ce{SiO2}`-related lower limit

       of :math:`\ce{O2}` concentration times
       
       :math:`\ce{Si}` concentration raised to 1/2
     - :math:`C_{\ce{O2}} \cdot C_{\ce{Si}}^{1/2}`
     - :math:`[wt.\%]`
     - ✔
     - :math:`-`
     - :math:`-`

The pressure at which to evaluate the properties can be specified at object's instantiation.
Otherwise, all the properties are given at atmospheric pressure (:math:`101325` :math:`[Pa]`) by default.
The correlations' validity range is checked at evaluation in terms of temperature value,
raising a warning in case it is not satisfied (see :any:`basic-usage` section for more details).
Some examples of instantiation are provided using also a target property value, see :any:`initialization-from-properties` 
section for instance. For the sake of completeness, the correlations are also reported in the docstring documentation.
The implementation is fully object-oriented to guarantee easy maintainability, extension and customization
of the package (see :any:`advanced-usage` section).

Go to :any:`API-Guide` section to see the full code documentation.

*lbh15* is developed and maintained by the **Codes & Methods** group of \ *new*\ cleo (https://www.newcleo.com/) and
is released under the GNU Lesser General Public License 3 (see :any:`License` section).

*lbh15* is listed among the Open-source Nuclear Codes for Reactor Analysis (https://nucleus.iaea.org/sites/oncore/SitePages/List%20of%20Codes.aspx) by IAEA.


=================
Project Structure
=================
The project is organized according to the following folder structure:

.. code:: text

  <lbh15 parent folder>
    ├── docs/
    ├── lbh15/
    ├── tests/
    ├── tutorials/
    ├── CHANGELOG.rst
    ├── LICENSE
    ├── MANIFEST.in
    ├── README.rst
    ├── pyproject.toml
    └── setup.py
    

- ``lbh15``: contains all modules, classes and methods implemented in *lbh15*;
- ``docs``: contains files for the generation of the documentation by Sphinx;
- ``tests``: collection of tests used to verify the correct implementation;
- ``tutorials``: collection of tutorials and examples, each one into a dedicated sub-folder.

============
Dependencies
============

To run the code, the following dependencies must be satisfied:

- ``Python`` :math:`>= 3.8.10`
- ``SciPy`` :math:`>= 1.8.1`
- ``NumPy`` :math:`>= 1.22.3`

To build the documentation in both *html* and *LaTeX* formats, the following dependencies must be satisfied:

- ``sphinx`` :math:`>= 6.2.1`
- ``sphinx-rtd-theme`` :math:`>= 1.3.0`
- ``myst-parser`` :math:`>= 1.0.0`
- ``sphinxcontrib-bibtex`` :math:`>= 2.5.0`

============
Installation
============
To install the *lbh15* package, please type the following command:

  .. code-block:: bash

      pip install lbh15

Otherwise, clone the package from https://github.com/newcleo-dev-team/lbh15.git
and execute the following command inside the resulting folder:

  .. code-block:: bash

      pip install .

To upgrade the *lbh15* package, please type the ``install`` command along with the ``--upgrade`` or ``-U`` flag:

  .. code-block:: bash

      pip install --upgrade lbh15

The Sphinx documentation can be built in *html* and *LaTeX* by executing
the following commands, respectively, in the ``docs/`` folder:
 
  .. code-block:: bash

      make html
 
  .. code-block:: bash

      make latexpdf

The *html* documentation is available on GitHub Pages at https://newcleo-dev-team.github.io/lbh15/index.html.

To see the available templates for generating the documentation in *PDF* format and to choose among them, please
look at the ``docs/conf.py`` file.

.. _Examples:

===============
Getting Started
===============

This section contains some examples of basic usage and possible customization
of the *lbh15* package. More examples are available in
:class:`.Lead`, :class:`.Bismuth` and :class:`.LBE` classes.

.. _basic-usage:

+++++++++++
Basic Usage
+++++++++++

This section shows a few examples of basic usage of *lbh15*.

- Create a :class:`.Lead` instance using Celsius degrees as temperature unit
  and print the corresponding dynamic viscosity :code:`mu`:
  
  >>> from scipy.constants import convert_temperature
  >>> from lbh15 import Lead
  >>> # Initialize Lead object with T=395 Celsius
  >>> liquid_lead = Lead(T=convert_temperature(395.0, 'C', 'K'))
  >>> # Print lead dynamic viscosity in [Pa*s]
  >>> liquid_lead.mu
  0.0022534948395446985

- Create two instances of :class:`.Lead` class, one at atmospheric pressure and one at twenty times the 
  atmospheric pressure. Then compare their density values :code:`rho`:

  >>> from lbh15 import Lead
  >>> from scipy.constants import atm
  >>> # Initialize first object, default pressure is atm
  >>> liquid_lead = Lead(T=800)
  >>> # Initialize the second object by specifying the pressure
  >>> liquid_lead_2 = Lead(T=800, p=20*atm)
  >>> # Compare their density
  >>> liquid_lead.rho, liquid_lead_2.rho
  (10417.4, 10418.185181757714)

- Create an instance of :class:`.Lead` class at a given temperature :code:`T`, then change the temperature value. Compare the conductivity
  values :code:`k` at the two temperatures:

  >>> from lbh15 import Lead
  >>> liquid_lead = Lead(T=750)
  >>> liquid_lead.k
  17.45
  >>> liquid_lead.T = 1200
  >>> liquid_lead.k
  22.4

- Create an instance of :class:`.Lead` class at a given temperature :code:`T`, then change the temperature value. Compare the Oxygen
  diffusivity values :code:`o_dif` at the two temperatures:

  >>> from lbh15 import Lead
  >>> liquid_lead = Lead(T=700)
  >>> liquid_lead.o_dif
  4.11000872874867e-06
  >>> liquid_lead.T = 850
  >>> liquid_lead.o_dif
  6.708316471487037e-06

- Request a property outside the range of validity of the corresponding correlation. In this example, a :class:`.Lead` object is initialized
  using a temperature value :code:`T` that is outside the range of physical validity of the surface tension :code:`sigma` correlation:

  >>> from lbh15 import Lead
  >>> liquid_lead = Lead(T=1400.0)
  >>> liquid_lead.sigma
  <stdin>:1: UserWarning: The surface tension is requested at temperature value of 1400.00 K that is not in validity range [600.60, 1300.00] K
  0.3676999999999999

- Get summary information of the liquid metal using *pprint* package (the warnings about out-of-range correlations are also written):

  >>> from lbh15 import Lead
  >>> import pprint
  >>> liquid_lead = Lead(T=900)
  >>> pprint.pprint(liquid_lead)
  .local/lib/python3.9/site-packages/lbh15/_lbh15.py:740: UserWarning: The iron diffusivity is requested at temperature value of 900.00 K that is not in validity range [973.00, 1273.00] K
    attr_value = getattr(self, key)
  .local/lib/python3.9/site-packages/lbh15/_lbh15.py:740: UserWarning: The silicon solubility is requested at temperature value of 900.00 K that is not in validity range [1323.00, 1523.00] K
    attr_value = getattr(self, key)
  .local/lib/python3.9/site-packages/lbh15/_lbh15.py:740: UserWarning: The cobalt diffusivity is requested at temperature value of 900.00 K that is not in validity range [1023.00, 1273.00] K
    attr_value = getattr(self, key)
  Lead(T=900.00, p=101325.00, fe_sol=2.02e-04, lim_cr=1.52e-15, in_dif=4.91e-05, lim_si_sat=2.69e-17, fe_dif=1.38e-05, k=19.10, lim_fe_sat=1.60e-07, lim_fe=2.71e-10, beta_s=3.24e-11, se_dif=6.02e-05, H=9010.76, lim_ni_sat=9.30e-05, r=1.09e-06, si_sol=8.10e-05, lim_ni=6.01e-05, alpha=1.24e-04, h=43488.20, cp=142.52, p_s=0.12, lim_si=2.42e-19, G=-1.96e+03, co_dif=2.38e-05, o_pp=4.23e-11, lim_cr_sat=4.92e-13, o_dif=7.62e-06, rho=10289.45, ni_sol=0.65, S=12.19, te_dif=3.71e-05, lim_al_sat=1.54e-22, cr_sol=1.71e-04, o_sol=4.23e-03, u_s=1731.60, mu=1.49e-03, sigma=0.42)


.. _initialization-from-properties:

+++++++++++++++++++++++++++++++++++++++++++++++
Initialization from Properties (*experimental*)
+++++++++++++++++++++++++++++++++++++++++++++++

The *lbh15* package gives the possibility to instantiate a liquid metal object by simply knowing the value of one of its
properties (see :class:`.Lead`, :class:`.Bismuth` and :class:`.LBE` classes documentation for the full list).
This is accomplished by finding the root of the correlation function matching the target property value. Such function,
which constitutes a physical correlation, must be injective in the range considered for the root. Note that this is a
necessary, but not jointly sufficient condition to find a root for the function.


Since the existence of a (single) root cannot be guaranteed for every correlation, this functionality is marked as *experimental*:
the user is invited to double-check the result (see :any:`advanced-usage` section).


In the following, some examples are provided:

- Initialize an :class:`.LBE` instance, i.e., lead-bismuth-eutectic object, by setting its density :code:`rho`
  and retrieve the corresponding temperature :code:`T` in Kelvin degrees:

  >>> from lbh15 import LBE
  >>> # Initialize LBE with rho=9800 [kg/m^3]
  >>> liquid_lbe = LBE(rho=9800)
  >>> # Print lbe temperature in [K]
  >>> liquid_lbe.T
  978.3449342614074

- Compare properties of different liquid metal objects at a given temperature. In this 
  example, a :class:`.Lead` object is initialized by specifying a value of the thermal
  conductivity :code:`k`; then, a :class:`.Bismuth` object is initialized using the :class:`.Lead`
  instance temperature :code:`T` in Kelvin degrees. Finally, the thermal conductivity :code:`k` of the :class:`.Bismuth` object
  is printed for comparison purposes:

  >>> from lbh15 import Lead
  >>> from lbh15 import Bismuth
  >>> # Inititialize Lead with k=17.37 [W/(m*K)]
  >>> liquid_lead = Lead(k=17.37)
  >>> # Initialize Bismuth with Lead temperature in K
  >>> liquid_bismuth = Bismuth(T=liquid_lead.T)
  >>> # Print Bismuth conductivity
  >>> liquid_bismuth.k
  14.395909090909091

- The initialization from mass-specific heat capacity :math:`c_p` needs some attention because the corresponding function of temperature is not injective.
  In particular, two temperature values may be possible for the same value of :math:`c_p`. This occurrence must be handled carefully.
  Currently, the package allows the user to look for the root in the two distinct ranges where the function is monotone.
  The default range index is 0, which corresponds to the lowest temperature range.
  Here is an example with :class:`.Lead` class (the same holds for :class:`.Bismuth` and :class:`.LBE` classes):

  >>> from lbh15 import Lead
  >>> from lbh15 import lead_properties
  >>> # Get an instance of cp property, sobolev2011 correlation
  >>> cp = lead_properties.cp_sobolev2011()
  >>> # Compute correlation bounds (min, max, T_at_min, T_at_max)
  >>> cp.compute_bounds()
  >>> # Visualize temperature in [K] corresponding to cp min
  >>> cp.T_at_min
  1568.6647571773037
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
  (1437.4148683656551, 1699.157333532332)



.. _advanced-usage:

++++++++++++++
Advanced Usage
++++++++++++++

Advanced usage includes the possibility of adding new properties and new physical correlations according to the following examples.

- This first example shows how to define a custom correlation for the liquid lead density that 
  does not depend on pressure, and how to use it instead of the default one (the same holds for :class:`.Bismuth` and :class:`.LBE` classes).
  The names of the available correlations can be queried by a simple function call
  (the generic name :code:`lbh15` is used in case the correlation's name is not specified in the
  reference handbook :cite:`Agency2015`); two examples are provided, the first one asking for the available correlations
  for all the implemented properties, the second one asking for the available correlations for a few specific properties, that is,
  the heat capacity and the speed of sound:
  
  >>> from lbh15 import Lead
  >>> Lead.available_correlations()
  defaultdict(<class 'list'>, {'k': ['lbh15'], 'lim_ni': ['lbh15'], 'u_s': ['sobolev2011'], 'mu': ['lbh15'], 'H': ['lbh15'], 'lim_cr': ['venkatraman1988', 'alden1958', 'gosse2014'], 'sigma': ['jauch1986'], 'cp': ['sobolev2011', 'gurvich1991'], 'cr_sol': ['venkatraman1988', 'gosse2014', 'alden1958'], 'in_dif': ['lbh15'], 'o_pp': ['taskinen1979', 'charle1976', 'alcock1964', 'otsuka1979', 'otsuka1981', 'fisher1966', 'isecke1977', 'szwarc1972', 'ganesan2006'], 'lim_cr_sat': ['lbh15'], 'si_sol': ['lbh15'], 'fe_dif': ['lbh15'], 'lim_si': ['lbh15'], 'o_dif': ['charle1976', 'swzarc1972', 'arcella1968', 'gromov1996', 'ganesan2006b', 'otsuka1975', 'homna1971'], 'G': ['lbh15'], 'p_s': ['sobolev2011'], 'beta_s': ['lbh15'], 'se_dif': ['lbh15'], 'lim_al_sat': ['lbh15'], 'ni_sol': ['gosse2014'], 'r': ['lbh15'], 'S': ['lbh15'], 'h': ['sobolev2011'], 'alpha': ['lbh15'], 'co_dif': ['lbh15'], 'lim_si_sat': ['lbh15'], 'lim_fe_sat': ['lbh15'], 'fe_sol': ['gosse2014'], 'lim_fe': ['lbh15'], 'rho': ['sobolev2008a'], 'te_dif': ['lbh15'], 'lim_ni_sat': ['lbh15'], 'o_sol': ['lbh15']})
  >>> Lead.available_correlations(["cp", "u_s"])
  {'cp': ['gurvich1991', 'sobolev2011'], 'u_s': ['sobolev2011']}


  Let implement the new property in :code:`<execution_dir>/custom_properties/lead_properties.py` as:

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

  .. note:: It is mandatory to override the ``correlation`` method and the ``range``, ``units``, ``long_name`` and ``description`` properties.

  .. note:: Properties are not allowed having the name starting with ``__``. This means that neither the name of the corresponding class nor the name provided by the ``name`` attribute must start with ``__``.

  .. note:: It is strongly recommended to use the ``@range_warning`` decorator so that the correlation range is checked when property is queried as liquid metal property and warning is printed, if any, as in :ref:`basic-usage` section.

  Then, provided that the execution is performed in :code:`<execution_dir>`, one can check the correct implementation as follows:

  >>> from lbh15 import Lead
  >>> import os
  >>> Lead.set_custom_properties_path(os.getcwd() + '/custom_properties/lead_properties.py')
  >>> Lead.correlations_available()
  defaultdict(<class 'list'>, {'o_pp': ['taskinen1979', 'charle1976', 'alcock1964', 'otsuka1979', 'otsuka1981', 'fisher1966', 'isecke1977', 'szwarc1972', 'ganesan2006'], 'lim_cr_sat': ['lbh15'], 'fe_dif': ['lbh15'], 'o_dif': ['charle1976', 'swzarc1972', 'arcella1968', 'gromov1996', 'ganesan2006b', 'otsuka1975', 'homna1971'], 'rho': ['sobolev2008a', 'custom2022'], 'cp': ['gurvich1991', 'sobolev2011'], 'lim_si': ['lbh15'], 'G': ['lbh15'], 'se_dif': ['lbh15'], 'ni_sol': ['gosse2014'], 'lim_al_sat': ['lbh15'], 'k': ['lbh15'], 'si_sol': ['lbh15'], 'u_s': ['sobolev2011'], 'mu': ['lbh15'], 'sigma': ['jauch1986'], 'cr_sol': ['gosse2014', 'alden1958', 'venkatraman1988'], 'S': ['lbh15'], 'lim_cr': ['alden1958', 'gosse2014', 'venkatraman1988'], 'H': ['lbh15'], 'co_dif': ['lbh15'], 'fe_sol': ['gosse2014'], 'lim_si_sat': ['lbh15'], 'lim_fe_sat': ['lbh15'], 'lim_fe': ['lbh15'], 'beta_s': ['lbh15'], 'p_s': ['sobolev2011'], 'te_dif': ['lbh15'], 'lim_ni_sat': ['lbh15'], 'o_sol': ['lbh15'], 'r': ['lbh15'], 'lim_ni': ['lbh15'], 'h': ['sobolev2011'], 'alpha': ['lbh15'], 'in_dif': ['lbh15'], 'T_double': ['double2022']})

  The correlations currently available for the density property :code:`rho` are now 2: :code:`sobolev2008a` and :code:`custom2022`.
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
                Liquid Lead custom density

  It is also possible to change the correlation used by a liquid metal object instance by calling the :code:`change_correlation_to_use` method
  on the instance itself.

- *lbh15* also allows to add new properties to the liquid metal objects. For 
  instance, let's implement in :code:`<execution_dir>/custom_property/double_T.py`
  a custom property that is simply the double of the temperature:

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

  The new custom property can be set as :class:`.Lead` attribute by specifying the path to the module
  where it is defined:

  >>> from lbh15 import Lead
  >>> import os
  >>> Lead.set_custom_properties_path(os.getcwd() + '/custom_properties/lead_properties.py')
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

.. note:: The paths of the modules to load the properties from must be absolute.

.. _Learn more:

==========
Learn More
==========

This section contains additional information about the chemistry of heavy liquid metals in presence of dispersed
Oxygen in the bulk. It is made of two parts. The first part, presented in :any:`oxygen-control` section, describes
the Oxygen-related correlations implemented in *lbh15* and how they have been obtained. The second part,
presented in :any:`tutorials` section, describes a tutorial application coming together with *lbh15*, which is a
representation of a simple Oxygen control system applied to a liquid lead volume.

.. include:: learn_more.rst
 
.. _API-Guide:

=========
API Guide
=========

This section contains a detailed description of the implementation of the main modules the ``lbh15`` package is made of.
:any:`lead-module`, :any:`bismuth-module` and :any:`lbe-module` sections provide at first the list
of the default correlations implemented in the corresponding *lead*-, *bismuth*- and
*lbe*-related modules, and then the corresponding *Application Programming Interface* (*API*).
In the end, in :any:`properties-module` section, the *API Guide* is provided of all the properties classes.

.. toctree::
   :maxdepth: 2

   lbh15.rst
