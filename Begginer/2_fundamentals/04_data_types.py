# Every value in Python has a "type". type() tells you what it is.

name = "Roger"     # str   -> text
age = 8            # int   -> whole number
height = 1.5       # float -> decimal number
is_dog = True      # bool  -> True or False

print(type(name))
print(type(age))
print(type(height))
print(type(is_dog))

# isinstance checks if something is a certain type
print(isinstance(age, int))   # True

# You can convert between types too
print(int("20") + 5)     # text "20" becomes the number 20
print(str(10) + " dogs") # number 10 becomes the text "10"

# Other types you'll meet later: list, tuple, dict, set, complex
