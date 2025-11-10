# code to get marks of 5 student and store it in the list in assending order
a = []

for i in range(3):
    b = int(input(f"Enter the value {i+1} : "))
    a.append(b)
a.sort()
print(a)