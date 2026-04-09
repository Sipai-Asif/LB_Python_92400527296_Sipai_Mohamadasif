#Write a program to print factorial number using function.

# Function to calculate factorial
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact

# Input number
num = int(input("Enter a number: "))

# Check and print result
if num < 0:
    print("Factorial not defined for negative numbers")
else:
    print("Factorial =", factorial(num))