#WAP to sum all the item in a list.

#l=[12,8,4,6,10]

list1 = list()
total=0

a=int(input("Total Numbers for sum : "))
for i in range(0,a):
    #print("a is ",a)
    val = int(input("value : " ))
    list1.append(val)
    
    total+=list1[i]

print(total)
print(list1)
