# Operator overloading lets your own classes work with >, +, == and so on.
# You do it with special "dunder" (double underscore) methods.

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __gt__(self, other):  # what ">" means for dogs
        return self.age > other.age

    def __add__(self, other):  # what "+" means for dogs
        return self.age + other.age


roger = Dog("Roger", 8)
syd = Dog("Syd", 7)

print(roger > syd)  # True - Roger is older
print(roger + syd)  # 15 - combined age
