import asyncio
import time

import aiohttp

URL = "http://localhost:8000/process_order?user_id=123&product_id=456&zip_code=12345"

NUMBER_REQUESTS = 20


async def send_request(session):
    start = time.perf_counter()

    async with session.get(URL) as response:
        await response.text()

    end = time.perf_counter()
    return end - start


async def main()-> None:
    start_total = time.perf_counter()

    async with aiohttp.ClientSession() as session:
        tasks = [send_request(session) for item in range(NUMBER_REQUESTS)]
        result = await asyncio.gather(*tasks)

    total_time = time.perf_counter() - start_total
    avg_time = sum(result) / total_time
    requests_per_second = NUMBER_REQUESTS / total_time

    print(f"Total Time: {total_time:.2f} seconds")
    print(f"Average Response Time: {avg_time:.2f} seconds")
    print(f"Requests Per Second:{requests_per_second:.2f}")


if __name__ == "__main__":
    asyncio.run(main())
