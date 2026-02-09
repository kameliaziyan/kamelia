from solution.NumberPatternGenerator import generate_pyramid


def test_generate_pyramid_height_3():
    result = generate_pyramid(3)

    expected = (
        "  1\n"
        " 121\n"
        "12321"
    )

    assert result == expected




def test_generate_pyramid_height_1():
    result = generate_pyramid(1)
    assert result == "1"


def test_generate_pyramid_height_4():
    result = generate_pyramid(4)

    expected = (
        "   1\n"
        "  121\n"
        " 12321\n"
        "1234321"
    )

    assert result == expected


