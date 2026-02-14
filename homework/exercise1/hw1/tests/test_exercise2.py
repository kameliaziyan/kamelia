from solution.exercise2 import extract_title


def test_extract_title_basic() -> None:
    html = "<html><head><title>My Title</title></head><body></body></html>"

    result = extract_title(html)

    assert result == "My Title"
    assert isinstance(result, str)


def test_extract_title_with_spaces_and_newline() -> None:
    html = "<html>\n<head>\n<title>   kamelia   </title>\n</head></html>"

    result = extract_title(html)

    assert result == "   kamelia   "
    assert isinstance(result, str)


def test_extract_title_multiple_titles() -> None:
    html = "<title>page 1</title><title>page 2</title>"

    result = extract_title(html)

    assert result == "page 1"


def test_extract_title_special_characters() -> None:
    html = "<html><head><title>welcome to my page!</title></head></html>"

    result = extract_title(html)

    assert result == "welcome to my page!"
