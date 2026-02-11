
# returns only people who are 18 or older
def filter_adults(people: list[dict]) -> list[dict] :
    result = filter(lambda person: person["age"] >= 18, people)

    return list(result)

# returns a list of names only
def get_names(people: list[dict]) -> list[str] :
    result = map(lambda person: person["name"], people)


    return list(result)

# returns people sorted by age in ascending order
def sort_by_age(people: list[dict]) -> list[dict] :
    result = sorted(people, key=lambda person: person["age"])

    return list(result)



people = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 17},
    {"name": "Charlie", "age": 30},
    {"name": "Diana", "age": 16}
]

print(filter_adults(people))
# Output: [{"name": "Alice", "age": 25}, {"name": "Charlie", "age": 30}]

print(get_names(people))
# Output: ["Alice", "Bob", "Charlie", "Diana"]

print(sort_by_age(people))
# Output: [{"name": "Diana", "age": 16}, {"name": "Bob", "age": 17},
#          {"name": "Alice", "age": 25}, {"name": "Charlie", "age": 30}]
