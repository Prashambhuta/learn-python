#!/usr/bin/python3

# generate all combinations of N items
def powerSet(items):
    N = len(items)
    # enumerate the 2^N possible combinations
    for i in range(2**N):
        combo = []
        for j in range(N):
            # test bit jth of integer i
            if (i >> j) % 2 == 1:
                combo.append(items[j])
        yield combo


combo1 = powerSet(['a', 'b', 'c', 'e', 'f', 'g'])


def to_trinary(num):
    ans = ''
    while num > 0:
        ans = str(num % 3) + ans
        num = num // 3
    return ans


def yieldAllCombos(items):
    N = len(items)
    # TODO: i in items belong to either of two lists or none.
    for i in range(3**N):
        list1 = []
        list2 = []
        for j in range(N):
            if (i // 3**j) % 3 == 1:
                list1.append(items[j])
            if (i // 3**j) % 3 == 2:
                list2.append(items[j])
        yield tuple(list1), tuple(list2)

trial = yieldAllCombos(['a', 'b'])