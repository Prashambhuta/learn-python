#! usr/bin/env python3

def genSub(list):
    res = []
    if len(list) == 0:
        return [[]]
    smaller = genSub(list[:-1])
    extra = list[-1:]
    new = []
    for small in smaller:
        new.append(extra+small)

    return smaller + new

print(genSub([1, 2, 3]))