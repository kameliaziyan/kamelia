from functools import lru_cache


@lru_cache(maxsize=100)
def fibonacci(n: int) -> int:

    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(1))  # Output: 0
print(fibonacci(2))  # Output: 1
print(fibonacci(200))  # Output: 34
