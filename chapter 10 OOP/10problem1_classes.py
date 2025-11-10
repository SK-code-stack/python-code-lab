# creating calculator class to find square, cube and square root of a number 

class Calculator:
    def __init__(self, number):
        self.number = number

    # function to find square 
    def square(self):
        print(f"The square of {self.number} is --> {self.number*self.number}")
        
    # function to find cube
    def cube(self):
        print(f"The Cube of {self.number} is --> {self.number**3}")

    # function to find square root
    def squareroot(self):
        print(f"The Square root  of {self.number} is --> {self.number**1/2}")

    # static method it is used when we are not using self attribute (we dont want to use object attributes)
    @staticmethod
    def hello():
        print("hello")

num = int(input("Enter a number : "))

s = Calculator(num)
s.square()
s.cube()
s.squareroot()
s.hello()