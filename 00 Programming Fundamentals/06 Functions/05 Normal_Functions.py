class Animal:
    def eat(self):
        print("Eating...")

class Dog(Animal):
    def bark(self):
        print("Barking...")

class Cat(Animal):
    def mewo(self):
        print("Mewo...")

dog = Dog()
dog.bark()
dog.eat()
cat = Cat()
cat.mewo()
cat.eat()
