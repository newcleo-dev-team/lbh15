++++++++++++++
Oxygen Control
++++++++++++++

In lead and LBE systems, Oxgyen is the most important chemical compound, which results
from start-up operations, maintenance services and possibily incidental contaminations (:cite:`Agency2015`).
For the operation of a nuclear lead alloy system, it is thus important to
determine the upper and the lower oxygen concentration limits.

.. _ Oxygen concentration upper limit:

Oxygen Concentration Upper Limit
================================

The upper limit corresponds to the oxygen concentration value above which contamination by coolant oxides occurs.
It is represented by the *oxygen solubility* in lead and LBE alloys. *lbh15* provides
these properties in the ``lead_thermochemical_properties.solubility_in_lead``
and ``lbe_thermochemical_properties.solubility_in_lbe`` modules.
The implemented data are extracted from :cite:`Agency2015`, table 3.5.2,
"*Oxygen solubility in liquid Pb, Bi and LBE*", page 157: they were obtained by linear regression of
several correlations specified therein.

.. _ Oxygen concentration lower limit:

Oxygen Concentration Lower Limit
================================

The lower limit corresponds to the minimum value of the oxygen concentration enabling the formation of a protective oxide layer on the structural material.
The oxide layer formation is possible only when the oxygen potential in the liquid metal is above the
potential leading to the protective film formation. The correlations implemented in the
``lead_thermochemical_properties.lead_oxygen_limits`` and ``lbe_thermochemical_properties.lbe_oxygen_limits``
modules for computing the lower limits of oxygen concentration are obtained by applying the methodology
described in :cite:`Agency2015`, chapter 4, part 4.2.2, pages 187-192. A brief resume is provided in the following.

After determining the reference reaction equation and the associated Gibbs free energy, the oxygen
concentration will be expressed as a function of temperature, and eventually the correlations will
be derived that come from two different assumptions the user can choose between.

..

  1. The equation of the oxidation reaction (3) is set by considering that it occurs
     between the metal and the oxygen, with the oxygen supposed in solution as dissolved *PbO* below its saturation limit.
     The formation equation of the metal oxide (1) (equation 4.5, page 188 of :cite:`Agency2015`) is combined with the formation
     equation of *PbO* (2), (table 4.2.2, page 189 of :cite:`Agency2015`):

     :math:`\frac{2X}{Y}Me_{(dissolved)} + O_{2(dissolved)} \longrightarrow \frac{2}{Y}Me_XO_Y`    (1)

     :math:`2Pb + O_2 \longrightarrow 2PbO`    (2)

     thus resulting in the following oxidation reaction equation for a mole of *PbO*:

     :math:`\frac{X}{Y}Me_{(dissolved)} + O_{(dissolved)} + PbO \longrightarrow \frac{1}{Y}Me_XO_Y + Pb + O`, where:    (3)

     :math:`Me` represents the metal of the structural material involved in the oxidation reaction,
     :math:`X` and :math:`Y` are coefficients specific to the reaction.

..

  2. The Gibbs free energy associated to equation (3) results to be:

     :math:`\Delta G^0_{(3)} = \frac{\Delta G^0_{(1)}-\Delta G^0_{(2)}}{2}`
     :math:`= \frac{\left(\Delta H^0_{(1)}-T\cdot\Delta S^0_{(1)}\right)-\left(\Delta H^0_{(2)}-T\cdot\Delta S^0_{(2)}\right)}{2}`
     :math:`= \frac{\Delta H^0_{(3)}-T\cdot\Delta S^0_{(3)}}{2}`, where:

     :math:`\Delta G^0_{(i)}` is the Gibbs free energy of formation related to the (i)-th reaction equation;
     :math:`\Delta H^0_{(3)} = \Delta H^0_{(1)}-\Delta H^0_{(2)}` is the formation enthalpy related to equation (3);
     :math:`\Delta S^0_{(3)} =\Delta S^0_{(1)}-\Delta S^0_{(2)}` is the formation entropy related to equation (3);
     :math:`\Delta H^0` and :math:`\Delta S^0` values for each reaction are taken from the table 4.2.2 of :cite:`Agency2015`.

..

  3. In general, the Gibbs free energy of a reaction can also be expressed in the following way:

     :math:`\Delta_rG^0_{(T)} = -RT \ln{(K_{(T)})}`, where:

     - :math:`T` is the temperature in :math:`[K]`;

     - :math:`R` is the molar gas constant in :math:`[J\cdot K^{-1} \cdot mol^{-1}]`;

     - :math:`\Delta_rG^0_{(T)}` is the standard free enthalpy of reaction at constant pressure
       and temperature in :math:`[J\cdot mol^{-1}]`;

     - :math:`K_{(T)} = \prod\limits_{i=1}^{N} \alpha_i^{\nu_i}` is the equilibrium constant,
       being :math:`\alpha_i` the chemical activity of the :math:`i`-th specie at the equilibrium,
       :math:`\nu_i` the stoichiometric coefficient of the :math:`i`-th specie in the related reaction
       (positive for the reaction products and negative for the reactants), and :math:`N` the number of
       components appearing in the related reaction.

     In detail, the chemical activity :math:`\alpha` is a dimensionless quantity used to express the deviation
     of a mixture of chemical substances from a standard behaviour. It is defined by the following relations:

     - :math:`\alpha_i = \gamma_i\cdot\chi_i` , being :math:`\gamma` the dimensionless activity coefficient
       of the :math:`i`-th specie and :math:`\chi_i` the molar fraction of the same specie;

     - :math:`\alpha_i = \gamma_i\cdot\frac{C_i}{C_{iref}}`, being :math:`C_i` the concentration of the
       :math:`i`-th specie in the mixture and :math:`C_{iref}` the reference concentration for the same specie.

     In :cite:`Agency2015`, the concentration at saturation is adopted as reference concentration. In addition,
     by definition, the activity coefficient is assumed equal to one in two cases: when the related specie is a pure chemical
     element, and when it is very diluted. The activity of a pure element can then be defined as:
     
     :math:`\alpha_i=\frac{C_i}{C_{i(sat)}}`.

     About the chemical activity of lead in LBE, *lbh15* implements the correlation proposed by Gossé (2014)
     and written in chapter 3.3, part 3.3 of :cite:`Agency2015`.

..

  4. The aim is now to develop, for each possible dissolved metal, a correlation for the lower limit of the
     oxygen concentration that has the same structure as the equation 4.12, part 4.2.2 of :cite:`Agency2015`. Starting from the
     oxidation reaction equation (3), the following substitution is applied:

     :math:`\Delta_rG^0_{(T)}=-RT\ln{\left(\frac{\alpha_{Pb}\cdot\alpha_{Me_XO_Y}^{\frac{1}{Y}}}{\alpha_{PbO}\cdot\alpha_{Me{(dissolved)}}^{\frac{X}{Y}}}\right)}`,

     where the term :math:`\alpha_{Me_XO_Y}` can be considered equal to one: the lower limit is to be found of the oxygen
     concentration, thus the metal oxyde is considered very diluted.

     By considering the oxygen dissolved in the solution in the form of *PbO* below its saturation limit, as stated in :cite:`Agency2015`,
     thus taking the chemical activity of the dissolved oxygen equal to the chemical activity of the dissolved *PbO*, and by
     applying some transformations, one can obtain:

     :math:`\Leftrightarrow \quad \ln{\left( C_O \right)} = - \frac{X}{Y}\ln{\left(C_{Me}\right)} + \frac{X}{Y}\ln{\left(C_{Me}^{sat}\right)} + \frac{\Delta H^0_{(3)}}{2RT} - \frac{\Delta S^0_{(3)}}{2R} + \ln{\left(\alpha_{Pb}\right)} + \ln{\left(C_O^{sat}\right)}`  (4)

     In the above equation, the unknows are two, that is, the oxygen concentration :math:`C_O` and the concentration
     :math:`C_{Me}` of the dissolved metal, thus preventing the direct computation of the solution. For achieving
     a useful correlation, two strategies are proposed and adopted in *lbh15* the user can choose between. They differ
     on how they treat the chemical activity of the dissolved metal. The actual activities at the interface are
     influenced by how diffusion, convection and mass transfer phenomena interact in the liquid metal boundary layer.
     Ongoing researches are in progress, but currently the exact values for the chemical activities of the dissolved
     metal and of the oxygen are not known.

     a. The first approach is to consider the chemical activity of the dissolved metal equal to one.
        In this way, the first and the second terms of the right hand side of equation (4) become zero, enabling to
        compute the lower limit of the oxygen concentration directly through the following relation:

        :math:`\Leftrightarrow \quad C_O = \exp{\left(\frac{\Delta H^0_{(3)}}{2RT} - \frac{\Delta S^0_{(3)}}{2R} + \ln{\left(\alpha_{Pb}\right)} + \ln{\left(C_O^{sat}\right)}\right)}`,

        where:
  
        - :math:`\Delta H^0_{(3)}` and :math:`\Delta S^0_{(3)}` are extracted from table 4.2.2 of :cite:`Agency2015`;

        - :math:`C_O^{sat}` is computed by adopting the recommended coefficients from table 3.5.2 of :cite:`Agency2015`;

        - :math:`\alpha_{Pb}` is taken equal to one in pure Lead, while in LBE it is computed by adopting the
          correlation proposed by Gossé as indicated at page 146 of :cite:`Agency2015`.

     b. The second approach does not exploit any assumption. In order to make equation (4) solvable, the two unknowns
        :math:`C_O^{sat}` and :math:`C_{Me}` are collected into one single unknown, thus expressing equation (4) in terms
        of :math:`C_O  \cdot C_{Me}^{\frac{X}{Y}}`, as indicated in the following:

        :math:`\Leftrightarrow \quad C_O  \cdot C_{Me}^{\frac{X}{Y}} = \exp{\left(\frac{X}{Y}\ln{\left(C_{Me}^{sat}\right)} + \frac{\Delta H^0_{(3)}}{2RT} - \frac{\Delta S^0_{(3)}}{2R} + \ln{\left(\alpha_{Pb}\right)} + \ln{\left(C_O^{sat}\right)}\right)}`,

        where:

        - :math:`C_{Me}^{sat}` values are computed by using the data from table 3.5.1 of :cite:`Agency2015`;

        - :math:`\Delta H^0_{(3)}`, :math:`\Delta S^0_{(3)}`, :math:`C_O^{sat}` and :math:`\alpha_{Pb}` are computed as already
          indicated for the approach described above.

.. _ Ranges of validity:

Ranges of Validity
==================

As stated in the previous section, multiple correlations are involved in the computation of the lower limits of
oxygen concentration, each being valid over a specific temperature range. The temperature range of
validity specified in the *lbh15* package for each correlation is the most restrictive one.

In the following, the choices are detailed about the validity ranges that have been adopted:
  - For the lower limit correlations based on the saturation assumption (approach *a*), the lower temperature
    value is taken equal to the lower limit of the validity range of the oxygen solubility correlation,
    while the upper temperature value is taken equal to the upper limit of the validity range of the main
    oxides free enthalpy coefficients. The result is the [673;1000] *K* range.
  
  ..

  - For the lower limit of the oxygen concentration times the metal concentration raised to a certain exponent (approach *b*),
    the validity range is taken equal to that in the approach *a*, that is, [673;1000] *K*, but for the following correlations:

    - Concerning the chromium solubility in LBE given by Courouau in 2004, the upper limit of the validity range
      is taken equal to the upper limit of the validity range of the corresponding chromium solubility correlation, resulting in the [673;813] *K* range;

    ..

    - Concerning the chromium solubility in LBE given by Martynov in 1998, the upper limit of the validity range
      is taken equal to the upper limit of the validity range of the corresponding chromium solubility correlation, resulting in the [673;773] *K* range;

    ..

    - Concerning the nickel solubility in lead given by Gossé in 2014, the upper limit of the validity range
      is taken equal to the upper limit of the validity range of the corresponding nickel solubility correlation, resulting in the [673;917] *K* range;

    ..
    
    - Concerning the chromium solubility in lead given by Venkatraman in 1998 and by Alden in 1958, and the silicon solubility
      in lead extracted from *Tecdoc* (2002), there is no overlapping of the temperature validity ranges. It has then been decided
      to adopt the [673;1000] *K* range for analogy with the greatest amount of the other correlations. This is why the related
      correlations need to be used carefully.

.. _ Correlations adopted by default:

Correlations Adopted by Default
===============================

For most of the properties, correlations from different authors are available. This section provides a list of the
correlations chosen as the default ones in *lbh15*. For all the non-mentioned properties, only one correlation is
implemented since either it is the only one available or it is specifically recommended in :cite:`Agency2015`:

- *Gossé* correlation of 2014 for the solubility of iron, nickel and chromium in lead, LBE and bismuth;

..

- *Alcock* correlation of 1964 for the oxygen partial pressure divided by the oxygen concentration squared in lead;

..

- *Isecke* correlation of 1979 for the oxygen partial pressure divided by the oxygen concentration squared in bismuth;

..

- *Gromov* correlation of 1996 for the oxygen diffusivity in lead and in LBE;

..

- *Fitzner* correlation of 1964 for the oxygen diffusivity in bismuth.

..

The choice of the above default correlations has been driven by what recommended in :cite:`Agency2015` and by the temperature ranges.
In particular, since most of the liquid lead applications are working at low temperatures, the correlations are preferred whose validity ranges
are related to the lowest available temperature values and whose extension is the widest available.

The user is invited to check the ranges of validity of the correlations she/he is using to make sure they match with the specific
application requirements. In case other correlations are needed that are different from the ones already implemented in *lbh15*, please see
the "Advanced Usage" section.

.. YET TO CHECK
.. +++++++++
   Tutorials
   +++++++++
   
   This section contains an example of the application of the complete package.
   We chose to performed this tutorial considering a liquid lead system, in a cylindrical iron thank.
   
   This tutorial is aimed to compute:
     - the temperature variation over time
   
     - the level of the liquid metal over temperature
   
     - the oxygen concentration limits over temperature
   
     - the mean limit oxygen concentration over temperature
   
   
   The user can define:
     - the mass of the system
   
     - the initial temperature
   
     - the simulation duration
   
     - the power variation
   
     - the starting and ending time of this varition
   
     - the radius of the tank
   
   
   - The first step is to import all the modules needed and to set the constants:
   
     .. code-block:: python
   
       """Tutorial using thermophysical and thermochemical
       correlations of the lbh15 python package"""
       import numpy as np
       import matplotlib.pyplot as plt
       from lbh15 import Lead
   
   
       if __name__ == "__main__":
   
           # Setting of the constants
           T_0 = 683  # [K]
           SIMULATION_TIME = 100  # [s]
           STEP_SIZE = 0.1  # [s]
           MASS = 100  # [kg]
           #  Power variation
           NET_POWER = 43000  # [W]
           VARIATION_START = 20  # [s]
           VARIATION_END = 70  # [s]
           RADIUS = 1  # [m]
   
   - We then have to create all the arrays that will contain the values we are interested in:
   
     .. code-block:: python
   
       # Creation of the arrays
       # Array containing the time values
       time = np.arange(0, SIMULATION_TIME, STEP_SIZE)
       # Array containing the heat variation values
       heat_variation = np.zeros(len(time)-1)
       # Array containing the temperature values
       temperature = np.zeros_like(time)
       # Array containing the lower oxygen concentration values
       lower_oxygen_concentration = np.zeros_like(time)
       # Array containing the upper oxygen concentration values
       upper_oxygen_concentration = np.zeros_like(time)
       # Array containing the level of the liquid metal in the tank
       level = np.zeros_like(time)
   
   - Before starting the loop which wil computes our results, we have to initialize the temperature
     and the power variation, such that at each time step of the total variation time,
     the power will have the same variation value. 
   
     .. code-block:: python
   
           # Filling of the heat variation array,
           # computed according to the power variation
           VAR_START_IDX = int(VARIATION_START/STEP_SIZE)
           VAR_END_IDX = int(VARIATION_END/STEP_SIZE)
           heat_variation[VAR_START_IDX:VAR_END_IDX] = (
               NET_POWER * STEP_SIZE)
   
           # Initialization
           temperature[0] = T_0
           system = Lead(T=T_0)
           h_0 = system.h
           upper_oxygen_concentration[0] = system.o_sol
           lower_oxygen_concentration[0] = system.lim_fe_sat
           volume = MASS / system.rho
           level[0] = volume / (np.pi * (RADIUS**2))
   
           # Looping
           for i in range(1, len(time)):
               # Solving heat balance
               h_i = np.sum(heat_variation[0:i])/MASS + h_0
               # Creation of an object at a T temperature deduced from the h value
               system = Lead(h=h_i)
               temperature[i] = system.T
               # Updating the lower oxygen concentration
               lower_oxygen_concentration[i] = system.lim_fe_sat
               # Updating the upper oxygen concentration
               upper_oxygen_concentration[i] = system.o_sol
               # Updating the volume of the system
               volume = MASS / system.rho
               # Updating the level of the liquid metal
               level[i] = volume / (np.pi * (RADIUS**2))
   
   - Finally, we have to plot the graphs we are interested in. Here an example of what can be obtained:
    
   .. figure:: figures/tutorials.png
      :width: 700
   
   .. note:: This example can be used with Bismuth or LBE and considering an other metal than iron for the thank.
