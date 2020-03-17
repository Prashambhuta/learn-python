#! usr/bin/env python3
"""
Convert float such as 1.235 to binary.
"""

num = float(input("Enter a number: "))

# split the number into whole & fraction.
whole, frac = str(num).split(".")

# convert them from str to int & float respectively
whole = int(whole)
frac = int(frac)

# convert whole to binary
if whole < 0:
    is_whole_Neg = True
    whole = abs(whole)
else:
    is_whole_Neg = False

whole_result = ''     # declaring the whole result
if whole == 0:
    whole_result = '0' + whole_result
else:
    while whole > 0:
        whole_result = str(whole % 2) + whole_result
        whole = whole // 2
if is_whole_Neg:
    print("Whole part: " + "-" + whole_result)
else:
    print("Whole part: " + whole_result)

# convert float to binary
float_result = ''
new_frac = "." + str(frac)
new_frac = float(new_frac)  # convert fraction part from int to float
p = 0

# calculate p required to convert frac into whole number
while ((2**p)*new_frac) % 1 != 0:
    # print(((2**p)*new_frac) - int((2**p)*new_frac))
    p += 1

num = int(new_frac*(2**p))  # generate num in int

while num > 0:
    float_result = float_result + str(num % 2)
    num = num // 2

# add additional places at the start
for i in range(p - len(float_result)):
    float_result = "0" + float_result

# add "0." to the start
float_result = "0." + float_result
print("Float part: " + float_result)

# print final result
if is_whole_Neg:
    print("Complete: " + "-" + str(int(whole_result) + float(float_result)))
else:
    print("Complete: " + str(int(whole_result) + float(float_result)))
