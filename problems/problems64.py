# revision practiice upto functions:

message = "hello , world!"
print(message.replace("world!", "raju"))

t  = "python  programming"
print(t[0:6])
print(t[7:])

print("hello\\world!") 



sen = "Hi  bro  my name   is   nagraj    I am  from banglore"
print(sen.upper())
print(sen.lower())
print(sen.replace(" " , "_"))




print("hello\n\tworld")


fruits = ["orange" , "apple" , "jackfruit"]
fruits.clear()
print(fruits)

num = [0,1,2,3,4,5,6]
print(num[0:7:3])

name = "india"
print(name[-4: -1])


list = [1,2,3,44,3,6]

list = tuple(set(list))
print(list)

food = {"banglore" : "mutton",
        "mysore " :"mysore pak",
        "manduya ": "muddhe"}

food.update({"bgs": "dilme"})
print(food)


i = 1
while i <= 20:
    if i % 2 == 1:
        print(i)
    i += 1
    


# countdown timer:
i = 11
while i >=1:
        print(i)
        i = i-1
print("hapy new year")


name = "karnataka raja"
for word in name:
        print(word)
        
        
i = 3
for j in range(1,31):
        print(f"{i}*{j} = {i*j}")
print()
        
        
cites = {"bengluru", "shimoga", "mysore", "mandya", "hubuli", "sampekatte"}
for index , city in enumerate(cites):
        print(f"city {index+1}: {city}")
        
        
ladus  = 5
friends = ["rahulla" ,  "nagaraja" ,   " vikasa" , "akasaha" ,  "karthika"]
for index ,friend in enumerate(friends):
        if ladus>0:
           print(f"{index+1}: {friend} gets a laddu huray!")
           ladus -=1
        else:
             print("ladus over")
        
        
 
# vowels
words = "karthikeya"
vowels = "aeiou"
for word in words:
        if word in vowels:
                print(word)


numbers = [10,20,30,40,50]
doubled = []
for num in numbers:
        doubled.append(num*2)
print(doubled)

students = ["rahulla", "nagaraja","vikasa","akasha","pinnu","russel"]
marks = [25,100,67,78,94,93]
students_marks = {}
for i in range(len(students)):
       students_marks[students[i]] = marks[i]
print(students_marks)


#list comphrehension:
numbers = [1,2,3,4,5]
squares = [num for num in numbers if num%2 == 0]
print(squares)

cites  = ["bengluruu","mysore","dubai","bgsmandya","shivamogga"]
big_cities = [city.upper()for city in cites] 
print(big_cities)


name = "i love python it is fun to learn"
splitted = name.split(" ",3)
print(splitted)


# HOMEWORK:

l1 =  ["bajji", "biriyani","mutton"]
l2 = [food.upper()for food in l1]
print(l2)


dict = {"kabab":30,"biriyani":180,"egg rice":45}
total = 0
for price in dict.values():
        total += price
print(total)


numbers = [1,2,3,4,5,6,7,8,9,10]
squares = [num**2 for num in numbers]
print(squares)


list = [{"name": "nagaraj", "age": "18", "marks": "100"} , 
        {"name": "vikasa", "age": "28", "marks": "99"},
        {"name": "pinnu", "age": "8", "marks": "56"}]

for student in list:
        print(f"Name:{student['name']},age:{student['age']},marks:{student['marks']}")
        
        
cities = {"bengaluru":45,"mandya":34, "shivamogga":7,"bgsbanglore":4 }
for city, value in cities.items():
        if value > 10:
                print(city)
                
#nested list :
lists = [
        [1,2,3],
        [4,5,6],
        [7,8,9],
        
          [3,4,5],
          [5,7,3,2]
]
for list in lists:
        print(sum(list))
        
# functionss hw
        
        
def greet(greetings ="hello bro"):
        print(f"{greetings}, I am nagaraj ys from banglore ")
greet()



#sum functiom:
def add_numbers(a,b):
        sum = a+b
        return sum
result = add_numbers(10,20)
print(result)


# lambda function 
double = lambda num:num*2
print(double(500))




multi = lambda c,k: c*k
print(multi(2,10))


# variable length argumewnts 
def fun(*numbers):
        total = 0
        for num in numbers:
                total = total +num
        return total/len(numbers)
avg = fun(10,20,60)
print(avg)
        

        
        
        
        
        
        















        
        
        
        
        





        

        
        
        

        











               
        
        





        
        
       
        

        
    
    

      
               
                      
                






