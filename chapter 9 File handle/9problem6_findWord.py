# find word python is it present in long file 

word = "python"
found = False

with open("problem6txt.txt.txt", "r") as file:
    content=file.readlines()
    lineno = 1
    for line in content:
        if word in line:
            print(f"word python is present in line no {lineno} Content =  {line.capitalize()}")
        lineno += 1
    
if not found:
    print("word is not present")



