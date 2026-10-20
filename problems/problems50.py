#BASIC FUNCTIONS--PARTA - (1)
# Q1:

def welcome():
    print("welcome to python")
    
welcome()
welcome()
welcome()

 # Q2:
def greet(name):
    print("hello", name)
    
greet("nagaraj")
greet("python king")
greet("amazon")

#Q3

def add(a,b):
    print(a+b)
    
add(10,20)
add(50,100)
add(7,8)
    
#Q4
def introduce(name,college):
    print("my name is",name )
    print("I study at", college)
    
introduce("nagaraj","ksit")
introduce("rahulla","sit")

# Q5 
def square(num):
     return (num*num)
 
square(5)
result = square(5)
print(result)
#return Sends the value back to the place where the function was called.
'''print() displays the result on the screen, whereas return sends the result back to the caller so it
can be stored in a variable, reused, or passed to another function.'''
    
def test():
    return 100

x = test()

print(x)

'''NOTE :Function Call
        ↓
Parameter receives value
        ↓
Calculation
        ↓
Return sends value back
        ↓
Variable stores value
        ↓
Print (if needed)'''

