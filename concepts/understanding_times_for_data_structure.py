#! usr/bin/env python3
from time import time

list1 = [e for e in range(10000000)]
set1 = set(list1)
dict1 = {e:e for e in range(10000000)}

t0 = time()
9999999 in list1
t1 = time()
print("List time:", t1-t0)

t0 = time()
9999999 in set1
t1 = time()
print("set time:", t1-t0)

t0 = time()
9999999 in dict1
t1 = time()
print("dict time: ", t1-t0)

print("SET/DICT are way faster than LIST.")
print("NEXT: undestand the space tradeoff.")
