'''Write a program to compute the frequency of the words from the 
input. The output should output after sorting the key 
alphanumerically. 
Suppose the following input is supplied to the program: 
“Hello There this is Python. Python is good” 
Then output shall be as follows : 
Hello : 1 
There : 1 
This : 1 
is : 2 
Python : 2 
Good : 1 '''



text = input("Enter a sentence: ")

words = text.split()

freq = {}

for word in words:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1

for key in sorted(freq):
    print(key, ":", freq[key])