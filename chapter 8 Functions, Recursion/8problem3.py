# recursive function to calculate the sum of n natural numbers 

def sum(n):
    if n==0:
        return 0
    return sum(n-1) 

print(sum(3))