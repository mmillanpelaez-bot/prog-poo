import math
from point import Point
from shape3d import Shape3D

class Cylinder(Shape3D):
    def __init__(self, center: Point, radius: float, height: float):
        super().__init__(center)
        self.radius = radius
        self.height = height

    def diameter(self) -> float:
        return 2 * self.radius

    def surface_area(self) -> float:
        return 2 * math.pi * (self.radius ** 2) + 2 * math.pi * self.radius * self.height

    def volume(self) -> float:
        return math.pi * (self.radius ** 2) * self.height

    def __str__(self) -> str:
        return (
            f"Cylinder centered at {self.center} with radius {self.radius} and height {self.height}\n"
            f"Diameter: {self.diameter():.2f}\n"
            f"Surface Area: {self.surface_area():.2f}\n"
            f"Volume: {self.volume():.2f}"
        )
