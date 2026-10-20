# FUNCTION BASICS - PART C : (4) - *kwargs(**details)
#Q1:
def calculate_total(*prices,**discount):
    total = 0
    for price in prices:
        total = total + price
        discount["discount"]
    final = total - discount["discount"]
    return final

result = calculate_total(100, 200, 300, discount=50)
print(result)

#Q2:*args + **kwargs + Return
def process_numbers(*numbers, **options):
    total = 0
    operation = options["operation"]
    for num in numbers:
        total += num
    if operation == "double":
        return [num * 2 for num in numbers]
    return total
result = process_numbers(10,20,30, operation = "double")
print(result)
    #or
def process_numberss(*numbers, **options):
    operation = options["operation"]

    if operation == "double":
        return [num * 2 for num in numbers]

    return numbers
result = process_numberss(10,20,30, operation = "double")
print(result)

#Q3:
def new(*numbers, **options):
    total = 0 
    opertion  = options["opertion"]
    for num in numbers:
        total = total +num
    if opertion == "sum":
        return sum(numbers)
    elif opertion =="max":
        return max(numbers)
    return numbers
result = new(10, 20, 30, opertion="sum")
print(result)
#or
def calculate(*numbers, **options):
    total = 0
    operation = options["operation"]

    for num in numbers:
        total = total + num

    if operation == "sum":
        return total

    elif operation == "max":
        largest = numbers[0]

        for num in numbers:
            if num > largest:
                largest = num

        return largest

result = calculate(10, 20, 30, operation="max")
print(result)

#Q4:
def process_marks(*marks,**choice):
    total = 0
    operation = choice["operation"]
    for mark in marks:
        total = total + mark
    if operation =="average":
        total= total/len(marks)
        return total
    
    elif operation =="pass_count":
        count = 0
        for mark in marks:
             if mark>=35:
               count = count+1
        return count
    elif operation=="highest":
            highest = marks[0]
            
            for mark in marks:
                 if mark>highest: 
                     highest = mark
            return highest

result = process_marks(40, 25, 80, 35, 90, operation="pass_count")
print(result)

#Q5:
def student_analysis(*marks, **options):
    total = 0
    operation = options["operation"]

    for mark in marks:
        total = total + mark

    average = total / len(marks)

    count = 0
    for mark in marks:
        if mark >= 35:
            count = count + 1

    highest = marks[0]
    for mark in marks:
        if mark > highest:
            highest = mark

    if operation == "result":
        return {
            "total": total,
            "average": average,
            "pass_count": count,
            "highest": highest
        }


result = student_analysis(
    40, 25, 80, 35, 90,
    operation="result"
)

print(result)
                
        
        


    