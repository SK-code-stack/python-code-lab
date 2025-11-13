# we use enumerate function in python when we need index and item at the same time in a loop this can be done by  terdictional method like that 
l = [1, 2, 432, 234,122, 23, 3]

index = 0
for item in l :
    print(f"the number at index {index} is {item}")
    index += 1

print("---------------Emurate----------------------------")

for index, item in enumerate(l):
    print(f"the number at index {index} is {item}")
