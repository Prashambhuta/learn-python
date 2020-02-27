"""
Find block of codes that will deliver the same output as code below:
"""

iteration = 0
count = 0
while iteration < 5:
    for letter in ("Hello, world"):
        count += 1
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    iteration += 1