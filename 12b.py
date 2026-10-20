#FUNCTIONS ADVANCED FUNCTIONS:
#1.  LAMBDA FUNCTIONS<<<> :a small, one-line anonymous function that you can create 
# without giving it a name.Instead of using the standard def keyword, writing a name,
# and using a return statement, you pack everything into a single line of code

add = lambda a,b : a+b #a+b only one expreesion

print(add(79,8))

double  = lambda z : 2*z

print(double(8000))

students = [
    {"name": "nagaraj", "marks": 94},
    {"name": "viki", "marks": 99},
    {"name": "russel", "marks": 100},
]

students.sort(key=lambda x: x["marks"], reverse=True)
print(students)

#RECURSION:
"""Recursion occurs when a function call itself.it
used to solve problems that can broken into smalller
and simpler """
def factorial(n):
    if n == 1:
         return 1
    return n * factorial(n-1)
print(factorial(4))

#NESTED FUNCTIONS 
''' nested function is a function defined inside other function,
accesable insiode only inside outer function , allowing more modular 
and controlled code execution''' 
def cal(a,b):
    def add():
        print(a+b)
    def sub():
        print(a-b)
    def multi():
        print(a*b)
        
    add()
    sub()
    multi()
cal(10,5)