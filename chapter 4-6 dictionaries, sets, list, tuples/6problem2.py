#spandetector in the comment from user 
a1 = "make a lot of money"
a2 = "buy now"
a3 = "click this"

user = input("Enter yout comment : ")
if((a1 in user) or (a2 in user) or (a3 in user)):
    print("this is spam comment")

else:
    print("all clear")