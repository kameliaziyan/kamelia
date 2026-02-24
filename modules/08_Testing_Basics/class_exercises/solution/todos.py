from typing import Any
import requests

BASE_URL = "https://jsonplaceholder.typicode.com/todos"


def fetch_sorted_todos(limit: int = 20) -> list[dict[str, Any]]:
    if limit < 1:
        raise ValueError("limit must be bigger than 0")

    todos: list[dict[str, Any]] = []

    for number in range(1, limit + 1):
        response = requests.get(f"{BASE_URL}/{number}")
        response.raise_for_status()

        item: dict[str, Any] = response.json()

        todo = {
            "id": item["id"],
            "userId": item["userId"],
            "title": item["title"],
            "completed": item["completed"],
        }

        todos.append(todo)

    return sorted(todos, key=lambda todo: todo["title"])
