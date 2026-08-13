#FUNCTION ADVANCWED - PART D (1)- RECURSION PRACTICE
#Recursion alli stopping condition-na base case antare.
#BASE CASE:
def count (n):                
    if n == 0:
        return
    print(n)
    count(n -1)
count(3)

'''count(3)
 ↓
print 3
 ↓
count(2)
 ↓
print 2
 ↓
count(1)
 ↓
print 1
 ↓
count(0)
 ↓
STOP'''


#RECURSIVE CASE:function calls itself
'''Recursion can solve some problems that loops can also solve, but 
it does it by function calling itself.'''
#But what if return comes AFTER recursive call?-
'''Code before recursive call → happens while going DOWN.
Code after recursive call → happens while coming BACK UP.'''
def counts  (n):
    if n  == 0:
        return
    counts(n -1)# recursive call  
    print(n)
counts(3)
'''DOWN:
count(3)
  ↓
count(2)
  ↓
count(1)
  ↓
count(0) → STOP

UP:
count(1) → print 1
count(2) → print 2
count(3) → print 3'''
#trick print BEFORE recursive call → 3, 2, 1

 # print AFTER recursive call → 1, 2, 3
 
 #9️ Classic Example — Factorial
def fact(n):
     if n == 1:
        return 1
     return n * fact(n-1)
print(fact(5))

#Most important recursion formula
'''''def function (n):
    if base_condition:
        return base value
    return current_work + or * function(any small problem)'''