# read lines is a buit in function it read a file line by line and store it in a list
# readline (it will read one line and if you want to read n lines then you have to run it n time)
# readlines (it will store all lines as a list)

with open("file.txt") as file:
    data = file.readlines()
    print(data)
    data.pop(1)
    print(data)

    #readline function using while loop
    
    # data = file.readline()
    # while data != "":
    #     print(data)
    #     data = file.readline()
    file.close()

