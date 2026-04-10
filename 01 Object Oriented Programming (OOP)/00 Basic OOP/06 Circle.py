pi_value = 3.141592653589793
class circle:
    def __init__(self,circle_radius):
        self.circle_radius = circle_radius
  
    def area (self):
        return pi_value * (self.circle_radius**2)
    def circumference (self):
        return 2* pi_value *self.circle_radius
cir= circle(20)
print(f"The area of the circle is {cir.area()}")
print(f"The circumference of the circle is {cir.circumference()}")
