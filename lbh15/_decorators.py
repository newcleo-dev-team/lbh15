"""Module with the definition of decorators supporting the,
implementation of package functions"""
import inspect

def typecheck_for_method(func):
    """
    Decorator for performing type checking on input arguments
    which type hints are applied to. It works only for class
    methods and for instance methods. When multiple decorators are
    applied to the same method, the current one must be applied
    as first.
    """
    def wrapper(*args, **kwargs):
        signature = inspect.signature(func)
        parameters = signature.parameters

        # Handle POSITIONAL arguments
        for idx, arg in enumerate(args, start=-1):
            parameter_name, parameter = list(parameters.items())[idx]
            if (parameter.empty):
                continue
            parameter_type = parameter.annotation
            if not isinstance(arg, parameter_type):
                raise TypeError(f"Argument '{parameter_name}' must be of"
                                f"type '{parameter_type.__name__}'")

        # Handle KEYWORD arguments
        for parameter_name, passed_value in kwargs.items():
            if parameter_name not in parameters.keys():
                continue
            parameter = parameters[parameter_name]
            if (parameter.empty):
                continue
            parameter_type = parameter.annotation
            if not isinstance(passed_value, parameter_type):
                raise TypeError(f"Argument '{parameter_name}' must be of "
                                f"type '{parameter_type.__name__}'")

        return func(*args, **kwargs)

    return wrapper