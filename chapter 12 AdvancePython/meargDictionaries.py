# to mearge dictionaries 

a = {"salman":100}
b = {"khalid":90}
c = {"ali":87}
newDic = a | b | c
print(newDic)


# this is how you can open multiple files 
with (
    open("text.txt", "w") as f1,
    open("text2.txt", "w") as f2,
    open("text3.txt", "w") as f3
):
    f1.write("salman")
    f2.write("salman")
    f3.write("salman")