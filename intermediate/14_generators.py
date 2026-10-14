# Generators - functions that give values one at a time using "yield".
# They don't build the whole list in memory, which is great for big data.

def count_down(num):
    while num > 0:
        yield num   # hand back a value and pause here
        num -= 1


for n in count_down(3):
    print(n)

# You can also step through manually with next()
gen = count_down(2)
print(next(gen))   # 2
print(next(gen))   # 1
# next(gen) again would raise StopIteration - there's nothing left


# Memory comparison: a list holds everything, a generator holds almost nothing
import sys

def first_n(n):
    num = 0
    while num < n:
        yield num
        num += 1

big_list = [i for i in range(100000)]
big_gen = first_n(100000)
print("list size:", sys.getsizeof(big_list), "bytes")
print("generator size:", sys.getsizeof(big_gen), "bytes")
print(sum(first_n(10)))  # works with sum(), max() etc. too


# Fibonacci, the classic generator example
def fibonacci(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b

print(list(fibonacci(30)))

# Generator expression - like list comprehension but with round brackets
squares = (x * x for x in range(5))
print(list(squares))
