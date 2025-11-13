a = int(input("Enter a number: "))
b = int(input("Enter second number: "))

if (b == 0):
    raise ZeroDivisionError("You can divide number with 0")
else:
    print(a/b)    
