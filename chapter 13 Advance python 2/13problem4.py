# find the greatest numbers of a list using reduce function
# create a sored list using reduce function
from functools import reduce
l = [11,2232,33,4,232,6,333,8,9,10,45,2,342,1,234,2]

def max(a, b):
    if (a<b):
        return a
    return b

slist = []

while l: # we dont use for loop here because for loop run and make increment on every itration it may skip some indexes But while loop in this condition runs until the list goes empty and we are removing element after adding it to new list which means every time the list gets shorten and the index starts from 0 every time unlike for loop 
    snum = reduce(max, l)
    slist.append(snum)
    l.remove(snum)

print(slist)
