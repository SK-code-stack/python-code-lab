#snake water gun game 
import random
print("Welcome to Sanke, Water, Gun game")


def game(a, b):
    if ((a=="snake" and b == "water")):
        print("you win --  b pick water")
    elif(a=="snake" and b == "gun"):
        print("you loose --  b pick gun")
    elif(a=="water" and b == "snake"):
        print("you loose --  b pick snake")
    elif(a=="water" and b == "gun"):
        print("you win --  b pick gun")
    elif(a=="gun" and b == "snake"):
        print("you win --  b pick snake")
    elif(a=="gun" and b == "water"):
        print("you loose --  b pick water")
    elif(a==b):
        print("tie -- b pick the same")
    else:
        print("enter valid choice")



a = input("Enter your choice snake, water, gun: ")
a.lower()
b = random.choice(["snake", "water", "gun"])

game(a,b)