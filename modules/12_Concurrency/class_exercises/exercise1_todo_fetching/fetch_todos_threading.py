from __future__ import annotations

import time
from typing import Any

import requests
from concurrent.futures import ThreadPoolExecutor, as_completed

BASE_URL = "https://jsonplaceholder.typicode.com/todos"
TOTAL_TODOS = 20
MAX_WORKERS = 8
REQUEST_TIMEOUT = 5


def fetch_todo(todo_id: int) -> dict[str, Any]:
    response = requests.get(
        f"{BASE_URL}/{todo_id}",
        timeout=REQUEST_TIMEOUT,
    )
    response.raise_for_status()
    return response.json()


def print_summary(total_time: float, count: int) -> None:
    if count:
        avg_time = total_time / count

    else:
        avg_time = float()

    print(f"Total execution time: {total_time:.2f} seconds")
    print(f"Average time per request: {avg_time:.3f} seconds")


def main() -> None:

    start_time = time.time()
    results_count = 0

    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        futures = executor.map(fetch_todo, range(1, TOTAL_TODOS + 1))

        for result in futures:
            todo_id = result["id"]
            title = result["title"]
            print(f"TODO {todo_id}: {title}")
            results_count += 1

    total_time = time.time() - start_time
    print_summary(total_time, results_count)


if __name__ == "__main__":
    main()
