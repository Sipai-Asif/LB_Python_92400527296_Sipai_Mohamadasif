#Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 to 3000(both included).

# Numbers divisible by 7 but not multiple of 5 (2000 to 3000)

for i in range(2000, 3001):
    if i % 7 == 0 and i % 5 != 0:
        print(i)