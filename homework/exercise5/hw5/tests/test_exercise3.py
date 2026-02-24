import time
import pytest
from solution.exercise3 import MyLruCache


@pytest.mark.parametrize(
    "cache_key,cache_value",
    [
        ("first_key", 1),
        ("second_key", "hello"),
        ("third_key", {"field": 10}),
    ],
)
def test_set_and_get(
    cache_key: str,
    cache_value: object,
) -> None:
    cache = MyLruCache(maxsize=3, ttl=10)
    cache.set(cache_key, cache_value)

    assert cache.get(cache_key) == cache_value


def test_missing_key_and_len_behavior() -> None:

    cache = MyLruCache(maxsize=3, ttl=10)
    assert cache.get("non_existing_key") is None
    assert len(cache) == 0


def test_update_existing_key() -> None:
    cache = MyLruCache(maxsize=3, ttl=10)
    cache.set("user_identifier", 100)
    cache.set("user_identifier", 200)

    assert cache.get("user_identifier") == 200


@pytest.mark.parametrize(
    "first_inserted,second_inserted,third_inserted,expected_evicted",
    [
        ("first_key", "second_key", "third_key", "first_key"),
        ("alpha_key", "beta_key", "gamma_key", "alpha_key"),
    ],
)
def test_lru_eviction(
    first_inserted: str,
    second_inserted: str,
    third_inserted: str,
    expected_evicted: str,
) -> None:
    cache = MyLruCache(maxsize=2, ttl=10)
    cache.set(first_inserted, 1)
    cache.set(second_inserted, 2)
    cache.set(third_inserted, 3)

    assert cache.get(expected_evicted) is None


def test_access_prevents_eviction_maxsize() -> None:

    cache = MyLruCache(maxsize=2, ttl=10)
    cache.set("first_item", 1)
    cache.set("second_item", 2)
    cache.get("first_item")
    cache.set("third_item", 3)

    assert cache.get("second_item") is None
    assert cache.get("first_item") == 1
    assert cache.get("third_item") == 3


@pytest.mark.parametrize("time_to_live", [0.5, 1.0])
def test_ttl_expiration(time_to_live: float) -> None:
    cache = MyLruCache(maxsize=2, ttl=time_to_live)
    cache.set("temporary_key", 123)
    time.sleep(time_to_live + 0.1)

    assert cache.get("temporary_key") is None


def test_refresh_and_contains_behavior() -> None:
    cache = MyLruCache(maxsize=2, ttl=1)

    cache.set("refreshable_key", 10)
    time.sleep(0.5)
    cache.set("refreshable_key", 20)

    assert "refreshable_key" in cache
    time.sleep(0.6)
    assert cache.get("refreshable_key") == 20


def test_clear() -> None:

    cache = MyLruCache(maxsize=3, ttl=10)
    cache.set("first_key", 1)
    cache.set("second_key", 2)
    cache.clear()
    assert len(cache) == 0
