# program that take marks of students using loop and then store it in a list that have dictionaries in it containing name and marks of each student. Then create a txt file and store data in it. Then read it and tell whose marks is higest


data = []
# adding data into the data variable 
for i in range(1, 3):
    studentName = input("Enter name of student : ")
    studentMarks = input("Enter marks : ")
    studentInfo = {"Name":studentName, "Marks":studentMarks}
    data.append(studentInfo)


#looping through data variable
with open("studentInfo.txt", "w") as file:
    file.write("Names -- Marks\n")
    for student in data:
        file.write(f"{student['Name']} -- {student['Marks']}\n")
# Finding the highest marks in the list data
highestMarks = max(data, key=lambda x: x["Marks"])
toper = max(data, key=lambda x: x["Name"])
print(f"The highest mrks are {highestMarks["Marks"]} of {toper["Name"]}")
