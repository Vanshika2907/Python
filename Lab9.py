'''
To understand Lamba function.
'''
a=int(input("Enter 1st number:"))
b=int(input("Enter 2nd number:"))
n=int(input("Enter a number to check even or odd:"))

add=lambda a,b: a+b
msg=lambda: print("Hello")
print(add(a,b))
msg()
a=lambda n:"Even" if n%2==0 else "Odd"
print(a(n))
