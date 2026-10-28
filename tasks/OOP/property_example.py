
class Employee:
    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def annual_salary(self):
        return self.salary * 12


employee = Employee("Ali", "Karimov", 5000000)

print(employee.full_name)
print(employee.annual_salary)

employee.first_name = "Hasan"

print(employee.full_name)
