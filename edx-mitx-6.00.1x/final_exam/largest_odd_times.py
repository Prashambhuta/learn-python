#! usr/bin/env python3
def largest_odd_times(L):
    """ Assumes L is a non-empty list of ints
        Returns the largest element of L that occurs an odd number
        of times in L. If no such element exists, returns None """
    # ENTER CODE HERE
    # create a dict
    times = {}

    # for i in L
    for i in L:

        # dict[i] = dict.get(i, 0) +1
        times[i] = times.get(i, 0) + 1

    # sort dict, ascending = False
    number = sorted(times, reverse=True)

    # for key, value in dict.items()
    for number in number:
        # if value % 2 = 1
        if times[number] % 2 == 1:

            # return value
            print(number)
            return number

    # return None
    return None


largest_odd_times([3,9,5,3,5,3])
largest_odd_times([3,3,2,0])