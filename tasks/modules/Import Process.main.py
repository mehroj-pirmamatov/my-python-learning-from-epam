from employee import create_employee
import reports


def main():
    employees = [
        create_employee("Ali", "Python Developer", 1500),
        create_employee("Vali", "Backend Developer", 1800),
        create_employee("Hasan", "Software Engineer", 2000)
    ]

    reports.display_report(employees)


if __name__ == "__main__":
    main()
