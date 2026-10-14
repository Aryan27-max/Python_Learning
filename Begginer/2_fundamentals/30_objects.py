# In Python EVERYTHING is an object - numbers, strings, lists, all of it.
# Objects have attributes (data) and methods (functions you can call on them).

age = 8
print(age.real)            # an attribute
print(age.bit_length())    # a method

items = [1, 2]
items.append(3)            # list method
print(items)

# id() shows where the object lives in memory
print(id(age))

# Some objects can change (lists, dicts) - "mutable"
# Some can't (numbers, strings, tuples) - "immutable"
