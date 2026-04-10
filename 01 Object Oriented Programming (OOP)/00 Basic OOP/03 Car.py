class Car:
    def __init__(self,brand,model, year):
        self.brand = brand
        self.model = model
        self.year = year
    def display_info(self):
        print(f"{self.brand} is a {self.model} model car and its manufacture year is {self.year}")
car1 = Car("BMW"," X5",2023)
car2 = Car("Toyota","Corolla",2022)
car1.display_info()
car2.display_info()
