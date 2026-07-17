#problem : 23 "dictionary basics"

#Create a function that accepts a dictionary containing student names and marks.
students = {
    "Ravi": 85,
    "Anu": 92,
    "Kiran": 78,
    "Raj": 90
}
#QUESTIONS:
#Print all student names.
#Print all marks.
#Print each student with marks.
#Find the topper.
#Find the average marks.
#If "Ajay" is not present, add "Ajay":95.
#Return the updated dictionary.

print(students.keys())
print(students.values())
print(students)
topper = "" 
highest = 0
for name in students : 
    if students[name] > highest:
        highest = students[name]
        topper = name
print("Topper:", topper)
print("Marks:", highest)

total = sum(students.values())
average = total / len(students)
print("Average marks:", average)

if "Ajay" not in students:
    students["Ajay"] = 95

print("Updated dictionary:", students)
