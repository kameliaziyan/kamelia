from solution.count_calls_decorator import count_calls


def test_call_count_increments():
    @count_calls
    def greet(name: str) -> str:
        return f"Hello, {name}!"

    greet("Alice")
    greet("Bob")

    assert greet.call_count == 2


def test_return_value_preserved():
    @count_calls
    def add(a: int, b: int) -> int:
        return a + b

    result = add(2, 3)

    assert result == 5
    assert add.call_count == 1


def test_multiple_arguments():
    @count_calls
    def combine(a: int, b: int, c: int = 0) -> int:
        return a + b + c

    combine(1, 2)
    combine(1, 2, 3)

    assert combine.call_count == 2
