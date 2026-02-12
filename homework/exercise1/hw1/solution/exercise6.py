import sys


def print_value_info(value: object) -> None:
    value_type = type(value)
    size = sys.getsizeof(value)

    print(
        f'Type: {value_type}, '
        f'Value: {value}, '
        f'Size: {size} bytes.',
    )


def printing_variable_types() -> None:
    values = [
        2, 99, 5555, 10, 77,
        2.5, 7.999, 33.3, 9999.9,
        'HELLO', 'bye', 'kamelia', 'codevale', 'code',
        True, None,
    ]

    for value in values:
        print_value_info(value)
