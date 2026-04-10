class LivingBeing:
    def breathe(self):
        print("This living being is breathing.")
class Animal(LivingBeing):
    def move(self):
        print("This animal is moving.")
class Dog(Animal):
    def bark(self):
        print("The dog is barking: Woof!")
my_dog = Dog()
my_dog.breathe() 
my_dog.move()     
my_dog.bark()     
