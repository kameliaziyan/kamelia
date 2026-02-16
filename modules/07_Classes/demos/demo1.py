
from dataclasses import dataclass


class Room:
    def __init__(self, width: float, length: float) -> None:
        self.setWidth(width)
        self._length = length

    def getSquareMeter(self):
        return self._width * self._length
    
    def getWidth(self):
        return self._width
    
    def setWidth(self, width: float):
        if (width <= 0):
            return None
        
        self._width = width
    
living_room = Room(4, 5)
print(f"Living room square meter: {living_room.getSquareMeter()}")
living_room.setWidth(9)
living_room.setWidth(0)
print(f"Living room square meter: {living_room.getSquareMeter()}")

class RoomWithProperties:
    def __init__(self, width: float, length: float) -> None:
        self.width = width
        self._length = length
    
    @property
    def square_meter(self):
        return self._width * self._length
    
    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self, value: float):
        if (value <= 0):
            return None
        
        self._width = value
    
    @width.deleter
    def width(self):
        self._width = 0
    
room1 = RoomWithProperties(4,5)
room1.width = 9
print(f"Living room square meter: {room1.square_meter}")
del room1.width

# ========================================

class User:
    def __init__(self, username, email, phone) -> None:
        self.username = username
        self.email = email
        self.phone = phone

    def __str__(self) -> str:
        ...

@dataclass
class UserData:
    username: str
    email: str
    phone: str
    age: int

user_data = UserData("shayf", "shayf@codevalue.com", "0537851198", 42)
print(user_data)