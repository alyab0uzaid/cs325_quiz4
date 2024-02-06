# run.py
from folder1.function1 import greet as greet_function1
from folder2.function2 import square as square_function2
from folder3.function3 import multiply as multiply_function3

if __name__ == "__main__":
    # Demonstrate usage of imported functions
    name = "Alice"
    print(greet_function1(name))

    number = 5
    print(f"The square of {number} is: {square_function2(number)}")

    x, y = 3, 4
    print(f"The product of {x} and {y} is: {multiply_function3(x, y)}")
