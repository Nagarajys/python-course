# problems : 30 - WHILE LOOPS 
#Q1 - MMULTIPLICTION TABLE
n = int(input("enter a number - "))
i = 1
fact = 1
while i<=n:
    fact = fact*i
    i= i + 1
print("Factorial=", fact)

# note to remember
#Sum ➜ total = 0
#Count ➜ count = 0
#Factorial/Product ➜ fact = 1

#Q2 - REVERSE NUMBER
n = int(input("enter a number= "))
while n>0:
    digit = n%10 # a number divided by 10 always gives last digit of that number as a remainder
    print(digit, end = "") # digit na print madu matte next hako function digit jote nay end agli
    n = n//10 # float function removes number after decial and adds reversly
    break

#Q3 - GUESS THE PASSWORD
password = "python"

user = "" 

while user != password:
    user = input("enter your password:")
    
print("Access granted")










    
    



    