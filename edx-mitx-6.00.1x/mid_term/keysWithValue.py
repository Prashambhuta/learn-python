def keysWithValue(aDict, target):
    """
    aDict: a dictionary
    target: an integer
    returns: sorted list of keys with value 'target'. Empty list if none.
    """
    # initialise the result list.
    result = []

    # for loop iterating over the aDict.keys()
    for keys in aDict.keys():

        # if adict[keys] = target.
        if aDict[keys] == target:

        # append keys to result
            result.append(keys)

    # sort result in increasing order
    result.sort()

    # return result
    return result

keysWithValue({1:1, 2:2, 3:4, 4:4, 5:4}, 4)