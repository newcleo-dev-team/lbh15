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
from lbh15 import Lead
import support
from scipy import signal
from simple_pid import PID

######
# Data
# Operating conditions
Qin_max: float = 2.1e6 # Maximum value of entering heat power [W/m3]
Qin_freq: float = 0.1 # Frequency of the entering heat power square wave [Hz]
Qout_max: float = -1e6 # Maximum value of exiting heat power [W/m3]
T_start = 800 # Initial lead temperature [K]
Ox_start = 7e-4 # Initial oxygen concentration [wt.%]
# Simulation settings
start_time: float = 0 # Start time of the simulation [s]
end_time: float = 200 # End time of the simulation [s]
time_steps_num: float = 1000 # Number of integration time steps [-]

#####################
# Arrays of variables
# Time
time, delta_t = np.linspace(start_time, end_time, time_steps_num, retstep=True)
# Entering heat power
Qin_signal = Qin_max * np.heaviside(time - (end_time-start_time)/2.0, 0.5)
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
pid = PID(0.75, 0.9, 0, setpoint=Ox_stp[0], starting_output=Ox_start/2)
pid.sample_time = None
pid.time_fn = support.sim_time
pid.output_limits = (0, Ox_start)

######################################################################
# Solve the balance equation in T and control the oxygen concentration
i = 1
for t in time[1:]:
    lead.T = T_sol[i-1]
    T_sol[i], Ox_stp[i], Ox_sol[i] = \
        support.integrate_in_time(lead, t, float(delta_t), Qin[t],
                                  Qout_max, Ox_sol[i-1])
    pid.setpoint = Ox_stp[i]
    Ox_sol[i] = pid(Ox_sol[i])
    i += 1

#######
# Plots
# Qin signal
support.plotTimeHistory(1, time, np.array(list(Qin.values())),
                        "time [$s$]", "Qin [$W/m^3$]",
                        "Entering Heat Power Time History",
                        "time_Qin_oxControl_byMetal.png")
# T_sol
support.plotTimeHistory(2, time, T_sol,
                        "time [$s$]", "T [$K$]",
                        "Lead Temperature Time History",
                        "time_T_oxControl_byMetal.png")
# Ox_sol overlapped to Ox_stp
support.plot2TimeHistories(3, time, Ox_sol, "Control",
                           time, Ox_stp, "Set-Point",
                           "time [$s$]", "Oxygen Concentration [$wt.\\%$]",
                           "Oxygen Concentration vs Setpoint Time History",
                           "time_OxVsOxStp_oxControl_byMetal.png")
