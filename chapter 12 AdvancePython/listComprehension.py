# if we want to create a new list based on some list then we do that 

l = [2,3,5,6,3,44,1]

squareList = []
for i in l:
    squareList.append(i*i)
print(squareList)

# but this can be done in easy and short way 
print("---------------------------------------------------------------------")
squareList = [i*i for i in l] # what we want to do for i in the list name   
print(squareList)