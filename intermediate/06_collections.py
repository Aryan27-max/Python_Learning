# The collections module gives you some extra-handy container types.

from collections import Counter, namedtuple, OrderedDict, defaultdict, deque

# Counter - counts things for you
letters = "aaaaabbbbcc"
counts = Counter(letters)
print(counts)                    # Counter({'a': 5, 'b': 4, 'c': 2})
print(counts.most_common(1))     # the top one

# namedtuple - a tuple where each spot has a name
Point = namedtuple("Point", "x, y")
p = Point(1, -4)
print(p.x, p.y)

# OrderedDict - remembers insertion order.
# Normal dicts do this too now (Python 3.7+), so you'll see it less.
ordered = OrderedDict()
ordered["b"] = 2
ordered["a"] = 1
print(ordered)

# defaultdict - gives a default value for missing keys instead of crashing
scores = defaultdict(int)   # missing keys start at 0
scores["tom"] += 5
print(scores["tom"])   # 5
print(scores["amy"])   # 0, no error

# deque - a list that's fast to add/remove from BOTH ends
d = deque()
d.append(1)
d.append(2)
d.appendleft(0)
print(d)       # deque([0, 1, 2])
d.pop()
d.popleft()
print(d)       # deque([1])
d.extend([4, 5, 6])
d.rotate(1)    # shift everything one step right
print(d)
