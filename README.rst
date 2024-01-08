lbh15
=====

:Author: Daniele Panico, Daniele Tomatis
:Contributor: Gabriele Ottino, Lucie Kerleau, Chloé Largeron
:Date: 08/01/2024

Introduction
------------

*lbh15* (**L**\ ead **B**\ ismuth **H**\ andbook 20\ **15**) is a Python package that implements the
thermo-physical and the thermo-chemical properties of lead, bismuth and lead-bismuth eutectic (lbe) metal alloy available from
the handbook edited by 
`OECD/NEA <https://www.oecd-nea.org/jcms/pl_14972/handbook-on-lead-bismuth-eutectic-alloy-and-lead-properties-materials-compatibility-thermal-hydraulics-and-technologies-2015-edition?details=true>`_

*lbh15* is released under the **GNU Lesser General Public License 3**.

*lbh15* is listed among the Open-source Nuclear Codes for Reactor Analysis (`ONCORE <https://nucleus.iaea.org/sites/oncore/SitePages/List%20of%20Codes.aspx>`_) by IAEA.

Project Structure
-----------------

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

Dependencies
------------

To run the code, the following dependencies must be satisfied:

- ``Python`` :math:`>= 3.8.10`
- ``SciPy`` :math:`>= 1.8.1`
- ``NumPy`` :math:`>= 1.22.3`

To build the documentation in both *html* and *LaTeX* formats, the following dependencies must be satisfied:

- ``sphinx`` :math:`>= 6.2.1`
- ``sphinx-rtd-theme`` :math:`>= 1.3.0`
- ``myst-parser`` :math:`>= 1.0.0`
- ``sphinxcontrib-bibtex`` :math:`>= 2.5.0`

Installation
------------

To install the *lbh15* package, please type the following command:

  .. code-block:: bash

      pip install lbh15

Or use https://github.com/newcleo-dev-team/lbh15.git to clone the package.
After cloning the package, execute the following command inside the base folder:

  .. code-block:: bash

      pip install .

To upgrade the *lbh15* package, please type the ``install`` command along with the ``--upgrade`` or ``-U`` flag:

  .. code-block:: bash

      pip install --upgrade lbh15

Documentation
-------------

The Sphinx documentation can be built in *html* and *LaTeX* formats by executing
the following command in the folder ``docs/``:

  .. code-block:: bash

      make html

  .. code-block:: bash

      make latexpdf

The *html* documentation is available on GitHub Pages at `newcleo-dev-team.github.io/lbh15 <https://newcleo-dev-team.github.io/lbh15/index.html>`_.

To see the available templates for generating the documentation in *PDF* format and to choose among them, please
look at the ``docs/conf.py`` file.

How to Cite
-----------

.. code-block:: latex

  @inproceedings{NURETH20lbh15,
    author = {Panico, Daniele and Tomatis, Daniele},
    title = {{lbh15: a Python package implementing lead, bismuth, and lead-bismuth eutectic thermophysical properties for fast reactor applications}},
    booktitle = {Proc. of 20th International Topical Meeting on Nuclear Reactor Thermal Hydraulics (NURETH-20), Washington DC, USA},
    pages = {1--12},
    year = {2023},
    month = {Aug 20--25},
    editor = {ANS}
  }

.. code-block:: latex

  @article{lbh15JOSS2024,
    author = {Ottino, G.M., Panico, D., Tomatis, D. and Pantel, P.A.},
    title = {{lbh15: a Python package for standard use and implementation of physical data of heavy liquid metals used in nuclear reactors}},
    editor = {Journal of Open-Source Scientific Software}
    note={submitted}
  }