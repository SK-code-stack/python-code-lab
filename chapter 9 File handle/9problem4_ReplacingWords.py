# a file contain a word multiple times so write a code to replace it with ####


word = "donkey"
with open("problem4_txt.txt", "r") as file:
    content = file.read()



contentNew = content.lower().replace("donkey", "####")
with open("problem4_txt.txt", "w") as file:
    file.write(contentNew)