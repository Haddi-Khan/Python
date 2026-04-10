class employee:
    def __init__(self, employee_name,employee_position,employee_salary):
        self.employee_name = employee_name
        self.employee_position = employee_position
        self.employee_salary = employee_salary
        
        print(f"The name of employee is {employee_name} his current position in the company is {employee_position}\nhis monthly salary is {employee_salary}")
    def yearly_salary(self):
        return self.employee_salary * 12
emp = employee("Haddi", "Software Engineer", 50000)
print(f"Yearly Salary of {emp.employee_name}: {emp.yearly_salary()}")