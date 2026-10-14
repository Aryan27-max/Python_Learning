# Polymorphism = different classes having the same method name,
# so you can treat them the same way.

class Dog:
    def eat(self):
        print("Eating dog food")


class Cat:
    def eat(self):
        print("Eating cat food")


for pet in [Dog(), Cat()]:
    pet.eat()  # same call, different behaviour
