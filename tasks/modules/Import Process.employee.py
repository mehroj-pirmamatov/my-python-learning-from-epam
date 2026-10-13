def create_employee(name, position, salary):
    return {
        "name": name,
        "position": position,
        "salary": salary
    }


def get_employee_info(employee):
    return (
        f"Name: {employee['name']}\n"
        f"Position: {employee['position']}\n"
        f"Salary: ${employee['salary']}"
    )
