from typing import Protocol

class Shape(Protocol):
    def area(self) -> float:
        pass

    def perimeter(self) -> float:
        pass

class Circle:
    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        return 3.14 * self.radius ** 2

    def perimeter(self) -> float:
        return 2 * 3.14 * self.radius

class Rectangle:
    def __init__(self, length: float, width: float):
        self.length = length
        self.width = width

    def area(self) -> float:
        return self.length * self.width

    def perimeter(self) -> float:
        return 2 * (self.length + self.width)

if __name__ == "__main__":
    # Instantiate objects of the derived classes and call the methods
    circle = Circle(radius=5)
    rectangle = Rectangle(length=4, width=6)

    print("Circle Area:", circle.area())
    print("Circle Perimeter:", circle.perimeter())

    print("Rectangle Area:", rectangle.area())
    print("Rectangle Perimeter:", rectangle.perimeter())
