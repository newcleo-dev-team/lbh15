"""Module with the definition of decorators supporting the,
implementation of package functions"""
import collections.abc
import inspect
import warnings
from functools import wraps
import numpy as np

warnings.simplefilter("always")


def range_warning(function):
    """
    Decorator used to check validity range
    of correlation
    """
    @wraps(function)
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
