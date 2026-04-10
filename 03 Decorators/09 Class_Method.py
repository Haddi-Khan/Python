class Student():
    count = 0
    def __init__(self,name):
        self.name=name
        Student.count +=1
    @classmethod
    def total_students(cls):
        return cls.count
s1 = Student("Haddi")
s2 = Student("Ali")
s3 = Student("Zara")
print("Total Students:", Student.total_students())
    