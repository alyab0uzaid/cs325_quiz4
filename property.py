class Rectangle:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    @property
    def area(self):
        return self._length * self._width

    @property
    def perimeter(self):
        return 2 * (self._length + self._width)

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, value):
        if value >= 0:
            self._length = value
        else:
            print("Length cannot be negative.")

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value >= 0:
            self._width = value
        else:
            print("Width cannot be negative.")

# Example usage:
if __name__ == "__main__":
    # Create an instance of the Rectangle class
    rectangle = Rectangle(length=4, width=6)

    # Access the properties using @property
    print("Area:", rectangle.area)
    print("Perimeter:", rectangle.perimeter)

    # Access and modify the properties using getters and setters
    print("Length:", rectangle.length)
    rectangle.length = 5
    print("Modified Length:", rectangle.length)

    print("Width:", rectangle.width)
    rectangle.width = 8
    print("Modified Width:", rectangle.width)
