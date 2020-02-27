# Return First and Last Parameter
# Published by Helen Yu
# Write two functions
# first_arg() should return the first parameter
# last_arg() should return the last parameter

def first_arg(*args):
    try:
        print(args[0])
    except IndexError:
        print("None")

def last_arg(*y):
    try:
        print(y[-1])
    except IndexError:
        print("None")

first_arg("as","asdsa","sdas")
last_arg()