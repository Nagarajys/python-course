# FUNCTION BASICS - PART B: (1)
#Q1:
#Function Returning a Value to Another Function
def subtract(a,b):
    return a-b
def triple(num):
    return num *3
def display():
    result = triple(subtract(20,5))
    print(result)
display()

#Q2:Nested Function Calls (3 Levels)
def add(a, b):
    return a + b

def square(num):
    return num * num

def subtractt(num):
    return num - 10

result = subtractt(square(add(8, 2)))

print(result) #return immediately ends the function.


# Q3:Nested Function Calls (4 Levels)
def addd(a,b):
    return a+b
def multi(num):
    return num *2
def squa(num):
    return num **2
def subt(num):
    return num -5
result = subt(squa(multi(addd(5,5))))    
print(result)

#Q4:Variable Scope + Return + Parameters
x = 100

def calculate(x):
    x = x + 10
    return x

result = calculate(20)

print(result)
print(x)

#Q5:mixes scope + return + function calls.
def increase(num):
    num = num +5
    return num
def show():
    value = 50
    new_value = increase(value)
    print(new_value)
    print(value)
show()
