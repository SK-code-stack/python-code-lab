# create class employee and add salary and increment properties in it

class Employee:
    salary = 234
    increment = 20

    @property
    def salaryAfterIncrement(self):
        return (self.salary + self.salary *(self.increment/100))
    
    @salaryAfterIncrement.setter
    def salaryAfterIncremant(self, salary):
        self.increment = ((salary/self.salary) -1)*100

e = Employee()

e.salaryAfterIncremant = 280.8
print(e.increment)    