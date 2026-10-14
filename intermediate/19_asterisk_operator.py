# The * (asterisk) has a lot of jobs in Python. Here they all are.

# 1. Multiply and power
print(5 * 7)
print(2 ** 4)

# 2. Repeat lists and strings
print([0] * 5)
print("ab" * 3)

# 3. *args and **kwargs in functions (collect extra arguments)
def foo(*args, **kwargs):
    print(args, kwargs)

foo(1, 2, x=3)

# 4. Force keyword-only arguments
def bar(a, *, b):
    print(a, b)

bar(1, b=2)

# 5. Unpack into a function call
def add(a, b, c):
    return a + b + c

print(add(*[1, 2, 3]))
print(add(**{"a": 1, "b": 2, "c": 3}))

# 6. Unpack into variables (the starred one takes "the rest")
first, *rest = [1, 2, 3, 4]
print(first, rest)
*start, last = [1, 2, 3, 4]
print(start, last)

# 7. Merge lists, tuples, sets and dicts
a = [1, 2]
b = (3, 4)
merged = [*a, *b]
print(merged)

d1 = {"x": 1}
d2 = {"y": 2}
print({**d1, **d2})
