from pathlib import Path

from solution.repository.csv_accessor import CsvFileAccessor


def test_read_empty_file(tmp_path: Path) -> None:
    file_path = tmp_path / "data.csv"
    accessor = CsvFileAccessor(str(file_path))

    result = accessor.read()

    assert result == []


def test_write_and_read(tmp_path: Path) -> None:
    file_path = tmp_path / "data.csv"
    accessor = CsvFileAccessor(str(file_path))

    rows = [
        {"id": "1", "account_name": "Account1"},
        {"id": "2", "account_name": "Account2"},
    ]
    accessor.write(rows)
    result = accessor.read()

    assert result == rows
