'''
Write a Python program to check whether a given positive number is a prime 
number or not.
'''
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
