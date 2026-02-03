class Point:
    def __init__(self, x: float, y: float, z: float):
        self.x = x
        self.y = y
        self.z = z

    def toString(self) -> str:
        return f"The point coordinates are: ({self.x}, {self.y}, {self.z})"

    def __str__(self) -> str:
        return self.toString()

    def __eq__(self, other) -> bool:
        return self.x == other.x and self.y == other.y and self.z == other.z