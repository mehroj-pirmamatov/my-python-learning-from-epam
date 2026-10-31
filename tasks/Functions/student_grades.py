
def calculate_average(*grades):
    if not grades:
        return 0

    return sum(grades) / len(grades)


def get_grade_status(average):
    if average >= 90:
        return "Excellent"

    elif average >= 70:
        return "Good"

    elif average >= 50:
        return "Satisfactory"

    return "Failed"


def student_report(name, *grades):
    average = calculate_average(*grades)
    status = get_grade_status(average)

    return {
        "student": name,
        "average": round(average, 2),
        "status": status
    }


report = student_report("Mehroj", 85, 90, 78, 95)

print(report)
