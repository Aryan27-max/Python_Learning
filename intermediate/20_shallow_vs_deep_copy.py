# Copying in Python can be sneaky. There are three things that look similar.

import copy

# 1. Plain assignment - NOT a copy at all, just a second name for the same thing
original = [1, 2, 3]
same = original
same[0] = 99
print(original)   # [99, 2, 3] - the original changed too!

# 2. Shallow copy - a new outer list, but anything INSIDE is still shared
original = [[1, 2], [3, 4]]
shallow = copy.copy(original)   # same as original.copy() or list(original)
shallow[0][0] = 99
print(original)   # [[99, 2], [3, 4]] - the inner list changed!

# Shallow is fine when the list only holds simple things like numbers or strings
simple = [1, 2, 3]
simple_copy = simple.copy()
simple_copy[0] = 99
print(simple)     # [1, 2, 3] - untouched

# 3. Deep copy - copies EVERYTHING, all the way down. Fully independent.
original = [[1, 2], [3, 4]]
deep = copy.deepcopy(original)
deep[0][0] = 99
print(original)   # [[1, 2], [3, 4]] - untouched


# Same idea works for your own objects
class Person:
    def __init__(self, name):
        self.name = name

class Team:
    def __init__(self, members):
        self.members = members

team = Team([Person("Ana"), Person("Ben")])
team_copy = copy.deepcopy(team)
team_copy.members[0].name = "Changed"
print(team.members[0].name)   # still "Ana"
