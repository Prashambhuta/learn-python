import re

message = "This is Alfred speaking, the Batmobile is at the top of " \
          "Vez Central HQ. Batman or Batwoman should go there and get " \
          "it " \
          "first. The other option is to call Robin, his phone number " \
          "is +123-555-1234"

batRegex = re.compile(r'Bat(wo)?man')
matchedObject = batRegex.search(message)
print(matchedObject.group())

phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
phoneObject = phoneRegex.search(message)
print("phone Regex is %s" % phoneObject.group())

dRegex = re.compile(r'(\d){1,4}')
dMO = dRegex.search(message)
print(dMO.group())