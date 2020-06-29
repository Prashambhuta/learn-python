import math


def polysum(n, s):
    """
    takes number of sides (n) and side length (s) as input.
    returns sum of area and perimeter square.
    """
    area = (0.25 * n * s ** 2) / math.tan(math.pi / n)
    perimeter = s * n
    return round(area + perimeter ** 2, 4)
