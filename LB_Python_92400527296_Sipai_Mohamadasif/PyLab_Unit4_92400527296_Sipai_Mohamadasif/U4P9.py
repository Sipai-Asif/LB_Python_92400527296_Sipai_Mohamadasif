'''Write a Python Program that creates a class with function 
overloading '''

class Calculator:

    def add(self, a=None, b=None, c=None):
        if a != None and b != None and c != None:
            print("Sum =", a + b + c)
        elif a != None and b != None:
            print("Sum =", a + b)
        else:
            print("Provide at least two numbers")

obj = Calculator()

obj.add(10, 20)
obj.add(10, 20, 30)