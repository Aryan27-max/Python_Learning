# A class is like a blueprint for making objects.
# Each object can have its own name and age.

class Student:
    def introduce(self):
        print(f"Hi, I'm {self.name} and I'm {self.age} years old.")


student1 = Student()
student1.name = "Aryan"
student1.age = 21

student1.introduce()
