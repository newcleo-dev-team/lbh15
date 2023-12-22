.. raw:: latex

   \setcounter{secnumdepth}{-1}

=============
Release Notes
=============

This section collects all the modifications included in the :math:`2.0.0` release of the `lbh15` package.
They are tracked as issues that have been managed during the development process, and they are subdivided into
three lists according to the labels assigned to them. To access the entire issue history and comments and commits
related to each one, please look at https://github.com/newcleo-dev-team/lbh15.

1. **Enhancements**

   - Remove typecheck for performance reasons - **#129**

   - Review for v2.0.0 release - **#120**

   - Tutorial: code and doc - **#118**

   - Allow to deeply copy *LiquidMetal* objects - **#115**

   - Need for a test covering all temperatures - **#113**

   - :code:`set_custom_properties_path` Improvement - **#110**

   - Making element-wise the correlation functions of all properties - **#103**

   - Horner's Scheme - **#100**

   - Update :code:`test_custom_properties`` to test correct assignment of custom properties to different liquid metal classes - **#86**

   - Thermochemical Modules Corrections and Improvements - **#76**

   - Constants Into Commons - **#71**

   - :code:`change_correlation_to_use()` Method (:code:`_lbh15.py`) Improvement - **#69**

   - :code:`__assign_p()` Method (:code:`_lbh15.py`) Improvement - **#68**

   - :code:`__compute_T()` Method (:code:`_lbh15.py`) Improvement - **#67**

   - :code:`__check_temperature()` Method (:code:`_lbh15.py`) Improvement - **#66**

   - :code:`__fill_class_attributes` Method (:code:`_lbh15.py`) Improvement - **#65**

   - :code:`__check_properties()` Method (:code:`_lbh15.py`) Improvement - **#64**

   - :code:`__add_property()` Method (:code:`_lbh15.py`) Improvement - **#63**

   - :code:`__fill_instance_properties()` Method (:code:`_lbh15.py`) Improvement - **#62**

   - Attribute Storing the Available Correlations (:code:`_lbh15.py`) - **#61**

   - Attribute Storing All Property Objects (:code:`_lbh15.py`) - **#60**

   - :code:`__load_custom_properties()` Method (:code:`_lbh15.py`) Improvement - **#59**

   - :code:`__custom_properties_path` Attribute (:code:`_lbh15.py`) Modification - **#58**

   - :code:`__property_list()` Method (:code:`_lbh15.py`) Improvement - **#57**

   - :code:`_properties` Dict (:code:`_lbh15.py`) Keys Modification - **#56**

   - :code:`is_injective()` Method (:code:`interface.py`) Name - **#54**

   - :code:`info()` Method (:code:`interface.py`) Improvement - **#53**

   - :code:`compute_bounds` Method (:code:`interface.py`) Improvement - **#52**

   - Type Hints and Type Checking - **#49**
 
   - Define two new sections of the documentation to give the user more insights about thermochemical properties and their usage - **#48**

   - Update the documentation to show the new thermochemical properties - **#47**

   - Set the default correlations to use for the thermochemical properties of all liquid metals - **#44**

   - Define module containing oxygen limits correlations related to Lead - **#42**

   - Define module containing thermochemical correlations related to Lead - **#41**

   - Define module containing diffusivity of elements in Lead - **#40**

   - Define module containing solubility of elements in Lead - **#39**

   - Define module containing oxygen limits correlations related to LBE - **#38**

   - Define module containing thermochemical correlations related to LBE - **#37**

   - Define module containing diffusivity of elements in LBE - **#36**

   - Define module containing solubility of elements in LBE - **#35**

   - Define module containing thermochemical properties in Bismuth - **#34**

   - Define module containing diffusivity of elements in Bismuth - **#33**

   - Modify the :code:`test_lbh15_fromX` so that it dynamically tests the initialization from all the available properties - **#31**

   - Modifiy liquid metal classes to read thermochemical properties - **#30**

   - Properties module attribute of :code:`LiquidMetalInterface`` must be a dictionary to handle multiple modules - **#29**

   - Modify the properties sub-package for the implementation of thermochemical properties - **#28**

   - Define solubility of elements in Bismuth - **#27**

   - Define iron solubility property classes for Bismuth - **#25**

   - provide :code:`pyproject.toml` - **#22**

   - Support of thermo-chemical properties - **#7**

..

2. **Documentation**
   
   - Regularization of :code:`\displaystyle` equations and :code:`\Big` modifiers - **#126**

   - Add equation automatic numbering to Sphinx - **#124**

   - Use :code:`mhchem` *LaTeX* package for chemical equations - **#123**

   - Tutorial: code and doc	- **#118**

   - :code:`lbh15` within IAEA Oncore Codes List - **#73**

   - Define two new sections of the documentation to give the user more insights about thermochemical properties and their usage - **#48**

   - Update the documentation to show the new thermochemical properties - **#47**

   - Update the API guide of the documentation to include the new thermochemical properties - **#43**

   - Use the tex corporate class when generating the pdf documentation - **#24**

   - Enable :code:`latexpdf` to generate the documentation - **#21**

..

3. **Bugs**

   - Allow to deeply copy *LiquidMetal* objects - **#115**
  
   - Warnings management - **#107**

   - Add the pressure info inside the :code:`__repr__`` method - **#106**

   - Fix initialization of liquid metal object from thermochemical properties - **#83**

   - Thermochemical Modules Corrections and Improvements - **#76**

   - Fix build of online documentation - **#72**

   - :code:`__check_properties()` Method (:file:`_lbh15.py`) Improvement - **#64**

   - Attribute Change within :file:`_lbh15.py` - **#55**

   - Bug into "range_warning" Method ("interface.py") - **#51**

   - Fix loading of duplicate properties - **#45**

   - Modify the :file:`test_lbh15_fromX.py` so that it dynamically tests the initialization from all the available properties - **#31**

Some issues are yet to be solved. Here in the following the list of currently open issues subdivided according to their labels:

1. **Enhancements**

   - Refactor physical constants variables with dataclasses - **#122**

   - Refactor path usages with pathlib.Path objects - **#121**

   - Speed test addition - **#50**

   - Support corrosion and interaction with steel - **#9**

   - Revise properties considering radiation effects under exposure - **#8**

2. **Documentation**

   - :code:`graphivz`-generated diagrams - **#125**

3. **Question**   
  
   - Investigating asynchronous approach - **#102**

4. **Help wanted**   

   - :code:`__repr__()` Method (:code:`_lbh15.py`) Improvement - **#70**
   