"""
Model where a heated volume of lead is controlled
by a PID in terms of oxygen concentration: the setpoint
of the oxygen concentration is chosen as the middle value
of the range the Iron oxyde layer generation
is assured within.

This model exploits lbh15 by accessing the lead
properties correlations through the definition of the lead metal instance.
"""
import numpy as np
from lbh15 import Lead # LBH15 package
from simple_pid import PID # PID controller
import support # Supporting functions

######
# Data
# Operating conditions
T_start: float = 800 # Initial lead temperature [K]
Qin_max: float = 2.1e6 # Maximum value of heat load [W/m3]
t_jump: float = 100 # Time instant when the heat load jump happens [s]
Qout: float = -1e6 # Value of dissipated heat power [W/m3]
Ox_start = 7e-4 # Initial oxygen concentration [wt.%]
# PID controller settings
P_coeff: float = 0.75 # Proportional coefficient [-]
I_coeff: float = 0.9 # Integral coefficient [-]
D_coeff: float = 0.0 # Derivative coefficient [-]
max_output: float = Ox_start # Maximum value of the output [wt.%]
# Simulation settings
start_time: float = 0 # Start time of the simulation [s]
end_time: float = 200 # End time of the simulation [s]
time_steps_num: float = 1000 # Number of integration time steps [-]

#####################
# Arrays of variables
# Time
time, delta_t = np.linspace(start_time, end_time, time_steps_num, retstep=True)
# Heat load time history
t_jump = t_jump if start_time < t_jump and end_time > t_jump else\
    (end_time-start_time)/2.0
Qin_signal = Qin_max * np.heaviside(time - t_jump, 0.5)
Qin = {t:q for t,q in zip(time, Qin_signal)}
# Lead temperature
T_sol = np.zeros(len(time))
# Oxygen concentrations
Ox_stp = np.zeros(len(time))
Ox_sol = np.zeros(len(time))

########################
# Set the initial values
T_sol[0] = T_start
lead = Lead(T=T_start)
Ox_stp[0] = support.ox_concentration_setpoint(lead)
Ox_sol[0] = Ox_start

########################
# Set the PID controller
pid = PID(P_coeff, I_coeff, D_coeff,
          setpoint=Ox_stp[0], starting_output=Ox_start/2)
pid.sample_time = None
pid.time_fn = support.sim_time
pid.output_limits = (0, max_output)

######################################################################
# Solve the balance equation in T and control the oxygen concentration
i = 1
for t in time[1:]:
    lead.T = T_sol[i-1]
    T_sol[i], Ox_stp[i], Ox_sol[i] = \
        support.integrate_in_time(lead, t, float(delta_t), Qin[t],
                                  Qout, Ox_sol[i-1])
    pid.setpoint = Ox_stp[i]
    Ox_sol[i] = pid(Ox_sol[i])
    i += 1

#######
# Plots
# Qin signal
support.plotTimeHistory(1, time, np.array(list(Qin.values())),
                        "time [$s$]", "Qin [$W/m^3$]",
                        "Heat Load Time History",
                        "time_Qin.png")
# T_sol
support.plotTimeHistory(2, time, T_sol,
                        "time [$s$]", "T [$K$]",
                        "Lead Temperature Time History",
                        "time_T.png")
# Ox_sol overlapped to Ox_stp
support.plot2TimeHistories(3, time, Ox_sol, "Control",
                           time, Ox_stp, "Set-Point",
                           "time [$s$]", "Oxygen Concentration [$wt.\\%$]",
                           "Oxygen Concentration vs Setpoint Time History",
                           "time_OxVsOxStp.png")
