from functools import lru_cache


@lru_cache(maxsize=100)
def fibonacci(number: int) -> int:

    if number == 0:
        return 0
    if number == 1:
        return 1
    
    else:
        return fibonacci(number - 1) + fibonacci(number - 2)