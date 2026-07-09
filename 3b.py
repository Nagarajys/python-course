# string adtatype and access manipulation
first_name = "nagaraj"
last_name = "ys"
full_name = first_name + " " + last_name
print(full_name)  # Output: nagaraj ys
#repitition
message = "warning!"
print(message*100)  # Output: warning!
print(len(message))
name = "nagaraj"
print(name[3])  # index = position -1
# position starting from 1 add index starting from 0
name = "chandans"
print(name[2:7])  # Output: andan
name = "nagaraj"
print(name[1:5])
print(name[1:])
name = "karthik"
print(name[0:])# must put colon: symbol otherwisw wrong result
# extra- nagaraj
        #0123456
        #-6-5-4-3-2-1 
    
    # therfore both are  same from front index starts from 0 and from reverse it start from -1

print(name[3])
print(name[-4])
name = "nagaraj"
print(name[:]) # full start
print(name[::2]) # giving 2 after 2times coolon skips 1 letter
print(name[::3])
name = "chandan"
print(name[::3])# giving 3 after 2 colon skip 2 letters
name = "subramanya"
print(name[::2])
print(name[::4])
sentence = "nagaraj is a good boy"
print(sentence)
s ="nagaraj\n have big dreams" # slash n is used to seprate 2 lines up and down
print(s)
s= "nagaraj \t have big dreams"
print(s)



