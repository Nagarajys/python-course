# Problem: 22 - practice on sets
numbers = {10, 20, 10, 30, 40, 30, 50, 20}
print(numbers)
##Tasks

#1.Common languages
#2.Only Student A knows
#3.Only Student B knows
#4.Total different languages
studentA = {"Python", "Java", "C", "SQL"}

studentB = {"Python", "JavaScript", "SQL", "AI"}

print("common languages:", studentA & studentB)
print("only studentA knows:" , studentA - studentB)
print("only studentB knows:" , studentB - studentA)
print("total diffrent languages:" , studentB | studentA)



