'''Write a program to create list in such a way that it should add 
square roots of number between 1 to n in the list... At the end, the 
list shall be displayed.  
Example : [1, 4, 9, 16, 25, ....]'''



n = int(input("Enter the value of n: "))

square_list = []

for i in range(1, n + 1):
    square = i * i
    square_list.append(square)

print("List of squares:", square_list)