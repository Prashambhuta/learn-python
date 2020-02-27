# create a box printing function that prints box based on symbol,
#  height, and weight

import traceback

"""
************
*          *
*          *
*          *
************
"""

# define a box_print function
def box_print(symbol, width, height):
    if len(symbol) > 1:     # Raising exceptions if len of symbol is > 1
        raise Exception("'Symbol' needs to be of length 1 character.")
    if (width < 3) or (height < 3):
        raise Exception("'Width' and 'Height' must be greater than 3.")
    print(symbol * width)   # print the first line
    for i in range(1,height-1):
        print(symbol + (" " *(width - 2)) + symbol)
    print(symbol*width)

box_print("!", 3, 3)

# trying to append exception string to a file
try:
    raise Exception("This is an error message")
except:
    error_file = open("error_log.txt", "a")
    error_file.write("\n")
    error_file.write(traceback.format_exc())
    error_file.close()
    print("Message appended")