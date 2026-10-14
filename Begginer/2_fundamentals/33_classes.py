# A class is a blueprint for making your own objects.

class Animal:
    def walk(self):
        print("Walking...")


# Dog "inherits" from Animal, so it gets walk() for free
class Dog(Animal):
    # __init__ runs automatically when you create a new dog
    def __init__(self, name, age):
        self.name = name  # self = this particular dog
        self.age = age

    def bark(self):
        print(self.name + " says woof!")


roger = Dog("Roger", 8)
print(roger.name, roger.age)
roger.bark()
roger.walk()  # came from Animal
