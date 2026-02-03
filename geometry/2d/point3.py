class Point3:
    def __init__(self, x: float, y: float):
        self.__x = self.set_x(x)
        self.__y = self.set_y(y)

    def set_x(self, x):
        if type(x) == int or type (x) == float:
            if x > 3:
                self._x = x

    def toString(self) -> str:
        return f"The point coordinates are: ({self.x}, {self.y}, {self.z})"

    def __str__(self) -> str:
        return self.toString()

    def __eq__(self, other) -> bool:
        return self.x == other.x and self.y == other.y and self.z == other.z