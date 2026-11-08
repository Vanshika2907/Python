'''
Student Grading System
'''
students = {}

n = int(input("Enter number of students: "))

for i in range(n):
    name = input("\nEnter student name: ")

    marks = []

    for j in range(3):
        mark = float(input("Enter subject mark: "))
        marks.append(mark)

    total = sum(marks)
    average = total / 3

    if average >= 90:
        grade = "A"
    elif average >= 80:
        grade = "B"
    elif average >= 70:
        grade = "C"
    elif average >= 60:
        grade = "D"
    else:
        grade = "F"

    students[name] = {
        "marks": marks,
        "total": total,
        "average": average,
        "grade": grade
    }

print("\n--- STUDENT RESULTS ---")

for name, details in students.items():
    print("\nName:", name)
    print("Marks:", details["marks"])
    print("Total:", details["total"])
    print("Average:", details["average"])
    print("Grade:", details["grade"])