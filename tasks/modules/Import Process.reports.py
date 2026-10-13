def calculate_total_salary(employees):
    return sum(employee["salary"] for employee in employees)


def display_report(employees):
    for employee in employees:
        print(
            f"{employee['name']} - "
            f"{employee['position']} - "
            f"${employee['salary']}"
        )

    total = calculate_total_salary(employees)
    print(f"\nTotal salary: ${total}")
