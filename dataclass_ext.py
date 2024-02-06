from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int
    city: str

    def greet(self) -> None:
        print(f"Hello, {self.name}! Welcome to {self.city}.")

# Example usage:
if __name__ == "__main__":
    # Create instances of the Person class
    person1 = Person(name="Alice", age=30, city="Wonderland")
    person2 = Person(name="Bob", age=25, city="Cityville")

    # Call the extra function
    person1.greet()
    person2.greet()
