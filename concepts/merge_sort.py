#! usr/bin/env python3

from time import time

def merge_sort(L):
    """
    Merge sorts
    returns:// sorted list(L)
    """
    def merge(left, right):
        """
        merges left and right of a list
        returns res: merged list
        """
        res = []
        i,j = 0,0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                res.append(left[i])
                i += 1
            else:
                res.append(right[j])
                j += 1
        while (i < len(left)):
            res.append(left[i])
            i += 1
        while (j < len(right)):
            res.append(right[j])
            j += 1
        return res

    if len(L) < 2:
        return L
    mid = len(L) // 2
    first = merge_sort(L[:mid])
    last = merge_sort(L[mid:])
    return merge(first, last)

t0 = time()
merge_sort([100, 10, 4, 91, 7, 5, 12, 21, 19])
t1 = time()
print(t1-t0)
