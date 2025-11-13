# create a table and then convert it in to a vertical string
table = [str(2*i) for i in range(1,11)]
s = "\n".join(table)
print(s)