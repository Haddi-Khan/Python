class Student :
    def __init__(self,name,grade):
        self.name=name
        self.grade=grade       
    def display(self):
        return f"Student: {self.name}, Grade: {self.grade}"        
class  Teacher :
    def __init__(self,name,subject):
        self.name=name
        self.subject=subject        
    def display(self):
        return f"Teacher: {self.name}, Subject: {self.subject}"        
class School:
    def __init__(self,school_name):
        self.school_name=school_name
        self.students=[]
        self.teachers=[]         
    def add_student(self,student):
        self.students.append(student)        
    def add_teacher(self, teacher):
        self.teachers.append(teacher)        
    def show_students(self):
        print("     Students       ")
        for s in self.students:
            print(s.display())
    def show_teachers(self):
        print("     Teachers        ")
        for t in self.teachers:
            print(t.display())
    def school_info(self):
        print(f"School: {self.school_name}")
        print(f"Total Students: {len(self.students)}")
        print(f"Total Teachers: {len(self.teachers)}") 
my_school = School("The Trust school")
s1 = Student("Haddi", "10th")
s2 = Student("Ahmed", "9th")
my_school.add_student(s1)
my_school.add_student(s2)
t1 = Teacher("Mr. Ali", "Math")
t2 = Teacher("Ms. Sara", "Computer Science")
my_school.add_teacher(t1)
my_school.add_teacher(t2)
my_school.school_info()
my_school.show_students()
my_school.show_teachers()