import random
print("Welcome to guess the number game. What is your name?")
name = input()
print("Hi %s, guess a number between 1 and 10." % name)
secretnumber = random.randint(1,10)

for numberofguesses in range(1,4):
    try:
        print("Take a guess")
        guess = int(input())
        if guess > secretnumber:
            print("You guessed high.")
        elif guess < secretnumber:
            print("You guessed low.")
        else:
            break
    except ValueError:
        print("Incorrect input.")

try:
    if guess == secretnumber:
        print("Good job, you guessed correctly in %d tries." % numberofguesses)
    else:
        print("Sad luck, the correct guess was %d" % secretnumber)
except NameError:
    print("Incorrrect input.")