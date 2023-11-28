import copy
import matplotlib.pyplot as plt
import numpy as np
import __main__
from typing import Generator
from typing import Tuple
from scipy.optimize import fsolve

#######################################################
# Function returning the Oxygen concentration set-point
def ox_concentration_setpoint(lead: __main__.Lead) -> float:
    return (lead.o_sol + lead.lim_fe_sat) / 2

###########################
# Balance equation to solve
def eqn_to_solve(T_new: float, lead: __main__.Lead, delta_t: float,
                 Qin: float, Qout_max: float) -> float:
    T_old = lead.T
    T_avg = (T_old + T_new) / 2.0
    lead_avg = copy.deepcopy(lead)
    lead_avg.T = T_avg
    return lead_avg.rho * lead_avg.cp * (T_new - T_old) / delta_t \
        - Qin - Qout_max

#########################################################
# Function integrating the system over a single time-step
def integrate_in_time(lead: __main__.Lead, t: float, delta_t: float,
                      Qin: float, Qout_max: float,
                      Ox: float) -> Tuple[float, float, float]:
    T_curr, _, ier, mesg = fsolve(eqn_to_solve, x0=[lead.T],
                                  args=(lead, delta_t, Qin, Qout_max),
                                  xtol=1e-10, full_output=True)
    if ier != 1:
        raise RuntimeError("Error when integrating heat balance equation "
                           f"from time = {t - delta_t} s to time = "
                           f"{t} s. The reason is:\n"
                           f"{mesg}\n")
    lead.T = T_curr
    Ox_stp_curr = ox_concentration_setpoint(lead)
    return T_curr, Ox_stp_curr, Ox

#######################################################################
# Functions and variables for setting the time function used by the PID
def time_generator() -> Generator[float, None, None]:
    for t in __main__.time:
        yield t
time_gen = time_generator()
def sim_time() -> float:
    return next(time_gen)

#################################
# Function for plotting 2D graphs
def plotTimeHistory(id: int, x: np.ndarray, y: np.ndarray,
                    x_label: str, y_label: str, title: str,
                    output_name: str) -> None:
    plt.figure(id)
    plt.plot(x, y)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.grid()
    plt.savefig(output_name)

##########################################################
# Function for plotting 2D graphs with 2 overlapped curves
def plot2TimeHistories(id: int, x1: np.ndarray, y1: np.ndarray, label1: str,
                       x2: np.ndarray, y2: np.ndarray, label2: str,
                       x_label: str, y_label: str, title: str,
                       output_name: str) -> None:
    plt.figure(id)
    plt.plot(x1, y1, label=label1)
    plt.plot(x2, y2, label=label2)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.legend()
    plt.grid()
    plt.savefig(output_name)
