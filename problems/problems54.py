# FUNCTION BASICS - PART B: (2)
#Q6:Updating a Value Using a Returned Value
def increase(num):
    num = num +10
    return num 
salary = 25000
salary = increase(salary)
print(salary)

# not storing here     
def increasee(num):      
    num = num + 10
    return num

salary = 25000

increasee(salary)

print(salary)

'''salary = 25000
increase(salary) → Python sends 25000 to num.
Inside the function:
num = 25010
return 25010
 But nobody receives the returned value.
Function ends. num is destroyed.
salary was never updated.'''

'''return does not automatically change a 
variable. It only 
sends a value back. We must store the returned value if we want to use it. '''


#Q7:Calling the Same Function Multiple Times
def bonus(salary):
    salary = salary +5000
    return salary
salary = 30000
update_salary = bonus(salary)
updated_salary = bonus(update_salary)
print(updated_salary)

#Q8:Function + Return + if Statement
def check_pass(mark):
    if mark>=35:
     return "pass"
    else:
        return "fail"
student_mark = 20
result = check_pass(student_mark)
print(result)

#Q9:Function + Return + if + Another Function
def check_age(age):
    if age>=18:
        return True
    else:
        return False
def show_result(age):
    check_age(age)
    result = check_age(18)
    if result is True:
        print("eligible for vote")
    else:
        print("not eligible for vote")
    
show_result(21)

#Q10:Function + Boolean Return + Reusing the Returned Value
def is_even(number):
    if number%2 == 0:
        return True
    else:
        return False
def display(number):
    result =is_even(number)
    if result is True:
        print("even number ")
    else:
        print("odd number")
display(24)
    