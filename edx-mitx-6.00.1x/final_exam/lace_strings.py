#! usr/bin/env python3
def laceStrings(s1, s2):
    """
    s1 and s2 are strings.

    Returns a new str with elements of s1 and s2 interlaced,
    beginning with s1. If strings are not of same length,
    then the extra elements should appear at the end.
    """
    i = 0
    j = 0
    if len(s1) == 0 and len(s2) == 0:
        return ''
    res = ''
    while i < len(s1) and j < len(s2):
        res += s1[i]
        res += s2[j]
        i += 1
        j += 1
    while i < len(s1):
        res += s1[i]
        i += 1
    while j < len(s2):
        res += s2[j]
        j += 1
    print(res)
    return res


laceStrings('abcd', 'efgh')
laceStrings('', '')
laceStrings('', 'abcd')
laceStrings('efgh', 'ab')
