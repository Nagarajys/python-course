#Q2:Nested Function Calls (3 Levels)
def add(a,b):
    return a+b
def square(num):
    return num * num 
def subtractt(num):
    return num -10
def dis():
    result = subtractt(square(add(8,2)))
    print(result)
    

