"""Module with the definition of common property interfaces
for thermophysical properties"""
from .interface import PropertyInterface


class SaturationVapourPressureInterface(PropertyInterface):
    """
    Liquid metal *saturation vapour pressure* property abstract class.
    """
    @property
    def units(self) -> str:
        """
        str : Saturation vapour pressure unit
        """
        return "[Pa]"

    @property
    def long_name(self) -> str:
        """
        str : Saturation vapour pressure long name
        """
        return "saturation vapour pressure"


class SurfaceTensionInterface(PropertyInterface):
    """
    Liquid metal *surface tension* property abstract class.
    """
    @property
    def units(self) -> str:
        """
        str : Surface tension unit
        """
        return "[N/m]"

    @property
    def long_name(self) -> str:
        """
        str : Surface tension long name
        """
        return "surface tension"


class DensityInterface(PropertyInterface):
    """
    Liquid metal *density* property abstract class.
    """
    @property
    def units(self) -> str:
        """
        str : Density unit
        """
        return "[kg/m^3]"

    @property
    def long_name(self) -> str:
        """
        str : Density long name
        """
        return "density"


class ThermalExpansionInterface(PropertyInterface):
    """
    Liquid metal *thermal expansion coefficient* property abstract class.
    """
    @property
    def units(self) -> str:
        """
        str : Thermal expansion coefficient unit
        """
        return "[1/K]"

    @property
    def long_name(self) -> str:
        """
        str : Thermal expansion coefficient long name
        """
        return "thermal expansion coefficient"


class SpeedOfSoundInterface(PropertyInterface):
    """
    Liquid metal *sound velocity* property abstract class.
    """
    @property
    def units(self) -> str:
        """
        str : Sound velocity unit
        """
        return "[m/s]"

    @property
    def long_name(self) -> str:
        """
        str : Sound velocity long name
        """
        return "sound velocity"


class IsentropicCompressibilityInterface(PropertyInterface):
    """
    Liquid metal *isentropic compressibility* property abstract class.
    """
    @property
    def units(self) -> str:
        """
        str : Isentropic compressibility unit
        """
        return "[1/Pa]"

    @property
    def long_name(self) -> str:
        """
        str : Isentropic compressibility long name
        """
        return "isentropic compressibility"


class SpecificHeatInterface(PropertyInterface):
    """
    Liquid metal *specific heat capacity* property abstract class.
    """
    @property
    def correlation_name(self) -> str:
        """
        str : Name of the correlation
        """
        return "imbeni1998"

    @property
    def is_injective(self) -> bool:
        """
        bool : `True` if the correlation is injective,
        `False` otherwise.
        """
        return False

    @property
    def units(self) -> str:
        """
        str : Specific heat capacity unit
        """
        return "[J/(kg*K)]"

    @property
    def long_name(self) -> str:
        """
        str : Specific heat capacity long name
        """
        return "specific heat capacity"


class SpecificEnthalpyInterface(PropertyInterface):
    """
    Liquid metal *specific enthalpy* property abstract class.
    """
    @property
    def units(self) -> str:
        """
        str : Specific enthalpy unit
        """
        return "[J/kg]"

    @property
    def long_name(self) -> str:
        """
        str : Specific enthalpy long name
        """
        return "specific enthalpy"


class DynamicViscosityInterface(PropertyInterface):
    """
    Liquid metal *dynamic viscosity* property abstract class.
    """
    @property
    def units(self) -> str:
        """
        str : Dynamic viscosity unit
        """
        return "[Pa*s]"

    @property
    def long_name(self) -> str:
        """
        str : Dynamic viscosity long name
        """
        return "dynamic viscosity"


class ElectricalResistivityInterface(PropertyInterface):
    """
    Liquid metal *electrical resistivity* property abstract class.
    """
    @property
    def units(self) -> str:
        """
        str : Electrical resistivity unit
        """
        return "[Ohm*m]"

    @property
    def long_name(self) -> str:
        """
        str : Electrical resistivity long name
        """
        return "electrical resistivity"


class ThermalConductivityInterface(PropertyInterface):
    """
    Liquid metal eutectic *thermal conductivity* property class.
    """

    @property
    def units(self) -> str:
        """
        str : Thermal conductivity unit
        """
        return "[W/(m*K)]"

    @property
    def long_name(self) -> str:
        """
        str : Thermal conductivity long name
        """
        return "thermal conductivity"
