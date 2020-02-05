# without having values for all the functions, partial can be used to
# make another function work

# To import and use the partial function use the foll:
from functools import partial

def multiply(x,y):
        return x * y

# create a new function that multiplies by 2
dbl = partial(multiply,2) # use of partial function

print(dbl(6))

# Exercise
# Using partial compute the value of the "fun" to match 60.
# Tip: the values will start replacing from the left.

def fun(u,v,w,x):
    return u*4 + v*3 + w*2 + x

par = partial(fun,7,5,7)

print(par(3))
