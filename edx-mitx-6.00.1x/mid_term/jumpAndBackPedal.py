from random import randint

def jumpAndBackpedal(isMyNumber):
    '''
    isMyNumber: Procedure that hides a secret number.
     It takes as a parameter one number and returns:
     *  -1 if the number is less than the secret number
     *  0 if the number is equal to the secret number
     *  1 if the number is greater than the secret number

    returns: integer, the secret number
    '''
    guess = 1
    if isMyNumber(guess) == 0:
        return guess
    foundNumber = False
    while not foundNumber:
        sign = isMyNumber(guess)
        if sign == -1:
            guess += 1
        elif sign == +1:
            guess -= 1
        else:
            foundNumber = True
    return guess


def isMyNumber(x):
    secret = randint(1,10000)
    if x < secret:
        return -1
    elif x == secret:
        return 0
    elif x > secret:
        return 1


jumpAndBackpedal(isMyNumber)