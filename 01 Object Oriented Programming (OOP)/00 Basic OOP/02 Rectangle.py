class rectangle:
    def __init__(self,lenght,width):
        self.lenght = lenght
        self.width = width
        print (f"rectangle has been created with lenght = {self.lenght} and width = {self.width}")
    def area (self):
      return self.lenght *self.width
    def perimeter (self):
        return 2*(self.lenght+self.width)

rect = rectangle(10,5)
print(f"Area: {rect.area()}")
print(f"Perimeter: {rect.perimeter()}")            
