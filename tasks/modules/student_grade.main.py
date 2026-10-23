from grades import calculate_average, get_status

students = {
    "Ali": [90, 85, 92],
    "Vali": [75, 80, 68],
    "Sardor": [45, 55, 50],
}

for name, grades in students.items():
    average = calculate_average(grades)
    status = get_status(average)

    print(f"{name}: Average = {average:.2f}, Status = {status}")
