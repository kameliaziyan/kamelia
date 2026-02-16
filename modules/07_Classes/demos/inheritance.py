from abc import ABC


class Animal:
    def __init__(self, type, number_of_legs, age) -> None:
        self.type = type
        self.number_of_legs = number_of_legs
        self.age = age

    def breath(self):
        print("I'm breathing")

    def swim(self):
        print("I'm swimming")
    
    def walk(self):
        print("Put first leg forward")

class FourLeggedAnimal(Animal):
    def __init__(self, type, age, is_pet) -> None:
        super().__init__(type, 4, age)
        self.is_pet = is_pet
        
    def walk(self):
         super().walk()
         print("Also put back leg forward")
         print("put other legs forward")
         super().walk()

class TwoLeggedAnimal(Animal):
    def walk(self):
         print("I'm walking with 2 legs")

dog = FourLeggedAnimal("Dog", 3, True)
dog.breath()
dog.walk()

cat = FourLeggedAnimal("Cat", 3, False)
cat.breath()
cat.walk()

human = TwoLeggedAnimal("Human", 2, 20)
human.breath()
human.walk()

fish = Animal("Fish", 0, 1)
fish.breath()
fish.swim()

# ======= MIXINS ======

class PrettyPrintMixin:
    def pretty_print(self):
        self.pretty_print_color = "Red"
        self.pretty_print_line = "~*~" * 10
        print(self.pretty_print_line)
        print(self)
        print(self.pretty_print_line)
    
class Carr:
    def __init__(self, type, color) -> None:
        self.type = type
        self.color = color
    
    def drive(self):
        print("Driving")

class Truck(Carr, PrettyPrintMixin):
    pass

truck = Truck("Chevrolet", "Red")

""" JSON
{
  "name": "Shay"
  "age": 42 
}
"""
""" XML
<Object>
 <Name type="string">Shay</Name>
 <Age type="int">42</Age>
</Object>

"""

class Z:
    def __init__(self):
        print("Z's initializer")
        super().__init__()

class A:
    def __init__(self):
        print("A's initializer")
        super().__init__()

class B(Z):
    def __init__(self):
        print("B's initializer")
        super().__init__()

class C(A):
    def __init__(self):
        print("C's initializer")
        super().__init__()

class D(B, C):
    def __init__(self):
        print("D's initializer")
        super().__init__()

d = D()

# ==== ABSTRACT =====

class Vehicle(ABC):
    def drive(self):
        ...

class Car(Vehicle, ABC):
    def __init__(self, motor_type) -> None:
        self.motor_type = motor_type

    def start_motor(self):
        ...

    def drive(self):
        ...

class Toyota(Car, ABC):
    def start_motor(self):
        #....
        print("Starting the Toyota motor...")

class ToyotaCorola(Toyota):
    def __init__(self) -> None:
        self.motor_type = "Good"

    def drive(self):
        # .....
        print("Driving Toyota Corola")

vehicle = ToyotaCorola()
vehicle.drive()

class CarTestPlace:
    def test_car(self, car: Car):
        # test...
        pass




class Duck:
    def quack(self):
        print("Quack")
    
    def walk(self):
        print("Walk like a duck")

def quack(): 
    print("Quack")

def walk():
    print("Walk like a duck")

duck2 = {
    "quack": quack,
    "walk": walk
}

obj = Duck()


















obj.quack()
obj.walk()

duck2.quack()
duck2.walk()