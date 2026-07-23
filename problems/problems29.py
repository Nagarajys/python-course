#  problem : 29 -while loop problems 
#Q1 print 1 to 10
i = 1
while i <= 10:
    print(f"{i}")
    i = i +1
    
    
# Q2 print 10 to 1
i = 10
while i<=10 and i>=1:
    print(f"{i}")
    i = i-1
    
# Q3 print even numbers 1 to 100
i = 1
while i <= 100:
    if i % 2 == 0: # only even numbers
        print(f"{i}")
    i = i + 1
    
# Q4 print odd numbes 1 to 100
i = 1
while i <=100:
    if i%2 ==1: # only odd numbers
        print(f"{i}")
    i = i +1
    
#Q5 print sum 1 to n
n = int(input("enter a number - "))
i= 1
total = 0
while i<=n:
    total = total+i
    i = i+1
print("sum=", total)





    
    
     

