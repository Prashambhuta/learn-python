#!/usr/bin/env python3

import re
import pyperclip
import pprint

# Generate regex for phone_numbers.
phone_regex = re.compile(r'''
# 415-555-0000, 4155550000, (415) 555-0000, 555-0000 ext 12345, ext., .x
(
((\d\d\d)|(\(\d\d\d\)))?    # area code (optional)
(\s|-)   # first separator
(\d\d\d)    # first 3 digits
-    # separator
(\d\d\d\d)    # last 4 digits
((\s(\w*)?(.)?\s)|(\w)    # extension word-part
 (\d{2,5}))?   # extension number
)

''', re.VERBOSE)

# Create a regex for email address.
email_regex = re.compile(r'''
# someth.+_ing@someth.+_ing.com/edu/gov/in

([a-z0-9.+_]+    # name part
@    # @ symbole
[a-z0-9.+_]+    # domain name part
.\w{2,5})    # extension

''', re.VERBOSE | re.I)

# Get the text off from clipboard.
TEXT = pyperclip.paste()

# Extract phone number and email address from this text.
phone_object = phone_regex.findall(TEXT)
email_object = email_regex.findall(TEXT)

# Copy extracted phone_numbers & email_address to clipboard.
phone_numbers = []
for numbers in phone_object:
    phone_numbers.append(numbers[0])

pyperclip.copy('\n'.join(phone_numbers))
print('\n'.join(email_object))
# pprint.pprint(phone_numbers)
# pprint.pprint(phone_object)
# pprint.pprint(email_object)