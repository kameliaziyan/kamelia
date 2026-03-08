import datetime
import json
from collections.abc import AsyncGenerator
from typing import Any

import pytest
from httpx import ASGITransport, AsyncClient

from src.secrets_accessor import RunMode, get_secrets_accessor

# Exercise 4: Uncomment these imports after completing the database exercises
# from src.database import Base, async_session_maker, engine
# from src.models.student import Student
# from sqlalchemy import insert


async def _verify_test_mode() -> None:
    """Verify that we're running in test mode."""
    sa = get_secrets_accessor()
    assert sa.get_app_mode() == RunMode.TEST.value


async def _setup_database() -> None:
    """
    Connect to the database, drop all tables, and create them again.

    Exercise 4: Implement this function after completing the database exercises.
    First, uncomment the database imports at the top of this file.
    Then use engine.begin() as a context manager to run sync operations:

        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.drop_all)
            await conn.run_sync(Base.metadata.create_all)
    """
    raise NotImplementedError()


def _load_mock_students() -> list[dict[str, Any]]:
    """Load mock student data from JSON, parsing date strings."""
    with open(
        "src/tests/fixtures/mock_students.json", "r", encoding="utf-8"
    ) as mock_file:
        raw_data: list[dict[str, Any]] = json.load(mock_file)
    result: list[dict[str, Any]] = []
    for item in raw_data:
        birth_date_str = item.get("birth_date")
        if birth_date_str:
            item["birth_date"] = datetime.date.fromisoformat(birth_date_str)
        result.append(item)
    return result


async def _insert_mock_data() -> None:
    """
    Load and insert mock students into the test database.

    Exercise 4: Implement this function after completing the models exercise.
    First, uncomment the model and database imports at the top of this file.
    Then:
    1. Load students using _load_mock_students()
    2. Use async_session_maker() as a context manager to insert the data
    3. Use sqlalchemy's insert() function to bulk-insert records
    """
    raise NotImplementedError()


@pytest.fixture(autouse=True, scope="session")
async def prepare_database() -> None:
    """
    Main fixture to prepare the test database.
    This is executed automatically before any tests run.

    ******* Exercise 4 ********
    Implement this function to prepare the DB for each pytest session.
    Read the helper methods in this file.
    Uncomment the necessary imports to make it work.
    To fully prepare the test environment you must:

    - Verify that you are running in test mode
    - Re-create all the models in the test DB
    - Load the mock data to the DB
    """
    raise NotImplementedError()


@pytest.fixture
async def ac() -> AsyncGenerator[AsyncClient, None]:
    """Create a test client for the FastAPI application."""
    from src.app import app

    # Exercise 4
    # Use the FastAPI docs to create your AsyncClient instance:
    # https://fastapi.tiangolo.com/advanced/async-tests/?h=async+tests#async-tests
    #
    # async with AsyncClient(
    #     transport=ASGITransport(app=app), base_url="http://test"
    # ) as client:
    #     yield client
    raise NotImplementedError()
