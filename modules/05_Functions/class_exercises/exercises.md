# Class Exercises: Functions

## General Requirements

- Do not use any Generative-AI (like ChatGPT) tools to solve these exercises. The purpose is to practice your own skills. You can use Generative-AI tools to help you understand concepts, but not to generate the solution code.
- Provide unit tests where asked using the `pytest` framework.
- All the unit tests should be in a Python package called `tests`. Use a separate Python module for each exercise test suite.
- The unit test module should be called by convention `test_<subject>.py`
- Use Type Hints for function arguments and return values
- If the functions is long (beyond 15 lines of code), divide into more functions.



## Exercise 1: Count Calls Decorator

**Description:**
Create a decorator called `count_calls` that tracks how many times a decorated function has been called. The decorator should add a `call_count` attribute to the function that can be accessed to get the current count.

**Requirements:**
- Implement a `count_calls` decorator that increments a counter each time the decorated function is called
- The decorator should work with functions that have any number of arguments
- The decorator should preserve the original function's return value
- The counter should be accessible via the `call_count` attribute on the function
- Include type hints for the decorator
- Write at least 3 unit tests covering different scenarios

**Example:**

```python
@count_calls
def greet(name: str) -> str:
    return f"Hello, {name}!"

print(greet("Alice"))  # Output: "Hello, Alice!"
print(greet("Bob"))    # Output: "Hello, Bob!"
print(greet.call_count)  # Output: 2
```


## Exercise 2: Flexible Statistics Calculator

**Description:**
Create a function called `calculate_statistics` that accepts any number of keyword arguments representing named datasets and calculates statistics for each dataset. The function should return a dictionary with the dataset names as keys and a dictionary of statistics (sum, average, min, max) as values.

**Requirements:**
- Use `**kwargs` to accept arbitrary keyword arguments
- Each keyword argument value should be a list of numbers
- Calculate sum, average, min, and max for each dataset
- Return a dictionary with statistics for each dataset
- Handle empty lists by returning `None` for all statistics
- Include type hints for function arguments and return values
- Write at least 3 unit tests covering different scenarios including edge cases

**Example:**

```python
result = calculate_statistics(
    temperatures=[22.5, 24.0, 23.5, 25.0],
    humidity=[60, 65, 62, 68]
)

print(result)
# Output:
# {
#     'temperatures': {'sum': 95.0, 'average': 23.75, 'min': 22.5, 'max': 25.0},
#     'humidity': {'sum': 255, 'average': 63.75, 'min': 60, 'max': 68}
# }
```

