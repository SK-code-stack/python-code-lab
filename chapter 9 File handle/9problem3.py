# write a program to generate tables from 2 - 20 and write each table in different file and store in a seperate folder

# function to write tables by taking peramiter

import os
os.makedirs("Tables", exist_ok=True)

def table(n):
    output = ""
    count = 1
    while count <= 10:
        output += str((f"{n} X {count} = {n*count} \n"))
        count += 1
    return output


# loopint table from 2 to 20
for i in range(2, 21):
    with open(f"Tables/{i}-table.txt", "w") as file:
        file.write(table(i))

