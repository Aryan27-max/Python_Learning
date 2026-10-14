# Exceptions are errors. try/except lets you catch them so the program doesn't crash.

try:
    result = 2 / 0
except ZeroDivisionError:
    print("Can't divide by zero!")
else:
    print("This runs only if nothing went wrong")
finally:
    print("This always runs, no matter what")


# You can raise your own errors too
def check_age(age):
    if age < 0:
        raise ValueError("Age can't be negative")
    return age


try:
    check_age(-1)
except ValueError as error:
    print("Oops:", error)
