import asyncio
import timeit
from typing import Any

import aiohttp
import requests

BASE_URL = "https://jsonplaceholder.typicode.com/todos"
TOTAL_TODOS = 20
MAX_WORKERS = 8
REQUEST_TIMEOUT = 5


async def fetch_todo(session: aiohttp.ClientSession, todo_id: int) -> dict[str, Any]:

    url = f"{BASE_URL}/{todo_id}"

    async with session.get(url) as response:
        data = await response.json()
        print(f"TODO {todo_id}: {data['title']}")
        return data


async def main() -> None:
    start_time = timeit.default_timer()
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_todo(session, item) for item in range(1, TOTAL_TODOS + 1)]

        results = await asyncio.gather(*tasks)

    end_time = timeit.default_timer()

    total_time = end_time - start_time
    avg_time = total_time / len(results)

    print("\nSummary:")
    print(f"Total execution time: {total_time:.2f} seconds")
    print(f"Average time per request: {avg_time:.3f} seconds")


if __name__ == "__main__":
    asyncio.run(main())
