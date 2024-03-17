---
title: '`lbh15`: a Python package for standard use and implementation of physical data of heavy liquid metals used in nuclear reactors'
tags:
  - Python
  - heavy liquid metal
  - lead-bismuth eutectic alloy
  - standardization
  - nuclear reactor cooling
authors:
  - name: Gabriele Ottino
    orcid: 0000-0003-0937-8897
    corresponding: true
    affiliation: 1
  - name: Daniele Panico
    affiliation: 1
  - name: Daniele Tomatis
    orcid: 0000-0001-7314-2227
    affiliation: 1
  - name: Pierre-Alexandre Pantel
    affiliation: 2
affiliations:
  - name: '*new*cleo Srl, via Giuseppe Galliano 27, 10129 Torino, Italy'
    index: 1
  - name: '*new*cleo SA, 9 Rue des Cuirassiers, 69003 Lyon, France'
    index: 2
date: 08 January 2023
bibliography: paper.bib

---

# Summary

`lbh15` is a Python package that provides function correlations for the 
physical properties of the liquid metals used as coolant in GEN-IV liquid metal fast 
reactors (*LMFR*), such as those cooled by molten lead and lead-bismuth 
eutectic alloy. The package implements the correlations contained in the 
reference handbook edited by OECD/NEA [@nea], also offering the possibility of 
adding new customized properties with minimal effort for the user. The 
properties of the liquid metal are uniquely defined by its thermodynamic 
state, namely by the temperature and pressure values. As alternative, the 
physical properties can be used at liquid metal object's instantiation, 
provided that the inverse of the corresponding correlation has at least one 
root in the validity range (*injective function* property).

`lbh15` package is released under the *GNU Lesser General Public License v3.0*.

# Statement of Need

Thermal-hydraulic analysis is a key factor for the design and safety studies 
of *LMFR*s, involving the implementation and use of several numerical 
methods and physical data that are employed in different computational tools. 
A standardization of the methods is necessary to guarantee homogeneity, 
reproducibility, and comparability of the numerical results. This 
standardization is particularly important considering the growing community 
of users with robust quality assurance needs. This is an essential point to 
ensure effective and successful projects in both industrial and research 
environments, especially for nuclear science and engineering. As well, 
*new*cleo pursues efforts for data standardization to develop new units 
of lead-cooled fast reactors (*LFR*).

In this context, standard libraries providing the correlations of physical 
properties for thermal-hydraulic computational tools are needed, such as CFD, 
system and sub-channel codes concerning heavy liquid metals.

# Implementation

`lbh15` package takes inspiration from the `iapws`[@iapwscode] Python package, 
which implements the water-related *IAPWS* full standard [@iapws]. However, 
`lbh15` follows a different implementation approach.

The efficiency and the effectiveness are assured by the *Object-Oriented* 
design and the *Dynamic Loading* approach, which have been applied throughout 
the entire development process. `lbh15` relies on the abstract liquid metal 
class: all classes describing the different metals inherit from it. The 
abstract class does not directly implement the property correlations, but 
it instead instantiates the property objects and provides the property values. 
In other words, the abstract liquid metal class acts as both *factory* of 
the property objects and *proxy* of the property values [@pybook]. 
This allows the user to add new custom properties without modifying the 
existing implementation of the liquid metal class.

# Use

There are two main ways to use the package: either by instantiating 
a liquid metal object to access all its properties, or by instantiating 
an object for each specific property. The former approach provides a 
single entry point to all the liquid metal properties, which are evaluated 
at the specified thermodynamic state after checking that such state is valid 
(temperature between the melting and the boiling values, and positive 
pressure). In addition, this approach allows to select the default 
correlations of the properties by means of the available class methods. The 
latter approach is best suited to cases where only a few specific properties 
are required for an individual thermodynamic state, since it offers faster 
instantiation and evaluation of the correlation functions.

# Implemented Properties

The properties implemented so far can be subdivided into two groups:

* *thermo-physical*: saturation vapour pressure, surface tension, density, 
  thermal expansion coefficient, speed of sound, isentropic compressibility, 
  specific heat capacity, specific enthalpy, dynamic viscosity, electrical 
  resistivity, thermal conductivity, Prandtl number;

* *thermo-chemical*: diffusivity and solubility of Oxygen 
  and of the impurities in the liquid metals, Oxygen partial pressure, 
  molar enthalpy, molar entropy, Gibbs free energy, and Oxygen concentration 
  range assuring corrosion-protective oxide layer on metallic structure.

# Implementation History

The release of version *1.1.0* of the package `lbh15` was described in 
[@nureth20]. This version implemented only the thermo-physical properties.

The current version *2.0.0* implements the thermo-chemical properties and 
updates the documentation accordingly. It improves the performance and the 
readability. Moreover, solutions have been adopted to improve performance and 
usability such as, for instance, enforcing vectorisation over the whole 
implementation and using the Horner scheme to evaluate polynomials 
[@hornerbook]. The current version includes a tutorial focusing on a 
volume of lead that is subjected to time-varying thermal loads, where the 
Oxygen concentration is controlled to fall in the range where the protective 
oxide layer formation is assured [@nea]. Great attention is paid to 
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
development. The documentation contains examples for users, 
from basic use to short tutorials for more advanced 
applications.

# References