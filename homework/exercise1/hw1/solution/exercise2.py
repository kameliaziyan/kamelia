def extract_title(strr: str) -> str:
    try:
        return strr.split("<title>")[1].split("</title>")[0]
    except IndexError:
        raise ValueError("Title tag not found or malformed HTML")
