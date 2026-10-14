# The ternary operator is a one-line if/else.

age = 20

# the long way
if age > 18:
    status = "adult"
else:
    status = "kid"

# the short way - same thing in one line
status = "adult" if age > 18 else "kid"
print(status)
