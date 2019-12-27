@decorator
def function(arg):
    return "value"

# # is same as
def function(arg):
    return "value"
function = decorator(function)

#repeater function
@repeater
def multiply(num1, num2):
    print(num1 * num2)

    multiply(22,2)

# To change the output
def double_out(old_function):
    def new_function(*args, **kwds):
        return 2 * old_function(*args, **kwds) # modify the return value
    return new_function

# To change the input
def double_in(old_function):
    def new_function(arg):
        return old_function(arg * 2)
    return new_function
#
# # To do checking
def check(old_function):
    def new_function(arg):
        if arg < 0: raise (ValueError, "Negative Argument")
        # This will cause an error
        old_function(arg)
    return new_function

# Multiply the output by a variable amount

def multiply(multiplier):
    def multiply_generator(old_function):
        def new_function(*args, **kwds):
            return multiplier * old_function(*args, **kwds)
        return new_function
    return multiply_generator # it returns the new generator

# Usage
@multiply(3) # multiply is not a generator, but multiply(3) is
def return_num(num):
    return num

# Now return_num is decorated and reassigned to itself
return_num(5)

# Exercise
# Create a decorator which returns a decorator function with one argument.
# Check the input is correct, if not return "Bad Type".
def type_check(correct_type):
    # the code goes here


@type_check(int)
def times2(num):
    return 2*num

print(times2(2))
times2('Not a number')

@type_check(str)
def first_letter(word):
    return word[0]
