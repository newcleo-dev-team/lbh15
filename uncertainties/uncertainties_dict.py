# Uncertainty for Polonium vapour pressure
Dict_P_Po = { 'function_range' : { '10**(-(a/T) + b)' : [641, 877] }, 'param_uncert' : { 'a' : [5440, 60], 'b' : [9.46, 0.05]}}

# Uncertainty for test
Dict_test = { 'function_range' : { 'a*T + b' : [600, 800] }, 'param_uncert' : { 'a' : [105, 2], 'b' : [9.5, 0.5]}}

# Uncertainty for test
Dict_test2 = { 'function_range' : { 'a*T' : [600, 800] }, 'param_uncert' : { 'a' : [105, 2]}}

# Uncertainty for Polonium vapour pressure
Dict_Do_Homna1971 = { 'function_range' : { 'a*10**(-5)*exp(-b/(8.314*T))' : [1073, 1373] }, 'param_uncert' : { 'a' : [9.65, 0.71], 'b' : [20083, 6067]}}

# Uncertainty for enthalpy in pure Lead
Dict_h_lead = { 'function_range' : { '176.2 * (T - Tmo) - 2.4615 * 10^(-2) * (T**2 - Tmo**2) + 5.147 * 10**(-6) * (T**3 - Tmo**3) + 1.524 * 10**(6) * (1/T - 1/Tmo)' : [600.6, 2021] }, 'param_uncert' : { 'Tmo' : [600.6, 0.1]}} 