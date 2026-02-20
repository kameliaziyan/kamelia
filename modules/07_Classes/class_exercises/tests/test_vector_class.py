from solution.vector_class import Vector2D


def test_addition() -> None:
    v1 = Vector2D(3.0, 4.0)
    v2 = Vector2D(1.0, 2.0)
    assert (v1 + v2) == Vector2D(4.0, 6.0)


def test_magnitude() -> None:
    value = Vector2D(3.0, 4.0)
    result = round(value.__abs__())
    assert result == 5
