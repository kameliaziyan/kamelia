def extracting_key_value(given_key: str, line: str) -> str:
    try:
        return line.split(f"{given_key}:")[1].split("]")[0]
    except IndexError:
        raise ValueError(f"Key '{given_key}' not found in log line")
