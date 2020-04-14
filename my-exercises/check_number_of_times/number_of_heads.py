#! usr/bin/env python3
"""
To check the continuous number of times, 'heads' or 'tails' occur
"""

import random
items = ["H", "T"]
number_of_streaks = 0
counter = 0

for i in range(10000):
    value = random.choice(items)
    if value == "H":
        counter += 1
        if counter == 6:
            number_of_streaks += 1
            counter = 0
    else:
        counter = 0

print(number_of_streaks)
