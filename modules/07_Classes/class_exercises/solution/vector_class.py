import math


class Vector2D:
    x_axis: float
    y_axis: float

    def __init__(self, x_axis: float, y_axis: float):
        self.x_axis = x_axis
        self.y_axis = y_axis

    def __str__(self) -> str:
        return f"Vector2D({self.x_axis}, {self.y_axis})"

    def __repr__(self) -> str:
        return self.__str__()

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Vector2D):
            return False
        return self.x_axis == other.x_axis and self.y_axis == other.y_axis

    def __add__(self, other: Vector2D) -> Vector2D:
        return Vector2D(self.x_axis + other.x_axis, self.y_axis + other.y_axis)

    def __sub__(self, other: Vector2D) -> Vector2D:
        return Vector2D(self.x_axis - other.x_axis, self.y_axis - other.y_axis)

    def __mul__(self, scalar: float) -> Vector2D:
        return Vector2D(self.x_axis * scalar, self.y_axis * scalar)

    def __abs__(self) -> float:
        return math.sqrt((self.x_axis**2) + (self.y_axis**2))

    def magnitude(self) -> float:
        return math.hypot(self.x_axis, self.y_axis)

    def dot(self, other: "Vector2D") -> float:
        return self.x_axis * other.x_axis + self.y_axis * other.y_axis
