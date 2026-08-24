#Write a Python Program for a Simple Calculator

#taking input
print("----- Simple Calculator -----")
a=float(input("Enter first number: "))
b=float(input("Enter second number: "))
o=input("Enter operation (+, -, *, /,//): ")

#calculation and output
if o=='+':
    print("Result: ", a+b)
elif o=='-':
    print("Result: ", a-b)
elif o=='*':
    print("Result: ", a*b)
elif o=='/':
    if b!=0:
        print("Result: ", a/b)
    else:
        print("Error: Division by zero")
        b=float(input("Enter second number (non-zero): "))
        print("Result: ", a/b)
elif o=='//':
    if b!=0:
        print("Result: ", a//b)
    else:
        print("Error: Division by zero")
        b=float(input("Enter second number (non-zero): "))
        print("Result: ", a//b)
else:
    print("Invalid operation")  

