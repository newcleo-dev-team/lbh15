import math
from ._pyll import MELTING_TEMPERATURE


def p_s(T):
    return 1.88e13 * T * math.exp(-23325/T)


def sigma(T):
    return (525.9 - 0.113*T)/1000


def rho(T):
    return 11441 - 1.2795*T


def alpha(T):
    return 1/(8942 - T)


def u_s(T):
    return 1953 - 0.246*T


def beta_s(T):
    return 1/(rho(T) * u_s(T)**2)


def cp(T):
    return (175.1 - 4.961e-2*T + 1.985e-5*T**2
            - 2.099e-9*T**3 - 1.524e6*T**-2)


def delta_h(T):
    return (176.2*(T-MELTING_TEMPERATURE)
            - 2.4615e-2*(T**2 - MELTING_TEMPERATURE**2)
            + 5.147e-6*(T**3 - MELTING_TEMPERATURE**3)
            + 1.524e6*(T**-1 - MELTING_TEMPERATURE**-1))


def mi(T):
    return 4.55e-4*math.exp(1069/T)
