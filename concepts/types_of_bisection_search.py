#! usr/bin/env python3
from time import time

L = [1, 3, 4, 5, 7, 9, 11]

def bisect_search1(L, e):
    if len(L) == 0:
        return False
    if len(L) == 1:
        return L[0] == e
    mid = len(L)//2
    if L[mid] > e:
        return bisect_search1(L[:mid], e)
    else:
        return bisect_search1(L[mid:], e)


t0 = time()
print(bisect_search1(L, 8))
t1 = time()
print(t1-t0)

def bisect_search2(L, e):
    def bisect_helper(L, e, low, high):
        if high == low:
            return L[low] == e
        mid = (low + high)//2
        if L[mid] == e:
            return True
        elif L[mid] > e:
            if low == mid:
                return False
            else:
                return bisect_helper(L, e, low, mid -1)
        else:
            return bisect_helper(L, e, mid +1, high)
    if len(L) == 0:
        return False
    else:
        return bisect_helper(L, e, 0, len(L)-1)

t0 = time()
print(bisect_search2(L, 8))
t1 = time()
print(t1-t0)