# FUNCTION BASICS - PART C : (2)
#Q6:Using *args with calculations
def find_max(*numbers):
    largest = max(numbers)
    return largest
result = find_max(10, 45, 23, 67, 12)
print(result)
#or
def find_maxx(*numbers):
    largest = numbers[0]
    
    for num in numbers:
        if num>largest:
          largest = num
          
    return largest
result = find_maxx(10,45,67,230,185)
print(result)

#Q7:— *args + Loop
def calculate(*numbers):
    total = 0
    for num in numbers:
        total = total +num
        
    return total
result = calculate(10,20,30,40)
print(result)

#Q8: *args + if
def count_even(*numbers):
    count = 0 
    for num in numbers:
        if num%2==0:
         count = count+1
    return count 
result  = count_even(10, 15, 20, 23, 30, 41)
print(result)

#Q9:*args + Function + Return   Collect → *args
#                               Unpack → *numbers
def calculate_sum(*numbers):
    total = 0 
    for num in numbers:
        total = total+num
    return total
def calculate_average(*numbers):
    
      total= calculate_sum(*numbers)
      average = total/len(numbers)
      return average
result = calculate_average(10, 20, 30, 40)
print(result)

#Q10:: *args + Return + Function Calling
def multiply_all(*numbers):
    result = 1
    for num in numbers:
        result = result*num
    return result
def cal():
    answer = multiply_all(2,3,4) 
    final_answer = answer +10 
    return  final_answer
result = cal()
print(result)

   
    
        