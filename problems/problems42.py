# FOR LOOPS - NUMBERS PATTEREN PRINTING
# Pattern 5

for i in range(1, 6):          # Rows: 1,2,3,4,5
    for j in range(1, i + 1):  # Numbers: 1 to i using nested here
        print(j, end="")
    print()
    
# pattren -6
for i in reversed(range(1,6)):
    for j in range(1,i+1):
         print(j,end = "")
    print()
    
# pattern -7 
for i in range (1,6):
    for j in range(i): # j loop control madutte , but i print agutte 
        print(i,end = "")# evag j value 0 bandaga 1 print agutte. 
    print()              # 0 1 bandaga 2 2 print agutte

# pattern 8
for i in range(5,0,-1):
    for j in range(i):
        print(i,end="")
    print()