"""Tutorial using thermophysical and thermochemical
correlations of the lbh15 python package"""
import numpy as np
import matplotlib.pyplot as plt
from lbh15 import Lead


if __name__ == "__main__":

    # Setting of the constants
    T_0 = 683  # [K]
    SIMULATION_TIME = 100  # [s]
    STEP_SIZE = 0.1  # [s]
    MASS = 100  # [kg]
    #  Power variation
    NET_POWER = 43000  # [W]
    VARIATION_START = 20  # [s]
    VARIATION_END = 70  # [s]
    RADIUS = 1  # [m]

    # Creation of the arrays
    # Array containing the time values
    time = np.arange(0, SIMULATION_TIME, STEP_SIZE)
    # Array containing the heat variation values
    heat_variation = np.zeros(len(time)-1)
    # Array containing the temperature values
    temperature = np.zeros_like(time)
    # Array containing the lower oxygen concentration values
    lower_oxygen_concentration = np.zeros_like(time)
    # Array containing the upper oxygen concentration values
    upper_oxygen_concentration = np.zeros_like(time)
    # Array containing the level of the liquid metal in the tank
    level = np.zeros_like(time)

    # Filling of the heat variation array,
    # computed according to the power variation
    VAR_START_IDX = int(VARIATION_START/STEP_SIZE)
    VAR_END_IDX = int(VARIATION_END/STEP_SIZE)
    heat_variation[VAR_START_IDX:VAR_END_IDX] = (
        NET_POWER * STEP_SIZE)

    # Initialization
    temperature[0] = T_0
    system = Lead(T=T_0)
    h_0 = system.h
    upper_oxygen_concentration[0] = system.o_sol
    lower_oxygen_concentration[0] = system.lim_fe_sat
    volume = MASS / system.rho
    level[0] = volume / (np.pi * (RADIUS**2))

    # Looping
    for i in range(1, len(time)):
        # Solving heat balance
        h_i = np.sum(heat_variation[0:i])/MASS + h_0
        # Creation of an object at a T temperature deduced from the h value
        system = Lead(h=h_i)
        temperature[i] = system.T
        # Updating the lower oxygen concentration
        lower_oxygen_concentration[i] = system.lim_fe_sat
        # Updating the upper oxygen concentration
        upper_oxygen_concentration[i] = system.o_sol
        # Updating the volume of the system
        volume = MASS / system.rho
        # Updating the level of the liquid metal
        level[i] = volume / (np.pi * (RADIUS**2))

# Creation of the graphs
fig, axs = plt.subplots(nrows=3, ncols=1, figsize=(10, 8))
# Plot of the Temperature Variation over Time
axs[0].plot(time, temperature)
axs[0].set_xlabel("Time [s]")
axs[0].set_ylabel("Temperature [K]")
axs[0].set_title("Temperature Variation over Time")
axs[0].grid(True)
# Plot of the different Oxygen Concentrations over Temperature
axs[1].plot(time, lower_oxygen_concentration,
            label='Lower Limit of Oxygen Concentration')
axs[1].plot(time, upper_oxygen_concentration,
            label='Upper Limit of Oxygen Concentration')
axs[1].set_xlabel("Temperature [K]")
axs[1].set_ylabel("Oxygen Concentration log10([wt(%)]")
axs[1].set_title("Oxygen Concentrations over Time")
axs[1].set_yscale("log")
axs[1].grid(True)
axs[1].legend(loc='upper left', bbox_to_anchor=(1.05, 1), fontsize='small')
# Plot of the Level of the liquid metal over Temperature
axs[2].plot(time, level)
axs[2].set_xlabel("Temperature [K]")
axs[2].set_ylabel("Level of the liquid metal [m]")
axs[2].set_title("Level of the liquid metal over Time")
axs[2].grid(True)
# Automatically adjust spacing between subplots
plt.tight_layout()
# Creation of the figures in a png file
plt.savefig("tutorials.png")
