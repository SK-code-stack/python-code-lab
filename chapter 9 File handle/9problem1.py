# program to read a file and check that wheather it have word (salman) or not 

with open("file.txt") as file:
    data = file.read()
    print(data)
    if "salman" in data.lower():
        print("its preset")
    else:
        print("its not preset")
