import pytest
from solution.exercise1 import type_check


@type_check
def add(first_number: int, second_number: int) -> int:
    return first_number + second_number


def test_add_valid() -> None:
    assert add(2, 3) == 5


def test_add_wrong_type() -> None:
    with pytest.raises(TypeError):
        add(2, "3")


@type_check
def greet(name: str) -> str:
    return f"Hello {name}"


def test_greet_valid() -> None:
    assert greet("Dan") == "Hello Dan"


@type_check
def broken_function(value: int) -> str:
    return "Argument 'age' must be of type <class 'int'>, got <class 'str'> instead"


def test_wrong_return_type() -> None:
    with pytest.raises(TypeError):
        broken_function("hi")
