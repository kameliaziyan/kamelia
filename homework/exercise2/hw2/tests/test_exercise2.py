import io
from unittest.mock import patch
from solution.exercise2 import calculator, divide, multiply, subtract
from solution.exercise2 import add


def test_add() -> None:
    assert add(["add", "2", "to", "5"]) == "The answer is 7"
    assert add(["add", "10", "to", "0"]) == "The answer is 10"
    assert add(["add", "2", "from", "5"]) == "invalid operation"


def test_subtract() -> None:
    assert subtract(["subtract", "2", "from", "5"]) == "The answer is 3"
    assert subtract(["subtract", "5", "from", "5"]) == "The answer is 0"
    assert subtract(["subtract", "2", "to", "5"]) == "invalid operation"


def test_multiply() -> None:
    assert multiply(["multiply", "2", "by", "5"]) == "The answer is 10"
    assert multiply(["multiply", "0", "by", "5"]) == "The answer is 0"
    assert multiply(["multiply", "2", "to", "5"]) == "invalid operation"


def test_divide() -> None:
    assert divide(["divide", "10", "by", "5"]) == "The answer is 2.0"
    assert divide(["divide", "5", "by", "2"]) == "The answer is 2.5"
    assert divide(["divide", "10", "by", "0"]) == "invalid operation"
    assert divide(["divide", "10", "to", "5"]) == "invalid operation"


def test_calculator()-> None:
    user_inputs = [
        "add 2 to 5",
        "subtract 2 from 5",
        "multiply 2 by 5",
        "divide 10 by 5",
        "exit",
    ]

    expected_outputs = [
        "The answer is 7",
        "The answer is 3",
        "The answer is 10",
        "The answer is 2.0",
    ]
    with patch("builtins.input", side_effect=user_inputs):
        with patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
            result = calculator()
            output = mock_stdout.getvalue()

            for expected in expected_outputs:
                assert expected in output

            assert result == "Good Bye <3"
