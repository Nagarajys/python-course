# FOR LOOPS - LETTER AND NUMBER PATTERNS
# pattern -9
'''chr(number) → Number → Character
chr(65)   # A
chr(66)   # B
chr(67)   # C  i + 1 use madodhu alli 1 enda 2 jump next 3 jump madoke'''
for i in range(5):
    for j in range(i+1):#j na use madodu "eshtu sala print madbeku?" antha control madoke.
         print(chr(65+i),end ="")
    print()  
    
# pattern -9
for i in reversed(range(5)): 
    for j in range(i+1):
        print(chr(69-i), end ="")
    print()
    
# pattern -10 
for i in range(5):
    for j in range(i+1):
        print(chr(69-i), end ="")
    print()
    
'''Outer loop values:

4
3
2
1
0

Table:

i	Letter	Print Times	Output
4	A	5	AAAAA
3	B	4	BBBB
2	C	3	CCC
1	D	2	DD
0	E	1	E'''

# Pattern -11
for i in range(1,6):
    print(i)
print()

# Pattern -12
for i in range(5,0,-1):
    print(i)
print()

# pattern -13
num = 1 
for i in range(1,5):
    for j in range(i):
        print(num , end ="")
        num = num +1
    print()
    
# pattern -14
num = 10
for i in range(1,5):#edhu outer loop yast row edhave asth range tagondre saku row print agoke
    for j in range(i):# inner loop est sala llop run madeku anta control madakke
        print(num, end = "")
        num = num -1
    print()

#Pattern -15
for  i in range(1,6):
    for j in range(i,0,-1): # means i = 3 edhaga 3,0 andre 321 revese print madu anta -1
        print(j,end = "")
    print()