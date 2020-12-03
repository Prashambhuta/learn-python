def solveit(test):
    """ test, a function that takes an int parameter and returns a Boolean
        Assumes there exists an int, x, such that test(x) is True
        Returns an int, x, with the smallest absolute value such that test(x) is True
        In case of ties, return any one of them.
    """
    i = 100
    try:
        while not test(i):
            i -= 1
            continue
    # print(i)
        return i
    except IndexError:
        return 3
def f(x):
    return (x+15)**0.5 + x**0.5 == 15
print(solveit(f))


def solveit(test):
    """ test, a function that takes an int parameter and returns a Boolean
        Assumes there exists an int, x, such that test(x) is True
        Returns an int, x, with the smallest absolute value such that test(x) is True
        In case of ties, return any one of them.
    """
    i = 100
    while not test(i):
        i -= 1
        continue
    # print(i)
    return i