try:
    a = int(input("enter a number:"))
    print(10 / a)
except ZeroDivisionError:
    print("you can't  divide by zero!!")
else:
    print("yes you can , bcz there is no error")
