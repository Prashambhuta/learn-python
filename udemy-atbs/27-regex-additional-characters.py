# Additional characters for regular expressions.
import re

# use of ^ and $ character.
# ^ means the mo(matched object) should start with this
# $ means the mo must end with this

# Example
beginRegex = re.compile(r'^Prasham')
print(beginRegex.search('Prasham is studying python').group())

endRegex = re.compile(r'python$')
print(endRegex.search('Prasham is studying python').group())

# Using both ^ and $ confirms the entire length of the search object.

# Example
completeRegex = re.compile(r'^\d+$')
print(completeRegex.search('994298199').group())

# . means any character except new line (wild-card character)

# Example
dotRegex = re.compile(r'\d.+20')
print(dotRegex.search('The phone number that I am looking for is '
                      '79277-abc-20').group())

# Example
# Find out the first name and the last name from the following string
string = "First Name: Prasham Last Name: Bhuta"
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
nameObject = nameRegex.findall(string)

print(nameObject)
print("The first name is: %s and the last name is %s." % (nameObject[
                                                              0][0],
                                                          nameObject[
                                                              0][1]))

# ? is used for non greedy search
# Example
serve = "<To serve human> dinner is my job>"
nonGreedyRegex = re.compile(r'<(.*?)>')  # ? is used for non greedy
# search
print(nonGreedyRegex.findall(serve)[0])

# re.compile(r'.*', re.DOTALL)
# It is used to bypass even \n (new line character) and match everything
# Example

dotallRegex = re.compile(r'.*', re.DOTALL)
print(dotallRegex.search('The phone number \nthat I am \nlooking for '
                         'is 79277-abc-20').group())

# re.compile(r'.*', re.IGNORECASE)
# used to match characters irrespective of the case, i.e. match both
# UPPERCASE and lowercase characters.
# Example

caseRegex = re.compile(r'[aeiou]', re.IGNORECASE)
print(caseRegex.findall('A dog is jumping over the lazy fox.')) #
# Notice that the 'A' is also printed out.