#Write a program to input a number and display table of that number.

# Input number
num = int(input("Enter a number: "))

# Print table
for i in range(1, 11):
    print(num, "x", i, "=", num * i)