'''WAP to program to input age of person and display message as follow.
-if age <12 print you are kid
-if age between 12-17 print you are teenager
-if age beetween 18-60 print you are adult
-if age>60 print you are senior citizen'''

age=int(input("Enter your age: "))

if age<12:
    print("you are kid")

elif age in range(12,18):
    print("you are teenager")

elif age in range(18,61):
    print("you are adult")

elif age in range(61,126):
    print("you are senior citizen")

else:
    print("wrong data")
