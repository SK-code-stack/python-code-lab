# make a copy of file 

with open("problem6_txt.txt") as file:
    content1 = file.read()

with open("problem6_txt_copy.txt") as file:
    content2 = file.read()

if content1 == content2:
    print("therse are identical")
else:
    print("not identical")
