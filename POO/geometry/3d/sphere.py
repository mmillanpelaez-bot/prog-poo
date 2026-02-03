import math
from point import Point
from POO.geometry.shape3d import Shape3D

class Sphere(Shape3D):
    def __init__(self, center: Point, radius: float):
        super().__init__(center)
        self.radius = radius

    def diameter(self) -> float:
        return 2 * self.radius

    def surface_area(self) -> float:
        return 4 * math.pi * (self.radius ** 2)

    def volume(self) -> float:
        return (4/3) * math.pi * (self.radius ** 3)

    def __str__(self) -> str:
        return (
            f"Sphere centered at {self.center} with radius {self.radius}\n"
            f"Diameter: {self.diameter():.2f}\n"
            f"Surface Area: {self.surface_area():.2f}\n"
            f"Volume: {self.volume():.2f}"
        )
