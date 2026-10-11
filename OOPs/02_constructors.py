# __init__ runs automatically when we create an object.
# It helps us give the object its starting values.

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hi, I'm {self.name} and I'm {self.age} years old.")


student1 = Student("Aryan", 21)
student1.introduce()
