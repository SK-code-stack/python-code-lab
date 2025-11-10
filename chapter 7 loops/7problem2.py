# greet those users whose names starts with s
names = ["Salman", "sohail", "ali"]

for i in names:
    if ((i.startswith("S")) or (i.startswith("s"))):
        print(f"hello {i}")
    