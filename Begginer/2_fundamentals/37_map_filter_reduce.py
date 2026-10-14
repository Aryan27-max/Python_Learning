# map, filter and reduce - three ways to work on a whole list at once.

from functools import reduce

numbers = [1, 2, 3, 4]

# map: do something to every item
doubled = list(map(lambda n: n * 2, numbers))
print(doubled)  # [2, 4, 6, 8]

# filter: keep only items that pass a test
evens = list(filter(lambda n: n % 2 == 0, numbers))
print(evens)  # [2, 4]

# reduce: squash the list down to one value
total = reduce(lambda a, b: a + b, numbers)
print(total)  # 10
