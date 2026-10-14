# Dictionaries - key: value pairs. You look things up by key, not position.

person = {"name": "Max", "age": 28, "city": "New York"}
print(person)

# Another way to make one
person2 = dict(name="Mary", age=27)
print(person2)

# Reading a value
print(person["name"])
print(person.get("email", "no email"))  # .get won't crash if the key is missing

# Adding and changing
person["email"] = "max@xyz.com"
person["age"] = 29

# Removing
del person["city"]
person.pop("email")
print(person)

# Looping
for key in person:
    print(key)
for value in person.values():
    print(value)
for key, value in person.items():
    print(key, "=", value)

# Copying works like lists - use .copy() for a separate copy
person_copy = person.copy()

# Merging: update() adds new keys and overwrites matching ones
person.update({"age": 30, "job": "dev"})
print(person)

# Keys can be numbers or tuples too (anything that can't change)
points = {(1, 2): "first point", (3, 4): "second point"}
print(points[(1, 2)])
