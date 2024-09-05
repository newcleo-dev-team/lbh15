""" Module providing the uncertainty correlation for given parameters and
its correlations"""

from typing import Callable, Tuple, Dict, List
import numpy as np
from sympy import Basic, symbols, lambdify, diff, sympify, sqrt
from scipy.stats import norm
from uncertainties_dict import Dict_P_Po, Dict_Do_Homna1971, Dict_h_lead


def generate_sigma_f(func: str, params: dict, sigmas: dict) -> Tuple[Callable,
                                                                     Basic]:
    """
    Generates the symbolic and numerical uncertainty function of the property
    by applying the uncertainty propagation formula.

    Parameters
    ----------
    func : str
        The mathematical expression of the function.
    params: dict
        Dictionary of parameter names and their values.
    sigmas: dict
        Dictionary of parameter names and their uncertainties.

    Returns
    -------
    Numerical function of uncertainty and the symbolic expression.
    """
    # Symbolization of parameters
    temp = symbols('T')
    param_symbols = symbols(list(params.keys()))

    # Create a symbolic expression of the function
    func_sym = sympify(func)

    # Calculate partial derivatives with respect to each parameter
    partials = [diff(func_sym, param) for param in param_symbols]

    # Construct the symbolic expression for sigma_f
    sigma_f_expr = sum((partial**2) * (sigma**2) for partial, sigma in
                       zip(partials, sigmas.values()))
    sigma_f = sqrt(sigma_f_expr)

    # Convert the symbolic sigma_f expression to a numerical function
    sigma_f_func = lambdify((temp, *param_symbols), sigma_f, modules='numpy')

    return sigma_f_func, sigma_f


def fit_distribution(samples, **kwargs) -> list:
    """
    Determines parameters of the distributon fitted to the samples.

    Parameters
    ----------
    samples: array
        Sample data.

    Returns
    -------
    List of parameters of the fitted normal distribution.
    """

    # Fit and evaluate distributions
    norm_params = norm.fit(samples, **kwargs)

    # Return the parameters of the fitted normal distribution.
    return norm_params


def calculate_ratio_in_uncertainty(temp_scatter: List[float], f_scatter: List[float],
                                   temp_values: List[float], f_minus_uncertainty: np.ndarray,
                                   f_plus_uncertainty: np.ndarray) -> float:
    """
    Calculates the ratio of points within the uncertainty range.

    Parameters
    ----------
    temp_scatter: list
        List of temperature values from scatter data.
    f_scatter: list
        List of function values from scatter data.
    temp_values: list
        List of temperature values where the function is evaluated.
    f_minus_uncertainty: np.ndarray
        Array of function values minus uncertainty.
    f_plus_uncertainty: np.ndarray
        Array of function values plus uncertainty.

    Returns
    -------
    float
        Ratio of points within the uncertainty range.
    """
    in_uncertainty = [(f_minus_uncertainty[i] <= f <= f_plus_uncertainty[i])
                      for temp, f in zip(temp_scatter, f_scatter)
                      for i in range(len(temp_values))
                      if temp_values[i] == temp]
    ratio_in_uncertainty = sum(in_uncertainty) / len(in_uncertainty)
    return ratio_in_uncertainty


def f_uncertainty(func: str, parameters: dict, sigmas: dict, temp_values: list,
                  num_samples: int = 1000) -> Basic:
    """
    Returns and plots the function and its uncertainty range.

    Parameters
    ----------
    func: str
        Mathematical expression of the function.
    parameters: dict
        Dictionary of parameter names and their nominal values.
    sigmas: dict
        Dictionary of parameter names and their uncertainties.
    temp_values: list
        List of temperature values where the function is evaluated.
    num_samples: int, optional
        Number of samples to generate for uncertainty evaluation. Default is 
        1000.

    Returns
    -------
    Callable | ValueError
    
    ValueError
        If the ratio of points within the uncertainty range is less than 99% or
        if the distribution of function samples does not match the expected
        normal distribution.

    Callable
        The uncertainty correlation as a symbolic expression with parameters
        substituted.
    """

    # Create a symbolic expression of the function
    temp = symbols('T')
    param_symbols = symbols(list(parameters.keys()))
    param_values = tuple(parameters.values())
    func_sym = sympify(func)

    # Generate the uncertainty function
    sigma_f_func, sigma_f_sym = generate_sigma_f(func, parameters, sigmas)

    # Convert the symbolic function to a numerical function
    func_num = lambdify((temp, *param_symbols), func_sym, modules='numpy')

    # Evaluate the function and its uncertainty over the temperature range
    f_values = np.array([func_num(temp, *param_values) for temp
                         in temp_values])
    sigma_f_values = np.array([sigma_f_func(temp, *param_values) for temp
                               in temp_values])

    # Compute f + uncertainty and f - uncertainty
    f_plus_uncertainty = f_values + sigma_f_values
    f_minus_uncertainty = f_values - sigma_f_values

    # Generate scatter plot data with uniform distribution
    np.random.seed(0)
    param_samples = {name: np.random.normal(loc=mean, scale=sigma/3,
                                            size=num_samples)
                     for name, mean, sigma in zip(parameters.keys(),
                                                  parameters.values(),
                                                  sigmas.values())}

    scatter_data = []
    for temp in temp_values:
        for sample_set in zip(*param_samples.values()):
            scatter_data.append((temp, func_num(temp, *sample_set)))
    temp_scatter, f_scatter = zip(*scatter_data)

    # Calculate the ratio of points within the uncertainty range
    ratio_in_uncertainty = calculate_ratio_in_uncertainty(temp_scatter, f_scatter,
                                                          temp_values, f_minus_uncertainty,
                                                          f_plus_uncertainty)

    # Check if the ratio is less than 99% and raise an error if true
    if ratio_in_uncertainty < 0.99:
        raise ValueError(f"The ratio of points within the uncertainty range is\
                          less than 99%: {ratio_in_uncertainty:.2%}")

    # Print distribution's informations at a temperature for verification
    temperature = np.random.uniform(641, 877)
    samples_at_temp = [func_num(temperature, *sample_set) for
                       sample_set in zip(*param_samples.values())]
    norm_params = fit_distribution(samples_at_temp)
    if abs(func_num(temperature, *param_values) -
           norm_params[0]) > 0.1 * func_num(temperature, *param_values) or\
       abs(sigma_f_func(temperature, *param_values)/3 -
           norm_params[1]) > 0.1 * sigma_f_func(temperature, *param_values)/3:
        raise ValueError("The distribution of f may be innacurate")

    print(f'The uncertainty correlation is: {sigma_f_sym.subs(parameters)}')
    return sigma_f_sym.subs(parameters)


# Test
if __name__ == "__main__":
    # Collect Dictionary in the dictionary module
    available_dicts = {'Dict_P_Po': Dict_P_Po, 'Dict_Do_Homna1971':
                       Dict_Do_Homna1971, 'Dict_h_lead': Dict_h_lead}
    Dict_to_use_name = input(f"Enter the name of the dictionary to use\
({', '.join(available_dicts.keys())}): ")
    if Dict_to_use_name in available_dicts:
        Dict_to_use = available_dicts[Dict_to_use_name]
    else:
        raise ValueError("Invalid dictionary name.")

    # Check the number of parameters in the selected dictionary
    param_uncert = Dict_to_use['param_uncert']
    if len(list(param_uncert.keys())) >= 4:
        raise ValueError("The selected dictionary has four or more parameters,\
                         which is not allowed.")

    # Collect function and parameters from user
    func_range = Dict_to_use['function_range']
    f = list(func_range.keys())[0]

    param_dict = {}
    sigma_dict = {}
    for param in list(param_uncert.keys()):
        param_dict[param] = param_uncert[param][0]
        sigma_dict[param] = param_uncert[param][1]
    range_temp = list(func_range.values())
    T_min, T_max = range_temp[0][0], range_temp[0][1]
    temperature_values = np.linspace(T_min, T_max, num=100)

    f_uncertainty(f, param_dict, sigma_dict, temperature_values)