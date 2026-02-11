def extract_pid(logg: str) -> int:

    split_logg = logg.split("pid:")
    after_pid = split_logg[1]
    split_taking_number = after_pid.split("]")
    taking_number = split_taking_number[0]

    return int(taking_number)
