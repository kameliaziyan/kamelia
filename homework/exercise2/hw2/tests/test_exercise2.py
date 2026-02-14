from solution.exercise2 import divide, multiply, subtract
from solution.exercise2 import add
import pytest
from solution.exercise2 import INVALID_OPERATION


@pytest.mark.parametrize(
    "input_data,result",
    [
        (["add", "2", "to", "5"], "The answer is 7"),
        (["add", "10", "to", "0"], "The answer is 10"),
        (["add", "2", "from", "5"], INVALID_OPERATION),
    ],
)
def test_add(input_data: list[str], result: str) -> None:
    assert add(input_data) == result


@pytest.mark.parametrize(
    "input_data,result",
    [
        (["subtract", "2", "from", "5"], "The answer is 3"),
        (["subtract", "5", "from", "5"], "The answer is 0"),
        (["subtract", "2", "to", "5"], INVALID_OPERATION),
    ],
)
def test_subtract(input_data: list[str], result: str) -> None:
    assert subtract(input_data) == result


@pytest.mark.parametrize(
    "input_data,result",
    [
        (["multiply", "2", "by", "5"], "The answer is 10"),
        (["multiply", "0", "by", "5"], "The answer is 0"),
        (["multiply", "2", "to", "5"], INVALID_OPERATION),
    ],
)
def test_multiply(input_data: list[str], result: str) -> None:
    assert multiply(input_data) == result


@pytest.mark.parametrize(
    "input_data,result",
    [
        (["divide", "10", "by", "5"], "The answer is 2.0"),
        (["divide", "5", "by", "2"], "The answer is 2.5"),
        (["divide", "10", "by", "0"], INVALID_OPERATION),
        (["divide", "10", "to", "5"], INVALID_OPERATION),
    ],
)
def test_divide(input_data: list[str], result: str) -> None:
    assert divide(input_data) == result
