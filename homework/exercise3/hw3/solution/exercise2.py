from functools import lru_cache


@lru_cache(maxsize=None)
def fibonacci(number: int) -> int:
    if number < 1:
        raise ValueError("number must be greater than or equal to 1")

    if number == 1:
        return 0
    if number == 2:
        return 1

    else:
        return fibonacci(number - 1) + fibonacci(number - 2)
