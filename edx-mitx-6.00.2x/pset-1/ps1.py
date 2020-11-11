###########################
# 6.00.2x Problem Set 1: Space Cows 

from ps1_partition import get_partitions
import time


# ================================
# Part A: Transporting Space Cows
# ================================

def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """

    cow_dict = dict()

    f = open(filename, 'r')

    for line in f:
        line_data = line.split(',')
        cow_dict[line_data[0]] = int(line_data[1])
    return cow_dict


# Problem 1
def greedy_cow_transport(cows, limit=100):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    result = []
    cows_dict = cows.copy()
    sorted_cows = sorted(cows_dict.items(), key=lambda x: x[1], reverse=True)
    transferred = []
    weight = limit
    # print(sorted_cows)
    while len(transferred) != len(sorted_cows):
        current_count = 0
        trip = []
        for cow in sorted_cows:
            if cow not in transferred:
                if cow[1] + current_count <= weight:
                    trip.append(cow[0])
                    transferred.append(cow)
                    current_count += cow[1]
        result.append(trip)
    print(result)

# Problem 2
def brute_force_cow_transport(cows, limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    list_of_cows = list(cows.items())
    # list_of_cows = [('A', 3), ('B', 7), ('C', 9),('D', 2)]
    # print(list_of_cows)
    result = [[x[0]] for x in list_of_cows]
    weight = limit
    for items in get_partitions(list_of_cows):
        valid_trip = True
        for item in items:
            trip_weight = sum([x[1] for x in item])
            if trip_weight > weight:
                valid_trip = False
                break
        if valid_trip:
            if len(items) < len(result):
                temp = []
                for x in items:
                    temp.append(list(y[0] for y in x))
                result = temp

    print(result)


# Problem 3
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    start = time.time()
    greedy_cow_transport(cows)
    end =time.time()
    print("GREEDY ->" + str(end-start))

    start = time.time()
    brute_force_cow_transport(cows)
    end = time.time()
    print('BRUTE ->' + str(end-start))



"""
Here is some test data for you to see the results of your algorithms with. 
Do not submit this along with any of your answers. Uncomment the last two
lines to print the result of your problem.
"""

cows = load_cows("ps1_cow_data.txt")
limit = 10
print(cows)

# print(greedy_cow_transport(cows, limit))
# print(brute_force_cow_transport(cows, limit))
compare_cow_transport_algorithms()