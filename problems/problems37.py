# Reverse Number & Check Palindrome  WHILE CONCEPT

num = int(input("enter a number = "))
reverse = 0
original = num
while num>0:
    digit = num%10
    reverse = reverse *10 +digit
    num = num // 10
if original==reverse:
    print("palindromic sequence")
else:
    print("not palindome")
    