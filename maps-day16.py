# Understanding maps from learn-python.org
# maps allows to apply functions across a no of variables in one go.
# Example
# List of iterables of pet names in smaller case and convert them to upper case using map
# Without using maps
my_pets = ['alfred', 'tabitha', 'william', 'arla']
pet_upper = []
for x in my_pets:

    pet_upper.append(x.upper())

print(pet_upper)

# With using 'maps'
upper_using_maps = list(map(str.upper, my_pets))
print(upper_using_maps)

# Example 2
# reiterate the list with radius of circles with changing the decimal points according to their position
# that means the first position should have 1 decimal and second should have second and so on..

circle_areas = [3.56773, 5.57668, 4.00914, 56.24241, 9.01344, 32.00013]

new_areas = list(map(round, circle_areas, range(1,4)))
print(new_areas)

# round function requires two arguments, first, is item to round and second is decimal places to round, and with range (1,4)
# it gets everything
# When using range that is less than the no of items, the round function will stop after the given no of arguments.
# Check example above where range(1,4) stops after 3rd item.