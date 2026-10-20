# FOR LOOPS- HOLLOW PATTERNS
# pattern - 21
for i in range(1,6):# 5 rows so
    for j in range(1,6):# 5 coloums so
        if i == 1 or i ==5 or j ==1 or j ==5:# erows matte e cooloms bittu yalla kade space erli
            print("*", end="")
        else:
            print(" ",end="")
            
    print()
    
# pattern - 22
for i in range(1,6):# 5 rows so
    for j in range(1,6):# 5 coloums so
        if i == 1 or i ==5 or j ==1:# erows matte e cooloms bittu yalla kade space erli
            print("*", end="")
        else:
            print(" ",end="")
            
    print()
    
# pattern - 23
for i in range(1,6):# 5 rows so
    for j in range(1,6):# 5 coloums so
        if i == 1 or i ==5 or j == 5:# erows matte e cooloms bittu yalla kade space erli
            print("*", end="")
        else:
            print(" ",end="")
            
    print()
    
# pattern-24

for i in range(1,6):
    for j in range( 1,i+1):# range() decides how many columns exist.
# if j == 1 decides what to print in that colum
        if  i==j or j ==1 or i==5 :
            print("*",end="")
        else:
            print(" ",end="")
    print()
        
    