#! usr/bin/env python3

num = 20
if num < 0:
    num_neg = True
    num = abs(num)
else:
    num_neg = False

binary = ''
while num > 0:
    binary = str(num % 2) + binary
    num = num // 2
if num_neg:
    print('-' + binary)
else:
    print(binary)

