'''WAP to input marks 4 subjects and display total,percentage,result and grade.
if studnt is fail(<40)in any subject then result should be displayed as "FAIL"
and grade should be displayed as "with held**".'''

Name=input("Enter your Name:")
uni=input("Enter your uni name:")
sub1=int(input("Enter marks: "))
sub2=int(input("Enter marks: "))
sub3=int(input("Enter marks: "))
sub4=int(input("Enter marks: "))

total = sub1+sub2+sub3+sub4
per = total/4


if sub1-sub2-sub3-sub4 < 40:
    print("total is: ",total)
    print("percentage is: ",per)
    print("result is fail")
    print("grade is with held**")

elif per >=90:
    print("total is: ",total)
    print("percentage is: ",per)
    print("result is pass")
    print("grade is A+")

elif per in range(80,90):
     print("total is: ",total)
    print("percentage is: ",per)
    print("result is pass")
    print("grade is A")

elif per in range(70,80):
    print("total is: ",total)
    print("percentage is: ",per)
    print("result is pass")
    print("grade is B")

elif per in range(60,70):
     print("total is: ",total)
    print("percentage is: ",per)
    print("result is pass")
    print("grade is C")

elif per in range(50,60):
    print("total is: ",total)
    print("percentage is: ",per)
    print("result is pass")
    print("grade is D")

elif per in range(40,50):
     print("total is: ",total)
    print("percentage is: ",per)
    print("result is pass")
    print("grade is E")
