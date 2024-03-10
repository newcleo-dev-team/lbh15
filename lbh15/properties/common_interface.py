"""
Module with the definition of common property interfaces"""
from .interface import PropertyInterface


class OxygenDiffusivityInterface(PropertyInterface):
    """
    Liquid metal *Oxygen diffusivity* property abstract class.
    """
    @property
    def name(self) -> str:
        """
        str : Name of the property
        """
        return "o_dif"

    @property
    def units(self) -> str:
        """
        str : Oxygen diffusivity unit
        """
        return "[m^2.s^-1]"

    @property
    def long_name(self) -> str:
        """
        str : Oxygen diffusivity long name
        """
        return "oxygen diffusivity"


class OxygenPartialPressureInterface(PropertyInterface):
    """
    *Oxygen partial pressure in liquid metal divided by the
    Oxygen concentration in liquid metal squared* property abstract class.
    """
    @property
    def name(self) -> str:
        """
        str : Name of the property
        """
        return "o_pp"

    @property
    def units(self) -> str:
        """
        str : Oxygen partial pressure in liquid metal divided by the
        Oxygen concentration in liquid metal squared unit
        """
        return "[Pa.wt.%^-2]"

    @property
    def long_name(self) -> str:
        """
        str : Oxygen partial pressure in liquid metal divided by the
        Oxygen concentration in liquid metal squared long name
        """
        return ("Oxygen partial pressure divided by the"
                " oxygen concentration squared")


class IronSolubilityInterface(PropertyInterface):
    """
    Liquid metal *Iron solubility* property abstract class.
    """
    @property
    def name(self) -> str:
        """
        str : Name of the property
        """
        return "fe_sol"

    @property
    def units(self) -> str:
        """
        str : Iron solubility unit
        """
        return "[wt.%]"

    @property
    def long_name(self) -> str:
        """
        str : Iron solubility long name
        """
        return "iron solubility"


class NickelSolubilityInterface(PropertyInterface):
    """
    Liquid metal *Nickel solubility* property abstract class.
    """
    @property
    def name(self) -> str:
        """
        str : Name of the property
        """
        return "ni_sol"

    @property
    def units(self) -> str:
        """
        str : Nickel solubility unit
        """
        return "[wt.%]"

    @property
    def long_name(self) -> str:
        """
        str : Nickel solubility long name
        """
        return "nickel solubility"
