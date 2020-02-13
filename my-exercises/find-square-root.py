# Lets find out a square root of a number
square = int(input("Hi, enter the number you want to find square root of:"))
guess = int(input("Take an appropriate guess:"))

while int(guess*guess) != int(square):
    guess = (guess + (square / guess)) / 2
    print(guess)
else:
    print((guess))