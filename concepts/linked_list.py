"""
Understading the concept of linked list.

Linked list is a memory efficient way of storing data.
Each item consists of 2 elements, data & reference.
Reference- Each node refers to location of next node.
"""

# TODO: insert link to tutorial source.
"""
Learning source - 
"""


# Creating the node class
class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None


# Creating the linked list class
class linked_list:
    def __init__(self):
        self.start_node = None  # starting or the first node of the list.

    # Traversing (read data) the list
    def traverse_list(self):
        if self.start_node is None:  # checks traverse_list is empty or not.
            print("List has no elements.")
            return
        else:
            n = self.start_node
            while n is not None:
                print(n.data, " ")
                n = n.ref

    # Inserting items at the beginning.
    def insert_at_start(self, data):
        new_node = Node(data)  # create an object of Node class
        new_node.ref = self.start_node  # reference of 'start_node' to the 'ref'
        self.start_node = new_node  # set the value of start_node to new_node

    # Inserting items at the end.
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.start_node is None:
            self.start_node = new_node
            return
        n = self.start_node
        while n.ref is not None:
            n = n.ref
        n.ref = new_node

"""
Testing the insertion functions.
"""

# Create object of linked_list class
my_new_list = linked_list()

# Check insert_at_end function
my_new_list.insert_at_end(5)
my_new_list.insert_at_end(10)
my_new_list.insert_at_end(8)

# To check use the traverse function
my_new_list.traverse_list()

# Check insert_at_start function
my_new_list.insert_at_start(2)
my_new_list.insert_at_start(4)

# To check using traverse function
my_new_list.traverse_list()