# sum first n natural numbers using while loop
user = int(input("Enter a number : "))

i = 0
sum = 0
while (i<=user):
    sum += i
    i += 1

print(sum)