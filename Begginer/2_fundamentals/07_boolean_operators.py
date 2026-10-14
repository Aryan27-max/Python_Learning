# Boolean operators: not, and, or

condition1 = True
condition2 = False

print(not condition1)             # False - flips it
print(condition1 and condition2)  # False - both need to be True
print(condition1 or condition2)   # True  - at least one is True

# Fun fact: "or" gives back the first value that's truthy
print(0 or "backup")  # backup
