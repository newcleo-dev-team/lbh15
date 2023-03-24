lbh15
=====

:Author: Daniele Panico, Daniele Tomatis
:Date: 03/24/2023

Introduction
------------

lbh15 (**L**\ ead **B**\ ismuth **H**\ andbook 20\ **15**) is a Python package that implements the
thermo-physical properties of lead, bismuth and lead-bismuth eutectic (lbe) metal alloy available from
the handbook edited by 
`OECD/NEA <https://www.oecd-nea.org/jcms/pl_14972/handbook-on-lead-bismuth-eutectic-alloy-and-lead-properties-materials-compatibility-thermal-hydraulics-and-technologies-2015-edition?details=true>`_


lbh15 is released under the GNU Lesser General Public License 3.


Project Structure
-----------------
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

Dependencies
------------

- Python >=3.8.10
- Sphinx >=5.1.0
- SciPy >=1.8.1
- NumPy >=1.22.3

Installation
------------
To install the package lbh15, type please the following command:

  .. code-block:: bash

      pip install lbh15

Or use https://github.com/newcleo-dev-team/lbh15.git to clone the package.
After cloning the package, execute the following command inside the base folder:

  .. code-block:: bash

      pip install .

Documentation
-------------

The Sphinx documentation can be built in html and latex by executing
the following command in the folder ``docs/``:
 
  .. code-block:: bash

      make html
 
  .. code-block:: bash

      make latex
      cd _build/latex
      latexmk -pdf -f

The html documentation is available on GitHub Pages at `newcleo-dev-team.github.io/lbh15 <https://newcleo-dev-team.github.io/lbh15/index.html>`_.
