"""
# TODO: Finding out longest sub strings that are in alphabetical order.
"""
s = "sdsfdabc"
result = []
temp = []
iteration = len(s)

# generate all subsets of string

while iteration != 0:
    for i in range(0, iteration):
        temp.append(s[i:iteration])
    iteration -= 1

print(temp)



# TODO: remove elements from list that are not of alphabetical order.
i = ''
for strings in temp:
        #print(strings)
        for n in range(len(strings)):
            if strings[n:n+1] >= strings[n-1:n]:
                i += strings[n:n+1]
for z in range(len(i)):
    if i[z:z+1] >= i[z-1:z]:
        print(i[z:z+1])
print(i)


# for strings in temp:
#     if str(strings) < str(temp[i]):
#         result.append(strings)
#         i += 1
#     print(result)

# for n in range(0, len(temp)):
#     while i != len(temp):
#         if temp[i] > temp[n]:
#             result.append(temp[i])
#             i += 1
#         print(result)