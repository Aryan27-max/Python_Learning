# Each character in a string has a position (index), starting from 0.

name = "Roger"

print(name[0])    # R
print(name[1])    # o
print(name[-1])   # r  (negative counts from the end)

# Slicing: [start:end] - end is NOT included
print(name[0:2])  # Ro
print(name[2:])   # ger
print(name[:3])   # Rog
