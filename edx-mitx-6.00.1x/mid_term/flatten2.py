
def flatten(aList):
    """
    aList: a list
    Returns a copy of aList, which is a flattened version of aList
    """
    result = []
    list_copy = aList[:]
    def addToResult(list_copy):
        for items in list_copy:
            if type(items) == list:
                addToResult(items)
            else:
                result.append(items)

    addToResult(list_copy)
    print(result)


flatten([[1,'a',['cat', [2, 'doge',3],[],[4, ['as', 3, 4]]],2],[[[3]],'dog'],
          [[[4]]],5,
          [[[[[[[

]]]]]]]])
flatten([[[[12],2], 4, 6],6, 6, 7, 8,'as','fs'])
flatten([[' '], [23, 23, ['as', 2, ['ass', 2]]]])
flatten([{1:1}])