# Exercise on map, filter and reduce

from functools import reduce

# Use map to print the sqaure of each number rounded
# up to three decimal places
my_floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59]

sqaures = list(map(lambda x:round(x*x,3), my_floats))
print(sqaures)

# Use filter to print only the names that are less than seven letters

my_names = ["olumide", "akinremi", "josiah", "temidayo", "omoseum", "vikas", "prasham", "bhavik"]

filtered_names = list(filter(lambda y:len(y)>=7, my_names))
print(filtered_names)

# Use reduce to print the product of these numbers
my_numbers = [4, 6, 9, 23, 5]
product = reduce(lambda x,y:x*y, my_numbers)
print(product)