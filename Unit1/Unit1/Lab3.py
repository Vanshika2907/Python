'''
Write a Python Program that accepts a floating point number from the user
and displays the following:
1. Square
2. Cube
3. Square Root
4. Ceiling Value
5. Floor Value
6. Absolute Value
7. Type of the Variable
8. Memory Address (ID)
'''
import math
# Taking input
num = float(input("Enter a floating point number: "))

# Displaying results
print("Square: ", num**2)
print("Cube: ", num**3)
print("Square Root: ", math.sqrt(num))
print("Ceiling Value: ", math.ceil(num))
print("Floor Value: ", math.floor(num))
print("Absolute Value: ", abs(num))
print("Type of the Variable: ", type(num))
print("Memory Address (ID): ", id(num))