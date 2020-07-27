#! usr/bin/env python3

from time import time


def selection_sort(L):
    """
    Selects the smallest element in each iteration and places it on
    the first index.
    returns:// sorted(L)
    """
    for i in range(len(L)):
        print(L)
        smallest = L[i]
        for j in range(i + 1, len(L)):
            if L[j] < smallest:
                temp = smallest
                smallest = L[j]
                L[j] = temp
        L[i] = smallest
    return L


t0 = time()
selection_sort([100, 10, 4, 91, 7, 5, 12, 21, 19])
t1 = time()
print(t1 - t0)
