

def with_olives(pizza_func):
    def wrapper():
        description = pizza_func()
        return description + ' Olives'
    return wrapper


def with_onion(pizza_func):
    def wrapper():
        description = pizza_func()
        return description + ' Onion'
    return wrapper


@with_olives
@with_onion
def pizza() -> str:
    return 'I am a Pizza. My toppings are: '


if __name__ == '__main__':
    my_pizza = pizza()
    print(my_pizza)
