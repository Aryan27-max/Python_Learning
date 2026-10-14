# A closure is an inner function that "remembers" variables from
# the outer function, even after the outer one has finished.

def counter():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    return increment  # we hand back the inner function itself


my_counter = counter()
print(my_counter())  # 1
print(my_counter())  # 2  <- it remembered!
print(my_counter())  # 3
