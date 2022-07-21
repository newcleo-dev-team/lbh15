======
LBEH15
======

Python library that models properties of liquid metals: lead, bismuth and lead-bismuth eutectic (lbe).
Properties are taken from "Handbook on Lead-bismuth Eutectic Alloy and Lead Properties, Materials Compatibility, Thermal-hydraulics and Technologies"
(see :cite:p:`Agency2015`). The following properties are provided: 

.. list-table:: LBEH15 PROPERTIES
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

All properties are computed at atmospheric pressure (:math:`101325 [Pa]`).

Project Structure
*****************
The project is organized in the following folder structure:

.. code:: bash

  <lbeh15 parent folder>
    ├── lbeh15
    ├── docs

- lbeh15 folder: this folder collects all modules, classes and methods implemented in lbeh15
- docs: collection of material for the generation of the documentation