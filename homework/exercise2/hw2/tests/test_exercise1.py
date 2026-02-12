from solution.exercise1 import analyze_log_content


def test_analyze_log_content_counts_correctly() -> None:
    log_content = (
        "2024-04-29 15:45:00,089 INFO message one\n"
        "2024-04-29 15:45:05,123 WARNING message two\n"
        "2024-04-29 15:45:10,456 ERROR message three\n"
        "2024-04-29 15:46:00,789 INFO message four"
    )

    result = analyze_log_content(log_content)

    assert result == {
        "Error": 1,
        "Warning": 1,
        "Info": 2,
    }


def test_no_valid_entries() -> None:
    log_content = "Random line one\n" "Another random line\n" "No log level here"

    result = analyze_log_content(log_content)

    assert result == {
        "Error": 0,
        "Warning": 0,
        "Info": 0,
    }
