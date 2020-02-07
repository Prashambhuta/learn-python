def user_numbers():
    input = (1,2,3,4,5) #user input
    for i in range(20):  #output required with 20 enteries
        try:
            print_out_list(input[i]) #add input to output list
        except IndexError:
            print_out_list("No entries") # after input list is over, add output

def print_out_list(n):
    print(n)


user_numbers()

# Exercise

actor = {"name": "John Cleese", "rank": "awesome"}

def get_last_name():
    return actor["name"].split()[1] # split the "name" from actor and use the second input [1]


get_last_name()
print("All exceptions caught! Good job!")
print("The actor's last name is %s" % get_last_name())
