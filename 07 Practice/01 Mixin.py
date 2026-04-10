# Mixin are small specialize class that provide a specific behaviour to the other class 
class specialize:
    def energy (self):
        print("hello I need food")

class Animal (specialize):
    def __init__(self,name):
        self.name = name

class Car (specialize):
    def __init__ (self,model):
        self.model=model


a = Animal("sappor")
c = Car("BMW")

a.energy()
print(a.name)

c.energy()
print(c.model)