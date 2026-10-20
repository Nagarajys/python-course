#PART D — LAMBDA FUNCTIONS
#1. Lambda basics:
square  =  lambda x : x*x
print(square(10))

#2:sum
square  =  lambda x,y : x+y
print(square(20,30))

#3.:— Lambda + Condition
check = lambda z: "even" if z%2==0  else "odd"
print(check(24))

#4:Lambda Stored & Reused
cube  = lambda x: x**3
print(cube(3))
print(cube(5))
#or:
cube  = lambda x: x**3
first = cube(3)
second  =cube(5)
print(first)
print(second)

#5:Lambda + map()
numbers =  [2,4,6,8,10]
double =  list(map(lambda num : num * 2, numbers))
print(double)

#6:Lambda + filter()
numbers = [10, 15, 20, 23, 30, 41, 50]
result =  list(filter(lambda num : num% 2 == 0 , numbers))
print(result)

#7:— Lambda + map() + Condition
numbers = [10, 15, 20, 25, 30]
result = list(map(lambda num : num*2 if num %2 ==0 else num * 3, numbers))
print(result)

#8:Lambda + Sorting
students = [
    #0th ind    1th ind
    ("Nagaraj", 85),
    ("Ravi", 72),
    ("Kiran", 95),
    ("Chandan", 68)
]
students.sort(key = lambda student:student[1],reverse = True)
print(students)

#9:Lambda + Real-World Problem
salaries = [25000, 32000, 45000, 28000, 50000]
updated_salary = list(map(lambda salary: salary+5000, salaries))
print(updated_salary)

#10:FINAL LAMBDA INTERVIEW QUESTION
students = [
    ("Nagaraj", 85),
    ("Ravi", 32),
    ("Kiran", 91),
    ("Chandan", 28),
    ("Arjun", 76)
]
result = list(map(lambda student: student[0], filter(lambda student: student[1] > 35, students)))
print(result)