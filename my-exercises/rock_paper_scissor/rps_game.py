#! usr/bin/env python3
"""
Create a game that stimulates `Rock, Paper, Scissors game'
"""

import random, time

rps_values = ['Rock', 'Paper', 'Scissors']


def game():
    print("Welcome to Rock, Paper, Scissors Game. \n")
    time.sleep(2)
    print(check())


def user_input():
    user_inputs = input("""Press:
    'r' or '1' for Rock
    'p' or '2' for Paper
    's' or '3' for Scissors
    """)
    if user_inputs == 'r' or user_inputs == '1':
        user_inputs = 'Rock'
    elif user_inputs == 'p' or user_inputs == '2':
        user_inputs = 'Paper'
    elif user_inputs == 's' or user_inputs == '3':
        user_inputs = 'Scissors'
    else:
        user_inputs = None
    return user_inputs


def check():
    my_value = random.choice(rps_values)
    user_inputs = user_input()
    if user_inputs in rps_values:
        if user_inputs == 'Paper' and my_value == 'Scissors':
            return '''I win!\n%s beats %s''' % (my_value, user_inputs)
        elif user_inputs == 'Paper' and my_value == 'Rock':
            return '''You win!\n%s beats %s''' % (user_inputs, my_value)
        elif user_inputs == 'Paper' and my_value == 'Paper':
            return '''It's a tie'''

        if user_inputs == 'Rock' and my_value == 'Scissors':
            return '''You win!\n%s beats %s''' % (user_inputs, my_value)
        elif user_inputs == 'Rock' and my_value == 'Paper':
            return '''I win!\n%s beats %s''' % (my_value, user_inputs)
        elif user_inputs == 'Rock' and my_value == 'Rock':
            return '''It's a tie'''

        if user_inputs == 'Scissors' and my_value == 'Paper':
            return '''You win!\n%s beats %s''' % (user_inputs, my_value)
        elif user_inputs == 'Scissors' and my_value == 'Rock':
            return '''I win!\n%s beats %s''' % (my_value, user_inputs)
        elif user_inputs == 'Scissors' and my_value == 'Scissors':
            return '''It's a tie'''
    else:
        return 'Invalid input'


if __name__ == "__main__":
    game()