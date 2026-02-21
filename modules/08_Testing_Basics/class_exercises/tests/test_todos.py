import pytest
import requests
from solution.todos import fetch_sorted_todos
from unittest.mock import patch, Mock


@pytest.mark.parametrize("limit", [3, 6, 9])
def test_todos_sorted(limit : int) -> None:

    result = fetch_sorted_todos(limit)
    titles = [todo["title"] for todo in result]
    assert titles == sorted(titles)


@pytest.mark.parametrize("limit", [0, -3, -12])
def test_todos_invalidlimit(limit : int) -> None:

    with pytest.raises(ValueError):
        fetch_sorted_todos(limit)


@pytest.mark.parametrize("limit", [1, 3, 5])
@patch("requests.get")
def test_todos_success(mock_get : Mock, limit : int) -> None:

    example_data = [
        {"id": 1, "userId": 1, "title": "ccc", "completed": False},
        {"id": 2, "userId": 2, "title": "aaa", "completed": True},
        {"id": 3, "userId": 3, "title": "bbb", "completed": False},
    ]

    mock_response = Mock()
    mock_response.json.return_value = example_data
    mock_response.raise_for_status.return_value = None
    mock_get.return_value = mock_response

    result = fetch_sorted_todos(10)

    assert len(result) == 3

    titles = [todo["title"] for todo in result]
    assert titles == ["aaa", "bbb", "ccc"]


@pytest.mark.parametrize("status_code", [404, 500])
@patch("requests.get")
def test_todos_http_error(mock_get : Mock, status_code : int) -> None:

    mock_response = Mock()
    mock_response.raise_for_status.side_effect = requests.HTTPError()

    mock_get.return_value = mock_response

    with pytest.raises(requests.HTTPError):
        fetch_sorted_todos(3)
