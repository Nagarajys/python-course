#BASIC FUNCTIONS--PARTA - 2
#Q6:
def multiply(a,b):
    return a*b

first = multiply(10,5)
second  = multiply(7,8)

print(first)
print(second)


#Q7 :
def average(a,b,c):
    return (a+b+c)/3

result = average(10,20,30)
print(result)

#Q8:
def cube(num):
    return num**3

first = cube(2)
second = cube(3)
total = first + second
print(total)

'''Why store the returned value in variables?

"Storing the returned value in variables makes the code more readable 
and allows us to reuse the values later without calling the 
function again. If we only need the value once, we can directly use 
the function call inside print()."'''

#Q9:
def doubled(num):
    return(num*2)

a = doubled(10)
b = doubled(a)
print(b)


#Q10:
def square(num):
    return(num**2)
def cubes(num):
    return(num*num*num)


a = square(4)
b = cubes(2)
print(a+b)