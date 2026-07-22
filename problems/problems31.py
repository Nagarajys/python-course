# Q : Count the number of digits in a number.
num = 123456
print(len(str(num)))
#OR
num = int(input("enter number"))
count = 0
while num>0:
    count = count+1 
num =num//10
print(count)

#Q ATM PIN:
correct_pin = 3730
attempts = 3
balance = 20000

while attempts > 0:
    entered_pin = int(input("ENTER YOUR PIN: "))

    if entered_pin == correct_pin:
        amount = int(input("Please enter amount: "))

        if amount <= balance:
            balance = balance - amount
            print("Withdrawal successful.")
            print("Remaining balance:", balance)
        else:
            print("Insufficient funds")

        break

    else:
        attempts = attempts - 1
        print("Wrong PIN. Attempts remaining:", attempts)

if attempts == 0:
    print("Account Locked")
    
    




    
    
    