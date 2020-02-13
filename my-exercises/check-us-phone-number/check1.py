# Check phone number in US/Canada format eg. 555-000-4444
def check1(text):
    if len(text) != 12:
        return False
    if not text[0:3].isdecimal():
        return False
    if not text[3] == '-':
        return False
    if not text[4:7].isdecimal():
        return False
    if not text[7] == '-':
        return False
    if not text[8:11].isdecimal():
        return False
    else:
        print("The number is %s" % text)

check1('555-000-4414')

message = "My phone number is 444-222-1111 and another is 555-222-3333"

for i in range(len(message)):
    chunk = message[i:i+12]
    if check1(chunk):
        print("The number is %s" % chunk)