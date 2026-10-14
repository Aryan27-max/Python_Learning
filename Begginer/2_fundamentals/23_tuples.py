# Tuples are like lists, but you can't change them once made.
# Use round brackets.

point = (10, 20)

print(point[0])      # 10
print(len(point))    # 2

# point[0] = 5  <- this would give an error, tuples are locked

# Unpacking: pull values out into separate variables
x, y = point
print(x, y)
