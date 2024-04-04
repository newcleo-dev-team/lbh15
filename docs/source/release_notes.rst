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

   - Increase abstraction level of `OxygenDiffusivityInterface` and `IronSolubility` classes - **#160**

   - Including all the dependencies for doc building and testing into toml and `setup.py` - **#155**

   - Checking separator when calling `set_custom_properties_path()` method - **#153**

..

2. **Documentation**
   
   - Review for v2.1.0 release - **#179**

   - Add monospace expression of all liquid metal properties - **#159**

   - Unnecessary page in the html doc - **#158**

   - Checking the way the correlations provided with different validity ranges have been selected - **#157**

   - Refactor *Advanced Usage* section in the doc and correct errors therein - **156**

   - Unnecessary use of `pprint` - **#154**

   - Add contributing document - **#150**

   - Clarify the statement of need	- **#148**

..

3. **Bugs**

   - `print()` method not working - **#152**

Some issues are yet to be solved. Here in the following the list of currently open issues subdivided according to their labels:

1. **Enhancements**

   - Testing with `pytest` not working - **#175**

   - Introduce the ability to restore the default correlations - **#146**

   - Giving the user the possibility to choose which module to load - **#137**

   - Refactor physical constants variables with dataclasses - **#122**

   - Refactor path usages with pathlib.Path objects - **#121**

   - Speed test addition - **#50**

   - Support corrosion and interaction with steel - **#9**

   - Revise properties considering radiation effects under exposure - **#8**

2. **Documentation**

   - Include automatic tests description into doc for Verification purposes - **#138**

   - :code:`graphivz`-generated diagrams - **#125**

3. **Question**   

   - New elements and correlations for lead thermochemistry - **#134**

   - Investigating asynchronous approach - **#102**

4. **Help wanted**   

   - :code:`__repr__()` Method (:code:`_lbh15.py`) Improvement - **#70**
