# TOPIC- FUNCTIONS BASICS..function in Python is a reusable block of organized code designed to perform a single, specific task. Instead of writing the same code repeatedly, you enclose it in a function, give it a name, and run (call) it whenever needed.

def marriage(boy,girl):#parameters Parameter = Function ಒಳಗೆ value receive ಮಾಡೋ Variable.
    print(f"boy is {boy}")
    print(f"girl is {girl}")
    print(f"{boy} married {girl}")
    
marriage("nagraj","nandini")# here we calling  , this is positional argument
# andre boy anno position alli nagaraj edhane nav run madtidvi adhe rithi girl kda

marriage( boy = "vikas" , girl="pooja")# key argument
''' function heng useful andre mate matte print mado neccesity ella just function call
madudre aythu'''


# example tables
def tables(num):# yav number tables beku anta hakoke
    for i in range(1,11):
        print(f"{num}x{i}= {num*i}")

tables(3)
tables(28)
tables(6789)

# deafalt parameter values: Parameter is a variable that receives a value when the function is called.
def loves(boy,girl="girl"):
    print(f"boy is {boy}")
    print(f"girl is {girl}")
    print(f"{boy} married {girl}")

'''parameters elli girl yaru anta gothilla so deafalt 
agi girl barli anta girl = " girl kododhu'''
loves("nagraj")


# return values from a function
'''A function can return a value from return keyword, 
which allows the output of function reused elsewhre'''
def func(num):
    return int(str(num)*5)

a = 10000
b = func(5)
c = a + b

print(c)

# local variables and global variables
'''Local variables exist only within the specific function or code block
where they are declared, whereas global variables are declared outside of 
all functions and can be accessed from anywhere in the entire program'''
def variable():
    x = "raja" # local variable 
    print(x)
y = "viki"# global variable

print(y)

'''Function create ಮಾಡಿದಾಗ name ಗೆ value ಇರಲ್ಲ.

Function call ಆದಾಗ ಮಾತ್ರ value ಬರುತ್ತೆ.'''

def greet(name):
    print("hello", name)
    
greet("nagraj")
greet("ravi")
greet("arya")
greet("skibidi")
greet("deganth skibidi")

def square(num):
    print(num**2) # "Function call ಆದಾಗ ಈ statement execute ಮಾಡಬೇಕು."

square(5)
square(25)
''' Parameter ಯಾವಾಗಲೂ function definition ನಲ್ಲಿ ಇರುತ್ತೆ.
Parameter ಒಂದು variable.
Function call ಆದಾಗ value receive ಮಾಡುತ್ತೆ.
ಒಂದೇ Function ಅನ್ನು ಬೇರೆ ಬೇರೆ values ಜೊತೆ use ಮಾಡಬಹುದು.'''


#Argument is the actual value passed to a function during function call.
#NOTE:Parameter receives. Argument gives.


# LOCAL VARIABLE-
'''A local variable is a variable that is
created inside a function and can be used only inside that function.'''

def student():
    name = "Nagaraj"# LV
    print(name)

student()

def demo():
    x = 50
    print(x)
demo()

def studenta():
    name = "Nagaraj"

studenta()

#GLOBAL VARIABLES
''' A Global Variable is a variable that is created outside the 
function and can be accessed inside and outside the function'''

name = "nagaraj"
def hi():
    print(name)
    
hi()
print(name)


y= 2000
def vari():
    print(y)
vari()
print(y) # global variable runs both outside and insisde function


city = "banglore"
def love():
    print(city) 
love()
print(city)


'''If a variable is assigned anywhere inside a
function, Python treats that variable as LOCAL throughout the entire function.'''

#Local variable must receive a value before it is used.



