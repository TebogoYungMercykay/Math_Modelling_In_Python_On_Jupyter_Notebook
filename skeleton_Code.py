# This is the code to Print Hello World in Python
# No Need to Import modules yet!!
print("Hello world")
#
#
# D O N E !!
#
#
# This Code is for A Simple Class declaration and Object creation:
# Example:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")


# Creating objects of the Person class
person1 = Person("Alice", 25)
person2 = Person("Bob", 30)

# Accessing object properties
print(person1.name)  # Output: Alice
print(person2.age)  # Output: 30

# Calling object methods
person1.introduce()  # Output: Hello, my name is Alice and I am 25 years old.
person2.introduce()  # Output: Hello, my name is Bob and I am 30 years old.