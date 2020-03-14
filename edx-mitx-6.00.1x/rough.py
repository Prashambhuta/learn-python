"""
Approximation method
"""

x = 0.6030290455
epsilon = 0.01  # for accuracy
steps = 0.1 # for increment
guess = 0.0

while abs(guess**2 - x) >= epsilon:
    if guess <= x:
        guess += steps
    else:
        break

if abs(guess**2 - x) >= epsilon:
    print('failed')
else:
    print('succeded: ' + str(guess))


"""
Bisection Method
"""
low = 0
high = 1
number_guess = 0
guess2 = (low + high) / 2.0
while abs(guess2**2 - x) >= epsilon:
    print("Not correct: " + str(guess2))
    number_guess += 1
    if guess2**2 < x:
        low = guess2
    else:
        high = guess2
    guess2 = (low + high) / 2

print("The correct ans is: " + str(guess2))
