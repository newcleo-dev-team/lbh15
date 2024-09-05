from typing import List
import numpy as np
from lbh15._decorators import range_warning
from lbh15.properties.interface import PropertyInterface
from scipy.constants import atm
from ..._commons import LEAD_MELTING_TEMPERATURE as T_m0_pb
from ..._commons import LEAD_BOILING_TEMPERATURE as T_b0_pb
from ..._commons import BISMUTH_MELTING_TEMPERATURE as T_m0_bi
from ..._commons import BISMUTH_BOILING_TEMPERATURE as T_b0_bi
from ..._commons import LBE_MELTING_TEMPERATURE as T_m0_lbe
from ..._commons import LBE_BOILING_TEMPERATURE as T_b0_lbe


class CadmiumVapourPressureLandolt1960(PropertyInterface):
        """
        Pure metallic *Cadmium Vapour Pressure* property class
        implementing the correlation by *landolt1960*.
        """
        @range_warning
        def correlation(self, T: float, p: float = atm,
                        verbose: bool = False) -> float:
            """
            Returns the value of the pure metallic *Cadmium Vapour Pressure* by
            applying the property correlation.
            Parameters
            ----------
            T : float
                Temperature in :math:`[K]`
            p : float, optional
                Pressure in :math:`[Pa]`, by default the atmospheric pressure
                value, i.e., :math:`101325.0 Pa`
            verbose : bool, optional
                `True` to tell the decorator to print a warning message in case of
                range check failing, `False` otherwise. By default, `False`
            Returns
            -------
            float:
                Vapour pressure in :math:`[Pa]`
            """
            return np.power(10, - 5711 / T - 1.0867 * np.log(T) + 13.78)
        
        @property
        def name(self) -> str:
            """
            str : Name of the property
            """
            return "p_0"
        
        @property
        def correlation_name(self) -> str:
            """
            str : Name of the correlation
            """
            return "landolt1960"
        
        @property
        def units(self) -> str:
            """
            str : Vapour pressure unit
            """
            return "[Pa]"
        
        @property
        def long_name(self) -> str:
            """
            str : Cadmium vapour pressure long name
            """
            return "Vapour pressure of Cadmium"
        
        @property
        def description(self) -> str:
            """
            str : Cadmium vapour pressure description
            """
            return f"{self.long_name} in its pure metallic form."
        
        @property
        def range(self) -> List[float]:
            """
            List[float] : Temperature validity range of the Cadmium
            vapour pressure correlation function
            """
            return [min(T_m0_pb, T_m0_bi, T_m0_lbe), 
                    max(T_b0_pb, T_b0_bi, T_b0_lbe)]