# Dictionaries store key: value pairs. Think of a real dictionary - word and meaning.

dog = {"name": "Roger", "age": 8}

print(dog["name"])          # Roger
print(dog.get("color", "unknown"))  # safe way, gives a default if missing

dog["color"] = "brown"      # add a new pair
dog["age"] = 9              # update a value
print(dog)

dog.pop("color")            # remove one
print(dog.keys())           # all keys
print(dog.values())         # all values
print("name" in dog)        # True

# loop through it
for key, value in dog.items():
    print(key, "->", value)
