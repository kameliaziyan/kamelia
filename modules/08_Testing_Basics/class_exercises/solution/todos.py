from typing import Any
import requests

BASE_URL = "https://jsonplaceholder.typicode.com/todos"


def fetch_sorted_todos(limit: int) -> list[dict[str, Any]]:

    if limit < 1:
        raise ValueError("limit must be begger than 0")

    response = requests.get(BASE_URL)
    response.raise_for_status()

    result = response.json()
    todos = []

    for item in result[:limit]:
        todo = {
            "id": item["id"],
            "userId": item["userId"],
            "title": item["title"],
            "completed": item["completed"],
        }

        todos.append(todo)

    sorted_todos = sorted(todos, key=lambda todo: todo["title"])
    return sorted_todos


