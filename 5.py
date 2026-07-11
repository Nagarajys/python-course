# lists
items = ["milk", "sugar", "bru", "glass"]
print(items)
items = ["milk", "bru", "sugar", "glass", "bru2"]
print(items)
items.pop() # To remove last word use.pop() empty bracket
print(items)
items.append("marigold") ## toadd items at end fill bracket with reqired item
print(items)
items.pop(1) #to remove required item use pop with index number of that specific item
print(items)
items.insert(1, "mutton") ## here insert is used to insert an items with specific position using index number of that element
print(items)
items.clear() ## to clear whole list
print(items)
items = ["milk", "bru", "sugar", "glass", "bru2"]
items[2] = "coffee powder" ## to change old item by new using specific index
print(items)

##slicing lists
# here start-stop-step
# start is inclusive, stop is exclusive, step skips elements
l = (100,200,300,400,500,600,700,800,900)
l[0:3] # here stop is exclusive means index number 3 would not count only upto index number 2 will become output
print(l[0:3])
print(l[0:]) ## full list will become output
print(l[2:9])
print(l[0::2]) # to skip elements using 2 colons step
print(l[2::5])
print(l[0::4])
print(l[0::4])
print(l[2::6])
print(l[1:3])
l2 = (l[1:3])
print(l2)
items = (23,55,66,33,22,1,100,3500,250)
print(sorted(items)) ## asending  order
sorted_items = sorted(items)
print(sorted_items)
numbers = (1,2,3,4,5,6,1,2,2,3)
print(numbers.count(2)) ## to count required number 
print(numbers.index(2)) ## to check index of number
print(sum(numbers)) ## to add all numbers in list

fruits = ["apple", "banana" , "cakefruit", "pineapple"]
fruits.reverse()
print(fruits)

m = [[1,2],[3,6],[5,7]]
print(m) ## nesting
print(m[0]) 
print(m[0][0]) ## to get list of list number put 2 times of index
print(type(m))





