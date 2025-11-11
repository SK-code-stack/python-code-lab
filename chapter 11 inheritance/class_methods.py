# class methods allow us to use the value from the class even if we have an instance value below

class Employee:
    a = 1
    @classmethod # this is how we use class metod  and we use cls in stead of self
    def show(cls):
        print(f"The value of class attribute 'a' is {cls.a} ")

e = Employee()
e.a = 33
e.show()