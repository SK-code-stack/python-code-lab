#PARENT CLASS
class Employee:
    name = "salman"

class Programmer(Employee): 
    post = "ML Engineer"

#PARENT CLASS
class Language(Programmer):
    language = "python"



# now we will create object of the last child class and call all parent attributes

o = Language()
print(o.name)
print(o.post)
print(o.language)
