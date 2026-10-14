# A decorator wraps a function to add something extra before/after it runs.

def logtime(func):
    def wrapper():
        print("before")
        func()
        print("after")
    return wrapper


@logtime  # same as writing: hello = logtime(hello)
def hello():
    print("hello!")


hello()
