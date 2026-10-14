# Strings - text. They're ordered and can't be changed in place.

text = "Hello World"

# Indexing and slicing
print(text[0])      # H
print(text[-1])     # d
print(text[0:5])    # Hello
print(text[::-1])   # backwards

# Join with +, and check with "in"
greeting = "Hi " + "Tom"
print(greeting)
print("World" in text)

# Useful methods (they give back a NEW string)
messy = "   hello there   "
print(messy.strip())        # removes spaces on both ends
print(text.upper())
print(text.lower())
print(text.startswith("He"))
print(text.find("o"))       # position of first "o"
print(text.count("o"))
print(text.replace("World", "Python"))

# split turns a string into a list, join does the opposite
words = "how are you".split(" ")
print(words)
print("-".join(words))

# Tip: joining a list with "".join() is faster than adding with + in a loop

# Formatting - f-strings are the easiest way
name = "Tom"
age = 25
print(f"{name} is {age} years old")
print(f"Pi is roughly {3.14159:.2f}")   # 2 decimal places

# The older ways you might still see
print("{} is {}".format(name, age))
print("%s is %d" % (name, age))
