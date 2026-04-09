'''Write a program to read names from keyboard and store into text 
file'''


file = open("names.txt", "w")

n = int(input("How many names you want to enter: "))

for i in range(n):
    name = input("Enter name: ")
    file.write(name + "\n")

file.close()

print("Names successfully stored in file.")