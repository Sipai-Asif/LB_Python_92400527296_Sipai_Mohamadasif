#Write a program to print all numbers which are diviiable by 7 between 1 to 200.

# Print numbers divisible by 7 from 1 to 200

for i in range(1, 201):
    if i % 7 == 0:
        print(i)