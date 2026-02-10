from solution.number_pattern_generator import generate_pyramid


def test_height_9():
    result = generate_pyramid(9)
    assert result == "12345678987654321"

def test_height_7():
    result = generate_pyramid(7)
    assert result == "1234567654321"

def test_height_1():
    result = generate_pyramid(1)
    assert result == "1"

