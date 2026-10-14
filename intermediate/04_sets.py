# Sets - no duplicates, no order. Great for "unique" stuff.

my_set = {1, 2, 3, 3, 3}
print(my_set)   # {1, 2, 3} - the extra 3s are gone

# Turn a string into a set of unique letters
print(set("hello"))

# Careful: {} is an empty DICTIONARY. An empty set is set()
empty = set()

# Adding and removing
my_set.add(4)
my_set.remove(1)    # crashes if the item isn't there
my_set.discard(99)  # same idea but never crashes
print(my_set)

# The fun part - combining sets
odds = {1, 3, 5, 7}
primes = {2, 3, 5, 7}

print(odds | primes)   # union: everything from both
print(odds & primes)   # intersection: only what's in both
print(odds - primes)   # difference: in odds but not primes
print(odds ^ primes)   # in one or the other, but not both

# Subset checks
a = {1, 2}
b = {1, 2, 3}
print(a.issubset(b))    # True
print(b.issuperset(a))  # True

# frozenset - a set you can't change
locked = frozenset([1, 2, 3])
print(locked)
