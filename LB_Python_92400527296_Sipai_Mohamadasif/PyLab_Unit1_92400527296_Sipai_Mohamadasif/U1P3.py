#Write a program to input Principal Amount, Rate and Year and display Simple Interest.


p = int(input("Enter Principal Amount: "))
r = int(input("Enter Rate of Interest: "))
n = int(input("Enter Time (in years): "))

si = (p * r * n) / 100


print("Simple Interest =", si)
