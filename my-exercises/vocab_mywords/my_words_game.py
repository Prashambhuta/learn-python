#! usr/bin/env python3
"""
The aim is to create a game that reads from .ods file and generates MCQ for
words listed
"""

import pyexcel_ods
import pandas as pd
import urllib.request
import random as rand

# start from scratch

# get the file from the repo and save it locally
# url_object = urllib.request.urlretrieve(
#     "https://github.com/Prashambhuta/vocab/blob/master/my-word.ods?raw=true",
#     "words.ods")

# get the data by using the pyexcel ods
file_object = pyexcel_ods.get_data('words.ods', start_column = 0,
                                   column_limit=2)

# define the sheet object
sheet_object = file_object['Sheet1']

column_names = sheet_object.pop(0)

# define the dataframe dictionary
df = pd.DataFrame(sheet_object, columns=column_names)

# print the sheet_objects
# print(df)

# locating the object
# print(df.Words[6])

# architect the game

# select a random question and its answer





def question():
    """
    Generates question
    """
    que = rand.choice(df.Meaning)
    answer = df.loc[df.Meaning == que, 'Words']
    global ans
    ans = [answer.values[0]]
    print("""The QUESTION is:
"%s" """ % que)
    # print(ans)

    # select 3 random options

    random_opt = rand.choices([word for word in df.Words if word is not
                               None and word != ans], k=3)
    global final_options
    final_options = random_opt + ans
    rand.shuffle(final_options)
    print("\nYour options are:")
    n = 1
    for i in final_options:
        print("%d: %s" % (n, i))
        n += 1

    answer_input()


def answer_input():
    """
    Checks for correct answer
    """

    try:
        ans_input = int(input("\nSelect your option: "))
        if final_options[ans_input - 1] == ans[0]:
            print("CORRECT ANSWER")
        else:
            print("INCORRECT")

        restart = input("\nPress 'r' to start again, 'b' to quit: ")
        if restart == 'r':
            question()
        else:
            print("BYE")

    except ValueError:
        print("Input not recognised.")



# lets start the game
user_input = input("""
Welcome to Prasham's word guessing game.

A meaning of a word is shown, and you have to guess the correct word that 
represents that meaning.

ENTER 's' TO START: """)

if user_input.strip() == 's':
    question()
else:
    print("Did not enter 's' ")
