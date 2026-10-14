# "in" checks if something is inside a list, string, etc.
dogs = ["Roger", "Syd"]
print("Roger" in dogs)  # True
print("Bob" in dogs)    # False

# "is" checks if two names point to the exact SAME object (not just equal)
a = [1, 2]
b = a
c = [1, 2]
print(a is b)  # True  - same list
print(a is c)  # False - looks the same, but it's a different list
