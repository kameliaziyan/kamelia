from solution.list_operations import filter_adults, get_names, sort_by_age


def test_filter_adults_basic():
    people = [
        {"name": "Alice", "age": 25},
        {"name": "Bob", "age": 17},
    ]

    result = filter_adults(people)

    assert result == [{"name": "Alice", "age": 25}]



def test_get_names_basic():
    people = [
        {"name": "Alice", "age": 25},
        {"name": "Bob", "age": 17},
    ]

    assert get_names(people) == ["Alice", "Bob"]



def test_sort_by_age_basic():
    people = [
        {"name": "Alice", "age": 25},
        {"name": "Bob", "age": 17},
        {"name": "Charlie", "age": 30},
    ]

    result = sort_by_age(people)

    assert result == [
        {"name": "Bob", "age": 17},
        {"name": "Alice", "age": 25},
        {"name": "Charlie", "age": 30},
    ]


