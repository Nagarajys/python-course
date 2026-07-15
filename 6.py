# topic : tuples and sets
## NOTE : unmutable(unchangeble) and we use curved bracket
gender = ("male", " female", " others")
print(gender)
# gender[0] = "male2"  # Cannot modify tuples - they are immutable
print(len(gender))
print(gender[1])
print(gender[2])
print(gender[1:2])
print(gender[0:3])


#tuple concatination
tuple1 = (1,2,3)
tuple2 = (10,20,30)
combined_tuple = tuple1 + tuple2
print(combined_tuple)

#tuple repetation
repeated_tuple = (1234,99,"nagaraj")*100
print(repeated_tuple)

##SETS..
s = {1,2,3}# unordered and unindexed
print(s)
print(set[1])
s = {20,132,3325}
print(s)
print(set()) # empty set
s = set()
print(type(s))
s1 = {1,2,3}
s2 = {3,4,5}
s3 = {5,6,7}
print(s1 | s2 | s3) # union
print(s1 & s2)# intersection
print(s1 - s2 ) # differnce
print(s1 - s3)
s = {1,4,5,6,7,78,9}
s.add(100)
print(s)
s.discard(7) 
s.pop()
print(s)
s = {1,2,3,4,5,6}
a = s.pop()
print(a) # we cant guess which element will be removed
s = {67,87,44}