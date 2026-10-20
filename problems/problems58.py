# FUNCTION BASICS - PART C : (3) - *kwargs(**details)
#Q1:
def show_details(**details):
    for key,value in details.items():
        print(key,value)
        
show_details(name = "raja", college = "ksit", age = 19)

#Q2:**kwargs + Loop
def show(**details):
    for key , value in details.items():
        print(key,value)
        
show(name = "nagaraj", age = 98 , branch = "AIML")

#Q3:*args + **kwargs Together
def show_data(*args , **kwargs):
    print("positional:",args)
    print("keyword:",kwargs)
show_data(10,20,30,40,name = "nagaraj",age = 25)

#Q4:— **kwargs + if
def check_student(**details):
    marks = details["marks"]#details["marks"] → dictionary alli marks key-ge iruva value (85) tegedukollutte.
    if marks >=35:
        print("pass")
    else:
        print("fail")
        
check_student(name="nagaraj", age = 19, marks = 98)

#Q5:**kwargs + Return
def get_marks(**details):
    marks = details["marks"]
    if marks >=35:
        return "pass"
    else:
        return "fail"
    
result = get_marks(name = "nagaraj", marks = 56)
print(result)