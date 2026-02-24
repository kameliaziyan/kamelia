import pytest
import requests
import responses

from solution.todos import fetch_sorted_todos

BASE_URL = "https://jsonplaceholder.typicode.com/todos"


@pytest.mark.parametrize("limit", [3, 6, 9])
@responses.activate
def test_todos_sorted(limit: int) -> None:
    for number in range(1, limit + 1):
        title_number = limit - number

        responses.add(
            responses.GET,
            f"{BASE_URL}/{number}",
            json={
                "id": number,
                "userId": number,
                "title": f"title-{title_number}",
                "completed": False,
            },
            status=200,
        )

    result = fetch_sorted_todos(limit)

    titles = [todo["title"] for todo in result]
    assert titles == sorted(titles)
    assert len(result) == limit


@pytest.mark.parametrize("limit", [0, -3, -12])
def test_todos_invalidlimit(limit: int) -> None:
    with pytest.raises(ValueError):
        fetch_sorted_todos(limit)


@pytest.mark.parametrize("limit", [1, 3, 2])
@responses.activate
def test_todos_success(limit: int) -> None:
    example_data = [
        {"id": 1, "userId": 1, "title": "ccc", "completed": False},
        {"id": 2, "userId": 2, "title": "aaa", "completed": True},
        {"id": 3, "userId": 3, "title": "bbb", "completed": False},
        {"id": 4, "userId": 4, "title": "eee", "completed": False},
        {"id": 5, "userId": 5, "title": "fff", "completed": False},
    ]

    for index, item in enumerate(example_data[:limit], start=1):
        responses.add(
            responses.GET,
            f"{BASE_URL}/{index}",
            json=item,
            status=200,
        )

    result = fetch_sorted_todos(limit)

    assert len(result) == limit

    titles = [todo["title"] for todo in result]
    assert titles == sorted(titles)
