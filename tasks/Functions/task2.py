def calculate_average(scores):
    return sum(scores) / len(scores)


def get_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"


scores = [85, 90, 78, 92, 88]

average = calculate_average(scores)
grade = get_grade(average)

print(f"Average: {average:.2f}")
print(f"Grade: {grade}")
