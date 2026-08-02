# TEST ON COMPHREHENSION
#q1
new_list = []
numbers = [2, 4, 6, 8, 10]
for num in numbers:
    new_list.append(num//2)
print(new_list)

#Q2. List Comprehension + if

numbers = [5, 10, 15, 20, 25, 30]
new_list = [num for num in numbers if num%10 == 0 ]
print(new_list)

#Q3. Dictionary Comprehension

names = ["Ram", "Sita", "Krishna", "Arjun"]
n2 = {name:len(name) for name in names}
print(n2)

#Q4. Convert Normal Loop → List Comprehension
result = [i+100 for i in range(1,6 )]
print(result)

#Q5. Convert Normal Loop → Dictionary Comprehension
square = {i:i**2 for i in range(1,6)}
print(square)
    
    
#if num % 10 == 0 ✔ Correct (checking divisible by 10) 
# remainder 0 bandre divisible by 10 anta

# q1
list = [num for num in range(1,21) if num%2 ==0]
print(list)

#q2
list = [num for num in range(1,21) if num%2 ==1]
print(list)

#q3
numbers = [5, 10, 15, 20, 25, 30]
list = [num for num in numbers if num>=15]
print(list)

#q4
numbers = [2, 3, 4, 5, 6]
list = [num**2 for num in numbers]
print(list)

#q5
words = ["apple", "hi", "banana", "cat", "elephant"]
w2 = [word for word in words if len(word)>3]
print(w2)

#q6
dict = {num:"even" if num%2 == 0 else "odd" for num in range(1,11)}
print(dict)

#q7
names = ["Ram", "Sita", "Krishna", "Arjun"]
dict = {name for name in names if len(name)>4}
print(dict)

#q8
numbers = [10, 15, 20, 25, 30]
dict={num**2 for num in numbers if num % 10 ==0}
print(dict)

#q9
marks = [28, 45, 33, 90, 60]
list = ["pass" if mark>=35 else "fail" for mark in marks]
print(list)

#q10
numbers = [1, 2, 3, 4, 5, 6]
list = [num*10 if num%2 == 0 else num*100 for num in numbers]
print(list)
