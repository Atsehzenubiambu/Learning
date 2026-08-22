# Task 1: Students Names and Grades
students = {
    "Rahim": "A",
    "Favour": "B",
    "Zennie": "A",
    "Alice": "C"
}

for name, grade in students.items():
    print(name, grade)


# Task 2: get() with default value
student = {
    "name": "Zennie",
    "age": 22
}

print(student.get("grade", "Grade not found"))