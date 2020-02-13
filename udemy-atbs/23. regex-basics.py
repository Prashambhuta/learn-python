# Find phone numbers using regex
import re

message = "My first phone number is: 333-444-2222, while my whatsapp number is 544-444-0000 and " \
          "my office number is 444-676-9999 not 444-5555-666."  # Search string

PhoneNumberRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')    # Define the Regex function.
MatchedObject = PhoneNumberRegex.search(message)    # Regex.search finds 1st matched instance.
print(MatchedObject.group())    # Print the first match, remember to user group().
print(PhoneNumberRegex.search(message))

MatchedObjectall = PhoneNumberRegex.findall(message)    # Regex.findall finds all the matches.
print(MatchedObjectall) # Prints all matches.
print(PhoneNumberRegex.findall(message))
