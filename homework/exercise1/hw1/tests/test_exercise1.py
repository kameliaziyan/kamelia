# Provide the missing imports
from solution.exercise1 import extract_pid


def test_extract_pid_large_number() -> None:
    log_line = "DEBUG [name:test][pid:123456][uuid:abc]"

    result = extract_pid(log_line)

    assert result == 123456
    assert isinstance(result, int)


def test_extract_pid_different_position() -> None:
    log_line = "[account:10][uuid:xyz][pid:8888][process:test]"

    result = extract_pid(log_line)

    assert result == 8888
    assert isinstance(result, int)


def test_extract_pid_single_digit() -> None:
    log_line = "INFO [pid:7][account:123]"

    result = extract_pid(log_line)

    assert result == 7
    assert isinstance(result, int)
