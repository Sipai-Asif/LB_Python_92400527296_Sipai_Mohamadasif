'''Write a program to read any text file line by line '''



file = open("names.txt", "r")

for line in file:
    print(line)

file.close()