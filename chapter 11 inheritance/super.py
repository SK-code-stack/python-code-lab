# In inheritance if we have constructor in all classes and we want to get this constructor in our child class as well then we use super().__init__() this keyword. This will make the super constructor so that we can use it in child class otherwise we can not even access one construcor in its own class 

#PARENT CLASS
class Employee:
    def __init__(self):
        print("this is from employee class")

    name = "salman"

class Programmer(Employee): 
    def __init__(self):
        print("this is from prgrammer class")

    post = "ML Engineer"

#PARENT CLASS
class Language(Programmer):
    def __init__(self):
        super().__init__()
        print("this is from language class")

    language = "python"



# now we will create object of the last child class and call all parent attributes

o = Language()
print(o.name)
print(o.post)
print(o.language)
