from solution.exercise4 import type_conversion


def test_binary_zero() -> None:
    result = type_conversion("0")

    assert result == 0
    assert isinstance(result, int)


def test_binary_with_leading_zeros() -> None:
    result = type_conversion("000101")

    assert result == 5


def test_binary_large_number() -> None:
    result = type_conversion("11111111")

    assert result == 255
