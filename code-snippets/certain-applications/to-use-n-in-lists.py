def check_score(a,b):
    for n in range(len(a)):
        if a[n] > b[n]:
            print("The first element is larger.")
check_score((7,3),(3,4))