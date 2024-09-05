uncertainties\_dict module
==========================

Before adding our uncertainty calcuator in lbh15, we decided to implement it in local. The code uses dictionnaries written in an other module, to help preparing the necessary modularity and adaptability in order to introduce it in lbh15 package.
The dictionnaries of properties which uncertainties can be calculated are of the following form:

   function_range : dict
                 Dictionnary of the correlation of the property (str)
                 and the range of temperature (tuple)
   params : dict
         Dictionary of the parameters and their values
   sigmas : dict
         Dictionary of the uncertainties' parameters
         and their values  

.. module:: uncertainties_dict

.. automodule:: uncertainties_dict
   :members:
   :undoc-members:
   :show-inheritance:
   :noindex:
