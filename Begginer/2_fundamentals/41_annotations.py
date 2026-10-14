# Annotations are hints about what type something should be.
# Python doesn't enforce them - they're just for humans and editors.

def increment(n: int) -> int:
    return n + 1


count: int = 0
print(increment(count))

# Tools like mypy can read these hints and warn you about mistakes.
