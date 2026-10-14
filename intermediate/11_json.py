# JSON - a text format for sending data around. It looks a lot like a Python dict.
# dumps/loads = to and from a STRING.  dump/load = to and from a FILE.

import json

person = {"name": "John", "age": 30, "city": "New York", "has_children": False, "titles": ["engineer", "programmer"]}

# Python dict -> JSON string
person_json = json.dumps(person, indent=4)   # indent makes it pretty
print(person_json)

# Save it to a file
with open("person.json", "w") as file:
    json.dump(person, file, indent=4)

# JSON string -> Python dict
back = json.loads(person_json)
print(back["name"])

# Read it back from the file
with open("person.json", "r") as file:
    from_file = json.load(file)
print(from_file)


# Your own classes don't turn into JSON automatically.
# The simple trick: turn the object into a dict first.
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age


user = User("Max", 27)
user_json = json.dumps(user.__dict__)   # __dict__ holds the object's data
print(user_json)

# And back again
data = json.loads(user_json)
user_again = User(**data)
print(user_again.name, user_again.age)
