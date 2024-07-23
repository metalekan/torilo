from main import home
# from main import *
# import main   # different ways to import in python

def dothis():
    a = int (input("Enter a number:"))
    b = int (input("Enter a number:"))
    # c = main.home(a, b)
    c = home(a, b)
    
    return c

solution = dothis()
print(solution)