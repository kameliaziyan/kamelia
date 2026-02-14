def detect_level(line: str) -> str:
    if line.find("ERROR") >= 0:
        return "ERROR"
    if line.find("WARNING") >= 0:
        return "WARNING"
    if line.find("INFO") >= 0:
        return "INFO"
    return ""


def analyze_log_content(log_content: str) -> dict:
    count_error = 0
    count_warning = 0
    count_info = 0

    for line in log_content.splitlines():
        level = detect_level(line)

        match level:
            case "ERROR":
                count_error += 1
            case "WARNING":
                count_warning += 1
            case "INFO":
                count_info += 1
            case _:
                pass

    return {
        "Error": count_error,
        "Warning": count_warning,
        "Info": count_info,
    }
