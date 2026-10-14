# Random numbers. The random module is great for games and simulations.

import random

print(random.random())          # a float between 0 and 1
print(random.uniform(1, 10))    # a float between 1 and 10
print(random.randint(1, 6))     # a whole number 1 to 6 (like a dice)
print(random.randrange(1, 10))  # 1 to 9 (the end is NOT included)

colors = ["red", "green", "blue", "yellow"]
print(random.choice(colors))       # one random item
print(random.sample(colors, 2))    # 2 different items
print(random.choices(colors, k=3)) # 3 items, repeats allowed

random.shuffle(colors)             # mixes the list in place
print(colors)

# seed - same seed means the same "random" results every time.
# Handy for testing, so you can repeat a run exactly.
random.seed(1)
print(random.randint(1, 100))
random.seed(1)
print(random.randint(1, 100))   # same number as above

# IMPORTANT: random is NOT safe for passwords or security.
# Use the secrets module for that instead.
import secrets
print(secrets.randbelow(10))     # 0 to 9
print(secrets.token_hex(8))      # a random secure token
