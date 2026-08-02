#If Else inside comprehension
marks= [30,35,25,99,100,44,66,88,43]
result= ["pass" if marks>=35 else "fail" for marks in marks]
print(result)

#Nested List Comprehension
matrix= [[1,4],[3,9],[6,8]]
numbers = {j for i in matrix for j in i}# i is entire row and j is each element in that row
print(numbers)

# dict comphresension
square= {i:i**2 for i in range(1,21)}
print(square)

names= ["nagaraj","vikas","rahul"]
uppercase = [name.upper() for name in names]# upper() used to caps big letters
print(uppercase)
# or...
uppercase = [name.upper() for name in["nagaraj","vikas","rahul"]]
print(uppercase)

# length
names= ["nagaraj","vikas","rahul"]
l2 = {name:len(name) for name in names}
print(l2)

#Interview Questions
# Q1

numbers = [1,4,6,8,0,9,25,12,13]
numsq = {num**2 for num in numbers if num%2 == 1}
print(numsq)

# Q2
names = ["adb","viki","naga","abi","bro"]
len= {name:len(name) for name in names}
print(len)

# Q3
num = [ 10,20, 30, 40]
n2 = {num//10 for num in num}
print(n2)

'''Biggest Difference Table
Normal FOR LOOP	  FOR + LIST	  LIST COMPREHENSION	  FOR + DICTIONARY	        DICTIONARY COMPREHENSION
Print madutte	  List build  List build madutte (short   Dictionary build madutte	Dictionary build madutte (short)
print()          useappend() use	append() beda	     dict[key]=value                       One line'''

# Q4 lc
S1 = [2,6, 8 ,7,9,5,4,3,]
Square= {num ** 2 for num in S1}
print(Square)

# OR
square = {num **2 for num in range(1,11)}
print(square)

#Q5 dc
square = {num:num **2 for num in range(1,6 )}
print(square)