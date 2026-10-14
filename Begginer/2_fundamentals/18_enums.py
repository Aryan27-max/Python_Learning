# Enums give names to a fixed set of values. Makes code easier to read.

from enum import Enum


class State(Enum):
    INACTIVE = 0
    ACTIVE = 1


print(State.ACTIVE)        # State.ACTIVE
print(State.ACTIVE.value)  # 1
print(State(1))            # look it up by value -> State.ACTIVE
print(len(State))          # 2 options
