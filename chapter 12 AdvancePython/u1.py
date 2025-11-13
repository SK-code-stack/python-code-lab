# this is our one file which i am going to import in another file but here we have an issue. If i import this file in any other file then the whole file code will goes to the second file but i dont want to shear whole code 
# For this purpose we need __name__ 

def helo():
    print("hellow world")

helo()

if(__name__ == "__main__"):
    # this is the code that i dont want any other file to access by even importing this whole file 
    def hide():
        print("this is hiden info for any other file that will import this file")

    hide()
    print(__name__)