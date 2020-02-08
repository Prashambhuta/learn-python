def divby42(number):
    try:
        return 42 / number
    except ZeroDivisionError:
        print("Cannot divide by 0.")
print(divby42(2))
print(divby42(24))
print(divby42(0))
print(divby42(3))
    