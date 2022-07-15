import numpy as np
from ._pyll import MELTING_TEMPERATURE


def p_s(T):
    """
    Computes lead saturation vapour pressure in [Pa].

    Parameters
    ----------
    T : float
        temperature in [K]
    """
    return 1.88e13 * T * np.exp(-23325/T)


def sigma(T):
    """
    Computes lead surface tension in [N/m].

    Parameters
    ----------
    T : float
        temperature in [K]
    """
    return (525.9 - 0.113*T)/1000


def rho(T):
    """
    Computes lead density in [kg/m^3].

    Parameters
    ----------
    T : float
        temperature in [K]
    """
    return 11441 - 1.2795*T


def alpha(T):
    """
    Computes lead thermal expansion coefficient in [1/K].

    Parameters
    ----------
    T : float
        temperature in [K]
    """
    return 1/(8942 - T)


def u_s(T):
    """
    Computes speed of sound in lead in [m/s].

    Parameters
    ----------
    T : float
        temperature in [K]
    """
    return 1953 - 0.246*T


def beta_s(T):
    """
    Computes lead isentropic compressibility in [1/Pa].

    Parameters
    ----------
    T : float
        temperature in [K]
    """
    return 1/(rho(T) * u_s(T)**2)


def cp(T):
    """
    Computes lead specific heat capacity in [J/(kg*K)].

    Parameters
    ----------
    T : float
        temperature in [K]
    """
    return (175.1 - 4.961e-2*T + 1.985e-5*T**2
            - 2.099e-9*T**3 - 1.524e6*T**-2)


def delta_h(T):
    """
    Computes lead specific enthalpy (in respect to melting point) in [J/K].

    Parameters
    ----------
    T : float
        temperature in [K]
    """
    return (176.2*(T-MELTING_TEMPERATURE)
            - 2.4615e-2*(T**2 - MELTING_TEMPERATURE**2)
            + 5.147e-6*(T**3 - MELTING_TEMPERATURE**3)
            + 1.524e6*(T**-1 - MELTING_TEMPERATURE**-1))


def mi(T):
    """
    Computes lead dynamic viscosity in [Pa*s].

    Parameters
    ----------
    T : float
        temperature in [K]
    """
    return 4.55e-4*np.exp(1069/T)
