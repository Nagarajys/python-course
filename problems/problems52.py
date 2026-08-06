#BASIC FUNCTIONS--PARTA - 3
# here one func call other function
#Q11:
def adds(a,b):
    return(a+b)
def displays():
    result = adds(15, 25)
    print(result)
displays()

#Q12:
#Function Calling Another Function + Return Value Reuse
def multiply(a,b):
    return(a*b)
def calculate():
    answer = multiply(5,6)
    print(" The answer is",answer)
    
calculate()
'''We use two functions because each function has 
a separate responsibility. multiply() only performs the calculation and 
returns the result. 
calculate() calls the function, stores 
the returned value, and displays the output.
This makes the code reusable, organized, and easier to maintain.'''

# Q13:
def addi(a,b):
    return a+b
    # square should accept a number and return its square
def square(num):
    return num * num

result = square(addi(10, 5))
print(result)

#Q14:
#One Function Calling Another Function (Chain of Functions)
def add(a,b):
    return(a+b)

def double(num):
    return(num * 2)

def display():
    result = double(add(10,5))
    print(result)
display()

#Q15:
def add(a, b):
    return a + b

def multiply(num):
    return num * 3

def square(num):
    return num * num

result = square(multiply(add(5, 5)))

print(result)
