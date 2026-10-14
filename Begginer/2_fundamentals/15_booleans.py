# Booleans are just True or False. Great for making decisions.

done = False
if done:
    print("yes")
else:
    print("not yet")

# "Falsy" values - these all act like False:
# 0, "", [], {}, None
print(bool(0))      # False
print(bool(""))     # False
print(bool("hi"))   # True

# any() is True if at least one is True, all() needs every one True
print(any([False, True]))  # True
print(all([False, True]))  # False
