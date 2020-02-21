"""
Hangman game based on filmography of Martin Scorcese.
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

# Convert Movies to lower string
moviesLower = [n.lower() for n in Movies]


# Generate a random movie using random
movieIndex = random.randint(0, len(moviesLower))
ranMovie = moviesLower[movieIndex - 1]
iranMovie = list(ranMovie)

# Convert alphabets into * and display movie to user.
dispMovie = "".join(
    ["-" if x.isalpha() else x for x in ranMovie])
print('''Welcome to hangman game.
%s

Here is the movie: 

%s ''' % (HangmanPics[0], dispMovie))

# From here user interaction begins.
total_guess = []
MAXIMUM_TRY = 6
correct_guess = []
incorrect_guess = []


def user_interaction():
    while len(incorrect_guess) < MAXIMUM_TRY:
        user_input = input("\nTake a guess:").lower()
        if len(user_input) > 1:
            print("\nInvalid Input!, \nGuess 1 letter at a time.")
        elif len(user_input) == 0:
            print("\nInvalid Input! \nYou pressed enter")
        elif user_input == ' ' and len(user_input) == 1:
            print("\nInvalid Input! You pressed space")
        elif user_input in total_guess:
            print("\nInavlid Input! \nAlready guessed")
        # elif user_input in incorrect_guess:
        #     print("Already guessed.")
        elif len(user_input) == 1 and user_input != ' ' and \
                user_input.isalpha() and user_input in iranMovie and \
                user_input not in correct_guess:
            total_guess.append(user_input)
            correct_guess.append(user_input)
            print(correct_guess)
            print(range(len(correct_guess)))

            # TODO: save & display correct guesses in dispMovie

        else:
            incorrect_guess.append(user_input)
            total_guess.append((user_input))
            print("Incorrect guess, I will now show the next step in hangman")

    print('''Tries finished, your guess were:
    %s''' % incorrect_guess)
    print('''The correct answer was:
    %s''' % ranMovie)
    print(total_guess)
    print(correct_guess)




while len(incorrect_guess) < MAXIMUM_TRY:
    user_interaction()
