
import random
import numpy as np
from itertools import chain, combinations, product

def find_combination(choices, total):
    """
    choices: a non-empty list of ints
    total: a positive int

    Returns result, a numpy.array of length len(choices)
    such that
        * each element of result is 0 or 1
        * sum(result*choices) == total
        * sum(result) is as small as possible
    In case of ties, returns any result that works.
    If there is no result that gives the exact total,
    pick the one that gives sum(result*choices) closest
    to total without going over.
    """
    answer = np.zeros_like(choices)
    combinations_set = list(product(range(2), repeat=len(choices)))
    for sets in combinations_set:
        set_array = np.array(sets)
        if np.sum(set_array* np.array(choices)) == total:
            print(sets)
            break

x = find_combination([1,1,3,5,3], 5)
# y = find_combination([1, 1, 1, 9], 4)
# print(x)
# print(y)
