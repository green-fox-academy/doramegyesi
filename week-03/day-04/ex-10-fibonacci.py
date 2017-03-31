# Define a recursive fibonacci(n) method that returns the nth
# fibonacci number, with n=0 representing the start of the sequence.

def fibonacci(n):
    if n < 2:
        return n
    else:
        return (fibonacci(n-1) + fibonacci(n-2))

print(fibonacci(8))
print(fibonacci(17))
print(fibonacci(21))
