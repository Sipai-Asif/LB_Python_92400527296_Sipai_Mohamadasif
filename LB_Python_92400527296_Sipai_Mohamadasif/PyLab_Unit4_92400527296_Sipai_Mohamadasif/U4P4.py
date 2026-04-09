'''Write a Python Program to create a function which accepts 3 
arguments. (2 numbers and one arithmetic operator). Display 
answer accordingly'''



def calculate(a, b, op):
    if op == '+':
        print("Result:", a + b)
    elif op == '-':
        print("Result:", a - b)
    elif op == '*':
        print("Result:", a * b)
    elif op == '/':
        print("Result:", a / b)
    else:
        print("Invalid Operator")


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")

calculate(num1, num2, operator)