class person:
    def __init__(self,name,age):
        self.name= name
        self.age = age 
    def display_detail(self):
        print(f"The name of a peron is {self.name} and his age is {self.age}")
class student(person):
    def __init__(self, name, age,student_id):
        super().__init__(name, age)
        self.student_id = student_id
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, Student ID: {self.student_id}")             
p=person("haddi",23)
p .display_detail() 
s = student("Haddi", 23, "S101")
s.display()
