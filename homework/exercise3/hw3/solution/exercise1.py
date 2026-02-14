from functools import wraps


def validate_args(args, expected_arg_type_names, parameter_names, all_types):
    for index, expected_type in enumerate(expected_arg_type_names):
        if expected_type in all_types:
            actual_type = type(args[index]).__name__

            if actual_type == expected_type:
                continue

            raise TypeError(
                f"Argument '{parameter_names[index]}' "
                f"must be of type {expected_type}, "
                f"got {actual_type} instead."
            )


def validate_kwargs(kwargs, annotations, parameter_names, all_types):
    for kwarg_name, kwarg_value in kwargs.items():
        if kwarg_name not in parameter_names:
            continue

        expected = annotations[kwarg_name].__name__
        actual = type(kwarg_value).__name__

        if expected not in all_types:
            continue

        if actual == expected:
            continue

        raise TypeError(
            f"Argument '{kwarg_name}' must be of type {expected}, "
            f"got {actual} instead."
        )


def validate_return(result, annotations, all_types):
    expected_type = annotations.get("return")
    if expected_type is None:
        return

    expected = expected_type.__name__
    actual = type(result).__name__

    if expected in all_types:
        if actual == expected:
            return

        raise TypeError(
            f"Return value must be of type {expected}, " f"got {actual} instead."
        )


def type_check(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        """
        A decorator that checks whether the function's arguments and return
        value match the defined in the type annotations.
        """
        annotations = func.__annotations__

        expected_arg_type_names = []
        parameter_names = []
        for param_name, expected_type in annotations.items():
            if param_name == "return":
                continue

            # expected_type = expect_type.__name__
            expected_arg_type_names.append(expected_type.__name__)
            parameter_names.append(param_name)

        all_types = ("int", "float", "str", "list", "dict", "bool", "NoneType")

        validate_args(args, expected_arg_type_names, parameter_names, all_types)
        validate_kwargs(kwargs, annotations, parameter_names, all_types)

        result = func(*args, **kwargs)

        validate_return(result, annotations, all_types)

        return result

    return wrapper
