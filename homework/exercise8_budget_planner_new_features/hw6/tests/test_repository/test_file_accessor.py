import json
from pathlib import Path
import pytest
from solution.repository.file_accessor import JsonFileAccessor


def test_write_and_read(tmp_path: Path) -> None:

    file_path = tmp_path / "data.json"

    accessor = JsonFileAccessor(str(file_path))
    data = {"items": [{"id": 1, "amount": 100}]}
    accessor.write(data)
    result = accessor.read()

    assert result == data


def test_read_non_existing_file(tmp_path: Path) -> None:

    file_path = tmp_path / "missing.json"
    accessor = JsonFileAccessor(str(file_path))
    result = accessor.read()
    assert result == {"items": []}


def test_overwrite_data(tmp_path: Path) -> None:
    file_path = tmp_path / "data.json"

    accessor = JsonFileAccessor(str(file_path))
    accessor.write({"items": []})
    accessor.write({"items": [{"id": 2}]})
    result = accessor.read()

    assert result["items"][0]["id"] == 2
