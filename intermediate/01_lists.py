# Lists - an ordered collection you can change.
# You can mix types in one list, and duplicates are allowed.

fruits = ["banana", "cherry", "apple"]
print(fruits)

# Grab items by position (starts at 0). -1 means the last one.
print(fruits[0])
print(fruits[-1])

# Loop through it
for fruit in fruits:
    print(fruit)

# Check if something is in there
if "banana" in fruits:
    print("yes, we have bananas")

# Adding and removing
fruits.append("lemon")       # add to the end
fruits.insert(1, "mango")    # add at position 1
fruits.remove("cherry")      # remove by value
last = fruits.pop()          # remove the last one and hand it back
print(fruits, "| popped:", last)

# Sorting - sorted() makes a new list, .sort() changes the original
print(sorted(fruits))
fruits.sort()
print(fruits)

# Quick ways to make lists
zeros = [0] * 5
print(zeros)
numbers = [1, 2, 3, 4, 5, 6]
print(numbers[1:4])   # slicing: items 1, 2, 3
print(numbers[::2])   # every second item
print(numbers[::-1])  # reversed

# Careful when copying! This makes two names for the SAME list.
same_list = fruits
# These make a real separate copy:
real_copy = fruits.copy()
also_copy = list(fruits)

# List comprehension - build a new list in one line
squares = [n * n for n in numbers]
print(squares)
