# to create an empty dictionary we use 
d = {}

marks = {
    "Salman":90,
    "TS":95,
    "Ali":40,
}

print(marks)
print(marks['Salman']) # use key to print its crossponding value
print(marks.keys()) # use to print all keys
print(marks.values()) # use to print all values
marks.update({"Ali":20, "khan":33}) # use to update existing value or you can add new value in it as well
print(marks)

print(marks.get("rohan")) # this will return none if key is not present in dictionary
print(marks["rohan"]) # this will return error if key is not present in dictionary