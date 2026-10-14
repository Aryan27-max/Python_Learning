# Errors happen. Syntax errors stop the code from running at all.
# Exceptions happen while the code runs - and those we can catch.

# Some common ones you'll bump into:
#   ZeroDivisionError - dividing by 0
#   TypeError         - mixing types, like 5 + "10"
#   NameError         - using a variable that doesn't exist
#   IndexError        - list position that's out of range
#   KeyError          - dictionary key that isn't there
#   FileNotFoundError - opening a file that doesn't exist

# try / except - catch it so the program keeps going
try:
    a = 5 / 0
except ZeroDivisionError as e:
    print("Caught it:", e)

# You can catch different errors separately
try:
    numbers = [1, 2, 3]
    print(numbers[10])
except IndexError:
    print("That position doesn't exist")
except TypeError:
    print("Wrong type")
else:
    print("Runs only if nothing went wrong")
finally:
    print("Runs no matter what - good for cleanup")

# raise - throw an error yourself
x = -5
try:
    if x < 0:
        raise ValueError("x should be positive")
except ValueError as e:
    print(e)

# assert - a quick sanity check
try:
    assert x >= 0, "x is not positive"
except AssertionError as e:
    print("Assert failed:", e)


# Your own error type: just make a class based on Exception
class ValueTooHighError(Exception):
    pass


def check(value):
    if value > 100:
        raise ValueTooHighError("value is too high")


try:
    check(200)
except ValueTooHighError as e:
    print(e)
