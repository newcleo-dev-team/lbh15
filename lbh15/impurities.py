"""Module with the definition of some compounds properties, in their pure
metallic form, for contamination assessment."""
import sys
import warnings
import numpy as np
import inspect
from abc import ABC, abstractmethod
from typing import Dict, List, Type, Union
from scipy.constants import atm
from lbh15._decorators import range_warning
from ._commons import LEAD_MELTING_TEMPERATURE as T_m0_pb
from ._commons import LEAD_BOILING_TEMPERATURE as T_b0_pb
from ._commons import BISMUTH_MELTING_TEMPERATURE as T_m0_bi
from ._commons import BISMUTH_BOILING_TEMPERATURE as T_b0_bi
from ._commons import LBE_MELTING_TEMPERATURE as T_m0_lbe
from ._commons import LBE_BOILING_TEMPERATURE as T_b0_lbe
from .properties.interface import PropertyInterface



class MetallicImpurities:
    """
    Class collecting all radiation-induced metallic impurities.
    """
    def __init__(self):

        def is_valid(obj):
            '''
            Predicate for filtering the modules to load
            '''
            return inspect.isclass(obj) and obj is not SingleImpurity \
                and obj is not PropertyInterface and issubclass(obj, SingleImpurity)
        
        self.__impurities_dict = {name : metallic_impurity() for name, metallic_impurity in inspect.getmembers(sys.modules[__name__], is_valid)}

    @property
    def impurities_list(self) -> List[str]:
            '''
            List : list of the available impurities' names
            '''
            return [impurity for impurity in self.__impurities_dict.keys()]

    @property
    def impurities(self) -> Dict[str, PropertyInterface]:
            '''
            List : list of the available impurities' names
            '''
            return self.__impurities_dict




class SingleImpurity(ABC):

    _properties = None
    
    @property
    def name(self) -> str:
        """
        str : Name of the property
        """
        return type(self).__name__
    
    def get_correlations(self) -> List[str]:
        """
        Returns the correlations' names for Polonium.

        Returns
        -------
        Type[PropertyInterface]
            Correlations' names for Polonium.
        """
        return [item.correlation_name for item in self._properties.value()]  
    
    def _get_properties(self, module_name: str) -> Dict[str, PropertyInterface]:

        def is_valid(obj):
            '''
            Predicate for filtering the modules to load
            '''
            return inspect.isclass(obj) and issubclass(obj, PropertyInterface) \
                and obj is not PropertyInterface
        
        return {metallic_prop().name : metallic_prop() for _, metallic_prop in inspect.getmembers(sys.modules[module_name], is_valid)}
    
    @property
    def properties(self) -> Dict[str, PropertyInterface]:
        return self._properties





class Polonium(SingleImpurity):

    _properties_module: str = 'lbh15.properties.impurities_properties.polonium_properties'

    def __init__(self):

        super().__init__()
        self._properties: Dict[str, PropertyInterface] = self._get_properties(self._properties_module)

    @property
    def name(self) -> str:
        return "[Po]"
    
    


class Mercury(SingleImpurity):

    _properties_module: str = 'lbh15.properties.impurities_properties.mercury_properties'

    def __init__(self):

        super().__init__()
        self._properties: Dict[str, PropertyInterface] = self._get_properties(self._properties_module)

    @property
    def name(self) -> str:
        return "[Hg]"

    
class Thallium(SingleImpurity):

    _properties_module: str = 'lbh15.properties.impurities_properties.thallium_properties'

    def __init__(self):

        super().__init__()
        self._properties: Dict[str, PropertyInterface] = self._get_properties(self._properties_module)


    @property
    def name(self) -> str:
        return "[Tl]"



class Cadmium(SingleImpurity):

    _properties_module: str = 'lbh15.properties.impurities_properties.cadmium_properties'

    def __init__(self):

        super().__init__()
        self._properties: Dict[str, PropertyInterface] = self._get_properties(self._properties_module)

    @property
    def name(self) -> str:
        return "[Cd]"


class Caesium(SingleImpurity):

    _properties_module: str = 'lbh15.properties.impurities_properties.caesium_properties'

    def __init__(self):

        super().__init__()
        self._properties: Dict[str, PropertyInterface] = self._get_properties(self._properties_module)

    @property
    def name(self) -> str:
        return "[Cs]"
    

class Rubidium(SingleImpurity):

    _properties_module: str = 'lbh15.properties.impurities_properties.rubidium_properties'

    def __init__(self):

        super().__init__()
        self._properties: Dict[str, PropertyInterface] = self._get_properties(self._properties_module)

    @property
    def name(self) -> str:
        return "[Rb]"


