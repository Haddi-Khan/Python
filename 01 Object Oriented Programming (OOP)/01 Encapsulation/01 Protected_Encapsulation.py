class Company:
    def __init__(self):
        self._project = "Internal AI" 

class Department(Company):
    def show_project(self):
        
        print(f"Working on: {self._project}")

dept = Department()
dept.show_project()
print(dept._project) 
