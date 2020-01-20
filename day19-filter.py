# Filters
# map() passes each element of iterable through func and returns the result.
# filter() only passes 'TRUE' values to the function thus filtering the FALSE values.
# Key points - unlike map(), only 1 iterable is required
# - func argument requires to return a boolean value.
# - filter only passes TRUE iterables through the function.
# Example
# Following is a list of score of 10 students. Using filter check out who scored more than 75.

scores = [66, 90, 68, 59,76, 60, 88, 74, 81, 65]

# def A_student(score):
#     return score >75

passed = list(filter(lambda x: x >75, scores))

print(passed)

# Example
# Filter out names that are palindrome from a list

dromes = ("demigod", "rewire","madam", "freer", "anutforajaroftuna", "kiosk","nitin")

palindromes = list(filter(lambda y: y == y[::-1], dromes))
print(palindromes)
