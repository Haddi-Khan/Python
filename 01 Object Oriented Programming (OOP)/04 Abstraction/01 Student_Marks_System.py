class Student:
    def __init__(self,Name,Marks):
        self.Name=Name
        self.Marks=Marks
    def average_marks(self):
        return sum(self.Marks)/len(self.Marks)
    def garde_students(self):
        avg = self.average_marks()
        if avg>=90:
            return "A+"
        elif avg>=80:
            return "A"
        elif avg>= 70:
            return "B+"
        elif avg>= 60:
            return "C+"
        elif avg>= 50:
            return "C"
        else:
            return "Fail"
    def display_result(self):
        print(f"Student: {self.Name}")
        print(f"Marks: {self.Marks}")
        print(f"Average: {self.average_marks():.2f}")
        print(f"Grade: {self.garde_students()}")
s1=Student("Haddi",[86,98,78,87,97,96])
s2=Student("Ali",[34,76,78,98,21,31])
s1.display_result()
print("----------------------")
s2.display_result()
