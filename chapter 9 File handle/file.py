# file handelig 


with open("file.txt") as file:
    data = file.read()
    print(data)
    file.close()

with open("file.txt", "a") as file:
    file.write("\nI am learning python.")
    file.close()

with open("file.txt") as file:
    data = file.read()
    print(data)
    file.close()
