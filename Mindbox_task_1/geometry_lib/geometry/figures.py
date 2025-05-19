import math
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        pass


class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        return math.pi * self.radius ** 2


class Triangle(Shape):
    def __init__(self, a: float, b: float, c: float):
        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError("Стороны не образуют треугольник.")
        self.a, self.b, self.c = a, b, c

    def area(self) -> float:
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def is_right(self) -> bool:
        sides = sorted([self.a, self.b, self.c])
        return math.isclose(sides[0]**2 + sides[1]**2, sides[2]**2)


class Square(Shape):
    def __init__(self, side: float):
        self.side = side

    def area(self) -> float:
        return self.side ** 2
