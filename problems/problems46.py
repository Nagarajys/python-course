# FOR LOOPS - NUMBER PATTERNS and LETTERS - DIFFRRENT TYPES OF PATTERNS
# pattern - 25
for i in range(1,6):
    for j in range(1,i+1):
        if (i+j)%2 == 0:# to check even
            print("1",end="")
        else:
            print("0",end="")
    print()


# PATTERN -26
for i in  range(1,6):
    for j in range(1,i+1):
        print(chr(64+j),end="")
    print()
    
    '''Row 3
    print(chr(64+i), end="")
Iteration	i	j	chr(64+i)	Printed
1	3	1	67	C
2	3	2	67	C
3	3	3	67	C'''



'''print(chr(64+j), end="")
Same row.
Iteration	i	j	chr(64+j)	Printed
1	3	1	65	A
2	3	2	66	B
3	3	3	67	C'''

#pattern -27
for i in  range(5,0,-1):
    for j in range(1,i+1):
        print(chr(64+j),end="")
    print()
    
# pattern -28
for i in range(1,6):
    for j in range(i+1,1,-1):
        print(chr(71-j),end="")
    print()
    
# pattern -29
for i in range(1,6):
    for j in range(1,i+1):
        print(i,end="")
    print()
for i in reversed(range(1,5)):
    for j in range(1,i+1):
        print(i,end="")
    print()   

# pattern -30
for i in range(1,6):
    for j in range(1,i+1):
        print("*",end="")
    print()
for i in reversed(range(1,5)):
    for j in range(1,i+1):
        print("*",end="")
    print()   
