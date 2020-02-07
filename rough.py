numbers = [236, 938, 231, 111, 237, 138,192, 160]

# print odd numbers and stop at 237

for i in numbers:
    if i%2 == 1:
        print(i)
    else:
        if i == 237:
            break
