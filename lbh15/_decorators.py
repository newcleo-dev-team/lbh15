"""Module with the definition of decorators supporting the,
implementation of package functions"""
import collections.abc
import inspect
import warnings
import numpy as np

warnings.simplefilter("always")


def _check_instance_type(parameter_name: str,
                         parameter_type, arg_value) -> None:
    """
    Function for checking whether the "arg_value" value assigned to the
    "parameter_name" parameter is of "parameter_type" type.

    Parameters
    ----------
    parameter_name : str
                     Name of the parameter the type check is about
    parameter_type : any
                     Type of the parameter to check the value against
    arg_value : any
                Value to check the type

    Returns
    -------
    None
        If the check is passed, None is returned, otherwise a TypeError
        is raised.
    """
    if parameter_type == inspect.Parameter.empty:
        return
    if not isinstance(arg_value, parameter_type):
        # Accept INT arg when FLOAT is required
        if ((parameter_type == float)
                and isinstance(arg_value, (int, np.integer))):
            return
        # Analyse CONTAINERS recursively when made by only one element
        if isinstance(arg_value, (collections.abc.Sequence, np.ndarray)):
            for arg in arg_value:
                _check_instance_type(parameter_name, parameter_type, arg)
            return
        raise TypeError(f"Argument '{parameter_name}' must be of "
                        f"type '{parameter_type.__name__}'")


def typecheck_for_method(function):
    """
    Decorator for performing type checking on input arguments
    which type hints are applied to. It works only for class
    methods and for instance methods. When multiple decorators are
    applied to the same method, the current one must be applied
    as first.
    """
    def wrapper(*args, **kwargs):
        # Retrieve the parameters that should be passed to the function
        signature = inspect.signature(function)
        parameters = signature.parameters

        # Handle POSITIONAL arguments
        for idx, arg in enumerate(args):
            parameter_name, parameter = list(parameters.items())[idx]
            parameter_type = parameter.annotation
            _check_instance_type(parameter_name, parameter_type, arg)

        # Handle KEYWORD arguments
        for parameter_name, passed_value in kwargs.items():
            if parameter_name not in parameters.keys():
                continue
            parameter_type = parameters[parameter_name].annotation
            _check_instance_type(parameter_name, parameter_type, passed_value)

        return function(*args, **kwargs)

    return wrapper


def range_warning(function):
    """
    Decorator used to check validity range
    of correlation
    """
    def wrapper(*args):
        range_lim = args[0].range
        p_name = args[0].long_name
        temp = args[1]
        if hasattr(temp, "__len__"):
            temp = temp[0]
        if temp < range_lim[0] or temp > range_lim[1]:
            if (len(args) == 4) and args[3]:
                warnings.warn(f"The {p_name} is requested at "
                              f"temperature value of {temp:.2f} K "
                              "that is not in validity range "
                              f"[{range_lim[0]:.2f}, {range_lim[1]:.2f}] K",
                              stacklevel=3)
        return function(*args)
    return wrapper
