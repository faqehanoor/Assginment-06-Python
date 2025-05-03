class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_details(self):
        return f"Name: {self.name}, Position: {self.position}"

class Department:
    def __init__(self, department_name, employee):
        self.department_name = department_name
        self.employee = employee 

    def show_employee_details(self):
        return f"Department: {self.department_name}\nEmployee Details: {self.employee.get_details()}"

emp = Employee("John Doe", "Software Engineer")

dept = Department("IT Department", emp)

print(dept.show_employee_details())
