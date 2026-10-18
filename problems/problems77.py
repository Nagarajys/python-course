# ERRORS AND EXCEPTION HANDLING::::::
# 1. AGE VERIFIER:::

try:
    age = int(input("Enter your age please: "))
    result = 100 - age
    print(f"IN {result} years you will be 100 years old")
except ValueError as error:
    print("ERROR IS:", error)

    #  OR
try:
    age = int(input("Enter your age please: "))
    result = 100 - age

except Exception as age:
    print("ERROR IS:", {age})
else:
    print(f"IN {result} years you will be 100 years old")
finally:
    print("program ended!")

# 2.SAFE DIVIDERRR::
try:
    a = int(input("Enter a number a:"))
    b = int(input("Enter a number b:"))
    print(a / b)
except ZeroDivisionError as e:
    print("you cant divide number by zerooo", {e})
except ValueError as e:
    print("enter a valid number", {e})
else:
    print("there is no error")
finally:
    print("program will be at endddd")


# 3.FILE READERR:::
try:
    file = input("enter your file here::")
    if file != "Python course.D.drive":
        raise Exception("THIS FILE IS NOT FOUND ,PLEASSE SELECT- Python course.D.drive")
except Exception as e:
    print("ERROR:", {e})
else:
    print("yes you can access this file in D drivee")


try:
    amount = float(input("Enter expense amount: "))

    if amount <= 0:
        raise ValueError("Amount must be positive.")

except ValueError as error:
    print("Invalid expense:", {error})

else:
    print("Expense amount accepted:", amount)

finally:
    print("Expense entry process finished.")


try:
    result = 10 / 0
    print("A")

except ValueError:
    print("B")

else:
    print("C")

finally:
    print("D")

print("E")


try:
    amount = float("hello")

except ValueError as error:
    raise RuntimeError("Expense processing failed") from error
