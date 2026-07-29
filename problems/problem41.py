# FOR LOOPS - PATTERN PRINTING
# pat -1
for i in range(5):
    print("*")

    
    
# pat -2
for i in range(5):
    
    for j in range(i +1):
        print("*", end = " ")
    print() # move to next line
    
'''  i	range(i+1)	Stars printed
0	range(1) → 0	⭐
1	range(2) → 0,1	⭐⭐
2	range(3) → 0,1,2	⭐⭐⭐
3	range(4)	⭐⭐⭐⭐
4	range(5)	⭐⭐⭐⭐⭐'''  # for understanding purpose

# pat -3
for i in range(5,0,-1):
    for j in range(i+1):
        print("*",end = "")
    print()

# pat -4
for i in range(5):
    for j in range(5):
        print("*",end = "")
    print()
    

