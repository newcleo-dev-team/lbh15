.. raw:: latex

   \setcounter{secnumdepth}{3}

============================
Propagation of uncertainties
============================

According to the *Evaluation of measurement data* :cite:`jcgm2008evaluation`, the formulae of the propagation of uncertainties is:

.. math:: 
   u_{c}^{2}(y) = \displaystyle\sum_{i=1}^{N} (\frac{\partial f}{\partial x_i})^{2}  u^{2}(x_{i})
  :label: prop_uncer

where :

.. math:: 
   \begin{aligned}
   & \text{$y$ is the measurement resulting from the composition of each single measurement $x_{i}$,}\\
   & \text{with $y=f(x_{1}, x_{2}, ..., x_{N});$}\\
   & \text{$u_{c}$ is the standard deviation of the measurement $y$;}\\
   & \text{$f$ is the correlation between $y$ and the $x_{i}$;}\\
   & \text{$u$ is the standard deviation of each single measurement $x_{i}.$}
   \end{aligned}

In the following section, the theory is illustrated by taking the correlation for the vapour pressure of Polonium as an example.
