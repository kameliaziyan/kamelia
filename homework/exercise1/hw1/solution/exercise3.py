def extracting_key_value(given_key: str, line: str) -> str:

    after_pid = line.split(given_key + ":")
    cut_after_pid = after_pid[1]
    taking_number = cut_after_pid.split("]")
    cut_taking_number = taking_number[0]

    return cut_taking_number
