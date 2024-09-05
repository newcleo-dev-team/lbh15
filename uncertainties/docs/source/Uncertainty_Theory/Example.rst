.. raw:: latex

   \setcounter{secnumdepth}{3}

============================
Example on Metallic Polonium
============================

The vapour pressure of Po is described by the equation :eq:`met_po`.
This equation can be re-written in the following form :

.. math:: 
   f(T) = 10^{-\frac{a\pm\sigma_{a}}{T} + b\pm\sigma_{b}}
   :label: f_p_po

.. math:: 
    \begin{aligned}
    \text{where $a=5440, \sigma_{a}=60, b=9.46, \sigma_{b}=0.05$.}
    \end{aligned}

By applying :eq:`prop_uncer`, the uncertainty for the vapor pressure value is retrieved:

.. math::
    \sigma_{P_{Po}\degree} = f(T)\ln{10}\sqrt{\frac{\sigma_{a}^2}{T^2} + \sigma_{b}^2}
    :label: sigma_p_po

In next sections, the validity of this formula is provided.
