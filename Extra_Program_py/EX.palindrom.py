#WAP to check wether number is palindrom or not.

string = input("Enter a string: ")

if string == string[::-1]:
    print(f"{string}' is palindrom.")
else:
    print(f"{string}' is not palindrom.")
