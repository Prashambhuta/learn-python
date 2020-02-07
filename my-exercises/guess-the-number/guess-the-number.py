# The goal is to check if the number guessed by user matches the random number generated
import random
print("Welcome to Guess The Number Game")
print("Kindly guess a number between 1 and 10.")
usernumber = input()
x = random.randint(1,10)
try:
    y = int(usernumber)
    if y in range(1,11) and x == y:
        print("Hurray! You have guessed correctly. :)")
    elif y in range(1,11) and x < y:
        print("Your guess is incorrect. Guess Lower.")
        usernumber = input()
        try:
            y = int(usernumber)
            if y in range(1, 11) and x == y:
                print("Hurray! You have guessed correctly. :)")
            elif y in range(1, 11) and x < y:
                print("Your guess is incorrect. Guess Lower.")
                usernumber = input()
                try:
                    y = int(usernumber)
                    if y in range(1,11) and x == y:
                        print("Hurray! You have guessed correctly. :)")
                    elif y in range(1,11) and x < y:
                        print("Your guess is incorrect.")
                    elif y in range(1,11) and x > y:
                        print("Your guess is incorrect.")
                    else:
                        print("Number outside of range.")
                except ValueError:
                    print("Input not an integer. Exiting.")
            elif y in range (1,11) and x > y:
                print("Your guess is incorrect. Guess Higher.")
                usernumber = input()
                try:
                    y = int(usernumber)
                    if y in range(1, 11) and x == y:
                        print("Hurray! You have guessed correctly. :)")
                    elif y in range(1, 11) and x < y:
                        print("Your guess is incorrect.")
                    else:
                        print("Number outside of range.")
                except ValueError:
                    print("Input not an integer. Exiting.")

            else:
                print("Number outside of range. Enter number between 1 and 10.")
                usernumber = input()
                try:
                    y = int(usernumber)
                    if y in range(1, 11) and x == y:
                        print("Hurray! You have guessed correctly. :)")
                    elif y in range(1, 11) and x != y:
                        print("Guess is incorrect. :(")
                    else:
                        print("Failed Multiple times. Exiting.")
                except ValueError:
                    print("Not an integer. Exiting")
        except ValueError:
            print("Not an integer. Exiting")

    elif y in range(1, 11) and x > y:
        print("Your guess is incorrect. Guess Higher.")
        usernumber = input()
        try:
            y = int(usernumber)
            if y in range(1, 11) and x == y:
                print("Hurray! You have guessed correctly. :)")
            elif y in range(1,11) and x < y:
                print("Your guess is incorrect. Guess Lower.")
                usernumber = input()
                try:
                    y = int(usernumber)
                    if y in range(1, 11) and x == y:
                        print("Hurray! You have guessed correctly. :)")
                    elif y in range(1, 11) and x > y:
                        print("Your guess is incorrect.")
                    else:
                        print("Number outside of range.")
                except ValueError:
                    print("Input not an integer. Exiting.")

            elif y in range(1, 11) and x > y:
                print("Your guess is incorrect. Guess Higher.")
                usernumber = input()
                try:
                    y = int(usernumber)
                    if y in range(1, 11) and x == y:
                        print("Hurray! You have guessed correctly. :)")
                    elif y in range(1, 11) and x != y:
                        print("Your guess is incorrect.")
                    else:
                        print("Number outside of range.")
                except ValueError:
                    print("Input not an integer. Exiting.")

            else:
                print("Number outside of range. Enter number between 1 and 10.")
                usernumber = input()
                try:
                    y = int(usernumber)
                    if y in range(1, 11) and x == y:
                        print("Hurray! You have guessed correctly. :)")
                    elif y in range(1, 11) and x != y:
                        print("Guess is incorrect. :(")
                    else:
                        print("Failed Multiple times. Exiting.")
                except ValueError:
                    print("Not an integer. Exiting")
        except ValueError:
            print("Not an integer. Exiting")

    else:
        print("Number outside of range. Enter number between 1 and 10.")
        usernumber = input()
        try:
            y = int(usernumber)
            if y in range(1, 11) and x == y:
                print("Hurray! You have guessed correctly. :)")
            elif y in range(1, 11) and x < y:
                print("Your guess is incorrect. Guess Lower.")
                usernumber = input()
                try:
                    y = int(usernumber)
                    if y in range(1,11) and x == y:
                        print("Hurray! You have guessed correctly in your last attempt.")
                    elif y in range(1,11) and x != y:
                        print("Your guess is incorrect. Attempts finished.")
                    else:
                        print("Number of attempts over.")
                except ValueError:
                    print("Input not an integer.")
            elif y in range(1,11) and x > y:
                print("Your guess is incorrect. Guess Higher")
                usernumber = input()
                try:
                    y = int(usernumber)
                    if y in range(1, 11) and x == y:
                        print("Hurray! You have guessed correctly in your last attempt.")
                    elif y in range(1, 11) and x != y:
                        print("Your guess is incorrect. Attempts finished.")
                    else:
                        print("Number of attempts over.")
                except ValueError:
                    print("Input not an integer.")
            else:
                print("Number outside of range. Enter number between 1 and 10.")
                usernumber = input()
                try:
                    y = int(usernumber)
                    if y in range(1, 11) and x == y:
                        print("Hurray! You have guessed correctly. :)")
                    elif y in range(1, 11) and x != y:
                        print("Guess is incorrect. :(")
                    else:
                        print("Failed Multiple times. Exiting.")
                except ValueError:
                    print("Not an integer. Exiting")
        except ValueError:
            print("Not an integer. Exiting")
except ValueError:
    print("Not an integer. Exiting")

print("The correct answer was %d" % x)



# y = int(input())
# for y in (1,10):
#     try:
#         if y == x:
#             print("Guessed Correctly!")
#         else:
#             print("Incorrect Guess")
#
#     except ValueError:
#         print("Incorrect Input")




