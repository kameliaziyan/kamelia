from solution.TemperatureConverter import convert_temperature


def test_celsius_to_fahrenheit():
    result = convert_temperature(0, "C", "F")
    assert result == 32.0


def test_fahrenheit_to_celsius():
    result = convert_temperature(32, "F", "C")
    assert result == 0.0


def test_celsius_to_kelvin():
    result = convert_temperature(100, "C", "K")
    assert result == 373.15


