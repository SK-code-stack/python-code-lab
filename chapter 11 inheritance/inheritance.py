#PARENT CLASS
class Employee:
    name = "salman"
    id = "12221"
    def show(self):
        print(f"the name of employee is {self.name} and its id is {self.id}")
#PARENT CLASS
class Language:
    language = "python"
    def lang(self):
        print(self.language)
#CHILD CLASS
class Programmer(Employee, Language): # this is how we can use inheritance (single and multiple inheritance)
    def user(self):
        print(f"hlo  {self.name} are you learning {self.language}")




a = Programmer()
a.user()# this is from child class
a.show() # this is from parent class
a.lang() # this is from parent class

# Now we can call parent class functions as well without creating new instance or object 