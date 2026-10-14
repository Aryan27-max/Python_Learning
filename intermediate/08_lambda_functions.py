# Lambda - a tiny one-line function without a name.
# Format:  lambda arguments: expression

add10 = lambda x: x + 10
print(add10(5))   # 15

multiply = lambda a, b: a * b
print(multiply(2, 7))

# Where they're really useful: as a quick "key" for sorting
points = [(1, 2), (15, 1), (5, -1), (10, 4)]
print(sorted(points, key=lambda p: p[1]))       # sort by the y value
print(sorted(points, key=lambda p: p[0] + p[1]))

# map - run a function on every item
nums = [1, 2, 3, 4, 5]
print(list(map(lambda x: x * 2, nums)))

# filter - keep only the items that pass
print(list(filter(lambda x: x % 2 == 0, nums)))

# reduce - squash everything into one value
from functools import reduce
print(reduce(lambda a, b: a * b, nums))   # 1*2*3*4*5 = 120

# Honestly, list comprehensions often read nicer than map/filter:
print([x * 2 for x in nums])
