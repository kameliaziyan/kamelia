

def count_calls(func):

    def wrapper(*args, **kwargs):
        wrapper.call_count += 1
        return func(*args, **kwargs)

    wrapper.call_count = 0
    return wrapper


@count_calls
def greet(name: str) -> str:
    return f"Hello, {name}!"

print(greet("Alice"))  # Output: "Hello, Alice!"
print(greet("Bob"))    # Output: "Hello, Bob!"
print(greet.call_count)  # Output: 2





