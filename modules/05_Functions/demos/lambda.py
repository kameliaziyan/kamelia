"""
Demo - Lambda Expressions
"""


def square(a):
    return a * a


my_list = [1,2,3,4,5]
map_object = map(square, my_list)
squares = list(map_object)

print(map_object)
print(squares)
