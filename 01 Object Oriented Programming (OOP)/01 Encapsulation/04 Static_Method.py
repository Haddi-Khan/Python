class temperature():
    def C_to_f(c):
        return (c*9/5)+32
    def F_to_C(f ):
        return (f-32)*5/9
print(temperature.C_to_f(0))
print(temperature.F_to_C(98.6))
    