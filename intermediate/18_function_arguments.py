# Function arguments - all the ways to pass values into a function.

# Parameters are the names in the definition, arguments are the values you pass in.
def greet(name):        # name = parameter
    print("Hi", name)

greet("Sam")            # "Sam" = argument


# Positional vs keyword arguments
def describe(a, b, c):
    print(a, b, c)

describe(1, 2, 3)           # by position
describe(c=3, a=1, b=2)     # by name - order doesn't matter
describe(1, c=3, b=2)       # mix them (positional must come first)


# Default values - used if you don't pass anything
def power(base, exponent=2):
    return base ** exponent

print(power(3))      # 9
print(power(3, 3))   # 27


# *args collects extra positional arguments into a tuple
# **kwargs collects extra keyword arguments into a dict
def show_all(*args, **kwargs):
    print("args:", args)
    print("kwargs:", kwargs)

show_all(1, 2, 3, name="Max", age=5)


# Anything after a lone * MUST be passed by name
def make_user(name, *, admin=False):
    print(name, "admin?", admin)

make_user("Ana", admin=True)


# Unpacking a list or dict straight into a function
def add(a, b, c):
    return a + b + c

nums = [1, 2, 3]
print(add(*nums))
values = {"a": 1, "b": 2, "c": 3}
print(add(**values))


# A common gotcha: never use a list as a default value.
# The same list gets reused on every call!
def add_item_bad(item, items=[]):
    items.append(item)
    return items

print(add_item_bad(1))
print(add_item_bad(2))   # [1, 2] - surprise!

def add_item_good(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items

print(add_item_good(1))
print(add_item_good(2))  # [2] - as expected
