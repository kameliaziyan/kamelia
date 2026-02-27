import asyncio
from concurrent.futures import ProcessPoolExecutor
import time
import uvicorn
from fastapi import FastAPI
from typing import Any

process_pool = ProcessPoolExecutor()

app = FastAPI(title="Order Processing API", version="1.0.0")

USER_FETCH_DELAY = 0.5
INVENTORY_FETCH_DELAY = 0.3
SHIPPING_FETCH_DELAY = 0.4
PAYMENT_PROCESSING_DELAY = 0.2
FIBONACCI_INDEX = 30
SERVER_PORT = 8000


def calculate_fibonacci(index: int) -> int:
    if index <= 1:
        return index
    return calculate_fibonacci(index - 1) + calculate_fibonacci(index - 2)


async def fetch_user_data(user_id: int) -> dict:
    await asyncio.sleep(USER_FETCH_DELAY)
    return {
        "user_id": user_id,
        "name": f"User{user_id}",
        "email": f"user{user_id}@example.com",
    }


async def fetch_inventory_data(product_id: int) -> dict:
    await asyncio.sleep(INVENTORY_FETCH_DELAY)
    return {
        "product_id": product_id,
        "stock": 100,
        "warehouse": "Warehouse A",
    }


async def fetch_shipping_options(zip_code: str) -> list[dict[str, Any]]:
    await asyncio.sleep(SHIPPING_FETCH_DELAY)
    return [
        {"method": "Standard", "cost": 5.99, "days": 5},
        {"method": "Express", "cost": 15.99, "days": 2},
        {"method": "Overnight", "cost": 29.99, "days": 1},
    ]


@app.get("/process_order")
async def process_order(user_id: int, product_id: int, zip_code: str) -> dict:

    user = fetch_user_data(user_id)
    inventory = fetch_inventory_data(product_id)
    shipping = fetch_shipping_options(zip_code)

    user, inventory, shipping = await asyncio.gather(
        user,
        inventory,
        shipping,
    )
    loop = asyncio.get_running_loop()

    discount_factor = await loop.run_in_executor(
        process_pool,
        calculate_fibonacci,
        FIBONACCI_INDEX,
    )
    discount_factor %= 10
    await asyncio.sleep(PAYMENT_PROCESSING_DELAY)

    return {
        "user": user,
        "product": inventory,
        "shipping_options": shipping,
        "discount_percent": discount_factor,
        "status": "processed",
    }


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=SERVER_PORT)
