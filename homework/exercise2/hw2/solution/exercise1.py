def analyze_log_content(log_content: str) -> dict:

    count_error = 0
    count_warning = 0
    count_info = 0
    dict_count = {}

    for index, character in enumerate(log_content):
        if log_content.find("ERROR", index) == index:
            count_error += 1

        if log_content.find("WARNING", index) == index:

            count_warning += 1

        if log_content.find("INFO", index) == index:
            count_info += 1

    dict_count["Error"] = count_error
    dict_count["Warning"] = count_warning
    dict_count["Info"] = count_info

    return dict_count
