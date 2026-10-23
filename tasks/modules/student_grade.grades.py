def calculate_average(grades):
    if not grades:
        return 0

    return sum(grades) / len(grades)


def get_status(average):
    if average >= 86:
        return "Excellent"
    elif average >= 71:
        return "Good"
    elif average >= 60:
        return "Satisfactory"
    return "Failed"
