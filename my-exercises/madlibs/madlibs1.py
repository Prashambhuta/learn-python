# Madlibs Generator
# There is no pain you are receding, A distant ship smoke on the horizon,
# You are only coming through in waves, Your lips move but I can't hear what you are saying,
# For I have become comfortably numb.

noun = []
adjective = []
verb = []
adverb = []
place = []
bodypart = []

noun1 = str(input("Enter Noun:"))
verb2 = str(input("Enter Verb ending with -ing:"))
noun2 = str(input("Enter Thing:"))
verb3 = str(input("Enter Verb ending with -ing:"))
bodypart1 = str(input("Enter Bodypart:"))
adverb1 = str(input("Enter Adverb:"))
adjective1 = str(input("Enter Adjective:"))

verb.extend((verb2, verb3))
noun.extend((noun1, noun2))
bodypart.append((bodypart1))
adverb.append((adverb1))
adjective.append((adjective1))
print(noun)

print("There is no %s you are %s. A distant %s smokes on the horizon. You are only %s through in waves. \n"
      "Your %s moves but I can't hear what your saying. You have become %s %s." % (noun[0], verb[0], noun[1], verb[1], bodypart[0], adverb[0], adjective[0]))