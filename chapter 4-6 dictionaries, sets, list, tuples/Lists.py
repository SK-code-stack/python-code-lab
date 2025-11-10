a = ['salman', 'umer', 12, 23.221, True, False]
b = [1,2,432,4,3,2,34,5,6,23,6,63,23,4]
c = ['salman', 'ali', 'zohaib']

print(a[1:3])

# list methods
a.append("ali") # this will add a value to the end of the list
b.sort() # this will sort the list if we have strings only then it starts from a to z
b.reverse() # this will reverse your list starting from the last index to the first index
a.insert(1, "TS") # this will insert an elemet to the list but here we can also define the index where we wanna insert the new value (First the index then the value)
b.pop(-1) # this will pop (take it out) the given index from the list
b.remove(432) # this will delete the given value from the list

print(a)
print(b)