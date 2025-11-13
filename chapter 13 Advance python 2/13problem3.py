# list of numbers which are divisibe by 5
l = [1,2,3,4,5,6,7,8,9,10]

def div(n):
    if (n%5 == 0):
        return True
    return False

newl = filter(div, l)
print(list(newl))