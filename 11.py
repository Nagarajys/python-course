# LISTS AND DICTIONARIES WITH FOR LOOPS, LIST COMPREHENSION AND DICTIONARY COMPREHENSION
# looping through lists
 
list = [33,56,34,87,99]
total = 0
for num in list:
    total = total+num
print(total)


list = [33,56,34,87,99]
doubled = []
for num in list : # kali list gay ero list na double madi add madu anta 
    doubled.append(num*2)
print(doubled)

# looping through dictionaries
student_marks = {"nagaraj" : 1, "vikas" : 96, "rahul" : 98}
for student, marks in student_marks.items():
    print(f"{student}-{marks}") # student and marks print madu anta
    
# for loop with range()
students = ["nagaraj", "vikas", "rahul"]
marks = [1, 56, 98]
student_marks = {}
for index,student in enumerate(students):# enumerate means idex jote item na count madi print madu anta
    student_marks[student]= marks[index]
    # student marks olgade student na thafgo aa student gay aa student index alli ero marks na print madu anta
print(student_marks)

# list comprehension(short way)
# syntax: [expression for item in list if condition]
list =[37,56,34,23,67,345]
doubled= [num*2 for num in list] # doubled list na short way alli print madu anta
print(doubled)

# another type of list comprehension
list= [num for num in range(1,101)]
print(list)
doubled = [num**2 for num in list]
print(doubled)

# list comph - only even numbers
list= [num for num in range(1,101)]
print(list)
doubled = [num*2 for num in list if num%2 == 0]
print(doubled)

# list comph - only odd numbers
list= [num for num in range(1,101)]
print(list)
doubled = [num**2 for num in list if num%2 == 1]
print(doubled)

list=["naga","raja","winee"]
dict= [num[2] for num in list]
print(dict)


# dictionary compherhension
city_population = {
    "banglore": 100,
    "mysore": 67,
    "mangalore": 45,
    "udupi": 23
}
big_city = {key:value for key,value in city_population.items() if value >50}
print(big_city)
# city population anno dictionary li ero prathi ondhu city , population gu
# enondh list alli city:population na print madu anta if condition correct

# STRING SPLITTING INTO LIST
s = "i will crack microsoft"
l= s.split() # split function used to split string into list
print(l)



print("list input practice")

l1 = input("enter a list of integers: ")
print(l1.split())

# anothor type of list input
x = input("enter a list of integers: ")
l1 = [int(x)for x in x.split()]
print(l1)




