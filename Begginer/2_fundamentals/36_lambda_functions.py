# Lambdas are tiny one-line functions with no name.

double = lambda num: num * 2
print(double(5))  # 10

add = lambda a, b: a + b
print(add(2, 3))  # 5

# They really shine when passed to other functions, like sorting
people = [("Roger", 8), ("Syd", 3)]
people.sort(key=lambda person: person[1])  # sort by age
print(people)
