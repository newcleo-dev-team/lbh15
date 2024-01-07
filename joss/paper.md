---
title: '`lbh15`: a Python package for standard use and implementation of physical data of heavy liquid metals used in nuclear reactors'
tags:
  - Python
  - heavy liquid metal
  - lead-bismuth eutectic alloy
  - standardization
  - nuclear reactor cooling
authors:
  - name: Gabriele M. Ottino
    orcid: 0000-0003-0937-8897
    corresponding: true
    affiliation: 1
  - name: Daniele M. Panico
    affiliation: 1
  - name: Daniele Tomatis
    orcid: 0000-0001-7314-2227
    affiliation: 1
  - name: Pierre-Alexandre Pantel
    affiliation: 2
affiliations:
  - name: '*new*cleo S.r.l., Italy'
    index: 1
  - name: '*new*cleo SA, France'
    index: 2
date: 04 January 2023
bibliography: paper.bib

---

# Summary

`lbh15` is a Python package that provides function correlations for the physical 
properties of the liquid metals used as coolant in GEN-IV liquid metal fast 
reactors (*LMFR*), such as those cooled by molten lead, bismuth and their 
eutectic alloy. The package implements the correlations contained in the 
reference handbook edited by OECD/NEA [@nea], also offering the possibility of 
adding new customized properties with minimal effort for the user. The 
properties of the liquid metal are uniquely defined by its thermo-dynamic 
state, namely by the temperature and the pressure values. In addition, the 
value of several other properties can be used at liquid metal object's 
instantiation, provided that the inverse of the corresponding correlation 
has at least one root in the validity range (*injective function* property).

`lbh15` package is released under the *GNU Lesser General Public License v3.0*.

# Statement of Need

Thermal-hydraulic analysis is a key factor for the design and safety studies 
of *LMFR*s. It involves the implementation and use of several numerical 
methods and physical data that are employed in different computer tools. 
With a growing community of users and considering quality assurance needs 
for the engineering studies, a standardization of the approaches becomes 
necessary to guarantee homogeneity, reproducibility and comparability of 
the numerical results. This is an essential point to ensure work 
effectiveness and successful projects in both industry and research 
environments, especially for nuclear science and engineering. As well, 
*new*cleo pursues efforts for data standardization to develop new units 
of lead-cooled fast reactors (*LFR*).

In this context, standard libraries providing the physical correlations for 
thermal-hydraulic computer tools are needed.

# Implementation

`lbh15` package takes inspiration from the `iapws`[^1] Python package, 
that implements the water-related *IAPWS* full standard [@iapws]. However, 
`lbh15` follows a different implementation approach.

The efficiency and the effectiveness are assured by the *Object-Oriented* 
and the *Dynamic Programming* approaches, that have been applied throughout 
the entire development process. `lbh15` relies on the abstract liquid metal 
class: all classes describing the different metals inherit from it. The 
abstract class does not implement directly the property correlations, but 
it instantiates the property objects and provides the property values. In 
other words, the abstract liquid metal class acts as both *factory* of 
the property objects and *proxy* of the property values [@pybook]. 
This allows the user to add new custom properties without modifying the 
existing implementation of the liquid metal class.

[^1]: https://pypi.org/project/iapws/ - *Iapws 1.5.3* - jjgomera - 2022

# Use

There are two main ways to use the package, that is, either by instantiating 
a liquid metal object to access its related properties, or by instantiating 
an object for each specific property. The former approach provides one 
single entry point to all the liquid metal properties, which are evaluated 
at the specified thermo-dynamic state after checking its validity with
respect to the validity range of the properties themselves
(temperature between the melting and the boiling values, and positive 
pressure). In addition, the former approach allows to manage the properties 
correlations in a simpler way, by acting either on a single or on all
liquid metal instances at the same time. The latter approach is best suited 
to cases where only a few specific properties are required for an
individual thermo-dynamic state, i.e., where it may be too much to know the 
values of all the properties of the liquid metal at once.

# Implemented Properties

The properties implemented so far can be subdivided into two groups:

* *thermo-physical* (saturation vapour pressure, surface tension, density, 
  thermal expansion coefficient, speed of sound, isentropic compressibility, 
  specific heat capacity, specific enthalpy, dynamic viscosity, electrical 
  resistivity, thermal conductivity, Prandtl number);

* *thermo-chemical*, including the diffusivity and the solubility of Oxygen 
  and of the impurities within the liquid metals, the Oxygen partial pressure, 
  the molar enthalpy, the molar entropy, the Gibbs free energy and the range 
  of the Oxygen concentration values where a corrosion-protective oxide layer 
  on metallic structure is assured.

# Implementation History

The release of version *1.1.0* of the package `lbh15` was described in 
[@nureth20]. This version implemented only the thermo-physical properties.

The current version *2.0.0* implements the thermo-chemical properties and 
updates the documentation accordingly. It improves the performance and 
the readability. Moreover, solutions have been adopted improving 
performance and usability (enforced vectorisation over the whole 
implementation and use of the Horner scheme to evaluate polynomials 
[@hornerbook]). It includes a tutorial focusing on a volume of lead that 
is subjected to time-varying thermal loads, where the Oxygen concentration 
is controlled to fall in the range where the protective oxide 
layer formation is assured, see [@nea]. Great attention is paid to 
the code quality and readability. *PEP8* guidelines[^2] are ensured by 
the *pycodestyle* utility. In addition, the automatic static analysis 
of the code has been performed by applying the *pylint* tool throughout 
the entire development, achieving a score higher than 9 out of 10.

The implementation of irradiation-related properties with new tutorials is 
planned as future improvement.

[^2]: https://www.python.org/dev/peps/pep-0008/ - *Style Guide for Python Code. PEP 8.* - G. van Rossum, B. Warsaw, and N. Coghlan - 2001

# Documentation

The documentation of `lbh15` is generated by `Sphinx` and published on 
`lbh15` *Github Pages* at the following address:

`https://newcleo-dev-team.github.io/lbh15/index.html`.

It is composed of parts addressed separately to the developers and to the 
users. An advanced use of the package needs skills in Python software 
development. The documentation is completed with examples for the users, 
starting from basic use up to short tutorials for more advanced 
applications.

# References