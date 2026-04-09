'''Write a program which accepts a sequence of comma-separated 
numbers from console and generate a list and a tuple which 
contains every number.'''


values = input("Enter comma-separated numbers: ")

num_list = values.split(",")
num_tuple = tuple(num_list)

print("List:", num_list)
print("Tuple:", num_tuple)