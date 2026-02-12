from functools import wraps

# `int`, `float`, `str`, `list`, `dict`, `bool`, and `NoneType`.


# "Alice", 30, {"key": "value"}, 1234)
def type_check(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        data_type_dict = func.__annotations__
        lst_given_type = []

        # current given data input list
        for i, typ in enumerate(args):
            # print (type(typ))
            current_type = type(typ).__name__
            lst_given_type.append(current_type)

        # expected input list
        lst_expected_type = []
        names_inputs = []
        for name, expect_type in data_type_dict.items():
            if name == "return":
                continue
            expected_type = expect_type.__name__
            lst_expected_type.append(expected_type)
            names_inputs.append(name)

        all_types = ("int", "float", "str", "list", "dict", "bool", "NoneType")

        for key, value in kwargs.items():
            if key in names_inputs:
                expect_type_key = data_type_dict[key].__name__
                given_type_key = type(value).__name__

                if expect_type_key in all_types:
                    if given_type_key != expect_type_key:

                        raise TypeError(
                            f"Argument '{key}' must be of type {expect_type_key}, "
                            f"got {given_type_key} instead."
                        )

        for i in range(len(lst_expected_type)):
            if lst_expected_type[i] in all_types:
                if lst_given_type[i] != lst_expected_type[i]:

                    raise TypeError(
                        f"Argument '{names_inputs[i]}' must be of type {lst_expected_type[i]}, "
                        f"got {type(lst_given_type[i]).__name__} instead."
                    )
        result = func(*args, **kwargs)

        if "return" in data_type_dict:
            expected_return_type = data_type_dict["return"].__name__
            given_return_type = type(result).__name__
            if expected_return_type in all_types:
                if given_return_type != expected_return_type:

                    raise TypeError(
                        f"Return value must be of type {expected_return_type}, "
                        f"got {given_return_type} instead."
                    )

        return result

    return wrapper


@type_check
def format_data(name: str, age: int, data: dict, other_info=None) -> str:
    other_info_str = ", Other Info : " + str(other_info) if other_info else ""
    return f"Name: {name}, Age: {age}, Data: {data['key']}{other_info_str}"


# Test the function with correct types
print(format_data("Alice", 30, {"key": "value"}, 1234))


# print(format_data.__annotations__)

# Test the function with incorrect types
print(format_data("Alice", "thirty", {"key": "value"}))
# print(len(format_data.__annotations__))
