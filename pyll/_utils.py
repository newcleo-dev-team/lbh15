from ._pyll import MELTING_TEMPERATURE


def delta_h(T):
    return (176.2*(T-MELTING_TEMPERATURE)
            - 2.4615e-2*(T**2 - MELTING_TEMPERATURE**2)
            + 5.147e-6*(T**3 - MELTING_TEMPERATURE**3)
            + 1.524e6*(T**-1 - MELTING_TEMPERATURE**-1))
