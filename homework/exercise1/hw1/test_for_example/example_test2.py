from solution.exercise2 import extract_title


def test_extract_title() -> None:
    html = "<html><head><title>My Title</title></head><body></body></html>"
    expected_output = "My Title"
    # actual_result = extract_title(html)
    assert extract_title(html) == expected_output
