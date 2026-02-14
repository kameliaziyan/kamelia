import sys


def value_info(value: object) -> None:
    value_type = type(value)
    size = sys.getsizeof(value)

    print(
        f"Type: {value_type}, " f"Value: {value}, " f"Size: {size} bytes.",
    )


def variable_types() -> None:
    values = [
        2,
        99,
        5555,
        10,
        77,
        2.5,
        7.999,
        33.3,
        9999.9,
        54.3,
        "HELLO",
        "bye",
        "kamelia",
        "codevale",
        "code",
        True,
        None,
    ]

    for value in values:
        value_info(value)
