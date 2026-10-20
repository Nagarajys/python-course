# FUNCTION BASICS - PART C : (1)
#Q1 - Default Parameters
def greet(name , message = "welcome"):
    print(name)
    print(message)
greet("nagaraj")
greet("nagaraj","good morning")

#Q2:keyword argument
def introduce(name, age, college):
    print("name = ", name)
    print("age = " , age)
    print("college= ", college)
    
introduce(age = 19 , name = "raja", college = "cambridege")

#Q3:Positional + Keyword Arguments
def student(name ,  age , college):
    print(name)
    print(age)
    print(college)
student("nagaraj", age = 19 , college = "ksit")

#student(name="nagaraj", 19, college="ksit") THIS IS -
'''Invalid,
Because once you use a keyword 
argument, you cannot put a positional argument after it.'''


#Q4:Concept: Default + Keyword Arguments
def order(item , quantity = 1, price = 100):
    total = price * quantity
    print(item)
    print(total)
order("laptop")
order("mouse",3)
order("keyboard", price = 500 , quantity = 2)

#Q5:*args *numbers means:
"Nanige est arguments kodtira kodri, ella values-na collect madko."
#*args = "How many positional arguments? Doesn't matter, collect all."

def add_numbers(*numbers):
    total = sum(numbers)
    print(total)
    return total

add_numbers(10,20)
add_numbers(5,10,15,20)
add_numbers(100,200,300)