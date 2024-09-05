from typing import List
import numpy as np
from lbh15._decorators import range_warning
from lbh15.properties.interface import PropertyInterface
from scipy.constants import atm


class PoloniumVapourPressureAbakumov1974a(PropertyInterface):
        """
        Pure metallic *Polonium Vapour Pressure* property class
        implementing the correlation by *abakumov1974a*.
        """
        @range_warning
        def correlation(self, T: float, p: float = atm,
                        verbose: bool = False) -> float:
            """
            Returns the value of the Pure metallic *Polonium Vapour Pressure* by
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
            return np.power(10, - 5440 / T + 9.46)
        
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
            return "abakumov1974a"
        
        @property
        def units(self) -> str:
            """
            str : Vapour pressure unit
            """
            return "[Pa]"
        
        @property
        def long_name(self) -> str:
            """
            str : Polonium vapour pressure long name
            """
            return "Vapour pressure of Polonium"
        
        @property
        def description(self) -> str:
            """
            str : Polonium vapour pressure description
            """
            return f"{self.long_name} in its pure metallic form."
        
        @property
        def range(self) -> List[float]:
            """
            List[float] : Temperature validity range of the Polonium
            vapour pressure correlation function
            """
            return [641, 877]
        
#class PoloniumVapourPressureBrooks1955(PropertyInterface):
#    """
#    Pure metallic *Polonium Vapour Pressure* property class
#    implementing the correlation by *brooks1955*.
#    """
#    @range_warning
#    def correlation(self, T: float, p: float = atm,
#                    verbose: bool = False) -> float:
#        """
#        Returns the value of the pure metallic *Polonium Vapour Pressure* by
#        applying the property correlation.
#        Parameters
#        ----------
#        T : float
#            Temperature in :math:`[K]`
#        p : float, optional
#            Pressure in :math:`[Pa]`, by default the atmospheric pressure
#            value, i.e., :math:`101325.0 Pa`
#        verbose : bool, optional
#            `True` to tell the decorator to print a warning message in case of
#            range check failing, `False` otherwise. By default, `False`
#        Returns
#        -------
#        float:
#            Vapour pressure in :math:`[Pa]`
#        """
#        return np.power(10, - 5377.8 / T + 9.3594)
#    
#    @property
#    def name(self) -> str:
#        """
#        str : Name of the property
#        """
#        return "p_0"
#    
#    @property
#    def correlation_name(self) -> str:
#        """
#        str : Name of the correlation
#        """
#        return "brooks1955"
#    
#    @property
#    def units(self) -> str:
#        """
#        str : Vapour pressure unit
#        """
#        return "[Pa]"
#    
#    @property
#    def long_name(self) -> str:
#        """
#        str : Polonium vapour pressure long name
#        """
#        return "Vapour pressure of Polonium"
#    
#    @property
#    def description(self) -> str:
#        """
#        str : Polonium vapour pressure description
#        """
#        return f"{self.long_name} in its pure metallic form."
#    
#    @property
#    def range(self) -> List[float]:
#        """
#        List[float] : Temperature validity range of the Polonium
#        vapour pressure correlation function
#        """
#        return [711, 1018]