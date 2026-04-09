#Write a program to input a number and display factorial of that number. for ex., factorial of 5 = 5*4*3*2*1 = 120.

# Input number
num = int(input("Enter a number: "))

fact = 1

# Check for negative number
if num < 0:
    print("Factorial not defined for negative numbers")
else:
    for i in range(1, num + 1):
        fact = fact * i
    print("Factorial =", fact)