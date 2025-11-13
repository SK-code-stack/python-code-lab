from functools import reduce

# map function -- this is used to map a function to all the elements of list
l = [1, 2, 3, 4, 5]

square = lambda x : x*x
# map (function , list)
sqList = map(square, l)
print(list(sqList))


# Filter example -- this will filter items from list 
# filter (function , list)
def even(n):
    if (n%2 == 0):
        return True
    return False

onlyEven = filter(even, l)
print(list(onlyEven))

#Reduce example -- this will perform function of index 0 and 1 and return an output .. then perform function on output and index 3 then its output and index 4 and so on
sum = lambda a,b : a+b
print(reduce(sum, l))