# A simple calculator with python

print("Select 1 to Add")
print("Select 2 to Substract")
print("Select 3 to Multiply")
print("Select 4 to Divide")
print("Select 5 to check even number")

selection = input()

if selection == "1":
    val_1 = input("Enter first value: ")
    val_2 = input("Enter second value: ")
    print("Operation is " + str(int(val_1) + int(val_2)))  
elif selection == "2":
    val_1 = input("Enter first value: ")
    val_2 = input("Enter second value: ")
    print("Operation is " + str(int(val_1) - int(val_2))) 
elif selection == "3":
    val_1 = input("Enter first value: ")
    val_2 = input("Enter second value: ")
    print("Operation is " + str(int(val_1) * int(val_2))) 
elif selection == "4":
    val_1 = input("Enter first value: ")
    val_2 = input("Enter second value: ")
    print("Operation is " + str(int(val_1) / int(val_2))) 
elif selection == "5":
    value = input("Enter value: ")
    
    if int(value) % 2 == 0:
        print("True")
    else: print("False")
else: print("Invalid entry")
