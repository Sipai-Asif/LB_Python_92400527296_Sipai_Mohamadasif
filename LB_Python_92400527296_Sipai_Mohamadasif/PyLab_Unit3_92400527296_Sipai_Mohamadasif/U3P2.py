#Write a program to input a number and display whether number is prime or not.

# Input number
num = int(input("Enter a number: "))

# Check prime
if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print("Not a Prime Number")
            break
    else:
        print("Prime Number")
else:
    print("Not a Prime Number")