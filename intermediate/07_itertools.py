# itertools - tools for looping in clever ways.
# Most of these give back an "iterator", so we wrap them in list() to see them.

from itertools import product, permutations, combinations, accumulate, groupby, count, cycle, repeat

# product - every pairing of two lists
print(list(product([1, 2], [3, 4])))   # [(1, 3), (1, 4), (2, 3), (2, 4)]

# permutations - every possible ORDER
print(list(permutations([1, 2, 3], 2)))

# combinations - every group, order doesn't matter
print(list(combinations([1, 2, 3, 4], 2)))

# accumulate - running totals
print(list(accumulate([1, 2, 3, 4])))   # [1, 3, 6, 10]

# groupby - groups items next to each other by some rule
def smaller_than_3(x):
    return x < 3

for key, group in groupby([1, 2, 3, 4], key=smaller_than_3):
    print(key, list(group))

# Infinite ones - always add a way to stop!
for i in count(10):    # 10, 11, 12...
    print(i)
    if i == 12:
        break

n = 0
for item in cycle(["a", "b"]):   # a, b, a, b...
    print(item)
    n += 1
    if n == 4:
        break

for item in repeat("hi", 3):     # "hi" three times
    print(item)
