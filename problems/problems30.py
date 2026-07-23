# Problem 6

n = int(input("Enter number : "))

i = 1

while i <= 10:
    print(n, "x", i, "=", n*i)
    i += 1
    
# Problem 7

n = int(input("Enter number : "))

fact = 1
i = 1

while i <= n:
    fact *= i
    i += 1

print("Factorial =", fact)

# Problem 8

num = int(input("Enter number : "))

while num > 0:
    digit = num % 10 # gives remainder as last digit of given number
    print(digit, end="")
    num = num // 10 # remove num whoch is present after decimal adn add last number so on continue for remaining number also
    
# Problem 9

password = "python"

user = ""

while user != password:
    user = input("Enter Password : ")

print("Access Granted")

