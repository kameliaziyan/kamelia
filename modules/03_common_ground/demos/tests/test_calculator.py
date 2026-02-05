from solution.calculator import add, divide
import pytest


def test_add():
    assert add(1, 3) == 4


def test_divide():
    assert divide(4, 2) == 2


def test_divide_by_zero_raises():
    with pytest.raises(ZeroDivisionError):
        divide(4, 0)
