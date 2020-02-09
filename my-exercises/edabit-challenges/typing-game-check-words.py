# To check a set of words for their spelling

def correct_stream(user, correct):
    x = []
    for i, j in zip(user, correct):
        if i == j:
            x.append(1)
        else:
            x.append(-1)
    print(x)
    return(x)

    # Better solution

    return [1 if a == b else -1 for a,b in zip(user,correct)]

correct_stream(["it", "is", "find"], ["it", "isa", "fine"])