#!/usr/bin/python3

import random


def estimate_pi(no_of_needles):
    inside_circle = 0
    for i in range(no_of_needles):
        x = random.random()
        y = random.random()
        dist = (x**2 + y**2)**0.5
        if dist <= 1:
            inside_circle += 1
    print('Pi for ', no_of_needles, 'is: ', (4*inside_circle)/no_of_needles)

trials = [100, 10000, 100000]

for t in trials:
    estimate_pi(t)

