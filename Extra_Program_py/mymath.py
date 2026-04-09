''''1 Create a module named mymath.py that contains two functions:
    add(a, b) to return the sum of two numbers
    subtract(a, b) to return the difference.'''


def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

import mymath

print(mymath.add(5, 3))        # Output: 8
print(mymath.subtract(5, 3))   # Output: 2