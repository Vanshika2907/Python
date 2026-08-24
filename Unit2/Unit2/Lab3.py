'''
Write a python Program for generating fibonacci series till n using recursion.
'''
n=int(input("Enter the number of terms: ")) # n represents the index number
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print("Fibonacci Sequence:")
for i in range(n):
    print(fibonacci(i), end=" ")
    