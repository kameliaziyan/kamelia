from solution.exercise5 import quadratic_equation


def test_quadratic_standard_case() -> None:
    result = quadratic_equation(1, -3, 2)

    assert result == "x1 = 2.00, x2 = 1.00"


def test_quadratic_negative_roots() -> None:
    result = quadratic_equation(1, 5, 6)

    assert result == "x1 = -2.00, x2 = -3.00"


def test_quadratic_decimal_roots() -> None:
    result = quadratic_equation(2, -7, 3)

    assert result == "x1 = 3.00, x2 = 0.50"


def test_quadratic_symmetric_roots() -> None:
    result = quadratic_equation(1, 0, -4)

    assert result == "x1 = 2.00, x2 = -2.00"
