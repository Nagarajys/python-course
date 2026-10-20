# for loops - star patterns:
# pattern-16
'''Need one loop for spaces.

Need another loop for stars. , total 2 inner loop'''
for i in range(1,6):
    
    
    for j in range(5-i):
        print(" " ,end ="")
        
        
    for j in range(i):
        print("*",end="")
        
        
    print() 
#pattern -17
for i in reversed(range(1,6)):
    
    
    for j in range(5-i):
        print(" " ,end ="")
        
        
    for j in range(i):
        print("*",end="")
        
        
    print()

# pattern -18
for i in range(1,10,2):
    
    for j in range((9-i)//2):
        print(" ", end ="")
        
    for j in range(i):
        print("*", end="")
        
    print()
    
# pattern -19
for i in reversed(range(1,10,2)):
    
    for j in range((9-i)//2):
        print(" ", end ="")
        
    for j in range(i):
        print("*", end="")
        
    print()
    
# pattern -20
for i in range(1,10,2):
    
    for j in range((9-i)//2):
        print(" ", end ="")
        
    for j in range(i):
        print("*", end="")
        
    print()
    
for i in reversed(range(1,8,2)):
    
    for j in range((9-i)//2):
        print(" ", end ="")
        
    for j in range(i):
        print("*", end="")
        
    print()


