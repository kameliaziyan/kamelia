def extract_pid(logg: str) -> int:
    try:
        return int(logg.split("pid:")[1].split("]")[0])
    except (IndexError, ValueError):
        raise ValueError("Invalid log format or pid not found")
