# Read a file and print only the unique words in sorted order.

with open("unique.txt") as file:
    content = file.read()

words = content.lower().split()

# set() it will remove duplicate words from a list
unique = set(words)

sotredWords = sorted(unique)

for w in sotredWords:
    print(w)