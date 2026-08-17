'''
Write a Python program to print the first n terms of fibonacci series.
0,1,1,2,3,5,8,...
'''
n=int(input("Enter the number of terms: "))
a=0
b=1
if n<=0:
    print("Invalid. Enter a positive integer:")
elif n==1:
    print("Fibonacci Sequence:")
    print(a)
else:
    print("Fibonacci Sequence:")
    print(a,end=" ")
    print(b,end=" ")
    for i in range(2,n):
        c=a+b
        print(c,end=" ")
        a=b
        b=c