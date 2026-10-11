# Polymorphism means different objects can use the same method name
# but respond in their own way.

class Dog:
    def speak(self):
        print("Woof!")


class Cat:
    def speak(self):
        print("Meow!")


for animal in [Dog(), Cat()]:
    animal.speak()
