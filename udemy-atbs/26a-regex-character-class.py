import re

# \d - any digit between 0 to 9
digitRegex = re.compile(r'\d')
message = "My first phone number is: 333-444-2222, while my whatsapp " \
          "number is 544-444-0000 and " \
          "my office number is 444-676-9999 not 444-5555-666."
print((digitRegex.findall(message)))

# \D - any character not 0 to 9 i.e. not \d
DigitRegex = re.compile(r'\D')
print((DigitRegex.findall(message)))

# \w - any number, alphabet, underscore( _ ).
wordRegex = re.compile(r'\w')
print((wordRegex.findall(message)))

# \W - any thing that is not \w
WordRegex = re.compile(r'\W')
print(WordRegex.findall(message))

# \s - any space, tab or newline character
spaceRegex = re.compile(r'\s')
print(spaceRegex.findall(message))

# \S - any thing that is not \s
SpaceRegex = re.compile(r'\S')
print(SpaceRegex.findall(message))

# Example - 12 days of Christmas, finding 12 drummers, 11 pipers etc.
lyrics = """ 12 drummers drumming
                11 pipers piping
                10 lords-a-leaping
                9 ladies dancing
                8 maids-a-milking
                7 swans-a-swimming
                6 geese-a-laying
                5 golden rings
                4 calling birds
                3 French hens
                2 turtle doves
                and 1 partridge in a pear tree. """

xmasRegex = re.compile(r'\d+\s\w+')
print(xmasRegex.findall(lyrics))

# Custom creating your own regex character class.
# Example - For finding double 'm' i.e double-m.
doublemRegex = re.compile(r'\w+[mm]\w+')
print(doublemRegex.findall(lyrics))

# Example - For finding words any double alphabets
DoublealphaRegex = re.compile(r'\w+[lm]{2}\w+')
print(DoublealphaRegex.findall(lyrics))

# Negative character class uses ^.
# Example - Fing every character not 1 to 4
negativeRegex = re.compile(r'[^1-4]')
print(negativeRegex.findall(lyrics))

