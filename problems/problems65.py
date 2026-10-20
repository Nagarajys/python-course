#SMALL REVISION FOR WORKSHOP:
#input practice:

student = {
    "name": "Nagaraj",
    "age": 18
}

print(student["name"])

name = input("enter your name please:")
print("hello", name, "welcome to cmr university workshop")




# condition practice:

gender = input("enter your gender:")

if gender =="female":
    print("free ksrtc bus ticket by gvt")
else:
    print("TICKET IS COMPULSARY")
    
    
#3.
age = int(input("enteryour age please:"))
if age >=60:
    print("senior citizen")
elif age<=10:
    print("child ticket")
else:
    print("adult")
    
#loop:
for i in range(1,10):
    if i == 7:
        break
    print(i)
    
    
#functions:
def greet(name,age):
    print("happy birthday", name , "you are succsesfuly completed age", age)
    
greet("nagaraj",18)

# lists:
expenses = [22,56,98,32,27,99,109]
total = 0
for num in expenses:
    if num%2 == 0:
        total = total +num
print("total of even sum:", total)

#dictionary:
list = []
student_details = {"name:","nagaraj",
                "age:", "19",
                "course:", "aiml",
                "college:", "cmr university"
}                           
list.append(student_details)
print(list)
