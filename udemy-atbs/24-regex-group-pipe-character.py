import re

message = '''My Phone number is +444-333-2222 &
            222-333-4567. My wife's phone number is
            876-543-9999.
            '''
PhoneNumberRegex = re.compile(
    r'(\d\d\d)-(\d\d\d-\d\d\d\d)')  # define the pattern to find &
# group numbers into 2list value
MatchedObject = PhoneNumberRegex.findall(message)

print(MatchedObject)

message1 = '''This is the description to find all bat related items.
Batwatch is in the drawer, Batknife is in the kitchen.
            Batmobile is in the garage and Batman is sleeping on the
            roof.'''

batRegex = re.compile(r'Bat(man|watch|knife|mobile)')
batObject = batRegex.search(message1)
print(batObject.group())
