from functools import wraps


def type_check(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        """
        A decorator that checks whether the function's arguments and return
        value match the defined in the type annotations.
        """
        annotations = func.__annotations__
        given_arg_type_names = []

        # current given data input list
        for arg in args:
            given_arg_type_names.append(type(arg).__name__)
        # for i, typ in enumerate(args):
        #   # print (type(typ))
        #  current_type = type(typ).__name__
        # lst_given_type.append(current_type)

        # expected input list
        expected_arg_type_names = []
        parameter_names = []
        for param_name, expected_type in annotations.items():
            if param_name == "return":
                continue

            # expected_type = expect_type.__name__
            expected_arg_type_names.append(expected_type.__name__)
            parameter_names.append(param_name)

        all_types = ("int", "float", "str", "list", "dict", "bool", "NoneType")

        for kwarg_name, kwarg_vale in kwargs.items():
            if kwarg_name in parameter_names:
                expected_type_key = annotations[kwarg_name].__name__
                actual_type_key = type(kwarg_vale).__name__

                if expected_type_key in all_types:
                    if actual_type_key != expected_type_key:

                        raise TypeError(
                            f"Argument '{kwarg_name}' must be of type {expected_type_key}, "
                            f"got {actual_type_key} instead."
                        )

        for index in range(len(expected_arg_type_names)):
            if expected_arg_type_names[index] in all_types:
                if given_arg_type_names[index] != expected_arg_type_names[index]:

                    raise TypeError(
                        f"Argument '{parameter_names
                                     [index]}' must be of type {expected_arg_type_names[index]}, "
                        f"got {type(given_arg_type_names[index]).__name__} instead."
                    )
        result = func(*args, **kwargs)

        if "return" in annotations:
            expected_return_type_name = annotations["return"].__name__
            actual_return_type_name = type(result).__name__
            if expected_return_type_name in all_types:
                if actual_return_type_name != expected_return_type_name:

                    raise TypeError(
                        f"Return value must be of type {expected_return_type_name}, "
                        f"got {actual_return_type_name} instead."
                    )

        return result

    return wrapper


@type_check
def format_data(name: str, age: int, data: dict, other_info=None) -> str:
    other_info_str = ", Other Info : " + str(other_info) if other_info else ""
    return f"Name: {name}, Age: {age}, Data: {data['key']}{other_info_str}"


# Test the function with correct types
# print(format_data("Alice", 30, {"key": "value"}, 1234))

# print(format_data.__annotations__)

# Test the function with incorrect types
# print(format_data("Alice", "thirty", {"key": "value"}))
# print(len(format_data.__annotations__))
