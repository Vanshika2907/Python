
# To create a student data management system using file handling operations.

def add_student():
    with open("students.txt", "a") as file:
        roll = input("Enter Roll Number: ")
        name = input("Enter Student Name: ")
        marks = input("Enter Marks: ")

        file.write(roll + "," + name + "," + marks + "\n")
        print("Student added successfully!")

def display_students():
    try:
        with open("students.txt", "r") as file:
            print("\nStudent Records:")
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("No student records found.")

def search_student():
    roll = input("Enter Roll Number to Search: ")

    try:
        with open("students.txt", "r") as file:
            found = False

            for line in file:
                data = line.strip().split(",")

                if data[0] == roll:
                    print("Student Found!")
                    print("Roll Number:", data[0])
                    print("Name:", data[1])
                    print("Marks:", data[2])
                    found = True
                    break

            if not found:
                print("Student not found.")

    except FileNotFoundError:
        print("No student records found.")

while True:
    print("\n1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        display_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        print("Exiting Program.")
        break
    else:
        print("Invalid Choice!")
