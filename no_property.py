class Rectangle:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def area(self):
        return self._length * self._width

    def perimeter(self):
        return 2 * (self._length + self._width)

    def get_length(self):
        return self._length

    def set_length(self, value):
        if value >= 0:
            self._length = value
        else:
            print("Length cannot be negative.")

    def get_width(self):
        return self._width

    def set_width(self, value):
        if value >= 0:
            self._width = value
        else:
            print("Width cannot be negative.")

# Example usage:
if __name__ == "__main__":
    # Create an instance of the Rectangle class
    rectangle = Rectangle(length=4, width=6)

    # Access the properties using getter methods
    print("Area:", rectangle.area())
    print("Perimeter:", rectangle.perimeter())

    # Access and modify the properties using getter and setter methods
    print("Length:", rectangle.get_length())
    rectangle.set_length(5)
    print("Modified Length:", rectangle.get_length())

    print("Width:", rectangle.get_width())
    rectangle.set_width(8)
    print("Modified Width:", rectangle.get_width())
