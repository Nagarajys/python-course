#FUNCTION ADVANCWED - PART D (1)- LAMBDA FUNCTION PRACTICE
# LAMBDA SYNTAX - lambda parameters: expression
#Lambda internally expression-na result return madutte.(RETURN NOT REQUIRED)
double = lambda x : x*8
print(double(20))

# LAMBDA WITH ONE PARAMETER:
para  =  lambda x: x*x
print(para(7))

#lambda with 2 parameters:
add = lambda a,b : a+b
print(add(2,9))

#lambda with 3 parameters:
addi = lambda a,b,c : a+b-c
print(addi(10,20,10))

# lambda can have a condition:
check = lambda x : "even " if x % 2 ==0 else "odd"
print(check(45))

# lambda +if:
greater  =  lambda a, b : a if a>b else b
print(greater(10,5))

# Lambda + map()
numbers  = [4,8,10,12,14]
result = list(map(lambda num:num *2,numbers))
print(result)

#lambda + map() map() means:
"Ee function-na every element mele apply madu."
numbers = (4,6,8,10)
result = tuple(map(lambda num : num * 2 , numbers))
print(result)

#lambda filter():filter() meaning:
"Condition satisfy madro elements matra keep madu."
numbers = [10, 15, 20, 23, 30]
result  = list(filter(lambda num: num % 2==0 , numbers))
print(result)
#map = MODIFY
#filter = SELECT

#Lambda + sorting:
students=[("naga",98),
        ("ravi",56),
        ("raki",87) 
]
students.sort(key =  lambda student: student[0],)
print(students)