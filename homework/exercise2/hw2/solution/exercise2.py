INVALID_OPERATION = "invalid operation"


def print_invalid() -> None:
    print(INVALID_OPERATION)


def handle_command(words: list[str]) -> str:
    command = words[0]
    if command == "add":
        return add(words)

    elif command == "subtract":
        return subtract(words)

    elif command == "divide":
        return divide(words)

    elif command == "multiply":
        return multiply(words)

    return INVALID_OPERATION


def validate_input(words: list[str]) -> bool:
    is_valid = True

    if len(words) == 1:
        if words[0] == "help":
            print(
                "Available commands:\n"
                "add 2 to 5\n"
                "subtract 2 from 5\n"
                "multiply 2 by 5\n"
                "divide 10 by 5\n"
            )
        else:
            print_invalid()
        is_valid = False

    elif len(words) == 4:
        try:
            int(words[1])
        except ValueError:
            print_invalid()
            is_valid = False

        try:
            int(words[3])
        except ValueError:
            print_invalid()
            is_valid = False

    else:
        print_invalid()
        is_valid = False

    return is_valid


def add(line: list[str]) -> str:
    if line[2] == "to":

        first_number = int(line[1])
        second_number = int(line[3])

        result = first_number + second_number
        return f"The answer is {result}"
    else:
        return INVALID_OPERATION


def subtract(line: list[str]) -> str:
    if line[2] == "from":

        first_number = int(line[1])
        second_number = int(line[3])

        result = second_number - first_number
        return f"The answer is {result}"
    else:
        return INVALID_OPERATION


def multiply(line: list[str]) -> str:
    if line[2] == "by":

        first_number = int(line[1])
        second_number = int(line[3])

        result = first_number * second_number
        return f"The answer is {result}"
    else:
        return INVALID_OPERATION


def divide(line: list[str]) -> str:
    if line[2] == "by":

        first_number = int(line[1])
        second_number = int(line[3])
        if second_number == 0:
            return INVALID_OPERATION

        result = first_number / second_number
        return f"The answer is {result}"

    return INVALID_OPERATION


def calculator() -> None:

    while True:
        data = input("enters a valid operation ")

        if not data:
            print_invalid()
            continue

        if data.lower() == "exit":
            break

        words = data.split()

        if validate_input(words):
            result = handle_command(words)
            print(result)
