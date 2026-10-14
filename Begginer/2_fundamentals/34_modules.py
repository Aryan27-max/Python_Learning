# Modules let you use code from other files.

# Our own module (dog_helper.py sits right next to this file)
import dog_helper
dog_helper.bark()

# Or grab just the bit you need
from dog_helper import bark
bark()

# Python's standard library has tons of modules ready to go
import math
print(math.sqrt(16))  # 4.0

import random
print(random.randint(1, 6))  # roll a dice
