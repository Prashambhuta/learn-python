spam = 0
while spam < 5:
    print("Hi")
    spam = spam +1

# Example with use of break
name = ''
print('PLease enter your name')
name = input()
while name != 'Prasham':
    print("Incorrect name")
    # print('Please enter your name')
    # name = input()
    break

print("Thanks")

# Use of continue
n = 0
while n <5:
    n = n + 1
    if n == 3:
        continue
    print(n)
