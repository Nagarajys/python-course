#  RECURSION 10 PROBLEMS : PRACTICE 
#1-BASIC PROBLEM:
def countdown(n):
    if n == 0:
        return
    print(n)
    countdown(n-1)
countdown(5)

#2-Recursion + Return
def sum_numbers(n):
    if n ==1:
        return 1
    return n + sum_numbers(n-1)
print(sum_numbers(5))

#3-Recursion + factorial
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)
print(factorial(5))

#4 — Recursion + Power
def power(base ,  exponent):
    if exponent == 0:
        return 1
    return base * power(base, exponent -1)
    #CURRENT BASE       SAME REMAINING BASE
print(power(2,5))

'''power(2,5)
= 2 × power(2,4)
= 2 × 2 × power(2,3)
= 2 × 2 × 2 × power(2,2)
= 2 × 2 × 2 × 2 × power(2,1)
= 2 × 2 × 2 × 2 × 2 × power(2,0)'''

#5 — Recursion + String Reverse
def reverse_string(text):
    if len(text) <=1:
        return text
    return text[-1] + reverse_string(text[:-1])
print(reverse_string("python"))

#6 Recursion + Palindrome
def is_palindrome(text):
    if len(text)<=1:
        return True
    if text[0]!= text[-1]:
        return False
    return is_palindrome(text[1: -1])
print(is_palindrome("madam"))


'''len <= 1?
→ yes → True

first != last?
→ yes → False

otherwise
→ first & last remove madu
→ middle string-na again check madu'''

#7— Recursion + Digit Sum
def digit_sum(n):
    if n ==0:
      return  n //10
    return n%10 +digit_sum(n//10)

print(digit_sum(12345))

#8 -Recursion 
def sum_all(*numbers):
    if len(numbers) == 1:
        return numbers[0]
    return numbers[0] + sum_all(*numbers[1:])
result = sum_all(10, 20, 30, 40, 50)
print(result)
    
    
    


