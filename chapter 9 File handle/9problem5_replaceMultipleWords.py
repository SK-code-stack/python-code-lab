# a file contain a multiple words multiple times so write a code to replace it with ####


words = ["donkey", "cow"]
with open("problem4_txt.txt", "r") as file:
    content = file.read()

# using for loop to fetch and change words
for word in words:
    content = content.replace(word, "#"*len(word))

# write it back to file
with open("problem4_txt.txt", "w") as file:
    file.write(content.capitalize())