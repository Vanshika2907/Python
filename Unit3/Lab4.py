'''
Attendance Tracker
'''
students = {}

while True:
    print("\n--- ATTENDANCE TRACKER ---")
    print("1. Add Student")
    print("2. Mark Attendance")
    print("3. View Attendance")
    print("4. Attendance Percentage")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter student name: ")

        if name not in students:
            students[name] = []
            print("Student added successfully!")
        else:
            print("Student already exists!")

    elif choice == 2:
        name = input("Enter student name: ")

        if name in students:
            status = input("Enter P for Present or A for Absent: ").upper()

            if status == "P" or status == "A":
                students[name].append(status)
                print("Attendance marked!")
            else:
                print("Invalid attendance status!")
        else:
            print("Student not found!")

    elif choice == 3:
        print("\n--- ATTENDANCE RECORDS ---")

        for name, records in students.items():
            print(name, ":", records)

    elif choice == 4:
        name = input("Enter student name: ")

        if name in students:
            records = students[name]

            total = len(records)
            present = records.count("P")

            if total > 0:
                percentage = (present / total) * 100
                print("Student:", name)
                print("Total Classes:", total)
                print("Present:", present)
                print("Absent:", records.count("A"))
                print("Attendance Percentage:", percentage, "%")
            else:
                print("No attendance records available.")
        else:
            print("Student not found!")

    elif choice == 5:
        print("Exiting Attendance Tracker.")
        break

    else:
        print("Invalid choice!")