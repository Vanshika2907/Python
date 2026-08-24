'''
Write a Python program to check whether a given positive number is a prime 
number or not and also to give the factorial of the number.
'''
# Prime Number
num=int(input("Enter a positive number: "))
if num<=1:
    print(num,"is not a prime number")
    exit()
prime=True
for i in range(2,num):
    if (num%i==0):
        prime=False
        break
if(prime==True):
    print(num,"is a prime number")
else:
    print(num,"is not a prime number")

# Factorial

n=int(input("Enter a number: "))
if(n<0):
    print("Factorial does not exist for negative numbers")
elif(n==0):
    print("The factorial of 0 is 1")
else:
    f=1
    for i in range(1,n+1):
        f=f*i
    print("The factorial of",n,"is",f)
