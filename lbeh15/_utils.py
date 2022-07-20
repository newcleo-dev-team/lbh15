import numpy as np
from ._lbeh15 import LEAD_MELTING_TEMPERATURE
from ._lbeh15 import BISMUTH_MELTING_TEMPERATURE
from ._lbeh15 import LBE_MELTING_TEMPERATURE
from ._lbeh15 import LEAD_KEYWORD, BISMUTH_KEYWORD
from ._lbeh15 import LBE_KEYWORD


def p_s_initializer(p_s):
    """
    Returns a temperature guess according to the value
    of the saturation vapour pressure

    Parameters
    ----------
    p_s : float
        saturation vapour pressure in [Pa]

    Returns
    -------
    rvalue : float
        Temperature guess in [K]
    """
    rvalue = 0
    if p_s < 1e-2:
        rvalue = 800
    elif p_s >= 1e-2 and p_s < 1e2:
        rvalue = 1200
    else:
        rvalue = 2000

    return rvalue


def p_s(T, fluid):
    """
    Computes fluid saturation vapour pressure in [Pa].

    Parameters
    ----------
    T : float
        temperature in [K]
    fluid : str
        fluid for which calculation shall be performed,
        can be one among lead, bismuth or lbe
    """
    if fluid == LEAD_KEYWORD:
        return 5.76e9 * np.exp(-22131/T)
    elif fluid == BISMUTH_KEYWORD:
        return 2.67e10 * np.exp(-22858/T)
    elif fluid == LBE_KEYWORD:
        return 1.22e10 * np.exp(-22552/T)
    else:
        raise ValueError("Fluid can be one among: {:s},"
                         "{:s}, {:s}. {:s} was provided"
                         .format(LEAD_KEYWORD, BISMUTH_KEYWORD,
                                 LBE_KEYWORD, fluid))


def sigma(T, fluid):
    """
    Computes fluid surface tension in [N/m].

    Parameters
    ----------
    T : float
        temperature in [K]
    fluid : str
        fluid for which calculation shall be performed,
        can be one among lead, bismuth or lbe
    """
    if fluid == LEAD_KEYWORD:
        return (525.9 - 0.113*T)*1e-3
    elif fluid == BISMUTH_KEYWORD:
        return (420.8 - 0.81*T)*1e-3
    elif fluid == LBE_KEYWORD:
        return (448.5 - 0.0799*T)*1e-3
    else:
        raise ValueError("Fluid can be one among: {:s},"
                         "{:s}, {:s}. {:s} was provided"
                         .format(LEAD_KEYWORD, BISMUTH_KEYWORD,
                                 LBE_KEYWORD, fluid))


def rho(T, fluid):
    """
    Computes fluid density in [kg/m^3].

    Parameters
    ----------
    T : float
        temperature in [K]
    fluid : str
        fluid for which calculation shall be performed,
        can be one among lead, bismuth or lbe
    """
    if fluid == LEAD_KEYWORD:
        return 11441 - 1.2795*T
    elif fluid == BISMUTH_KEYWORD:
        return 10725 - 1.22*T
    elif fluid == LBE_KEYWORD:
        return 11065 - 1.293*T
    else:
        raise ValueError("Fluid can be one among: {:s},"
                         "{:s}, {:s}. {:s} was provided"
                         .format(LEAD_KEYWORD, BISMUTH_KEYWORD,
                                 LBE_KEYWORD, fluid))


def alpha(T, fluid):
    """
    Computes fluid thermal expansion coefficient in [1/K].

    Parameters
    ----------
    T : float
        temperature in [K]
    fluid : str
        fluid for which calculation shall be performed,
        can be one among lead, bismuth or lbe
    """
    if fluid == LEAD_KEYWORD:
        return 1/(8942 - T)
    elif fluid == BISMUTH_KEYWORD:
        return 1/(8791 - T)
    elif fluid == LBE_KEYWORD:
        return 1/(8558 - T)
    else:
        raise ValueError("Fluid can be one among: {:s},"
                         "{:s}, {:s}. {:s} was provided"
                         .format(LEAD_KEYWORD, BISMUTH_KEYWORD,
                                 LBE_KEYWORD, fluid))


def u_s(T, fluid):
    """
    Computes speed of sound in fluid in [m/s].

    Parameters
    ----------
    T : float
        temperature in [K]
    fluid : str
        fluid for which calculation shall be performed,
        can be one among lead, bismuth or lbe
    """
    if fluid == LEAD_KEYWORD:
        return 1953 - 0.246*T
    elif fluid == BISMUTH_KEYWORD:
        return 1616 + 0.187*T - 2.2e-4*T
    elif fluid == LBE_KEYWORD:
        return 1855 - 0.212*T
    else:
        raise ValueError("Fluid can be one among: {:s},"
                         "{:s}, {:s}. {:s} was provided"
                         .format(LEAD_KEYWORD, BISMUTH_KEYWORD,
                                 LBE_KEYWORD, fluid))


def beta_s(T, fluid):
    """
    Computes fluid isentropic compressibility in [1/Pa].

    Parameters
    ----------
    T : float
        temperature in [K]
    fluid : str
        fluid for which calculation shall be performed,
        can be one among lead, bismuth or lbe
    """
    return 1/(rho(T, fluid) * u_s(T, fluid)**2)


def cp(T, fluid):
    """
    Computes fluid specific heat capacity in [J/(kg*K)].

    Parameters
    ----------
    T : float
        temperature in [K]
    fluid : str
        fluid for which calculation shall be performed,
        can be one among lead, bismuth or lbe
    """
    if fluid == LEAD_KEYWORD:
        return (175.1 - 4.961e-2*T + 1.985e-5*T**2
                - 2.099e-9*T**3 - 1.524e6*T**-2)
    elif fluid == BISMUTH_KEYWORD:
        return 118.2 + 5.934e-3*T + 7.183e6*T**-2
    elif fluid == LBE_KEYWORD:
        return (164.8 - 3.94e-2*T + 1.25e-5*T**2
                - 4.56e5*T**-2)
    else:
        raise ValueError("Fluid can be one among: {:s},"
                         "{:s}, {:s}. {:s} was provided"
                         .format(LEAD_KEYWORD, BISMUTH_KEYWORD,
                                 LBE_KEYWORD, fluid))


def delta_h(T, fluid):
    """
    Computes fluid specific enthalpy (in respect to melting point) in [J/K].

    Parameters
    ----------
    T : float
        temperature in [K]
    fluid : str
        fluid for which calculation shall be performed,
        can be one among lead, bismuth or lbe
    """
    if fluid == LEAD_KEYWORD:
        return (176.2*(T - LEAD_MELTING_TEMPERATURE)
                - 2.4615e-2*(T**2 - LEAD_MELTING_TEMPERATURE**2)
                + 5.147e-6*(T**3 - LEAD_MELTING_TEMPERATURE**3)
                + 1.524e6*(T**-1 - LEAD_MELTING_TEMPERATURE**-1))
    elif fluid == BISMUTH_KEYWORD:
        return (118.2*(T - BISMUTH_MELTING_TEMPERATURE)
                + 2.967e-3*(T**2 - BISMUTH_MELTING_TEMPERATURE**2)
                - 7.183e6*(T**-1 - BISMUTH_MELTING_TEMPERATURE**-1))
    elif fluid == LBE_KEYWORD:
        return (164.8*(T - LBE_MELTING_TEMPERATURE)
                - 1.97e-2*(T**2 - LBE_MELTING_TEMPERATURE**2)
                + 4.167e-6*(T**3 - LBE_MELTING_TEMPERATURE**3)
                + 4.56e5*(T**-1 - LEAD_MELTING_TEMPERATURE**-1))
    else:
        raise ValueError("Fluid can be one among: {:s},"
                         "{:s}, {:s}. {:s} was provided"
                         .format(LEAD_KEYWORD, BISMUTH_KEYWORD,
                                 LBE_KEYWORD, fluid))


def mi(T, fluid):
    """
    Computes fluid dynamic viscosity in [Pa*s].

    Parameters
    ----------
    T : float
        temperature in [K]
    fluid : str
        fluid for which calculation shall be performed,
        can be one among lead, bismuth or lbe
    """
    if fluid == LEAD_KEYWORD:
        return 4.55e-4*np.exp(1069/T)
    elif fluid == BISMUTH_KEYWORD:
        return 4.456e-4*np.exp(780/T)
    elif fluid == LBE_KEYWORD:
        return 4.94e-4*np.exp(754.1/T)
    else:
        raise ValueError("Fluid can be one among: {:s},"
                         "{:s}, {:s}. {:s} was provided"
                         .format(LEAD_KEYWORD, BISMUTH_KEYWORD,
                                 LBE_KEYWORD, fluid))


def r(T, fluid):
    """
    Computes fluid electrical resistivity [Ohm*m].

    Parameters
    ----------
    T : float
        temperature in [K]
    fluid : str
        fluid for which calculation shall be performed,
        can be one among lead, bismuth or lbe
    """
    if fluid == LEAD_KEYWORD:
        return (67.0 + 0.0471*T)*1e-8
    elif fluid == BISMUTH_KEYWORD:
        return (98.96 + 0.0554*T)*1e-8
    elif fluid == LBE_KEYWORD:
        return (90.9 + 0.048*T)*1e-8
    else:
        raise ValueError("Fluid can be one among: {:s},"
                         "{:s}, {:s}. {:s} was provided"
                         .format(LEAD_KEYWORD, BISMUTH_KEYWORD,
                                 LBE_KEYWORD, fluid))


def conductivity(T, fluid):
    """
    Computes fluid thermal conductivity [W/(m*K)].

    Parameters
    ----------
    T : float
        temperature in [K]
    fluid : str
        fluid for which calculation shall be performed,
        can be one among lead, bismuth or lbe
    """
    if fluid == LEAD_KEYWORD:
        return 9.2 + 0.011*T
    elif fluid == BISMUTH_KEYWORD:
        return 7.34 + 9.5e-3*T
    elif fluid == LBE_KEYWORD:
        return 3.284 + 1.617e-2*T - 2.305e-6*T**2
    else:
        raise ValueError("Fluid can be one among: {:s},"
                         "{:s}, {:s}. {:s} was provided"
                         .format(LEAD_KEYWORD, BISMUTH_KEYWORD,
                                 LBE_KEYWORD, fluid))
