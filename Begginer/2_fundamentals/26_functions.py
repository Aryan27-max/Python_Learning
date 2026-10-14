# A function is a reusable block of code. Write it once, use it many times.

def hello(name="friend"):  # "friend" is a default if nothing is passed
    print("Hello " + name + "!")


hello("Roger")
hello()


# Functions can send a value back with return
def add(a, b):
    return a + b


total = add(2, 3)
print(total)  # 5


# You can return more than one thing (it comes back as a tuple)
def min_max(nums):
    return min(nums), max(nums)


low, high = min_max([4, 1, 9])
print(low, high)
