# Docstrings are descriptions you put right under a function or class.
# Unlike comments, Python actually keeps them, so help() can show them.

def increment(n):
    """Take a number and return it plus one."""
    return n + 1


class Dog:
    """A simple class that represents a dog."""

    def bark(self):
        """Make the dog bark."""
        print("WOF!")


print(increment.__doc__)
help(Dog)
