# write a list comprehension to print a list which contain multiplication of table of user entered number  and store it in a file table.txt

n = int(input("Enter a number :"))
table = [n*i for i in range (1,11)]
print(table)

    

with open("table.txt", "a") as file:
    num=1
    for i in table:
        file.write(f"{n} x {num} = {i} \n")
        n += 1
    file.write("---------------------------------------------\n")
    