"""
Using debugger on simple simulation of coin toss.
"""

import random

heads = 0
total = 0
for i in range(0, 1000):
    number = random.randint(0,1)
    if number == 1:
        heads += 1
    total += 1
print(heads)
print(total)