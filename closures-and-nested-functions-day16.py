# Closures
# is a function that remembers the value in enclosing scopes
# even if they are not present in the memory

# Nested function
# is a function inside another function

# Example

def transmit_to_space(message):
    """This is the enclosing function"""
    def data_transmitter():
        """The nested function"""
        print(message)

    return data_transmitter() # Here data_transmitter can access the 'message'

print(transmit_to_space("Test message"))

# To call back using the original function we can use the follow:
fun2 = transmit_to_space("Burn the sun!")
fun2

# Use of the "nonlocal" keyword

def print_msg(number):
    def printer():
        """Using the 'nonlocal' keyword"""
        nonlocal number
        number=4
        print(number)
    printer()
    print(number)

print_msg(9) # Use of nonlocal keyword makes it print out only 4 instead of 9

# Another example
def number(x):
    x = 100
    def add(y):
        print(x+y)

    return add
result = number(100)
result(9)

# Exercise
# Use closure and nested function loop to make functions to get multiple
# multiplication function


def multiplier_of(x):
    def multiply_with(n):
        print(x*n)
    return multiply_with
multiplywith5 = multiplier_of(5)
multiplywith5(7)
