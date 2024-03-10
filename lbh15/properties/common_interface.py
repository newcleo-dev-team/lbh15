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


class IronDiffusivityInterface(PropertyInterface):
    """
    Liquid metal *Iron diffusivity* property class.
    """
    @property
    def name(self) -> str:
        """
        str : Name of the property
        """
        return "fe_dif"

    @property
    def units(self) -> str:
        """
        str : Iron diffusivity unit
        """
        return "[m^2.s^-1]"

    @property
    def long_name(self) -> str:
        """
        str : Iron diffusivity long name
        """
        return "iron diffusivity"


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


class MolarEnthalpyInterface(PropertyInterface):
    """
    Liquid metal *molar enthalpy variation* property class.
    """
    @property
    def name(self) -> str:
        """
        str : Name of the property
        """
        return "H"

    @property
    def units(self) -> str:
        """
        str : Molar enthalpy variation unit
        """
        return "[J.mol^-1]"

    @property
    def long_name(self) -> str:
        """
        str : Molar enthalpy variation long name
        """
        return "molar enthalpy variation"


class MolarEntropyInterface(PropertyInterface):
    """
    Liquid metal *molar entropy variation* property class.
    """
    @property
    def name(self) -> str:
        """
        str : Name of the property
        """
        return "S"

    @property
    def units(self) -> str:
        """
        str : Molar entropy variation unit
        """
        return "[J/(mol.K)]"

    @property
    def long_name(self) -> str:
        """
        str : Molar entropy variation long name
        """
        return "molar entropy variation"


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


class ChromiumSolubilityInterface(PropertyInterface):
    """
    Liquid metal *Chromium solubility* property abstract class.
    """
    @property
    def name(self) -> str:
        """
        str : Name of the property
        """
        return "cr_sol"

    @property
    def units(self) -> str:
        """
        str : Chromium solubility unit
        """
        return "[wt.%]"

    @property
    def long_name(self) -> str:
        """
        str : Chromium solubility long name
        """
        return "chromium solubility"


class OxygenSolubilityInterface(PropertyInterface):
    """
    Liquid metal *Oxygen solubility* property class.
    """
    @property
    def name(self) -> str:
        """
        str : Name of the property
        """
        return "o_sol"

    @property
    def units(self) -> str:
        """
        str : Oxygen solubility unit
        """
        return "[wt.%]"

    @property
    def long_name(self) -> str:
        """
        str : Oxygen solubility long name
        """
        return "oxygen solubility"
