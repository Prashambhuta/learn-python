def score(word, f):
    """
       word, a string of length > 1 of alphabetical
             characters (upper and lowercase)
       f, a function that takes in two int arguments and returns an int

       Returns the score of word as defined by the method:

    1) Score for each letter is its location in the alphabet (a=1 ... z=26)
       times its distance from start of word.
       Ex. the scores for the letters in 'adD' are 1*0, 4*1, and 4*2.
    2) The score for a word is the result of applying f to the
       scores of the word's two highest scoring letters.
       The first parameter to f is the highest letter score,
       and the second parameter is the second highest letter score.
       Ex. If f returns the sum of its arguments, then the
           score for 'adD' is 12
    """
    # initialise empty dict to keep track of scores
    scores = []

    # making a copy of word
    word_copy = word[:]

    # convert word to lower, and save it in new variable
    word_lower = word_copy.strip().lower()

    # if lower word = ''
    if len(word_lower) <= 1:

        # return 0
        return 0

    # loop over letters in word using index
    for i in range(len(word_lower)):

        # score = (ord(letter) - 96) * (index)
        letter_score = (ord(word_lower[i]) - 96) * i

        if letter_score > 0:

            # append letter as key, score as value to scores dict.
            scores.append(letter_score)

        else:
            scores.append(0)

    # Check dictionary
    print(scores)

    # Get the two highest score using 'get' and 'max' and save them into two
    # variables.
    list_of_scores = sorted(scores, reverse=True)
    print(list_of_scores)
    max_score = list_of_scores[0]
    second_score = list_of_scores[1]

    # return f(arg,arg)
    return f(max_score, second_score)

# def function f with two arguments.
def total_score(max_score, second_score):

    # return sum of two numbers
    print(max_score + second_score)


# Call the function to test.
score('assdfawwa', total_score)
