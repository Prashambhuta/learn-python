#! /usr/bin/python
# Single 6 faced dice
import random
print("Welcome to Dice Simulator. Press 'Enter' to start.")
Enter = input()
while Enter == "":
    x = random.randint(1,6)
    print(x)
    if x == 6:
        print ("Roll Again. Press 'Enter'")
        Enter = input()
        if Enter == "":
            x = random.randint(1,6)
            print(x)
            if x == 6:
                print("Two chances only.")
    print("Next Player Turn. Press 'Enter'")
    Enter = input()
else:
    print("You did not press Enter")
