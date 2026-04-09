a=int(input("Enter number:"))
b=int(input("Enter number:"))

even = 0
odd = 0

for n in range(a,b+1):
    if n%2==0:
        even+=n
        print("even-",n)
    else:
       odd+=n
       print("odd-",n)
      

print("Even sum:", even)
print("Odd sum:", odd)







