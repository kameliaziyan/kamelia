import pytest
import requests
from solution.todos import fetch_sorted_todos
from unittest.mock import patch, Mock


@pytest.mark.parametrize("limit", [3, 5, 10])
def test_fetch_sorted_todos_sorted(limit) -> None:
    result = fetch_sorted_todos(limit)
    titles = [todo["title"] for todo in result]
    assert titles == sorted(titles)


@pytest.mark.parametrize("limit", [0, -1, -10])
def test_fetch_sorted_todos_invalid_limit(limit) -> None:
    with pytest.raises(ValueError):
        fetch_sorted_todos(limit)



@pytest.mark.parametrize("limit", [1, 3, 5])
@patch("requests.get")
def test_fetch_sorted_todos_success(mock_get, limit):
    fake_data = [
        {"id": 1, "userId": 1, "title": "c title", "completed": False},
        {"id": 2, "userId": 1, "title": "a title", "completed": True},
        {"id": 3, "userId": 1, "title": "b title", "completed": False},
    ]

    mock_response = Mock()
    mock_response.json.return_value = fake_data
    mock_response.raise_for_status.return_value = None
    mock_get.return_value = mock_response

    result = fetch_sorted_todos(limit)

    assert len(result) == min(limit, len(fake_data))

    titles = [todo["title"] for todo in result]
    assert titles == sorted(titles)


@pytest.mark.parametrize("status_code", [404, 500])
@patch("requests.get")
def test_fetch_sorted_todos_http_error(mock_get, status_code):
    mock_response = Mock()
    mock_response.raise_for_status.side_effect = requests.HTTPError()
    mock_get.return_value = mock_response

    with pytest.raises(requests.HTTPError):
        fetch_sorted_todos(3)

