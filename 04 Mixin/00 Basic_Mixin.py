class FlyMixin:
    def fly(self):
        print("Flying...")

class Animals():
    def eat(self):
        print("Eating...")

class Bird(Animals, FlyMixin):
    def speak(self):
        print("Birds can Birding and ...")

class airplanes(Animals,FlyMixin):
    def sound(self):
        print("Airplane sound: vrrrrr! and people can ... ")

bird = Bird()
bird.speak()
bird.fly()
bird.eat()
Air=airplanes()
Air.sound()
Air.fly()
Air.eat()
