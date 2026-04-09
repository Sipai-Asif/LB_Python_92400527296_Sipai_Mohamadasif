#Write a program to input Principal Amount, Rate and Year and display Compound Interest

p = int(input("Enter Principal Amount: "))
r = int(input("Enter Rate of Interest: "))
n = int(input("Enter Time (in years): "))


amount = p * (1 + r / 100) ** n
ci = amount - p


print("Compound Interest =", ci)
