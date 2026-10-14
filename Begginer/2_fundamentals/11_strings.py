# Strings are just text. Use single or double quotes - both work.

name = "Roger"
greeting = 'Hello'

# Join strings with +
print(greeting + " " + name)

# You can't add a number to a string directly, convert it first
age = 8
print(name + " is " + str(age) + " years old")

# Multi-line strings use triple quotes
poem = """Roses are red,
Python is fun"""
print(poem)

print(len(name))  # how many characters -> 5
