from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int
    city: str

# Example usage:
if __name__ == "__main__":
    # Create instances of the Person class
    person1 = Person(name="Alice", age=30, city="Wonderland")
    person2 = Person(name="Bob", age=25, city="Cityville")

    # Print the instances
    print("Person 1:", person1)
    print("Person 2:", person2)
