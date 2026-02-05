def add(a: int, b: int) -> int:
    return a + b


def divide(a: int, b: int) -> float:
    if (b == 0):
        raise ZeroDivisionError()
    return a / b


def multiply(a: int, b: int) -> int:
    raise NotImplementedError()
