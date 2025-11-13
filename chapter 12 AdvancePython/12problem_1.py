# open 3 files at a same time and if any of these file is not present then print a message without leaving the program 
try:
    with open("file1.txt", "r") as f1:
        print(f1.read())
except Exception as e:
    print(e)

try:
    with open("file2.txt", "r") as f2:
        print(f2.read())
except Exception as e:
    print(e)

try:
    with open("file3.txt", "r") as f3:
        print(f3.read())
except Exception as e:
    print(e)

    