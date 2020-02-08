usernumber = input()
try:
    y = int(usernumber)
    if y in range(1,11):
        print("Hurray! You have guessed correctly. :)")
    elif y in range(1,11) and x < y:
        print("Your guess is incorrect.")
    elif y in range(1,11) and x > y:
        print("Your guess is incorrect.")
    else:
        print("Number outside of range.")
except ValueError:
    print("Input not an integer. Exiting.")
input()