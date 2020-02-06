# method 1
# Generate fibonacci series

def fib():
    a, b = 1, 1
    while True:  # while the loop remains true run this loop
        yield a  # yield means return the value of a, to stop loop
        a, b = b, a + b


c = 1  # define starting point of no of iteration
for n in fib():  # print values
    print(n)
    c += 1  # define increment steps
    if c == 14:  # no of steps
        break

# method 2
# Of generating fibonacci series

x, y = 1, 1  # define 2 variables
print(x)
print(y)

while y < 100:
    x, y = y, x + y  # here the value of y changes everytime
    print(y)
