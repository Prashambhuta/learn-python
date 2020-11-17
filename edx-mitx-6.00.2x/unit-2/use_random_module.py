#!/usr/bin/python3

import random

def get_even():
    """
    Return an even random number, where 0 <= x < 100
    """
    return random.randrange(0, 100, 2)

get_even()