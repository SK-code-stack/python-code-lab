# make a copy of file 

with open("problem6_txt.txt") as file:
    content = file.read()
with open("problem6_txt_copy.txt", 'w') as file:
    file.write(content)

