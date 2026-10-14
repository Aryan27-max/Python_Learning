# Context managers - the "with" statement. They do setup and cleanup for you.

# The classic: files close themselves, even if an error happens inside
with open("notes.txt", "w") as file:
    file.write("some notes")

# Locks work with "with" too
from threading import Lock
lock = Lock()
with lock:
    print("got the lock, it'll be released automatically")


# Making your own with a class: you need __enter__ and __exit__
class ManagedFile:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        print("enter: opening the file")
        self.file = open(self.filename, "w")
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        # this ALWAYS runs, even if something broke
        self.file.close()
        if exc_type is not None:
            print("an error happened, but the file is still closed")
        print("exit: file closed")
        return True   # True means "I handled the error, don't crash"


with ManagedFile("notes.txt") as f:
    f.write("hello")
    print("doing some work...")


# The shortcut: a generator plus the contextmanager decorator
from contextlib import contextmanager

@contextmanager
def open_managed_file(filename):
    f = open(filename, "w")
    try:
        yield f          # everything before yield is setup
    finally:
        f.close()        # everything after is cleanup
        print("closed via contextmanager")


with open_managed_file("notes.txt") as f:
    f.write("hi again")
