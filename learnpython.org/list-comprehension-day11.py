# Create new lists using existing list

sentence = "The quick brown fox jumps over the lazy dog."
words = sentence.split()
qord_length =[len(word) for word in words if word != "the"]

print(words)
print(qord_length)

# exercise
# Create a list "newlist" out of "numbers" which should only contain positive numbers.

numbers = [34.6, -283.4, 44.9, 68.3, -12.2, 44.6, 12.7]
newlist = [float(number) for number in numbers if number > 0]
# create newlist with inputs of number, number is inside numbers list, add only if number is >0 i.e. positive

print(newlist)
