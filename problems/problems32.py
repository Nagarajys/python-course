#Q:Check whether a number is a palindrome.
num = int(input("put a number"))

original = num
reverse = 0 
while num>0:
    digit = num%10
    reverse = reverse*10 + digit # understand this line you will got whole code
    num = num//10
if original == reverse:
    print("palindrome number")
else:
    print("not a palindrome number")