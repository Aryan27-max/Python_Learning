# Decorators - wrap a function to add something extra, without changing the function itself.

import functools


def start_end(func):
    # functools.wraps keeps the original function's name and info
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Start")
        result = func(*args, **kwargs)
        print("End")
        return result
    return wrapper


@start_end            # same as: add5 = start_end(add5)
def add5(x):
    return x + 5


print(add5(10))
print(add5.__name__)  # still "add5" thanks to functools.wraps


# A decorator that takes its own argument - one extra layer
def repeat(times):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                func(*args, **kwargs)
        return wrapper
    return decorator


@repeat(times=3)
def greet(name):
    print(f"Hello {name}")


greet("Alex")


# A class can be a decorator too. Here it counts how many times a function runs.
class CountCalls:
    def __init__(self, func):
        self.func = func
        self.calls = 0

    def __call__(self, *args, **kwargs):
        self.calls += 1
        print(f"Called {self.calls} time(s)")
        return self.func(*args, **kwargs)


@CountCalls
def say_hi():
    print("hi")


say_hi()
say_hi()
