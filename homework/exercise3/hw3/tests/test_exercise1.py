import pytest
from solution.exercise1 import type_check


@type_check
def add(first_number: int, second_number: int) -> int:
    return first_number + second_number


def test_add_valid():
    assert add(2, 3) == 5


def test_add_wrong_type():
    with pytest.raises(TypeError):
        add(2, "3")


@type_check
def greet(name: str) -> str:
    return f"Hello {name}"


def test_greet_valid():
    assert greet("Dan") == "Hello Dan"


@type_check
def broken_function(value: int) -> int:
    return "wrong"


def test_wrong_return_type():
    with pytest.raises(TypeError):
        broken_function(5)
