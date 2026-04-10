# MIXIN2
class Serializer:
    def energy(self):
        print("Needs energy (food or petrol).")
class Animal(Serializer):
    def __init__(self, name):
        self.name = name
    def species(self):
        print(f"Animal name: {self.name}")
class Fish(Animal):
    def action(self):
        print("This animal can swim ")
class Bird(Animal):
    def action(self):
        print("This animal can fly ")
class Vehicle(Serializer):
    def __init__(self, name):
        self.name = name
    def vehicle_name(self):
        print(f"Vehicle name: {self.name}")
class Truck(Vehicle):
    def type(self):
        print("This is a heavy vehicle ")
class Car(Vehicle):
    def type(self):
        print("This is a light vehicle ")
animal_input = input("Enter animal name: ")
vehicle_input = input("Enter vehicle name: ")
if animal_input == "fish":
    animal = Fish(animal_input)
else:
    animal = Bird(animal_input)
animal.species()
animal.action()
animal.energy()
print("------------")
if vehicle_input == "truck":
    vehicle = Truck(vehicle_input)
else:
    vehicle = Car(vehicle_input)
vehicle.vehicle_name()
vehicle.type()
vehicle.energy()

