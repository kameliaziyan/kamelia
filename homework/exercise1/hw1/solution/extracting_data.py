


def extract_title (strr : str) -> str :


    strr = strr.split("<title>")
    new_strr = strr[1]
    new_strr = new_strr.split("</title>")
    get_title = new_strr[0]


    return get_title




test_example =extract_title("<html><head><title>My Title</title></head><body></body></html>")
print(test_example)