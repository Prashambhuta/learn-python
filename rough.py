import pprint
numbers = [236, 938, 231, 111, 237, 138,192, 160]

# print odd numbers and stop at 237

for i in numbers:
    if i%2 == 1:
        print(i)
    else:
        if i == 237:
            break

message = 'It was a long and dark december, from the rooftops I remember.'
count = {}

for characters in message.upper():
    count.setdefault(characters, 0)
    count[characters] = count[characters] + 1

pprint.pprint(count)

def time_for_milk_and_cookies(date):
	if date[2] == 24:
		print("T")
time_for_milk_and_cookies((2,2,24))

list = "https://reddit.com/r/mildlyinteresting/"
print(list.split("/")[4])
print(''.join(sorted(list)))

def card_hide(card):
    print(card.replace(card[:-4],'*' * len(card[:-4])))
    print('*' * len(card[:-4]) + card[-4:])
card_hide('44443331234')

