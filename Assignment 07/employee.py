class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name         # public
        self._salary = salary    # protected (convention)
        self.__ssn = ssn         # private (name mangling)

    def display_info(self):
        print("Name:", self.name)
        print("Salary:", self._salary)
        print("SSN (inside class):", self.__ssn)

emp = Employee("Ali", 50000, "123-45-6789")

print("Public - Name:", emp.name)

print("Protected - Salary:", emp._salary)

try:
    print("Private - SSN:", emp.__ssn)
except AttributeError as e:
    print("Private - SSN: Error:", e)

print("Private - SSN (via mangling):", emp._Employee__ssn)

emp.display_info()
