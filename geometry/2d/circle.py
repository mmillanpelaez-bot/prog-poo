import math
from point import Point

class Circle:
    def __init__(self, center: Point, radius: float):
        self.center = center
        self.radius = radius

    def diameter(self) -> float:
        return 2 * self.radius

    def perimeter(self) -> float:
        return 2 * math.pi * self.radius

    def area(self) -> float:
        return math.pi * (self.radius ** 2)

    def __str__(self) -> str:
        return (
            f"Circle centered at {self.center} with radius {self.radius}\n"
            f"Diameter: {self.diameter():.2f}\n"
            f"Perimeter: {self.perimeter():.2f}\n"
            f"Area: {self.area():.2f}"
        )




