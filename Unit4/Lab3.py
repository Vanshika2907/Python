
# To create a payroll management system using CSV files to store employee details and calculate salaries.

import csv

def add_employee():
    emp_id = input("Enter Employee ID: ")
    name = input("Enter Employee Name: ")
    basic_salary = float(input("Enter Basic Salary: "))
    allowance = float(input("Enter Allowance: "))
    deduction = float(input("Enter Deduction: "))

    net_salary = basic_salary + allowance - deduction

    with open("payroll.csv", "a", newline="") as file:
        writer = csv.writer(file)

        writer.writerow([
            emp_id,
            name,
            basic_salary,
            allowance,
            deduction,
            net_salary
        ])

    print("Employee payroll added successfully!")

def display_payroll():
    try:
        with open("payroll.csv", "r") as file:
            reader = csv.reader(file)

            print("\nEmployee Payroll Details:")
            print("ID | Name | Basic | Allowance | Deduction | Net Salary")

            for row in reader:
                print(" | ".join(row))

    except FileNotFoundError:
        print("No payroll records found.")

while True:
    print("\n1. Add Employee")
    print("2. Display Payroll")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_employee()
    elif choice == "2":
        display_payroll()
    elif choice == "3":
        print("Exiting Program.")
        break
    else:
        print("Invalid Choice!")
