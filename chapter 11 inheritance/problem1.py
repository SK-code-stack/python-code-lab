# create class of name 2d vector and create another class that represent class of 3d vector
class TwoDVector:
    def __init__(self, i, j):
        self.i = i
        self.j = j

    def show(self):
        print(f"this vector is {self.i} and {self.j}")

class ThreeDVector(TwoDVector):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.k = k

    def show(self):
        print(f"this vector is {self.i} , {self.j} and {self.k}")

a = TwoDVector(1,2)
a.show()
b = ThreeDVector(1,2,3)
b.show()