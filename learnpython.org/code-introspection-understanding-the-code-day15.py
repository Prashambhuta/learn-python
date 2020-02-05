# Usage of help function to see what each function does.

help(dir)
help(hasattr)
help(id)

# Defining the Vehicle class
class Vehicle:
    name =""
    kind = "car"
    color = ""
    value = 100.00
def description(self):
    desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
    return desc_str

# Print all attributes of class Vehicle
print(dir(Vehicle))

# Check if certain attribute is part of class/object Vehicle eg. name, color
print(hasattr(Vehicle,"name"))
print(hasattr(Vehicle,"color"))
print(id(Vehicle.value))
