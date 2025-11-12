# property decorators 

class Employee:
    a = 1
    @classmethod # this is how we use class metod  and we use cls in stead of self
    def show(cls):
        print(f"The value of class attribute 'a' is {cls.a} ")

    @property
    def name(self):
        return f"{self.lname}"
    
    @name.setter
    def name(self, value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]




e = Employee()

e.name = "salman khan"
print(e.name)

e.a = 33
e.show()