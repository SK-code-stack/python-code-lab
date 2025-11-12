# create  clas pet from animal and then create dog form pet and add bark method to dog class

class Animal:
    sound = "bow bow"
    def __init__(self, sound):
        self.sound = sound

class Pet(Animal):
    def __init__(self):
        pass

class Dog(Pet):
    # @staticmethod
    def bark(self):
        print(self.sound)

class Cat(Pet):
    @staticmethod # here i dont need any self argument 
    def sound():
        print("meaow meaow")


d = Dog()
d.bark()

c = Cat()
c.sound()