from abc import ABC, abstractmethod
from point import Point

class Shape3D(ABC):
    def __init__(self, center: Point):
        self.center = center

    @abstractmethod
    def surface_area(self) -> float:
        pass

    @abstractmethod
    def volume(self) -> float:
        pass

    def __str__(self) -> str:
        return (
            f"{self.__class__.__name__} centered at {self.center}\n"
            f"Surface Area: {self.surface_area():.2f}\n"
            f"Volume: {self.volume():.2f}"
        )