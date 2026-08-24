'''
Write a Python Program that accepts student's personal and academic details 
and displays them in a neatly formatted manner using formatted strings
'''
#Accept the values
name=input("Enter Student's Name:")
usn=input("Enter USN:")
branch=input("Enter Branch:")
sem=input("Enter Semester:")
m1=float(input("Enter Physics Marks:"))
m2=float(input("Enter Chemistry Marks:"))
m3=float(input("Enter Math Marks:"))

#   Calculating
total=m1+m2+m3
avg=total/3

#Display
print("-----Student Information-----")
print(f"Name:{name}")
print(f"USN:{usn}")
print(f"Branch:{branch}")
print(f"Semester:{sem}")
print(f"Total Marks:{total}")
print(f"Averagr Marks:{avg}")
