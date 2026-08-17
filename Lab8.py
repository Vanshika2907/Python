'''
Write a python Program for generating fibonacci series till n using recursion.
'''
n=int(input("Enter the number of terms: "))
def fibonacci(n):
    # Base cases
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    # Recursive step
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Generate Fibonacci series
print("Fibonacci Sequence:")
for i in range(n):
    print(fibonacci(i), end=" ")