class Number:
    def __init__(self, n):
        self.n = n
    
    def __add__(self, number):
        return self.n + number.n
    
    def __sub__(self, number):
        return self.n - number.n
    

n = Number(2)
m = Number(24)

print(n-m)


# __ the methods starts and ends with double underscore are called dunder methods

# def __add__(self, number):  p1 + p2
# def __sub__(self, number):  p1 - p2
# def __mul__(self, number):  p1 * p2
# def __truediv__(self, number):  p1 / p2
# def __floordiv__(self, number): p1 / p2
