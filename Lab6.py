'''
Write a python code to calculate the factorial of a number using loop
'''
num=int(input("Enter a number: "))
if(num<0):
    print("Factorial does not exist for negative numbers")
elif(num==0):
    print("The factorial of 0 is 1")
else:
    f=1
    for i in range(1,num+1):
        f=f*i
    print("The factorial of",num,"is",f)