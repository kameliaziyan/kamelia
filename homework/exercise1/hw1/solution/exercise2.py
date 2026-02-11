def extract_title(strr: str) -> str:

    split_strr = strr.split("<title>")
    new_strr = split_strr[1]
    split_new_strr = new_strr.split("</title>")
    get_title = split_new_strr[0]

    return get_title
