#! usr/bin/env python3

from time import time


def bubble_sort(L):
    """
    Bubble sorts a list (L)
    returns: sorted list (L)
    """
    for j in range(len(L)):
        for i in range(len(L) - 1):
            print(L)
            if L[i] > L[i + 1]:
                L[i], L[i + 1] = L[i + 1], L[i]


t0 = time()
bubble_sort([100, 10, 4, 91, 7, 5, 12, 21, 19])
t1 = time()
print(t1 - t0)
