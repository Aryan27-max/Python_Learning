# Scope = where a variable can be seen.

age = 8  # global - everyone can see this


def test():
    inside = "only here"  # local - only exists inside this function
    print(age)            # functions can read globals just fine
    print(inside)


test()
# print(inside)  <- error! it doesn't exist out here
