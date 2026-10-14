# List comprehension = a short way to build a new list from another one.

numbers = [1, 2, 3, 4, 5]

# the long way
squares = []
for n in numbers:
    squares.append(n ** 2)

# the short way, same result
squares = [n ** 2 for n in numbers]
print(squares)  # [1, 4, 9, 16, 25]

# you can add a condition at the end
evens = [n for n in numbers if n % 2 == 0]
print(evens)  # [2, 4]
