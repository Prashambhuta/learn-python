from ps1_partition import get_partitions

cows = {'Maggie': 3, 'Herman': 7, 'Betsy': 9, 'Oreo': 6, 'Moo Moo': 3,
        'Milkshake': 2, 'Millie': 5, 'Lola': 2, 'Florence': 2, 'Henrietta': 9}


# def g_c_t(dictionary, limit=10):
#     result = []
#     cows_dict = dictionary.copy()
#     sorted_cows = sorted(cows_dict.items(), key=lambda x: x[1], reverse=True)
#     transferred = []
#     weight = limit
#     # print(sorted_cows)
#     while len(transferred) != len(sorted_cows):
#         current_count = 0
#         trip = []
#         for cow in sorted_cows:
#             if cow not in transferred:
#                 if cow[1] + current_count <= weight:
#                     trip.append(cow[0])
#                     transferred.append(cow)
#                     current_count += cow[1]
#                     # print(cow)
#                     # print(transferred)
#             # count = count + cow[1]
#             # iterative_list.remove(cow)
#         result.append(trip)
#     print(result)
#
# g_c_t(cows)

"""
BRUTE FORCE
"""

# Brute force algorithm
def brute_force_cow_transport(cows, limit=10):
    """
    Returns the list of minimum number of trips required to transport cows,
    using brute force method.

    Parameters:
        cows <- dictionary containing names and weights of cows in key,
        values pair
        limit <- limit of the cargo

    Returns:
        List of lists with cow names
    """
    list_of_cows = list(cows.items())
    # list_of_cows = [('A', 3), ('B', 7), ('C', 9),('D', 2)]
    # print(list_of_cows)
    list_of_cows_copy = list_of_cows.copy()
    result = [[x[0]] for x in list_of_cows]
    weight = limit
    min_len = len(list_of_cows)
    for items in get_partitions(list_of_cows):
        valid_trip = True
        # for i in range(len(items)):
        for item in items:
            total_weight = None
            # print(item)
            trip_weight = sum([x[1] for x in item])
            # print(trip_weight)
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

"""
CALLING THE BRUTE FORCE METHOD"""
brute_force_cow_transport(cows)
# for item in get_partitions(['Prasham', 'Bhuta', 'Vikas']):
#     print(item)