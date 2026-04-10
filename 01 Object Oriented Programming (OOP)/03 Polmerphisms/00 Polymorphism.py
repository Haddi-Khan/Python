class Animal():
    def speak(self):
        print("aminal speak")

class dog (Animal):
    def speak (self):
        print ("woof woof")

class cat (Animal):
    def speak (self):
        print ("meow meow")

class bird (Animal):
    def speak (self):
        print ("TWEET TWEET")

a= [dog(),cat(),bird()]
for Animal in a:
    Animal.speak()
   