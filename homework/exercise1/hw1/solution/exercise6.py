import sys


def PrintingVariableTypes() -> None:

    # int
    print(f"Type : {type(2)}, Value: {2}, Size: {sys.getsizeof(2)} bytes.")
    print(f"Type : {type(99)}, Value: {99}, Size: {sys.getsizeof(99)} bytes.")
    print(f"Type : {type(5555)}, Value: {5555}, Size: {sys.getsizeof(5555)} bytes.")
    print(f"Type : {type(10)}, Value: {10}, Size: {sys.getsizeof(10)} bytes.")
    print(f"Type : {type(77)}, Value: {77}, Size: {sys.getsizeof(77)} bytes.")

    # float
    print(f"Type : {type(2.5)}, Value: {2.5}, Size: {sys.getsizeof(2.5)} bytes.")
    print(f"Type : {type(7.999)}, Value: {7.999}, Size: {sys.getsizeof(7.999)} bytes.")
    print(f"Type : {type(33.3)}, Value: {33.3}, Size: {sys.getsizeof(33.3)} bytes.")
    print(
        f"Type : {type(9999.9)}, Value: {9999.9}, Size: {sys.getsizeof(9999.9)} bytes."
    )
    print(f"Type : {type(2)}, Value: {2}, Size: {sys.getsizeof(2)} bytes.")

    # str
    print(
        f"Type : {type('HELLO')}, Value: {'HELLO'}, Size: {sys.getsizeof('HELLO')} bytes."
    )
    print(f"Type : {type('bye')}, Value: {'bye'}, Size: {sys.getsizeof('bye')} bytes.")
    print(
        f"Type : {type('kamelia')}, Value: {'kamelia'}, Size: {sys.getsizeof('kamelia')} bytes."
    )
    print(
        f"Type : {type('codevale')}, Value: {'codevale'}, Size: {sys.getsizeof('codevale')} bytes."
    )
    print(
        f"Type : {type('code')}, Value: {'code'}, Size: {sys.getsizeof('code')} bytes."
    )

    # bool
    print(f"Type : {type(True)}, Value: {True}, Size: {sys.getsizeof(True)} bytes.")

    # None
    print(f"Type : {type(None)}, Value: {None}, Size: {sys.getsizeof(None)} bytes.")

    return None


# PrintingVariableTypes()
# **Example output**;


# Type: <class 'int'>, Value: 1, Size: 28 bytes
# Type: <class 'int'>, Value: 42, Size: 28 bytes
