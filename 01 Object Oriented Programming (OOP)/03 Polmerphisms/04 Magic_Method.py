class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
    def __str__(self):
        return f"{self.real} + {self.imag}i"
c1 = Complex(5, 7)
print(c1)