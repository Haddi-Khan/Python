pi=3.14159
class shape :
    def area(self):
        pass
class circle (shape):
    def __init__(self,radius):
       self.radius=radius
    def area(self):
        return 2* pi*self.radius
class Rectangle(shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
c = circle(5)
r = Rectangle(4, 6)
print("Circle Area:", c.area())      
print("Rectangle Area:", r.area())   