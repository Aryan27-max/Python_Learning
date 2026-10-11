# Inheritance lets one class reuse another class's features.

class Animal:
    def speak(self):
        print("This animal makes a sound.")


class Dog(Animal):
    def bark(self):
        print("Woof!")


dog = Dog()
dog.speak()  # Reused from Animal
dog.bark()
