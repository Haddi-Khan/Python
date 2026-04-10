class Teacher:
    def __init__(self,name,subject):
        self.name= name
        self.subject = subject
    def teach(self):
        print(f"The name of a techer is {self.name} and his subect is {self.subject}")
class Researcher:
    def __init__(self, field):
        self.field = field
    def research(self):
        print(f"Researching in the field of {self.field}.")           
class TeachingResearcher(Teacher, Researcher):
    def __init__(self, name, subject, field):
        Teacher.__init__(self, name, subject)   
        Researcher.__init__(self, field)       
    def display(self):
        print(f"Name: {self.name}, Subject: {self.subject}, Field: {self.field}")
tr = TeachingResearcher("Dr.Ahmed", "Computer Science", "Artificial Intelligence")
tr.display()
tr.teach()
tr.research()     
        
        
        
        
