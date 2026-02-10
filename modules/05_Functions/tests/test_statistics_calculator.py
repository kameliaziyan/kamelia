from class_exercises.flexible_statistics_calculator import calculate_statistics


def test_single_dataset():
    result = calculate_statistics(numbers=[1, 2, 3, 4])

    assert result["numbers"]["sum"] == 10
    assert result["numbers"]["average"] == 2.5
    assert result["numbers"]["min"] == 1
    assert result["numbers"]["max"] == 4


def test_multiple_datasets():
    result = calculate_statistics(
        temperatures=[20, 25, 30],
        humidity=[60, 70]
    )

    assert result["temperatures"]["average"] == 25
    assert result["humidity"]["sum"] == 130


def test_empty_dataset():
    result = calculate_statistics(empty=[])

    assert result["empty"]["sum"] is None
    assert result["empty"]["average"] is None
    assert result["empty"]["min"] is None
    assert result["empty"]["max"] is None
