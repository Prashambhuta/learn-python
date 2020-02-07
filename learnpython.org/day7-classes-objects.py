class MyClass:
    variable = "blah"
    def fun(self):
        print("Function message.")

myobjectx = MyClass()
myobjectx.variable2 = "bl"
print(myobjectx.variable)
(myobjectx.fun())
print(myobjectx.variable2)

# Exercise
# class is Vehicle. Create 2 new vehicles 'car1' and 'car2'
# Car1 is red convertible worth $60000 with name 'Fer'
# Car2 is blue van worth $10000 with name "Jump"

class Vehicle:
    color = ""
    kind = ""
    price = int()
    name = ""
    def output(self):
        n = 1
        print("The car %d is %s %s named %s worth $%d."% (n,self.color, self.kind, self.name, self.price))
        n += 1

car1 = Vehicle()
car2 = Vehicle()
car1.color = "red"
car1.kind = "convertible"
car1.price = 60000
car1.name = "Fer"
car1.output()

car2.color = "blue"
car2.kind = "van"
car2.price = 10000
car2.name = "Jump"
car2.output()