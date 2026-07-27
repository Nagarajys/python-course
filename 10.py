# FOR LOOPS CONCEPT ****
'''1. Difference Between While Loop and For Loop
WHILE LOOP:	                            FOR LOOP:
Condition based	                        Sequence based
Condition true iruvaregu run agutte	    Collection/Range mugiyuvaregu run agutte
Manual increment/decrement beku     	Automatic next value tagolutte
Infinite loop chance jaasti              Infinite loop chance kammi
Number of iterations gothillandre use madtivi	Number of iterations gothidre use madtivi'''
for i in range(5):
    print(i) #  only 1 to 4 start stop step
    
for i in range(1,6):
    print(i)  # 1 to 5 ,,, 6 is excluded
    
for i in range(1,10,2):
    print(i)# start.stop,step 2 means skip 1 element ,, if we put3 it skip 3 elements

for i in range(2,11,2):
    print(i)   
    
for i in range(2,11,1):
    print(i) # 1 means no skipping simply 
    
for i in range(10,0,-1):
    print(i)  # 10 to 0 but reverse manner so -1
    
for x in range(5):
    print(x)  # same simply we use varianle x insted of i
    
name = "Nagaraj"

for letter in name:
    print(letter) # name alli ero letter print madu anta
    
fruits = ["Apple","Mango","Orange"]

for fruit in fruits:
    print(fruit) 
    
    
bag = [ "red ", "green", "blue"]

for ball in bag:
    print(ball)
    
    
for i in range(3):
    for j in range(2):
        print(i, j)
        
# Because j belongs to the INNER loop. The inner loop must finish completely before the outer loop (i) is allowed to move to the next value.
'''i = 0

j = 0
print(0,0)

j = 1
print(0,1)

# j finished

i = 1

j = 0
print(1,0)

j = 1
print(1,1)

# j finished

i = 2

j = 0
print(2,0)

j = 1
print(2,1)'''   # for understanding


# 1. break Statement

for i in range(10):
    if i == 5:
        break
    print(i)  # at 5 loop will break
    
# 2.continue Statement
'''Current iteration skip madi Next iteration ge hogu.'''
for i in range (5):
    if i == 3 :  # means it skips 3 only   
        continue
    print(i)
    

# 3. pass statement Runs loop Does absolutely nothing.
for i  in range (10):
    pass  #later it can be replacable with code opr print..

# 4. for else
for i in range(5):
    print(i)
else:
   print("loop completed") # loop complete aythu adhike else print madutte
   
for i in range(10):
    print(i)
    if i == 7:
        break
else:
    print("Loop completed")
    # else runs only if the loop finishes normally (without break).
    
# 5. enumerate()
#enumerate() actually enu madutte?Adhu index + value erdannu ondhe sari kodutte.
fruits = [ " apple" , "banana" , " orange", " pineapple"]
for index,fruit in enumerate(fruits):
    print(index, fruit)
    
    
names= [ " ravi" , "rahulla", "rohana", "nagraj"," viki"]
for no,name in enumerate(names , start = 1):
    print(f"{no} .{name}")# Simple output → print(no, student) saaku.
#Sentence, formatting, symbols, labels, decimals, alignment beku → f-string best.


#  6.ZIP Zip means combine  2 lists 
names=  (" nagraj", " rahulla ", " vikas")
marks = (100 , 85 , 88 )
for name,mark in zip(names , marks):
    print(name,mark)
    
    
# 7. reversed()
for i in reversed(range(1, 21)):
    print(i)  
    
# 8. Membership (in and not in)
name = " nagaraj "
for letter in (name):
    print(letter)
    
name = "subramanya"
print("a"in name) # yes a is member of name
print("a" not in name)

#9. Loop Variable Scope
for i in range(8):
    print(i)
    
    
    
    
    