class Employee:
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary

    def calculate_salary(self):
        return self.base_salary


class Developer(Employee):
    def __init__(self, name, base_salary, bonus):
        super().__init__(name, base_salary)
        self.bonus = bonus

    def calculate_salary(self):
        return self.base_salary + self.bonus


class Manager(Employee):
    def __init__(self, name, base_salary, team_bonus):
        super().__init__(name, base_salary)
        self.team_bonus = team_bonus

    def calculate_salary(self):
        return self.base_salary + self.team_bonus


def main():
    employees = [
        Developer("Ali", 3000, 800),
        Manager("Vali", 4000, 1200),
        Employee("Hasan", 2500)
    ]

    for employee in employees:
        salary = employee.calculate_salary()
        print(f"{employee.name}: ${salary}")


if __name__ == "__main__":
    main()
