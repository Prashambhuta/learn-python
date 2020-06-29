# sample solution as per available in discussions.

"""
Find the largest alphabetically sequence of strings
"""

s = "asdfhhfueissdfdabcd"
i = 0
temp = s[i]
long = ""

while i < len(s) - 1:
    if s[i + 1] >= s[i]:
        temp += s[i + 1]
        # print(temp)
        i += 1
        if len(temp) > len(long):
            long = temp
    elif s[i + 1] < s[i]:
        temp = s[i + 1]
        i += 1
if len(long) == 0:
    long = s[0]
print("Longest substring in alphabetical order is: %s" % long)

