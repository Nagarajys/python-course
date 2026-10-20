# find the largest digit in a number WHILE CONCEPT

num = int(input("enter a number=")) # 5692
largest = 0 
while num>0: # largest is in memory as 0 , while we always give num >0
    
    digit = num%10 # from here wwe get 2 and
    if digit>largest:# 2>0
        largest=digit # then 2 is largest again loop runs 
    num = num//10 # here we get 569 loop runs 9 we get at 7th line
                 # therefore 9>2 so on 5 and 6 are false loop stops

    print("largest digit=", largest)
