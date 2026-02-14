from solution.exercise2 import fibonacci
import pytest


def test_febonacci1() -> None:
    assert fibonacci(5) == 3


def test_febonacci2() -> None:
    assert fibonacci(57) == 225851433717


def test_febonacci3() -> None:
    assert fibonacci(200) == 173402521172797813159685037284371942044301


def test_febonacci4() -> None:
    assert fibonacci(260) == (600224643828207248620196670234592075321836561403380341)


def test_febonacci5() -> None:
    assert fibonacci(500) == (
        86168291600238450732788312165664788095941068326060883324529903470149056115823592713458328176574447204501
    )


def test_fibonacci_invalid() -> None:
    with pytest.raises(ValueError):
        fibonacci(0)
