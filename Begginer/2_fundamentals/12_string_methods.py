# Strings come with handy built-in methods. They return a NEW string,
# the original stays the same.

name = "roger the dog"

print(name.upper())        # ROGER THE DOG
print(name.lower())        # roger the dog
print(name.title())        # Roger The Dog
print(name.startswith("r"))   # True
print(name.replace("dog", "cat"))
print(name.split(" "))     # ['roger', 'the', 'dog']
print("  hi  ".strip())    # removes extra spaces -> "hi"
print(name.find("the"))    # where "the" starts -> 6
