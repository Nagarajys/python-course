# STRONG NUMBER - WHILE CONCEPT- means 145 dhu each digit factorial maddhga ady 145 nay barbeku adhe strong number
# we use 2 loops here calculate factorial
num = 145
temp = num 
total = 0
while temp > 0 : 
    digit = temp % 10
    factorial = 1
    i = 1
    while i <= digit:
        factorial = factorial*i
        i = i + 1
        
    total = total + factorial # 0 +120
    temp = temp // 10
    # here we get 14 goes up and it become 4 ! =24  and adds with 120+24 = 144
    # again we get 1 and goes up and becomes 1 ! and get add tp 144 + 1 = 145
if total ==  num :
        print("strongnumber ")
else:
    print("not strong number")


    