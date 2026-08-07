# FUNCTION BASICS - PART B: (3)
#Q11:# Using One Function's Return Value in Another Calculation


def add(a,b):
    return a+b
def multi(num):
    return num *5
def display():
    total = add(12,8)
    final_answer = multi(total)
    print(final_answer)
display()

#Q12:Reusing the Same Function Multiple Times
def square(num):
    return num *num
def calculateee():
    first = square(5)
    second = square(8)
    total = first+second
    print(total)
calculateee()
'''3. Why not write?
25 + 64
Because functions are reusable. 
Tomorrow if the numbers change to 10, 15, or 100, we don't have
to calculate the square manually.
We just call square() with the new value.'''

#Q13:One Function Calling Another Function
def double(num):
    return num *2
def calculatee(num):
    result = double(num)
    final_result = result+10
    return final_result
final_result = calculatee(15)
print(final_result)

#Q14:Combining Multiple Returned Values
def addd(a,b):
    return a+b
def subtract(a,b):
    return a-b
def calculate():
    sum_value = addd(20,10)
    diff_value = subtract(20,10)
    answer = sum_value +diff_value
    return answer
answer = calculate()
print(answer)

#Q15:Function Chaining (3 Functions)
def increment(num):
    return num +1
def doublee(num):
    return num *2
def cal():
    step1 = increment(9)
    step2 = doublee(step1)
    return step2
result = cal()
print(result)

   

    


    
    
