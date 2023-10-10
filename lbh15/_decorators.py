"""Module with the definition of decorators supporting the,
implementation of package functions"""
import collections.abc
import inspect
import numpy as np


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
        if ((parameter_type == float) and (isinstance(arg_value, int))):
            return
        # Analyse CONTAINERS recursively when made by only one element
        if isinstance(arg_value, (collections.abc.Sequence, np.ndarray)) \
                and (len(arg_value) == 1):
            _check_instance_type(parameter_name, parameter_type, arg_value[0])
            return
        raise TypeError(f"Argument '{parameter_name}' must be of "
                        f"type '{parameter_type.__name__}'")


def typecheck_for_method(func):
    """
    Decorator for performing type checking on input arguments
    which type hints are applied to. It works only for class
    methods and for instance methods. When multiple decorators are
    applied to the same method, the current one must be applied
    as first.
    """
    def wrapper(*args, **kwargs):
        # Retrieve the parameters that should be passed to the function
        signature = inspect.signature(func)
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

        return func(*args, **kwargs)

    return wrapper
