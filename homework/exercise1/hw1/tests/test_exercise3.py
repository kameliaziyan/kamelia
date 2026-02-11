from solution.exercise3 import extracting_key_value


def test_extract_account() -> None:
    line = "[pid:2995]" "[account:519]" "[GamePlay:400004380]"

    result = extracting_key_value("account", line)

    assert result == "519"
    assert isinstance(result, str)


def test_extract_uuid() -> None:
    line = "[uuid:abc-123][pid:1111][account:22]"

    result = extracting_key_value("uuid", line)

    assert result == "abc-123"


def test_extract_gameplay() -> None:
    line = "[account:10][GamePlay:400004380][pid:8888]"

    result = extracting_key_value("GamePlay", line)

    assert result == "400004380"
