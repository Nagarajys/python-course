##PROBLEMS ON FOR LOOP :-
#Problem 1  Print numbers from 1 to 10
for i in range(1,11):
    print(i)
    
# Problem 2  Print numbers from 10 to 1
for i in reversed(range(1,11)):
    print(i)
    

# Problem 3  Print even numbers from 1 to 20
for x in range(2,21,2):
    print(x)
    
# Problem 4  Print odd numbers from 1 to 20
for x in range(1,21,2):
    print(x)
    
#Problem 5
for i in range(6):
    i = "python"
    print(i)
    
# Problem 6  Find the sum of numbers from 1 to 10
total = 0
for i in range(1, 11):
    total = total + i # 0+1 , 1 +2 = 3 , 3+3 = 6 eriti run agi add agute
    # hogute bcz this is loop
print(total)

# Problem 7  Find the sum of even numbers from 1 to 20
total = 0 
for i in range(2, 21, 2):
    total = total + i
print(total)


# Problem 8  Print the multiplication table of 7
for i in range(1, 11):
    print(f"{i}*7 = {i*7}")

# Problem 9  Count how many numbers are there from 1 to 100
count = 0 
for i in range(1,101):
    count = count +1
print(count)

# problem 10 - factorial in (a.)while loop version
num = 5 
factorial = 1
while num>0:
    factorial = factorial*num
    num = num - 1 # 5 erodh 4 agutte next 3 till 1
print(factorial)

# problem 11 - factorial in (b.)for loop version
factorial = 1
for i in range(1,6):
    factorial = factorial*i
print(factorial)
 #Indentation decides how many times a statement executes. If it is inside the loop:
# If it is outside the loop:print() executes 1 time (after the loop finishes).
    



    
    
    
    

