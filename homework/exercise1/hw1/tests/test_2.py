import pytest
# Provide the missing imports
from solution.extracting_data import  extract_title

def test_extract_title():
    html = "<html><head><title>My Title</title></head><body></body></html>"
    expected_output = "My Title"
    actual_result = extract_title(html)
    assert extract_title(html) == expected_output
