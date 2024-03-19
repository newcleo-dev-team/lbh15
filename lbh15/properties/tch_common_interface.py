"""Module with the definition of common property interfaces
for thermochemical properties"""
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
    Liquid metal *Iron diffusivity* property abstract class.
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
    Liquid metal *molar enthalpy variation* property abstract class.
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
    Liquid metal *molar entropy variation* property abstract class.
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


class GibbsFreeEnergyInterface(PropertyInterface):
    """
    Liquid metal *Gibbs free energy variation* property abstract class.
    """
    @property
    def name(self) -> str:
        """
        str : Name of the property
        """
        return "G"

    @property
    def units(self) -> str:
        """
        str : Gibbs free energy unit
        """
        return "[J/mol]"

    @property
    def long_name(self) -> str:
        """
        str : Gibbs free energy long name
        """
        return "Gibbs free energy variation"


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
    Liquid metal *Oxygen solubility* property abstract class.
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


class LowerLimitSaturationIronInterface(PropertyInterface):
    """
    *Lower limit of Oxygen concentration* to promote a
    protective oxide film in liquid metal considering
    *Iron at its saturation concentration* property abstract class.
    """
    @property
    def name(self) -> str:
        """
        str : Name of the property
        """
        return "lim_fe_sat"

    @property
    def units(self) -> str:
        """
        str : Oxygen concentration lower limit unit
        """
        return "[wt.%]"

    @property
    def long_name(self) -> str:
        """
        str : Oxygen concentration lower limit long name
        """
        return ("Oxygen concentration lower limit for"
                "iron at its saturation concentration")


class LowerLimitSaturationChromiumInterface(PropertyInterface):
    """
    *Lower limit of Oxygen concentration* to promote a
    protective oxide film in liquid metal considering
    *Chromium at its saturation concentration* property abstract class.
    """
    @property
    def name(self) -> str:
        """
        str : Name of the property
        """
        return "lim_cr_sat"

    @property
    def units(self) -> str:
        """
        str : Oxygen concentration lower limit unit
        """
        return "[wt.%]"

    @property
    def long_name(self) -> str:
        """
        str : Oxygen concentration lower limit long name
        """
        return ("Oxygen concentration lower limit for"
                " chromium at its saturation concentration")


class LowerLimitSaturationNickelInterface(PropertyInterface):
    """
    *Lower limit of Oxygen concentration* to promote a
    protective oxide film in liquid metal considering
    *Nickel at its saturation concentration* property abstract class.
    """
    @property
    def name(self) -> str:
        """
        str : Name of the property
        """
        return "lim_ni_sat"

    @property
    def units(self) -> str:
        """
        str : Oxygen concentration lower limit unit
        """
        return "[wt.%]"

    @property
    def long_name(self) -> str:
        """
        str : Oxygen concentration lower limit long name
        """
        return ("Oxygen concentration lower limit for"
                " nickel at its saturation concentration")


class LowerLimitSaturationSiliconInterface(PropertyInterface):
    """
    *Lower limit of Oxygen concentration* to promote a
    protective oxide film in liquid metal considering
    *Silicon at its saturation concentration* property abstract class.
    """
    @property
    def name(self) -> str:
        """
        str : Name of the property
        """
        return "lim_si_sat"

    @property
    def units(self) -> str:
        """
        str : Oxygen concentration lower limit unit
        """
        return "[wt.%]"

    @property
    def long_name(self) -> str:
        """
        str : Oxygen concentration lower limit long name
        """
        return ("Oxygen concentration lower limit for"
                " silicon at its saturation concentration")


class LowerLimitSaturationAluminiumInterface(PropertyInterface):
    """
    *Lower limit of Oxygen concentration* to promote a
    protective oxide film in liquid metal considering
    *Aluminium at its saturation concentration* property abstract class.
    """
    @property
    def name(self) -> str:
        """
        str : Name of the property
        """
        return "lim_al_sat"

    @property
    def units(self) -> str:
        """
        str : Oxygen concentration lower limit unit
        """
        return "[wt.%]"

    @property
    def long_name(self) -> str:
        """
        str : Oxygen concentration lower limit long name
        """
        return ("Oxygen concentration lower limit for"
                " aluminium at its saturation concentration")


class LowerLimitChromiumInterface(PropertyInterface):
    """
    *Lower limit of oxygen concentration* to promote a
    protective oxide film times the *Chromium concentration*
    raised to :math:`2/3` in liquid metal property abstract class.
    """
    @property
    def name(self) -> str:
        """
        str : Name of the property
        """
        return "lim_cr"

    @property
    def units(self) -> str:
        """
        str : Oxygen concentration lower limit unit
        """
        return "[wt.%]"

    @property
    def long_name(self) -> str:
        """
        str : Oxygen concentration lower limit long name
        """
        return ("Oxygen concentration lower limit times"
                " chromium concentration raised to 2/3")


class LowerLimitNickelInterface(PropertyInterface):
    """
    *Lower limit of oxygen concentration* to promote a
    protective oxide film times the *Nickel concentration*
    in liquid metal property abstract class.
    """
    @property
    def name(self) -> str:
        """
        str : Name of the property
        """
        return "lim_ni"

    @property
    def units(self) -> str:
        """
        str : Oxygen concentration lower limit unit
        """
        return "[wt.%]"

    @property
    def long_name(self) -> str:
        """
        str : Oxygen concentration lower limit long name
        """
        return ("Oxygen concentration lower limit times"
                " nickel concentration")


class LowerLimitIronInterface(PropertyInterface):
    """
    *Lower limit of oxygen concentration* to promote a
    protective oxide film times the *Iron concentration*
    raised to :math:`3/4` in liquid metal property abstract class.
    """
    @property
    def name(self) -> str:
        """
        str : Name of the property
        """
        return "lim_fe"

    @property
    def units(self) -> str:
        """
        str : Oxygen concentration lower limit unit
        """
        return "[wt.%]"

    @property
    def long_name(self) -> str:
        """
        str : Oxygen concentration lower limit long name
        """
        return ("Oxygen concentration lower limit times"
                " iron concentration raised to 3/4")
