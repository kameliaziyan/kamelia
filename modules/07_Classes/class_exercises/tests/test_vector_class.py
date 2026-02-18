from solution.vector_class import Vector2D   

def test_addition():
    v1 = Vector2D(3.0, 4.0)
    v2 = Vector2D(1.0, 2.0)
    assert (v1 + v2) == Vector2D(4.0, 6.0)


def test_magnitude():
    v = Vector2D(3.0, 4.0)
    assert abs(v) == 5.0
