import pytest
from solution.exercise1 import  format_data


def test_correct_types_input():
    result = format_data("kamelia", 28, {"key": "value"})
    assert result == "Name: kamelia, Age: 28, Data: value"


def test_correct_types_input_otherinfo():
    result = format_data("kamelia", 28, {"key": "value"}, 1234)
    assert result == "Name: kamelia, Age: 28, Data: value, Other Info : 1234"


def test_incorrect():
    with pytest.raises (TypeError):
        format_data(10, 30, {"key": "value"})
