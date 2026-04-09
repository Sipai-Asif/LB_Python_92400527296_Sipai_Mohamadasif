'''Write a program to read text file having number and display all 
numbers with total and average at the last. (Manually prepare a file 
having some numbers and then read it) '''

file = open("numbers.txt", "r")

total = 0
count = 0

for line in file:
    num = int(line)
    print(num)
    total = total + num
    count = count + 1

file.close()

average = total / count

print("Total =", total)
print("Average =", average)