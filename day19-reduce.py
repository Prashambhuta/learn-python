# Reduce
# reduce applies a fucntion of two arguments to elements of an iterable
# Eg SYNTAX - reduce(func, interable[,initial])
# Key pointers
# func requries two arguments,
# reduce reduces the iterable into a single value.
# Example

from functools import reduce
numbers = [3, 4, 6, 9, 34, 12]

sum1 = reduce(lambda x,y:x+y, numbers,100)
print(sum1)