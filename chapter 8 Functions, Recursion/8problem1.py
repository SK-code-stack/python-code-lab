# function to find the greatest number 

def greater(a, b, c):
    if (a > (b and c)):
        print("a is greater")
        
    if (b > (a and c)):
        print("b is greater")
    if (c > (b and a)):
        print("c is greater")

greater(1, 3, 4)