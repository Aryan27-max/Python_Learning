# Tuples - like a list, but you can't change it after you make it.
# Good for things that shouldn't change, like coordinates.

person = ("Max", 28, "Boston")
print(person)

# A tuple with one item needs a comma, otherwise it's just a string
single = ("Max",)
print(type(single))

# Reading works the same as lists
print(person[0])
print(person[-1])

# person[0] = "Tim"  <- this would crash, tuples are locked

# Loop and check, same as lists
for item in person:
    print(item)
print("Max" in person)

# A couple of handy methods
letters = ("a", "p", "p", "l", "e")
print(letters.count("p"))   # how many times "p" shows up
print(letters.index("l"))   # where "l" first appears

# Switch between tuple and list
as_list = list(letters)
back_to_tuple = tuple(as_list)

# Unpacking - pull the values out into separate names
name, age, city = person
print(name, age, city)

# Use * to scoop up "the rest"
first, *middle, last = (1, 2, 3, 4, 5)
print(first, middle, last)   # 1 [2, 3, 4] 5
