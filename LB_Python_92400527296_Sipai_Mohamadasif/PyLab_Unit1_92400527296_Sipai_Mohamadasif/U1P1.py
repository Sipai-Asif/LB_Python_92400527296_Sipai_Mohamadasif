#write a simple pytthon program to input two variables an print addition, subtraction, multiplication and division of both numbers. 

# Input two numbers
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

# Operations
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)

# Check division by zero
if b != 0:
    print("Division:", a / b)
else:
    print("Division: Cannot divide by zero")