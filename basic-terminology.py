def hello(name):
    print("Hello %s" % name)

hello("Prasham")                # Argument
hello("Abhu")

# Argument = value passed in function call/calling the function
# Parameter = variable inside the function, mostly when defining the function.

# In this example
# Argument = 'Prasham', 'Abhu'
# Parameter = name

# CLASS & OBJECTS

# Class is a template/pattern/format for creating Objects in Python.
# Objects are a coverage of multiple variables and functions into 1 item.
# Objects get their variable and function from the classes.

# Example
print("CLASS & OBJECTS EXAMPLE")
class myclass:                  # template for class that contains all the variables and functions.
    variable = "blah"           # variable defined
    def myfun(self):            # function defined
        print("Myfun message.")
myobjectx = myclass()           # variable "myobjectx" holds the objects of the class "myclass".

print(myobjectx.variable)       # accessing the object variable
myobjectx.myfun()               # accessing the object function.