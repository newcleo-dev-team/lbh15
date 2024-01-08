Changelog
=========

Version 2.0.0 (2024-01-08)
--------------------------

- implemented thermo-chemical data and properties (solubility and diffusivity of impurities, Oxygen concentration range where protective oxide layer formation is assured,
  entropy, specific enthalpy, Gibbs free energy, Oxygen partial pressure)

- improved performance by storing properties within dedicated attributes of liquid metal classes

- fixed known bugs

- implemented a tutorial where thermo-physical and thermo-chemical properties of liquid lead are needed for controlling the Oxygen concentration

- updated documentation to include thermo-chemical properties description

- included *Learn More* section into the documentation: it treats the properties related to the Oxygen concentration by the theoretical point of view and by providing
  the description of the above-mentioned tutorial

Version 1.2.0 (2023-07-04)
--------------------------

- constant variables substituted with the ones from :code:`scipy.constants`
- inserted :code:`pyproject.toml`

Version 1.1.1 (2023-03-24)
--------------------------

- refactored the collocation of some already implemented methods

Version 1.1.0 (2023-01-10)
--------------------------

- properties made dependent on the complete thermo-dynamic state (added pressure dependency)

- inserted functionality for computing upper and lower bounds of physical correlations

- implemented :code:`range_warning` decorator for verifying whether the value of the property is required within its temperature validity range

- properties handling moved from class level to instance level

- constant variables moved into a dedicated module
