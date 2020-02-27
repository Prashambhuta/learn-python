"""
Hangman game based on filmography of Martin Scorsese.
"""
import random
import re

Movies = ["Whos That Knocking at My Door", 'Bezeten Het Gat in de Muur',
          'Boxcar Bertha', 'Mean Streets', 'Mardik Martin',
          "Alice Doesnt Live Here Anymore", 'Taxi Driver',
          'New York, New York', 'Raging Bull', 'The King of Comedy',
          'After Hours', 'The Color of Money', 'The Last Temptation of Christ',
          'Goodfellas', 'Nicholas Pileggi', 'Cape Fear',
          'The Age of Innocence', 'Jay Cocks', 'Casino', 'Kundun',
          'Bringing Out the Dead', 'Gangs of New York', 'The Aviator',
          'The Departed', 'Shutter Island', 'Hugo', 'The Wolf of Wall Street',
          'Silence', 'The Irishman', 'Killers of the Flower Moon']

HangmanPics = ['''
  +---+
  |   |
      |
      |
      |
      |
   ======''', '''
  +---+
  |   |
  O   |
      |
      |
      |
   ====== ''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
   ======''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
   ======''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
   ======''', '''
  +---+
  |   |
  O   |
 /|\  |
  |   |
 /    |
   ======''', '''
  +---+
  |   |
  O   |
 /|\  |
  |   |
 / \  |
   ======''']

# Variables defined
total_guess = []
MAXIMUM_TRY = 6
correct_guess = []
incorrect_guess = []

# Convert Movies to lower string
moviesLower = [n.lower() for n in Movies]

# Generate a random movie using random
movieIndex = random.randint(0, len(moviesLower))

# generate a ranMovie in form of string
ranMovie = moviesLower[movieIndex - 1]

# convert str into list for easy manipulation
iranMovie = list(ranMovie)

# Convert alphabets into '-'(str) and display movie to user.
dispMovie = "".join(
    ["-" if x.isalpha() and x not in correct_guess else x for
     x in
     ranMovie])

print('''Welcome to hangman game.
%s\nHere is the movie: 

%s ''' % (HangmanPics[0], dispMovie))

# convert dispMovie into list for easy manipulation
list_dispMovie = list(dispMovie)


# Game starts
def user_interaction():
    while len(incorrect_guess) < MAXIMUM_TRY:
        user_input = input("\nTake a guess:\n").lower()
        if len(user_input) > 1:
            print("\nMultiple Enteries!, \nInput 1 letter at a time.")
        elif len(user_input) == 0:
            print("\nInvalid Input! \nYou pressed enter")
        elif user_input == ' ' and len(user_input) == 1:
            print("\nInvalid Input! You pressed space")
        elif user_input in incorrect_guess:
            print("\nInavlid Input! \nAlready guessed")
        elif user_input in correct_guess:
            print("\nCorrectly guessed before.")
        elif user_input.isnumeric():
            print("\nInavlid Input! \nNumber entered")
        elif len(user_input) == 1 and user_input != ' ' and \
                user_input.isalpha() and user_input in iranMovie and \
                user_input not in correct_guess:
            total_guess.append(user_input)
            correct_guess.append(user_input)
            print("\n CORRECT GUESS:%s \n" % correct_guess)
            #print(ranMovie.index(user_input))
            dispMovie = "".join(["-" if x.isalpha() and x not in correct_guess
                                 else x for x in ranMovie])
            if dispMovie != ranMovie:
                pass
            else:
                print("SUCCESSFULLY SOLVED")
                break
        else:
            incorrect_guess.append(user_input)
            total_guess.append((user_input))
            print("\nINCORRECT !")
            print(HangmanPics[len(incorrect_guess)])
            print("\n CORRECT GUESS:%s \n" % correct_guess)
        if len(correct_guess) != 0:
            print(dispMovie)
    print('''GAME OVER!!!, 
Your incorrect guess were:
%s\n''' % incorrect_guess)
    print('''The correct answer was: \n 
%s\n''' % ranMovie.upper())

    print('''Complete guess were: 
%s''' % total_guess)


if dispMovie == ranMovie:
    print("FINISH")
elif len(incorrect_guess) < MAXIMUM_TRY:
    user_interaction()
